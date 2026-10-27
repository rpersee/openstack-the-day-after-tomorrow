-- book-epub.lua — pandoc Lua filter that turns the GitHub-oriented Markdown
-- chapters into an EPUB book (HTML output).
--
-- What it does:
--   * drops the navigation footers ("← Previous · Contents · Next →")
--   * turns "*Part I — Title*" lines into <section class="part"> with <h1>
--   * "# Chapter N — Title"  -> <h1>Chapter N — Title</h1> (numbered chapter)
--     "# Appendix X — Title" -> <h1>Appendix X — Title</h1> (lettered appendix)
--     other level-1 headings -> <h1> listed in the contents
--   * turns the Technical note / Principle / From the field quotations into
--     <blockquote class="technote|principle|fromfield">
--   * turns "![Figure X.Y](path)" + "*Figure X.Y: caption*" into a real
--     <figure> with <img> and <figcaption>
--
-- The structural markers exist in two languages: English (the original
-- edition) and French (fr/, see fr/STYLE.md). The language is taken from the
-- "lang" metadata of the edition (tools/pdf/metadata*.yaml).
--
-- For reflowable EPUB, we preserve French typography (narrow no-break spaces,
-- guillemets, apostrophes) in the HTML source. CSS can be added for styling.

local stringify = pandoc.utils.stringify

local MARKERS = {
  en = {
    part = "^Part %u+ — ", chapter = "^Chapter %d+ — (.*)$", appendix = "^Appendix %u — (.*)$",
    appendices = "Appendices", references = "^References",
    technote = "^Technical note", principle = "^Principle", fromfield = "^From the field",
    figure = "^Figure %d+%.%d+:", figure_rest = "^Figure %d+%.%d+:%s*(.*)$",
    appendix_part = "Appendices",
  },
  fr = {
    part = "^Partie %u+ — ", chapter = "^Chapitre %d+ — (.*)$", appendix = "^Annexe %u — (.*)$",
    appendices = "Annexes", references = "^Références",
    technote = "^Note technique", principle = "^Principe", fromfield = "^Sur le terrain",
    figure = "^Figure %d+%.%d+[^:]*:", figure_rest = "^Figure %d+%.%d+[^:]*:%s*(.*)$",
    appendix_part = "Annexes",
  },
}

local M = MARKERS.en
local seen_parts = {}
local appendix_done = false
local backmatter_done = false

local function is_nav_para(block)
  if block.t ~= "Para" then return false end
  local has_md_link = false
  for _, inl in ipairs(block.content) do
    if inl.t == "Link" and inl.target:match("%.md$") then has_md_link = true end
  end
  return has_md_link
end

local function box_kind(bq)
  local first = bq.content[1]
  if not first or first.t ~= "Para" then return nil end
  local lead = first.content[1]
  if not lead or lead.t ~= "Strong" then return nil end
  local label = stringify(lead)
  if label:match(M.technote) then return "technote" end
  if label:match(M.principle) then return "principle" end
  if label:match(M.fromfield) then return "fromfield" end
  return nil
end

local function first_image(block)
  -- the image paragraph is parsed by pandoc either as Para{Image} or, with
  -- implicit_figures, as Figure{Plain{Image}}
  if block.t == "Para" and #block.content == 1 and block.content[1].t == "Image" then
    return block.content[1]
  end
  if block.t == "Figure" and #block.content == 1 and #block.content[1].content == 1 and block.content[1].content[1].t == "Image" then
    return block.content[1].content[1]
  end
  return nil
end

local function figure_from(img_block, cap_para)
  local img = first_image(img_block)
  local caption = cap_para.content[1].content        -- inlines inside Emph
  -- strip the "Figure X.Y:" prefix: EPUB figures keep original numbering
  local text = stringify(caption)
  local rest = text:match(M.figure_rest)
  local cap_inlines
  if rest then
    -- keep inline formatting if any: re-parse as markdown
    cap_inlines = pandoc.read(rest, "markdown").blocks[1].content
  else
    cap_inlines = caption
  end
  -- For EPUB, keep the original SVG path; pandoc will embed it
  img.attr = pandoc.Attr("", {}, {width = "100%"})
  local fig = pandoc.Figure({pandoc.Plain({img})}, {long = {pandoc.Plain(cap_inlines)}})
  return fig
end

function Pandoc(doc)
  local lang = doc.meta.lang and stringify(doc.meta.lang) or "en"
  M = MARKERS[lang:sub(1, 2)] or MARKERS.en
  local out = pandoc.List()
  local blocks = doc.blocks
  local i = 1
  while i <= #blocks do
    local b = blocks[i]
    local nxt = blocks[i + 1]

    -- navigation footer: HorizontalRule followed by a paragraph of .md links
    if b.t == "HorizontalRule" and nxt and is_nav_para(nxt) then
      i = i + 2
    elseif is_nav_para(b) then
      i = i + 1

    -- part lines: turn into <section class="part"><h1>Title</h1>
    elseif b.t == "Para" and #b.content == 1 and b.content[1].t == "Emph"
           and stringify(b):match(M.part) then
      local title = stringify(b):gsub(M.part, "")
      if not seen_parts[title] then
        seen_parts[title] = true
        local section = pandoc.Div(pandoc.List{b}, pandoc.Attr("part-" .. title:gsub("%s+", "-"):lower(), {"part"}, {}))
        out:insert(section)
      end
      i = i + 1
    elseif b.t == "Para" and stringify(b) == M.appendices then
      i = i + 1

    -- level-1 headings
    elseif b.t == "Header" and b.level == 1 then
      local text = stringify(b)
      local chap = text:match(M.chapter)
      local app = text:match(M.appendix)
      if chap then
        -- Chapter: keep as h1 with "Chapter N — " prefix
        local new_header = pandoc.Header(1, pandoc.read(chap, "markdown").blocks[1].content)
        out:insert(new_header)
      elseif app then
        -- Appendix: add appendix section marker before first appendix
        if not appendix_done then
          appendix_done = true
          local sec = pandoc.Div(pandoc.List{pandoc.Header(1, pandoc.Str(M.appendix_part))}, pandoc.Attr("", {"appendix-part"}, {}))
          out:insert(sec)
        end
        local new_header = pandoc.Header(1, pandoc.read(app, "markdown").blocks[1].content)
        out:insert(new_header)
      else
        -- Other level-1 headings (References, etc.)
        if text:match(M.references) and not backmatter_done then
          backmatter_done = true
        end
        out:insert(b)
      end
      i = i + 1

    -- boxed passages: turn into blockquote with class
    elseif b.t == "BlockQuote" and box_kind(b) then
      local kind = box_kind(b)
      local new_bq = pandoc.BlockQuote(b.content)
      new_bq.attr = pandoc.Attr("", {kind}, {})
      out:insert(new_bq)
      i = i + 1

    -- figures: image paragraph followed by an italic caption paragraph
    elseif first_image(b)
           and nxt and nxt.t == "Para" and #nxt.content == 1 and nxt.content[1].t == "Emph"
           and stringify(nxt):match(M.figure) then
      out:insert(figure_from(b, nxt))
      i = i + 2

    else
      out:insert(b)
      i = i + 1
    end
  end
  doc.blocks = out
  return doc
end
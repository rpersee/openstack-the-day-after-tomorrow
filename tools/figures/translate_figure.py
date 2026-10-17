#!/usr/bin/env python3
"""Produce a translated edition of a figure from the original SVG and a map.

    tools/figures/translate_figure.py assets/figures/figure-4-1.svg tools/figures/fr/figure-4-1.json assets/figures/fr/figure-4-1.svg

The original figures (assets/figures/*.svg) carry their text as outlined
glyphs. This script keeps every drawing element (boxes, lines, arrows) exactly
as it is and replaces each text line by a real <text> element whose content
comes from the map. The map is a JSON file:

    {
      "font": "Liberation Sans, Arial, Helvetica, sans-serif",
      "sets": {"0": {"weight": "bold"}, "1": {"style": "italic"}},
      "lines": {
        "0": {"text": "Observer"},                       # centred on the original line
        "7": {"text": "…", "anchor": "start"},            # left-aligned at the original x
        "21": {"text": "…", "anchor": "end"},             # right-aligned at the original end
        "9": {"text": ["ligne 1", "ligne 2"], "size": 5.5}   # several lines, custom size
      }
    }

Lines are numbered as tools/figures/debug_runs.py prints them. A line left out
of the map is reported and kept untranslated. The text is set in a font with
Helvetica/Arial metrics (Liberation Sans), which the build workflow installs;
GitHub's SVG rendering falls back along the font-family list.
"""
import json
import sys
from xml.sax.saxutils import escape
sys.path.insert(0, __import__("os").path.dirname(__file__))
from svg_runs import parse, font_sizes, merge_lines

src, map_path, dst = sys.argv[1], sys.argv[2], sys.argv[3]
spec = json.load(open(map_path, encoding="utf-8"))
head, defs, body, raw_runs, boxes = parse(open(src, encoding="utf-8").read())
sizes = font_sizes(raw_runs, boxes)
lines = merge_lines(raw_runs)
font = spec.get("font", "Liberation Sans, Arial, Helvetica, sans-serif")

missing = []
for ln in lines:
    entry = spec["lines"].get(str(ln.index))
    if entry is None:
        missing.append(ln.index)
        continue
    setspec = spec.get("sets", {}).get(ln.glyph_set, {})
    size = entry.get("size", setspec.get("size", sizes[ln.glyph_set]))
    anchor = entry.get("anchor", setspec.get("anchor", "middle"))
    x = {"start": ln.x0, "end": ln.x1, "middle": ln.xc}[anchor] + entry.get("dx", 0)
    attrs = [f'font-family="{font}"', f'font-size="{size}"', f'fill="{ln.fill}"', f'text-anchor="{anchor}"']
    if setspec.get("weight") or entry.get("weight"):
        attrs.append(f'font-weight="{entry.get("weight", setspec.get("weight"))}"')
    if setspec.get("style") or entry.get("style"):
        attrs.append(f'font-style="{entry.get("style", setspec.get("style"))}"')
    texts = entry["text"] if isinstance(entry["text"], list) else [entry["text"]]
    dy = entry.get("dy", setspec.get("dy", round(size * 1.15, 2)))
    out = []
    for k, t in enumerate(texts):
        out.append(f'<text x="{x:.3f}" y="{ln.y + k * dy + entry.get("dy0", 0):.3f}" {" ".join(attrs)}>{escape(t)}</text>')
    # replace the first run of the line by the text, drop the other runs
    body = body.replace(ln.parts[0].raw, "\n".join(out), 1)
    for part in ln.parts[1:]:
        body = body.replace(part.raw, "", 1)

if missing:
    print(f"warning: {len(missing)} line(s) not in the map, kept in English: {missing}", file=sys.stderr)
# the glyph definitions are no longer needed
result = head + body
result = result.rstrip() + "\n"
open(dst, "w", encoding="utf-8").write(result)
print(f"{dst}: {len(lines) - len(missing)}/{len(lines)} lines translated")

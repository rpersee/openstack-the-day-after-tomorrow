#!/usr/bin/env python3
"""Check that the French edition (fr/) stays in step with the original (chapters/, appendices/).

    python3 tools/check_editions.py

Exit code 0 when every check passes, 1 otherwise. For every source file of the
English edition the script finds its French counterpart (same chapter number
or appendix letter, see fr/STYLE.md) and compares the structure of the two:

  * the file exists, carries the part line (Partie / Annexes) when the original
    does, and a navigation footer whose links resolve
  * same number of level-1 and level-2 headings, of paragraphs, of bullet and
    numbered list items, of table rows, of figures and figure captions
  * same number of boxed passages of each kind (Technical note / Note technique,
    Principle / Principe, From the field / Sur le terrain)
  * the same inline `code` spans and the same URLs, in the same order (commands,
    options and links are not translated)
  * every "Chapter N" / "Appendix X" cross-reference of the original has a
    "chapitre N" / "annexe X" counterpart
  * French typography: narrow no-break space before : ; ! ?, inside « »,
    no-break space before %, typographic apostrophes, no straight quotes
  * the French README lists every French chapter, and every chapter link of
    fr/README.md resolves

The counts are structural, not textual: the script does not judge the
translation, it makes sure nothing was dropped, merged or left in English.
"""
import glob
import os
import re
import sys

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
NNBSP, NBSP = " ", " "

FRONT = {
    "00-front-matter.md": "00-pages-liminaires.md",
    "00-how-to-read-this-book.md": "00-comment-lire-ce-livre.md",
    "00-introduction.md": "00-introduction.md",
    "references-and-further-reading.md": "references-et-lectures-complementaires.md",
}
BOXES = {
    "technote": (r"^> \*\*Technical note", r"^> \*\*Note technique"),
    "principle": (r"^> \*\*Principle", r"^> \*\*Principe"),
    "fromfield": (r"^> \*\*From the field", r"^> \*\*Sur le terrain"),
}

# Deliberate differences of the French edition (see fr/STYLE.md)
ALLOWED_EXTRA = {
    "00-pages-liminaires.md": {"paragraphs": 1},   # the note that presents the French edition
    "annexe-f-glossaire.md": {"paragraphs": 1},     # the entry on "capacité" (capability / capacity)
}
ENGLISH_TITLES = ("OpenStack, the Day After Tomorrow: Operating Mission-Critical OpenStack Platforms",)

failures = []


def fail(msg):
    failures.append(msg)
    print(f"FAIL  {msg}")


def counterpart(en_path):
    name = os.path.basename(en_path)
    sub = "fr/chapters" if "/chapters/" in en_path else "fr/appendices"
    if name in FRONT:
        return os.path.join(ROOT, sub, FRONT[name])
    m = re.match(r"^(\d\d)-", name)
    if m:
        hits = glob.glob(os.path.join(ROOT, sub, f"{m.group(1)}-*.md"))
        return hits[0] if hits else os.path.join(ROOT, sub, f"{m.group(1)}-<missing>.md")
    m = re.match(r"^appendix-([a-f])-", name)
    if m:
        hits = glob.glob(os.path.join(ROOT, sub, f"annexe-{m.group(1)}-*.md"))
        return hits[0] if hits else os.path.join(ROOT, sub, f"annexe-{m.group(1)}-<missing>.md")
    return None


def strip_code(text):
    text = re.sub(r"```.*?```", "", text, flags=re.S)
    return re.sub(r"`[^`\n]*`", "`", text)


def structure(md):
    body = strip_code(md)
    lines = body.splitlines()
    s = {
        "h1": sum(1 for l in lines if l.startswith("# ")),
        "h2": sum(1 for l in lines if l.startswith("## ")),
        "bullets": sum(1 for l in lines if re.match(r"^\s*[-*] ", l)),
        "numbered": sum(1 for l in lines if re.match(r"^\s*\d+\. ", l)),
        "table_rows": sum(1 for l in lines if l.startswith("|") and not re.match(r"^\|[\s:-]+\|", l)),
        "figures": sum(1 for l in lines if l.startswith("![")),
        "captions": sum(1 for l in lines if re.match(r"^\*Figure \d+\.\d+", l)),
        "quotes": sum(1 for l in lines if l.startswith("> ")),
        "rules": sum(1 for l in lines if l.strip() == "---"),
        "paragraphs": len([b for b in re.split(r"\n\s*\n", body.strip()) if b.strip()]),
        "arrows": body.count("→"),
    }
    return s


def inline_code(md):
    md = re.sub(r"```.*?```", "", md, flags=re.S)
    return re.findall(r"`[^`\n]+`", md)


def urls(md):
    return re.findall(r"https?://[^\s)>\]]+", md)


def nav_links(md, path):
    """Return the .md links of the navigation footer (last paragraph) and check they resolve."""
    last = md.strip().split("\n\n")[-1]
    links = re.findall(r"\]\(([^)]+\.md)\)", last)
    for l in links:
        target = os.path.normpath(os.path.join(os.path.dirname(path), l))
        if not os.path.isfile(target):
            fail(f"{os.path.relpath(path, ROOT)}: navigation link does not resolve: {l}")
    return links


def check_typography(fr_path, md):
    rel = os.path.relpath(fr_path, ROOT)
    text = strip_code(md)
    # drop URLs and link targets, which legitimately contain ASCII punctuation
    text = re.sub(r"\]\([^)]*\)", "]()", text)
    text = re.sub(r"https?://\S+", "", text)
    for title in ENGLISH_TITLES:
        text = text.replace(title, "")
    for i, line in enumerate(text.splitlines(), 1):
        if re.search(r"[^\s  ]( )[:;!?](\s|$)", line) and not re.search(r"\d ?: ?\d", line):
            fail(f"{rel}:{i}: ordinary space before high punctuation (use U+202F)")
        if re.search(r"[A-Za-zÀ-ÿ»)][:;!?](?=\s)", line) and not line.startswith("#") and "http" not in line:
            # a colon glued to a word: allowed only inside code or at the start of a line of a table header
            if not re.match(r"^\|", line):
                fail(f"{rel}:{i}: missing space before high punctuation")
        if re.search(r"« [^ ]|[^ ] »", line) or "«" in line and f"«{NNBSP}" not in line and "« " in line:
            fail(f"{rel}:{i}: guillemets without narrow no-break space")
        if re.search(r"\d %", line) or re.search(r"\d%", line):
            fail(f"{rel}:{i}: percent sign without no-break space")
        if "'" in line:
            fail(f"{rel}:{i}: straight apostrophe (use ’)")
        if '"' in line:
            fail(f"{rel}:{i}: straight double quote (use « » or “ ”)")
        if re.search(r"\b(Chapter|Appendix|Figure \d+\.\d+:|Contents|Part [IVX]+ —)\b", line):
            fail(f"{rel}:{i}: English structural marker left in the text")


def main():
    en_files = (sorted(glob.glob(os.path.join(ROOT, "chapters", "*.md")))
                + sorted(glob.glob(os.path.join(ROOT, "appendices", "*.md"))))
    fr_seen = set()
    for en in en_files:
        rel = os.path.relpath(en, ROOT)
        fr = counterpart(en)
        if not fr or not os.path.isfile(fr):
            fail(f"{rel}: no French counterpart ({os.path.relpath(fr, ROOT) if fr else '?'})")
            continue
        fr_seen.add(os.path.abspath(fr))
        frrel = os.path.relpath(fr, ROOT)
        en_md = open(en, encoding="utf-8").read()
        fr_md = open(fr, encoding="utf-8").read()
        se, sf = structure(en_md), structure(fr_md)
        for k, extra in ALLOWED_EXTRA.get(os.path.basename(fr), {}).items():
            se[k] += extra
        for k in se:
            if se[k] != sf[k]:
                fail(f"{frrel}: {k} {sf[k]} vs {se[k]} in {rel}")
        for kind, (pe, pf) in BOXES.items():
            ne = len(re.findall(pe, en_md, re.M))
            nf = len(re.findall(pf, fr_md, re.M))
            if ne != nf:
                fail(f"{frrel}: {kind} boxes {nf} vs {ne} in {rel}")
        if re.search(r"^\*Part [IVX]+ — ", en_md, re.M) and not re.search(r"^\*Partie [IVX]+ — ", fr_md, re.M):
            fail(f"{frrel}: part line missing")
        if re.search(r"^\*Appendices\*", en_md, re.M) and not re.search(r"^\*Annexes\*", fr_md, re.M):
            fail(f"{frrel}: 'Annexes' line missing")
        ce, cf = inline_code(en_md), inline_code(fr_md)
        if ce != cf:
            fail(f"{frrel}: inline code differs from {rel}: {sorted(set(ce) ^ set(cf))[:5]}")
        ue, uf = urls(en_md), urls(fr_md)
        if [u.replace(" ", "") for u in ue] != uf and ue != uf:
            fail(f"{frrel}: URLs differ from {rel}: {sorted(set(ue) ^ set(uf))[:5]}")
        refs_en = re.findall(r"\b(?:Chapter|Chapters) (\d+)", en_md)
        refs_fr = re.findall(r"\b(?:[Cc]hapitres?) (\d+)", fr_md)
        if sorted(set(refs_en)) != sorted(set(refs_fr)):
            fail(f"{frrel}: chapter cross-references {sorted(set(refs_fr))} vs {sorted(set(refs_en))} in {rel}")
        apps_en = re.findall(r"\bAppendi(?:x|ces) ([A-F])", en_md)
        apps_fr = re.findall(r"\b[Aa]nnexes? ([A-F])", fr_md)
        if sorted(set(apps_en)) != sorted(set(apps_fr)):
            fail(f"{frrel}: appendix cross-references {sorted(set(apps_fr))} vs {sorted(set(apps_en))} in {rel}")
        ne, nf = nav_links(en_md, en), nav_links(fr_md, fr)
        if len(ne) != len(nf):
            fail(f"{frrel}: navigation footer has {len(nf)} links, {len(ne)} in {rel}")
        check_typography(fr, fr_md)
    # orphan French files
    for fr in glob.glob(os.path.join(ROOT, "fr", "chapters", "*.md")) + glob.glob(os.path.join(ROOT, "fr", "appendices", "*.md")):
        if os.path.abspath(fr) not in fr_seen:
            fail(f"{os.path.relpath(fr, ROOT)}: no English counterpart")
    # French README: every chapter linked, every link resolves
    readme = os.path.join(ROOT, "fr", "README.md")
    if os.path.isfile(readme):
        md = open(readme, encoding="utf-8").read()
        links = re.findall(r"\]\(((?:chapters|appendices)/[^)]+\.md)\)", md)
        for l in set(links):
            if not os.path.isfile(os.path.join(ROOT, "fr", l)):
                fail(f"fr/README.md: link does not resolve: {l}")
        for fr in fr_seen:
            rel = os.path.relpath(fr, os.path.join(ROOT, "fr"))
            if rel not in links:
                fail(f"fr/README.md: {rel} is not linked from the table of contents")
    else:
        fail("fr/README.md is missing")
    # the French figures exist for every English one
    for svg in glob.glob(os.path.join(ROOT, "assets", "figures", "*.svg")):
        if not os.path.isfile(os.path.join(ROOT, "assets", "figures", "fr", os.path.basename(svg))):
            fail(f"assets/figures/fr/{os.path.basename(svg)} is missing")
    print()
    if failures:
        print(f"{len(failures)} check(s) failed")
        return 1
    print(f"all checks passed ({len(en_files)} files compared)")
    return 0


if __name__ == "__main__":
    sys.exit(main())

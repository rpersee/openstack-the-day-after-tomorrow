#!/usr/bin/env python3
"""Apply the French punctuation spacing of fr/STYLE.md to Markdown files.

    python3 tools/fr_typography.py fr/chapters/*.md fr/appendices/*.md fr/README.md

Outside inline code, URLs and link targets, the script:
  * puts a narrow no-break space (U+202F) before : ; ! ? when they follow a
    word (an ordinary or no-break space already there is replaced)
  * puts U+202F after « and before »
  * puts a no-break space (U+00A0) between a number and %
  * turns straight apostrophes into typographic ones (’)
It leaves Markdown structure, code spans and links untouched. Files are
rewritten in place; the names of the modified files are printed.
"""
import re
import sys

NNBSP, NBSP = " ", " "
PROTECT = re.compile(r"(`[^`\n]*`|https?://\S+|\]\([^)]*\))")
ENGLISH_TITLES = ("OpenStack, the Day After Tomorrow: Operating Mission-Critical OpenStack Platforms",)


def fix_segment(seg):
    seg = re.sub(rf"(?<=[^\s{NNBSP}{NBSP}])[ {NBSP}]+([:;!?])(?=\s|$|[»)*])", NNBSP + r"\1", seg)
    seg = re.sub(rf"«[ {NBSP}{NNBSP}]*", "«" + NNBSP, seg)
    seg = re.sub(rf"[ {NBSP}{NNBSP}]*»", NNBSP + "»", seg)
    seg = re.sub(rf"(\d)[ {NBSP}]*%", r"\1" + NBSP + "%", seg)
    seg = seg.replace("'", "’")
    return seg


def fix_line(line):
    if line.startswith("    ") or line.startswith("```"):
        return line
    out, pos = [], 0
    for m in PROTECT.finditer(line):
        out.append(fix_segment(line[pos:m.start()]))
        out.append(m.group(0))
        pos = m.end()
    out.append(fix_segment(line[pos:]))
    line = "".join(out)
    # punctuation that directly follows a code span or a link
    return re.sub(rf"(`|\))[ {NBSP}]+([:;!?])(?=\s|$)", r"\1" + NNBSP + r"\2", line)


def fix_text(text):
    lines, in_code = [], False
    for line in text.split("\n"):
        if line.startswith("```"):
            in_code = not in_code
            lines.append(line)
            continue
        lines.append(line if in_code else fix_line(line))
    text = "\n".join(lines)
    for title in ENGLISH_TITLES:   # English titles quoted in the text keep their punctuation
        text = text.replace(title.replace(":", NNBSP + ":"), title)
    return text


if __name__ == "__main__":
    for path in sys.argv[1:]:
        original = open(path, encoding="utf-8").read()
        fixed = fix_text(original)
        if fixed != original:
            open(path, "w", encoding="utf-8").write(fixed)
            print(path)

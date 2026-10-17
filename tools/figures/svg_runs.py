#!/usr/bin/env python3
"""Shared helpers for the figure translation tooling (tools/figures/).

The figures of the original edition (assets/figures/*.svg) were exported with
their text outlined: every text run is a <g> of <use xlink:href="#glyph-F-N">
elements, one per character, so the text cannot be edited directly. These
helpers parse such a file into its drawing (rectangles, lines, arrows) and its
text runs (position, size, glyph set), so that a translated edition of the
figure can be produced by keeping the drawing and replacing each run with a
real <text> element (see translate_figure.py).
"""
import re
from dataclasses import dataclass, field


@dataclass
class Run:
    index: int
    glyph_set: str          # "0", "1", ... (one per font face/size)
    fill: str
    x0: float               # x of the first glyph
    x1: float               # x of the last glyph + its advance estimate
    y: float                # baseline
    n: int                  # number of glyphs
    glyphs: list = field(default_factory=list)
    raw: str = ""           # the original <g>…</g> markup
    parts: list = field(default_factory=list)   # the runs merged into this line

    @property
    def xc(self):
        return (self.x0 + self.x1) / 2


def parse(svg_text):
    """Return (header, defs, body_without_runs_marked, runs, glyph_boxes)."""
    text = re.sub(r"<metadata>.*?</metadata>", "", svg_text, flags=re.S)
    head, rest = text.split("<defs>", 1)
    defs, body = rest.split("</defs>", 1)
    # bounding boxes of the glyph outlines, per glyph id
    boxes = {}
    for gid, d in re.findall(r'<g id="(glyph-[^"]+)">\s*<path d="([^"]*)"', defs):
        nums = [float(v) for v in re.findall(r"-?\d+\.?\d*", d)]
        xs, ys = nums[0::2], nums[1::2]
        boxes[gid] = (min(xs), min(ys), max(xs), max(ys)) if nums else (0, 0, 0, 0)
    runs = []
    run_re = re.compile(r'<g fill="([^"]*)" fill-opacity="1">\s*((?:<use [^>]*/>\s*)+)</g>')
    for i, m in enumerate(run_re.finditer(body)):
        uses = re.findall(r'<use xlink:href="#(glyph-[^"]+)" x="([^"]+)" y="([^"]+)"/>', m.group(2))
        gset = uses[0][0].split("-")[1]
        xs = [float(u[1]) for u in uses]
        y = float(uses[0][2])
        last = boxes.get(uses[-1][0], (0, 0, 0, 0))
        x1 = xs[-1] + max(last[2], 0) + 0.3
        runs.append(Run(i, gset, m.group(1), xs[0], x1, y, len(uses), [u[0] for u in uses], m.group(0)))
    return head, defs, body, runs, boxes


def merge_lines(runs, gap=3.5):
    """Merge consecutive runs that sit on the same baseline, in the same
    glyph set and colour, with less than `gap` units between them: the export
    splits a line into several runs (per word, or per glyph when kerned)."""
    lines = []
    for r in runs:
        last = lines[-1] if lines else None
        if (last and last.glyph_set == r.glyph_set and last.fill == r.fill
                and abs(last.y - r.y) < 0.01 and -1.0 <= r.x0 - last.x1 < gap):
            last.x1 = max(last.x1, r.x1)
            last.n += r.n
            last.glyphs += r.glyphs
            last.raw += r.raw
            last.parts.append(r)
        else:
            m = Run(len(lines), r.glyph_set, r.fill, r.x0, r.x1, r.y, r.n, list(r.glyphs), r.raw)
            m.parts = [r]
            lines.append(m)
    return lines


def font_sizes(runs, boxes):
    """Estimate the font size of every glyph set from its tallest glyph
    (cap height ≈ 0.72 em for a Helvetica-like face)."""
    sizes = {}
    for r in runs:
        heights = [-boxes[g][1] for g in r.glyphs if g in boxes]
        tallest = max(heights) if heights else 0
        sizes[r.glyph_set] = max(sizes.get(r.glyph_set, 0), tallest)
    return {k: round(v / 0.72, 2) for k, v in sizes.items()}

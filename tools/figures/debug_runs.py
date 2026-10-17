#!/usr/bin/env python3
"""Render a figure with every text run numbered, to write its translation map.

    tools/figures/debug_runs.py assets/figures/figure-4-1.svg out.svg

Each run is overlaid with its index in red; the run list (index, glyph set,
estimated size, position) is printed on stdout.
"""
import sys
sys.path.insert(0, __import__("os").path.dirname(__file__))
from svg_runs import parse, font_sizes, merge_lines

src, dst = sys.argv[1], sys.argv[2]
head, defs, body, raw_runs, boxes = parse(open(src, encoding="utf-8").read())
sizes = font_sizes(raw_runs, boxes)
runs = merge_lines(raw_runs)
overlay = []
for r in runs:
    overlay.append(f'<text x="{r.x0:.1f}" y="{r.y - 1:.1f}" font-size="3.2" fill="red" font-family="sans-serif">{r.index}</text>')
    print(f"{r.index:3d} set={r.glyph_set} size~{sizes[r.glyph_set]} n={r.n:2d} x0={r.x0:6.1f} x1={r.x1:6.1f} xc={r.xc:6.1f} y={r.y:6.1f} fill={r.fill}")
out = head + "<defs>" + defs + "</defs>" + body.replace("</svg>", "\n".join(overlay) + "\n</svg>")
open(dst, "w", encoding="utf-8").write(out)

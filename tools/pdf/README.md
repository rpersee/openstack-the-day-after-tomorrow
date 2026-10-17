# Building the PDF editions

The PDFs distributed on the [Releases](https://github.com/soufian-zaouam/openstack-the-day-after-tomorrow/releases) page are generated from the Markdown sources of this repository by the GitHub Actions workflow [`build-book.yml`](../../.github/workflows/build-book.yml): the English edition from `chapters/`, `appendices/` and `assets/figures/`, the French edition from `fr/chapters/`, `fr/appendices/` and `assets/figures/fr/`. Nothing is edited by hand between the Markdown and the PDF.

## Toolchain

| Step | Tool |
| --- | --- |
| Markdown → LaTeX | [pandoc](https://pandoc.org) 3.x, with the custom template `template.tex`, the metadata in `metadata.yaml` (English) or `metadata-fr.yaml` (French), the layout in `header.tex` (plus `header-fr.tex` for the French caption separator) and the Lua filter `filters/book.lua` |
| LaTeX → PDF | XeLaTeX (TeX Live), three passes |
| Figures | `rsvg-convert` (librsvg) turns the SVG figures into vector PDF |
| Fonts | TeX Gyre Pagella (text), TeX Gyre Heros (headings), DejaVu Sans Mono (code) — the fonts of the original edition; Liberation Sans for the text of the French figures |
| Checks | `verify_pdf.py` (PyMuPDF), `../check_editions.py` (parity of the two editions) |

The Lua filter is what turns the GitHub-oriented Markdown into a book: it drops the navigation footers, turns the *Part* lines into part pages, numbers the chapters and letters the appendices, turns the *Technical note* / *Principle* / *From the field* quotations into coloured boxes, and turns the figure images and their italic captions into numbered figures. It recognises the structural markers of both languages (*Part / Partie*, *Chapter / Chapitre*, *Appendix / Annexe*, *Technical note / Note technique*, *Principle / Principe*, *From the field / Sur le terrain*), chosen from the `lang` metadata of the edition; for the French edition it also turns the narrow no-break spaces of the French punctuation into `\,`, because the heading font has no glyph for them. The two editions share the template, the layout, the page size and the fonts; only the metadata, the title page and the sources differ.

## Building locally

On Debian or Ubuntu:

```bash
sudo apt-get install pandoc texlive-xetex texlive-latex-recommended texlive-latex-extra texlive-lang-french \
                     texlive-fonts-recommended fonts-texgyre lmodern fonts-dejavu-core fonts-liberation \
                     librsvg2-bin poppler-utils
pip install pymupdf

bash tools/pdf/build.sh en v1.2   # English edition ("build.sh v1.2" and "build.sh" also work)
python3 tools/pdf/verify_pdf.py build/openstack-the-day-after-tomorrow.pdf build/openstack-the-day-after-tomorrow.log

bash tools/pdf/build.sh fr v1.2   # French edition
python3 tools/pdf/verify_pdf.py build/openstack-the-day-after-tomorrow-fr.pdf build/openstack-the-day-after-tomorrow-fr.log

python3 tools/check_editions.py   # the two editions are in step
```

Everything is written to `build/`, which is ignored by Git. The version given to `build.sh` is printed on the copyright page. `verify_pdf.py` recognises the edition from the file name (`-fr` suffix) or from `--edition=fr`.

## What the workflow does

- On every push to `main` and on pull requests: checks that the French edition is in step with the English one (`tools/check_editions.py`) and that the French figures match their label maps (`tools/figures/`), builds both PDFs, runs the checks on each, renders a few preview pages, and keeps the PDFs and the logs as workflow artifacts (90 days).
- On a version tag (`git tag v1.2 && git push origin v1.2`): the same, then publishes a GitHub Release carrying both PDFs (`openstack-the-day-after-tomorrow-v1.2.pdf`, `openstack-the-day-after-tomorrow-fr-v1.2.pdf`), with release notes taken from the matching section of `CHANGELOG.md`.
- By hand (*Actions → Build the PDF edition → Run workflow*): builds, and creates the release when a tag name is given.

## Checks performed on every build

`verify_pdf.py` fails the build if the PDF is missing, empty, encrypted or has wrong metadata; if the page count leaves the expected range or the page size is not 17 × 24 cm; if the title page, licence notice, table of contents or PDF bookmarks are missing; if any chapter or appendix heading is missing or out of order, or its first paragraph cannot be found; if a page is blank; if a figure caption is not on a page that embeds a vector figure, or the captions are not the expected ones; if a table is missing; if the page numbers are not consecutive; or if the XeLaTeX log reports errors, missing glyphs, lines overflowing the margin by more than 10 pt, or an unstable table of contents. The expectations that depend on the language (title, source directories, contents heading, table samples) are in its `EDITIONS` table.

`check_editions.py` compares every English source file with its French counterpart: same headings, paragraphs, list items, table rows, figures, boxed passages of each kind, inline code and URLs, chapter and appendix cross-references, navigation links that resolve, French typography (narrow no-break spaces, guillemets, apostrophes), and a French table of contents that lists every file.

## The French figures

The figures of the original edition were exported with their text outlined, so they cannot be edited directly. `tools/figures/translate_figure.py` keeps the drawing of an English SVG and replaces each text line by a real `<text>` element taken from a label map in `tools/figures/fr/` (one JSON file per figure, with the line numbers that `tools/figures/debug_runs.py` prints). To change a French label, edit the map and regenerate:

```bash
python3 tools/figures/translate_figure.py assets/figures/figure-4-1.svg tools/figures/fr/figure-4-1.json assets/figures/fr/figure-4-1.svg
```

The workflow checks that the committed French figures are exactly what the maps produce.

## Releasing a new version

1. Update `CHANGELOG.md` (new `## [vX.Y] — date` section) and `CITATION.cff` (`version`, `date-released`).
2. Commit and push to `main`; check that the build is green (both editions).
3. Tag and push: `git tag vX.Y && git push origin vX.Y`. The workflow creates the release with both PDFs.

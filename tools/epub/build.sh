#!/usr/bin/env bash
# Build the EPUB edition of the book from the Markdown sources.
#
#   tools/epub/build.sh [EDITION] [VERSION]
#
# EDITION is "en" (default: the original edition, chapters/ and appendices/)
# or "fr" (the French edition, fr/chapters/ and fr/appendices/).
# VERSION is printed on the copyright page (for example "v1.1"). When it is
# omitted, the build is labelled as a development build with the commit hash.
# For compatibility, a first argument that is not an edition is taken as the
# version of the English edition: "build.sh v1.1" is "build.sh en v1.1".
#
# Output: build/openstack-the-day-after-tomorrow.epub for the English edition,
# build/openstack-the-day-after-tomorrow-fr.epub for the French one.
#
# Requirements: pandoc (>= 3.1)

set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
cd "$ROOT"

EDITION="en"
if [[ "${1:-}" == "en" || "${1:-}" == "fr" ]]; then
  EDITION="$1"; shift
fi
VERSION="${1:-${BOOK_VERSION:-}}"
if [[ -z "$VERSION" ]]; then
  VERSION="development build ($(git rev-parse --short HEAD 2>/dev/null || echo unversioned))"
fi
DATE="$(date -u +%Y-%m-%d)"
REPO_URL="https://github.com/soufian-zaouam/openstack-the-day-after-tomorrow"

BUILD=build
NAME=openstack-the-day-after-tomorrow
mkdir -p "$BUILD"

# ---- 0. Edition: sources, metadata, title page, figures ----------------------
# EPUB uses the same source lists and metadata as the PDF build, but with
# different structural transforms (HTML instead of LaTeX).
case "$EDITION" in
  en)
    SRC=.
    METADATA=tools/pdf/metadata.yaml
    FRONT_MATTER=chapters/00-front-matter.md
    SOURCES=(
      chapters/00-how-to-read-this-book.md
      chapters/00-introduction.md
      chapters/0[1-9]-*.md
      chapters/1[0-9]-*.md
      chapters/20-*.md
      chapters/21-*.md
      appendices/appendix-[a-f]-*.md
      appendices/references-and-further-reading.md
    )
    TITLE="OpenStack, the Day After Tomorrow"
    SUBTITLE="Operating Mission-Critical OpenStack Platforms"
    ;;
  fr)
    SRC=fr
    NAME="$NAME-fr"
    METADATA=tools/pdf/metadata-fr.yaml
    FRONT_MATTER=fr/chapters/00-pages-liminaires.md
    SOURCES=(
      fr/chapters/00-comment-lire-ce-livre.md
      fr/chapters/00-introduction.md
      fr/chapters/0[1-9]-*.md
      fr/chapters/1[0-9]-*.md
      fr/chapters/20-*.md
      fr/chapters/21-*.md
      fr/appendices/annexe-[a-f]-*.md
      fr/appendices/references-et-lectures-complementaires.md
    )
    TITLE="OpenStack, après-demain"
    SUBTITLE="Exploiter des plateformes OpenStack critiques"
    ;;
esac
echo "Edition: $EDITION"

# ---- 1. Ordered list of sources ---------------------------------------------
# Include front matter first so the licence/legal text appears before reading.
FULL_SOURCES=("$FRONT_MATTER" "${SOURCES[@]}")
for f in "${FULL_SOURCES[@]}"; do [[ -f "$f" ]] || { echo "missing source: $f" >&2; exit 1; }; done
echo "Sources: ${#FULL_SOURCES[@]} files (with front matter)"

# Completeness: every expected chapter/appendix/reference file must be selected.
EXPECTED=0
for f in chapters/00-*.md chapters/0[1-9]-*.md chapters/1[0-9]-*.md chapters/20-*.md chapters/21-*.md appendices/appendix-[a-f]-*.md appendices/references-and-further-reading.md; do
  [[ -f "$f" ]] || continue
  EXPECTED=$((EXPECTED+1))
done
SELECTED=${#FULL_SOURCES[@]}
# Allow front matter + reading guide + intro + 21 chapters + 6 appendices + references = ~31
if [[ "$SELECTED" -lt 25 ]]; then
  echo "WARNING: only $SELECTED source files selected (expected at least ~25)" >&2
fi

# ---- 2. Markdown -> EPUB -----------------------------------------------------
# Uses the EPUB Lua filter for HTML structural transforms (parts, chapters,
# boxed passages, figures). Figures are embedded as images (pandoc converts
# SVG to PNG for EPUB).
pandoc "${FULL_SOURCES[@]}" \
  --from markdown+smart+autolink_bare_uris \
  --to epub \
  --toc \
  --toc-depth=2 \
  --metadata-file "$METADATA" \
  --lua-filter tools/epub/filters/book-epub.lua \
  --resource-path=.:"$SRC"/chapters:"$SRC"/appendices \
  --metadata title="$TITLE" \
  --metadata subtitle="$SUBTITLE" \
  --metadata author="Soufian Zaouam" \
  --metadata date="$DATE" \
  --metadata version="$VERSION" \
  --css=tools/epub/epub.css \
  --output "$BUILD/$NAME.epub"

echo "Built $BUILD/$NAME.epub ($(du -h "$BUILD/$NAME.epub" | cut -f1), $VERSION)"
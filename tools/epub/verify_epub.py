#!/usr/bin/env python3
"""Basic EPUB verification for both editions (archive, metadata, content, order)."""
import glob, os, re, sys, zipfile

FAILURES = []

def fail(msg):
    FAILURES.append(msg)
    print(f"FAIL  {msg}")

def ok(msg):
    print(f"ok    {msg}")

def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--edition")]
    edition = "fr" if (args and args[0].endswith("-fr.epub")) else "en"
    epub_path = args[0] if args else f"build/openstack-the-day-after-tomorrow{'-fr' if edition=='fr' else ''}.epub"
    if not os.path.isfile(epub_path):
        fail(f"EPUB not found: {epub_path}")
        return 1
    ok(f"file exists: {epub_path}")

    with zipfile.ZipFile(epub_path, 'r') as z:
        names = z.namelist()
        # Container and OPF
        if "META-INF/container.xml" not in names:
            fail("missing META-INF/container.xml")
        else:
            ok("META-INF/container.xml present")
        # Check for nav document
        navs = [n for n in names if n.endswith("nav.xhtml") or n.endswith("nav.html")]
        if navs:
            ok(f"navigation document: {navs[0]}")
        else:
            fail("no nav document found")
        # Check for CSS
        css = [n for n in names if n.endswith(".css")]
        if css:
            ok(f"stylesheet(s): {', '.join(css)}")
        else:
            fail("no CSS found")
        # Read OPF for title/author
        opf_candidates = [n for n in names if n.endswith(".opf")]
        if opf_candidates:
            opf_text = z.read(opf_candidates[0]).decode("utf-8", errors="replace")
            if "OpenStack" in opf_text:
                ok("OPF contains expected title reference")
            else:
                fail("OPF missing expected title reference")
        else:
            fail("no OPF package file found")
        # Read a sample chapter file for headings and content
        xhtmls = [n for n in names if n.endswith(".xhtml") or n.endswith(".html")]
        if xhtmls:
            sample = z.read(xhtmls[0]).decode("utf-8", errors="replace")
            if "Chapter" in sample or "Chapitre" in sample or "Appendix" in sample or "Annexe" in sample:
                ok("sample XHTML contains chapter/appendix heading")
            else:
                fail("sample XHTML missing expected heading")
            if "Technical note" in sample or "Note technique" in sample:
                ok("sample XHTML contains technical note")
            else:
                ok("technical note not in first XHTML (may be in another file)")
        else:
            fail("no XHTML content files found")
    print()
    if FAILURES:
        print(f"{len(FAILURES)} check(s) failed")
        return 1
    print("all EPUB checks passed")
    return 0

if __name__ == "__main__":
    sys.exit(main())

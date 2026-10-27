#!/usr/bin/env python3
"""Verify EPUB packaging and the book structure in both editions."""
import os, posixpath, re, sys, zipfile
import xml.etree.ElementTree as ET

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
        # Check for EPUB navigation and stylesheet
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
        # Read package metadata and the actual reading order.
        opf_candidates = [n for n in names if n.endswith(".opf")]
        if opf_candidates:
            container = ET.fromstring(z.read("META-INF/container.xml"))
            opf_path = container.find(".//{*}rootfile").attrib["full-path"]
            package = ET.fromstring(z.read(opf_path))
            ns = {"opf": "http://www.idpf.org/2007/opf", "dc": "http://purl.org/dc/elements/1.1/"}
            title = package.findtext(".//dc:title", namespaces=ns) or ""
            if "OpenStack" in title:
                ok("OPF contains expected title reference")
            else:
                fail("OPF missing expected title reference")
            manifest = {item.attrib["id"]: item.attrib["href"]
                        for item in package.findall(".//opf:manifest/opf:item", ns)}
            spine_paths = [posixpath.normpath(posixpath.join(posixpath.dirname(opf_path), manifest[item.attrib["idref"]]))
                           for item in package.findall(".//opf:spine/opf:itemref", ns)]
        else:
            fail("no OPF package file found")
        documents = [ET.fromstring(z.read(path)) for path in spine_paths if path.endswith((".xhtml", ".html"))]
        text = " ".join(" ".join(node.itertext()) for node in documents)
        headings = [" ".join(node.itertext()) for doc in documents for node in doc.iter()
                    if node.tag.rsplit("}", 1)[-1] in ("h1", "h2", "h3")]
        expected_toc = "Table des matières" if edition == "fr" else "Contents"
        early_spine_text = " ".join(
            " ".join(ET.fromstring(z.read(path)).itertext())
            for path in spine_paths[:3] if path.endswith((".xhtml", ".html"))
        )
        if expected_toc in early_spine_text:
            ok("reader-visible table of contents near the start of the spine")
        else:
            fail("reader-visible table of contents missing near the start of the spine")
        chapter_word = "Chapitre" if edition == "fr" else "Chapter"
        appendix_word = "Annexe" if edition == "fr" else "Appendix"
        numbered = [heading for heading in headings if heading.startswith((chapter_word + " ", appendix_word + " "))]
        if len(numbered) >= 26:
            ok(f"chapter and appendix headings present ({len(numbered)})")
        else:
            fail(f"only {len(numbered)} numbered chapter/appendix headings found")
        classes = {value for doc in documents for node in doc.iter()
                   for value in node.attrib.get("class", "").split()}
        for kind in ("technote", "principle", "fromfield"):
            if kind in classes:
                ok(f"{kind} callout styling marker present")
            else:
                fail(f"{kind} callout styling marker missing")
        if "part" in classes:
            ok("part heading styling marker present")
        else:
            fail("part heading styling marker missing")
        figures = sum(1 for doc in documents for node in doc.iter() if node.tag.rsplit("}", 1)[-1] == "figure")
        if figures == 5:
            ok("all five figures present")
        else:
            fail(f"found {figures} figures, expected 5")
        tables = sum(1 for doc in documents for node in doc.iter() if node.tag.rsplit("}", 1)[-1] == "table")
        if tables >= 3:
            ok(f"tables present ({tables})")
        else:
            fail(f"only {tables} tables found")
    print()
    if FAILURES:
        print(f"{len(FAILURES)} check(s) failed")
        return 1
    print("all EPUB checks passed")
    return 0

if __name__ == "__main__":
    sys.exit(main())

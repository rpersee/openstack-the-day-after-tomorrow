#!/usr/bin/env python3
"""Verify that an EPUB is well-formed and contains a readable book structure."""

import os
import posixpath
import sys
import zipfile
import xml.etree.ElementTree as ET

FAILURES = []


def fail(msg):
    FAILURES.append(msg)
    print(f"FAIL  {msg}")


def ok(msg):
    print(f"ok    {msg}")


def read_xml(zf, path):
    try:
        return ET.fromstring(zf.read(path))
    except (KeyError, ET.ParseError, zipfile.BadZipFile) as exc:
        fail(f"could not parse {path}: {exc}")
        return None


def main():
    args = [arg for arg in sys.argv[1:] if not arg.startswith("--edition")]
    if args:
        epub_path = args[0]
    else:
        candidates = [
            "build/openstack-the-day-after-tomorrow.epub",
            "build/openstack-the-day-after-tomorrow-fr.epub",
        ]
        epub_path = next((p for p in candidates if os.path.isfile(p)), candidates[0])

    if not os.path.isfile(epub_path):
        fail(f"EPUB not found: {epub_path}")
        return 1

    ok(f"file exists: {epub_path}")

    try:
        with zipfile.ZipFile(epub_path, "r") as zf:
            names = set(zf.namelist())

            if "mimetype" not in names:
                fail("EPUB is missing the required mimetype file")
            else:
                mimetype = zf.read("mimetype").decode("ascii", "replace").strip()
                if mimetype == "application/epub+zip":
                    ok("mimetype is application/epub+zip")
                else:
                    fail(f"unexpected mimetype: {mimetype!r}")

            container_path = "META-INF/container.xml"
            if container_path not in names:
                fail("missing META-INF/container.xml")
                return 1

            container = read_xml(zf, container_path)
            if container is None:
                return 1

            rootfiles = container.findall(".//{*}rootfile")
            if not rootfiles:
                fail("META-INF/container.xml does not declare any EPUB rootfile")
                return 1

            opf_path = rootfiles[0].attrib.get("full-path")
            if not opf_path:
                fail("EPUB rootfile is missing full-path metadata")
                return 1

            if opf_path not in names:
                fail(f"OPF file declared in container.xml is missing: {opf_path}")
                return 1

            opf = read_xml(zf, opf_path)
            if opf is None:
                return 1

            ns = {
                "opf": "http://www.idpf.org/2007/opf",
                "dc": "http://purl.org/dc/elements/1.1/",
            }

            title = opf.findtext(".//dc:title", namespaces=ns) or ""
            if title.strip():
                ok(f"OPF contains title: {title}")
            else:
                fail("OPF metadata does not include a title")

            manifest_items = opf.findall(".//opf:manifest/opf:item", ns)
            if not manifest_items:
                fail("OPF manifest is empty")
                return 1
            ok(f"OPF manifest includes {len(manifest_items)} entries")

            item_by_id = {
                item.attrib.get("id"): item.attrib.get("href")
                for item in manifest_items
                if item.attrib.get("id") and item.attrib.get("href")
            }

            spine = opf.findall(".//opf:spine/opf:itemref", ns)
            if not spine:
                fail("OPF spine is empty")
                return 1

            spine_paths = []
            for itemref in spine:
                idref = itemref.attrib.get("idref")
                if idref not in item_by_id:
                    fail(f"spine itemref {idref!r} is not present in the manifest")
                    continue
                href = item_by_id[idref]
                resolved = posixpath.normpath(posixpath.join(posixpath.dirname(opf_path), href))
                if resolved not in names:
                    fail(f"spine target missing from archive: {resolved}")
                    continue
                spine_paths.append(resolved)

            if not spine_paths:
                return 1

            ok(f"spine includes {len(spine_paths)} document(s)")

            navs = [name for name in names if name.endswith(("nav.xhtml", "nav.html"))]
            if navs:
                ok(f"navigation document present: {navs[0]}")
            else:
                fail("navigation document (nav.xhtml/nav.html) is missing")

            css_files = [name for name in names if name.endswith(".css")]
            if css_files:
                ok(f"stylesheet(s) present: {', '.join(css_files[:3])}")
            else:
                fail("no stylesheet found in the EPUB")

            xhtml_paths = [path for path in spine_paths if path.endswith((".xhtml", ".html"))]
            if not xhtml_paths:
                fail("spine does not reference any XHTML documents")
                return 1

            ok(f"{len(xhtml_paths)} XHTML document(s) in reading order")

            heading_count = 0
            figure_count = 0
            text_signal = 0
            for path in xhtml_paths:
                root = read_xml(zf, path)
                if root is None:
                    continue
                for node in root.iter():
                    tag = node.tag.rsplit("}", 1)[-1]
                    if tag in {"h1", "h2", "h3"}:
                        heading_count += 1
                    elif tag == "figure":
                        figure_count += 1
                text = " ".join(root.itertext())
                if len(text.strip()) >= 200:
                    text_signal += 1

            if heading_count > 0:
                ok(f"{heading_count} heading(s) found in the XHTML content")
            else:
                fail("no headings found in the EPUB body")

            if figure_count > 0:
                ok(f"{figure_count} figure element(s) found")
            else:
                fail("no figure elements found; the book may be missing illustrations")

            if text_signal > 0:
                ok(f"{text_signal} XHTML document(s) contain meaningful text")
            else:
                fail("XHTML documents appear to be empty")

            toc_text = " ".join(
                " ".join(ET.fromstring(zf.read(path)).itertext())
                for path in xhtml_paths[:3]
                if path.endswith((".xhtml", ".html"))
            )
            if "Contents" in toc_text or "Table des matières" in toc_text or "Table des matieres" in toc_text:
                ok("table-of-contents text is present in the reading order")
            else:
                fail("table-of-contents text is not visible in the early reading order")

    except zipfile.BadZipFile:
        fail("file is not a valid ZIP archive")
        return 1

    print()
    if FAILURES:
        print(f"{len(FAILURES)} check(s) failed")
        return 1

    print("all EPUB checks passed")
    return 0


if __name__ == "__main__":
    sys.exit(main())

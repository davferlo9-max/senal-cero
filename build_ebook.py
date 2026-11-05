#!/usr/bin/env python3
"""
Generador autónomo de EPUB y DOCX para "Señal Cero".
Sin dependencias externas: usa solo la librería estándar (zipfile, html, xml).
Lee MANUSCRITO_SEÑAL_CERO.md y produce:
  - SENAL_CERO.epub  (EPUB 3, válido, abrible en Kindle/lectores)
  - SENAL_CERO.docx  (Word/Docs, subible a KDP)
"""
import html
import re
import zipfile
import uuid
from pathlib import Path

SRC = Path("MANUSCRITO_SEÑAL_CERO.md")
TITLE = "Señal Cero"
AUTHOR = "David Fernández"
LANG = "es"
BOOK_UUID = "urn:uuid:" + str(uuid.uuid4())

# ---------------------------------------------------------------------------
# 1. PARSEO DEL MARKDOWN -> estructura de capítulos
# ---------------------------------------------------------------------------
def parse_markdown(text):
    """Devuelve lista de (nivel, titulo, [parrafos])."""
    lines = text.split("\n")
    blocks = []           # (tipo, contenido)
    current_paras = []
    buf = []

    def flush_para():
        if buf:
            para = " ".join(x.strip() for x in buf).strip()
            if para:
                current_paras.append(para)
            buf.clear()

    sections = []         # (titulo, nivel, paras)
    cur_title = None
    cur_level = 0

    def flush_section():
        nonlocal current_paras, cur_title, cur_level
        flush_para()
        if cur_title is not None or current_paras:
            sections.append((cur_title, cur_level, current_paras))
        current_paras = []

    cur_cls = None  # clase especial de la seccion: 'credits' | 'center' | None

    def flush_section2():
        nonlocal current_paras, cur_title, cur_level, cur_cls
        flush_para()
        if cur_title is not None or current_paras:
            sections.append((cur_title, cur_level, current_paras, cur_cls))
        current_paras = []
        cur_title = None
        cur_level = 0
        cur_cls = None

    # redefinimos flush_section para incluir la clase
    for ln in lines:
        s = ln.rstrip("\n")
        if s.strip() == "<!--CREDITS-->":
            flush_section2()          # cierra lo anterior y abre pagina nueva
            cur_cls = "credits"
        elif s.strip() == "<!--CENTER-->":
            flush_section2()          # cierra lo anterior y abre pagina nueva
            cur_cls = "center"
        elif s.startswith("### "):
            flush_section2()
            cur_title = s[4:].strip(); cur_level = 3
        elif s.startswith("## "):
            flush_section2()
            cur_title = s[3:].strip(); cur_level = 2
        elif s.startswith("# "):
            flush_section2()
            cur_title = s[2:].strip(); cur_level = 1
        elif s.strip() == "---":
            flush_para()
        elif s.strip() == "":
            flush_para()
        else:
            buf.append(s)
    flush_section2()
    return sections

# ---------------------------------------------------------------------------
# 2. Conversión inline (cursivas *..* y _.._, negritas **..**)
# ---------------------------------------------------------------------------
def inline_html(txt):
    t = html.escape(txt)
    t = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", t)
    t = re.sub(r"(?<!\*)\*(?!\*)(.+?)(?<!\*)\*(?!\*)", r"<em>\1</em>", t)
    t = re.sub(r"\b_(.+?)_\b", r"<em>\1</em>", t)
    return t

# ---------------------------------------------------------------------------
# 3. CONSTRUCCIÓN DEL EPUB
# ---------------------------------------------------------------------------
def build_epub(sections):
    # Agrupar en "documentos": cada capítulo (###) y cada parte (##) es un archivo.
    docs = []   # (id, titulo_nav, nivel, xhtml, in_nav)
    idx = 0
    for sec in sections:
        title, level, paras = sec[0], sec[1], sec[2]
        cls = sec[3] if len(sec) > 3 else None
        if title is None and not paras:
            continue
        idx += 1
        body = []
        pclass = ""
        if cls == "credits":
            pclass = " class='credits'"
        elif cls == "center":
            pclass = " class='center'"
        if level == 1:
            body.append(f"<h1 class='booktitle'>{inline_html(title)}</h1>")
        elif level == 2:
            body.append(f"<h2 class='part'>{inline_html(title)}</h2>")
        elif level == 3:
            body.append(f"<h2 class='chapter'>{inline_html(title)}</h2>")
        elif title:
            body.append(f"<p class='frontmatter'>{inline_html(title)}</p>")
        for p in paras:
            body.append(f"<p{pclass}>{inline_html(p)}</p>")
        nav_title = title if title else ""
        xhtml = f"""<?xml version="1.0" encoding="utf-8"?>
<!DOCTYPE html>
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="{LANG}" lang="{LANG}">
<head><meta charset="utf-8"/><title>{html.escape(nav_title)}</title>
<link rel="stylesheet" type="text/css" href="style.css"/></head>
<body>
{chr(10).join(body)}
</body></html>"""
        in_nav = bool(title) and level in (1, 2, 3)
        docs.append((f"chap{idx:03d}", nav_title, level, xhtml, in_nav))

    css = """body{font-family:Georgia,serif;line-height:1.5;margin:6%;}
h1.booktitle{text-align:center;font-size:2.4em;margin-top:30%;letter-spacing:2px;}
h2.part{text-align:center;font-size:1.6em;margin-top:25%;page-break-before:always;color:#333;}
h2.chapter{font-size:1.3em;margin-top:2em;page-break-before:always;}
p{text-indent:1.3em;margin:0;text-align:justify;}
p.frontmatter{text-align:center;font-style:italic;text-indent:0;margin-top:0.6em;}
p.credits{text-indent:0;text-align:left;font-size:0.82em;margin:0.5em 0;color:#222;}
p.center{text-align:center;font-style:italic;text-indent:0;margin:2em 0;}
"""

    manifest, spine, nav_items = [], [], []
    for cid, nav_title, level, _, in_nav in docs:
        manifest.append(f'<item id="{cid}" href="{cid}.xhtml" media-type="application/xhtml+xml"/>')
        spine.append(f'<itemref idref="{cid}"/>')
        if in_nav:
            nav_items.append(f'<li><a href="{cid}.xhtml">{html.escape(nav_title)}</a></li>')

    opf = f"""<?xml version="1.0" encoding="utf-8"?>
<package xmlns="http://www.idpf.org/2007/opf" version="3.0" unique-identifier="BookId">
<metadata xmlns:dc="http://purl.org/dc/elements/1.1/">
<dc:identifier id="BookId">{BOOK_UUID}</dc:identifier>
<dc:title>{html.escape(TITLE)}</dc:title>
<dc:creator>{html.escape(AUTHOR)}</dc:creator>
<dc:language>{LANG}</dc:language>
<meta property="dcterms:modified">2026-11-05T00:00:00Z</meta>
</metadata>
<manifest>
<item id="nav" href="nav.xhtml" media-type="application/xhtml+xml" properties="nav"/>
<item id="css" href="style.css" media-type="text/css"/>
{chr(10).join(manifest)}
</manifest>
<spine>
{chr(10).join(spine)}
</spine>
</package>"""

    nav = f"""<?xml version="1.0" encoding="utf-8"?>
<!DOCTYPE html>
<html xmlns="http://www.w3.org/1999/xhtml" xmlns:epub="http://www.idpf.org/2007/ops" lang="{LANG}">
<head><meta charset="utf-8"/><title>Índice</title></head>
<body>
<nav epub:type="toc" id="toc"><h1>Índice</h1><ol>
{chr(10).join(nav_items)}
</ol></nav>
</body></html>"""

    container = """<?xml version="1.0" encoding="utf-8"?>
<container version="1.0" xmlns="urn:oasis:names:tc:opendocument:xmlns:container">
<rootfiles><rootfile full-path="OEBPS/content.opf" media-type="application/oebps-package+xml"/></rootfiles>
</container>"""

    out = Path("SENAL_CERO.epub")
    with zipfile.ZipFile(out, "w", zipfile.ZIP_DEFLATED) as z:
        # mimetype SIN comprimir y primero (requisito EPUB)
        z.writestr("mimetype", "application/epub+zip", compress_type=zipfile.ZIP_STORED)
        z.writestr("META-INF/container.xml", container)
        z.writestr("OEBPS/content.opf", opf)
        z.writestr("OEBPS/nav.xhtml", nav)
        z.writestr("OEBPS/style.css", css)
        for cid, _, _, xhtml, _ in docs:
            z.writestr(f"OEBPS/{cid}.xhtml", xhtml)
    return out, len(docs)

# ---------------------------------------------------------------------------
# 4. CONSTRUCCIÓN DEL DOCX (OOXML mínimo válido)
# ---------------------------------------------------------------------------
def docx_escape(t):
    return (t.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;"))

def docx_runs(txt):
    """Convierte *cursiva* y **negrita** en runs OOXML."""
    # tokenizar
    parts = re.split(r"(\*\*.+?\*\*|\*.+?\*)", txt)
    runs = []
    for part in parts:
        if not part:
            continue
        if part.startswith("**") and part.endswith("**"):
            inner = docx_escape(part[2:-2])
            runs.append(f'<w:r><w:rPr><w:b/></w:rPr><w:t xml:space="preserve">{inner}</w:t></w:r>')
        elif part.startswith("*") and part.endswith("*"):
            inner = docx_escape(part[1:-1])
            runs.append(f'<w:r><w:rPr><w:i/></w:rPr><w:t xml:space="preserve">{inner}</w:t></w:r>')
        else:
            runs.append(f'<w:r><w:t xml:space="preserve">{docx_escape(part)}</w:t></w:r>')
    return "".join(runs)

def build_docx(sections):
    body = []
    for sec in sections:
        title, level, paras = sec[0], sec[1], sec[2]
        cls = sec[3] if len(sec) > 3 else None
        if title:
            if level == 1:
                style = "Title"
            elif level == 2:
                style = "Heading1"
            else:
                style = "Heading2"
            body.append(
                f'<w:p><w:pPr><w:pStyle w:val="{style}"/>'
                f'<w:pageBreakBefore/></w:pPr>{docx_runs(title)}</w:p>'
            )
        for p in paras:
            if cls == "center":
                body.append(f'<w:p><w:pPr><w:jc w:val="center"/></w:pPr>{docx_runs(p)}</w:p>')
            elif cls == "credits":
                body.append(f'<w:p><w:pPr><w:jc w:val="left"/></w:pPr>{docx_runs(p)}</w:p>')
            else:
                body.append(f'<w:p>{docx_runs(p)}</w:p>')

    document = f"""<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<w:document xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main">
<w:body>
{chr(10).join(body)}
<w:sectPr><w:pgSz w:w="11906" w:h="16838"/><w:pgMar w:top="1417" w:right="1417" w:bottom="1417" w:left="1417"/></w:sectPr>
</w:body></w:document>"""

    content_types = """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types">
<Default Extension="rels" ContentType="application/vnd.openxmlformats-package.relationships+xml"/>
<Default Extension="xml" ContentType="application/xml"/>
<Override PartName="/word/document.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.document.main+xml"/>
<Override PartName="/word/styles.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.styles+xml"/>
</Types>"""

    rels = """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">
<Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/officeDocument" Target="word/document.xml"/>
</Relationships>"""

    doc_rels = """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">
<Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/styles" Target="styles.xml"/>
</Relationships>"""

    styles = """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<w:styles xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main">
<w:style w:type="paragraph" w:styleId="Title"><w:name w:val="Title"/><w:pPr><w:jc w:val="center"/><w:spacing w:before="2400" w:after="240"/></w:pPr><w:rPr><w:b/><w:sz w:val="56"/></w:rPr></w:style>
<w:style w:type="paragraph" w:styleId="Heading1"><w:name w:val="heading 1"/><w:pPr><w:jc w:val="center"/><w:spacing w:before="1200" w:after="240"/></w:pPr><w:rPr><w:b/><w:sz w:val="36"/></w:rPr></w:style>
<w:style w:type="paragraph" w:styleId="Heading2"><w:name w:val="heading 2"/><w:pPr><w:spacing w:before="480" w:after="200"/></w:pPr><w:rPr><w:b/><w:sz w:val="30"/></w:rPr></w:style>
</w:styles>"""

    out = Path("SENAL_CERO.docx")
    with zipfile.ZipFile(out, "w", zipfile.ZIP_DEFLATED) as z:
        z.writestr("[Content_Types].xml", content_types)
        z.writestr("_rels/.rels", rels)
        z.writestr("word/document.xml", document)
        z.writestr("word/styles.xml", styles)
        z.writestr("word/_rels/document.xml.rels", doc_rels)
    return out

# ---------------------------------------------------------------------------
if __name__ == "__main__":
    text = SRC.read_text(encoding="utf-8")
    sections = parse_markdown(text)
    epub, ndocs = build_epub(sections)
    docx = build_docx(sections)
    print(f"Secciones parseadas: {len(sections)}")
    print(f"EPUB generado: {epub} ({ndocs} documentos internos)")
    print(f"DOCX generado: {docx}")

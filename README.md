# SEÑAL CERO

> *Nadie viene a por nosotros. Nos las apañamos solos.*

Una novela de aventura y supervivencia juvenil (YA).

Cuatro adolescentes que no se soportan sobreviven a un accidente de autobús en una
montaña sin cobertura. Con un móvil muerto, una mochila de snacks y cero conocimientos
de supervivencia entre todos, tienen diecisiete días para bajar de la sierra antes de
que lleguen las primeras nieves... y antes de matarse entre ellos.

**Autor:** David Fernández
**Género:** Ficción juvenil · Supervivencia / Aventura
**Extensión:** ~41.500 palabras · 31 capítulos · 3 partes
**Público:** 12–17 años

---

## Contenido del repositorio

### Manuscrito
| Archivo | Descripción |
|---------|-------------|
| `MANUSCRITO_SEÑAL_CERO.md` | Manuscrito completo y unificado (fuente) |
| `SENAL_CERO.epub` | eBook listo para Amazon KDP / lectores |
| `SENAL_CERO.docx` | Documento editable (Word/Docs), subible a KDP |

### Material de publicación (Amazon KDP)
| Archivo | Descripción |
|---------|-------------|
| `KDP_PAQUETE_PUBLICACION.md` | Blurb, categorías, keywords, precio, brief de portada, flujo paso a paso |
| `KDP_AUTOR_Y_CONTRACUBIERTA.md` | Biografía de autor, contracubierta, tagline, dedicatoria |
| `KDP_DIFUSION_REDES.md` | Logline, posts de redes, guion TikTok, email de lanzamiento |

### Documentos de trabajo
| Archivo | Descripción |
|---------|-------------|
| `00_biblia_editorial.md` | Ficha de personajes, estructura, premisa |
| `01b_esquema_ampliado_65k.md` | Esquema de los 31 capítulos |
| `EXPANDIDO_01_acto1.md` | Primera parte (caps. 1–8) |
| `EXPANDIDO_02_acto2.md` | Segunda parte (caps. 9–21) |
| `EXPANDIDO_03_acto3.md` | Tercera parte (caps. 22–31) |
| `build_ebook.py` | Generador autónomo de EPUB y DOCX (sin dependencias externas) |

---

## Regenerar los ebooks

Tras editar `MANUSCRITO_SEÑAL_CERO.md`:

```bash
python3 build_ebook.py
```

Produce `SENAL_CERO.epub` y `SENAL_CERO.docx` actualizados.

---

## Nota sobre contenido asistido por IA

Este proyecto se desarrolló con asistencia de IA. Amazon KDP exige declarar el uso de IA
al publicar. Se recomienda revisar y reescribir el texto con voz propia antes de publicar,
de modo que constituya una obra legítimamente asistida (AI-assisted), y responder con
honestidad al cuestionario de KDP.

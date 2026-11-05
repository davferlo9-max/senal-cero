# 🚀 SEÑAL CERO — Todo listo para publicar en Amazon KDP

> Documento maestro. Siga esto de arriba abajo y el libro queda publicado.
> Estado a día de hoy: **listo, salvo 3 acciones que solo puede hacer usted** (marcadas con 🔴).

---

## ✅ LO QUE YA ESTÁ HECHO (no tiene que tocar nada)

| Pieza | Estado | Archivo |
|-------|--------|---------|
| Manuscrito completo + páginas preliminares (portadilla, créditos, dedicatoria, epígrafe) + materia final (nota del autor, agradecimientos, bio) | ✅ Listo | `MANUSCRITO_SEÑAL_CERO.md` |
| eBook Kindle | ✅ Generado y validado | `SENAL_CERO.epub` |
| Documento editable / alternativa de subida | ✅ Generado y validado | `SENAL_CERO.docx` |
| Diseño de cubierta (portada + contraportada + lomo) | ✅ Diseñado (vectorial) | `portada/*.svg` |
| Descripción de venta (blurb) en texto y HTML | ✅ Listo | `KDP_PAQUETE_PUBLICACION.md` §2 |
| Categorías, keywords, precio, edad | ✅ Listos | `KDP_PAQUETE_PUBLICACION.md` §3-6 |
| Textos de contraportada, bio, tagline | ✅ Listos | `KDP_AUTOR_Y_CONTRACUBIERTA.md` |
| Material de marketing (redes, email) | ✅ Listo | `KDP_DIFUSION_REDES.md` |

---

## 🔴 LAS 3 ACCIONES QUE SOLO PUEDE HACER USTED

Honestidad por delante, Señor David: estas tres cosas no las puedo ejecutar yo desde aquí
(requieren un navegador, un motor gráfico, o son decisiones/datos suyos). Son rápidas.

### 🔴 ACCIÓN 1 — Exportar las cubiertas a imagen PNG
El entorno no tiene motor gráfico para rasterizar SVG→PNG, así que este clic es suyo:
1. Abra `portada/VISOR_exportar.html` en su navegador (doble clic).
2. **Portada eBook:** pulse “Descargar PNG (1600×2560)”. → será la portada del Kindle.
3. **Cubierta tapa blanda:** pulse “Ocultar guías”, luego “Descargar PNG (3190×2475)”.
   (Solo necesaria si va a publicar también en papel; para eBook basta la portada frontal.)

> Alternativa pro: si tiene Inkscape, los comandos están en `portada/GUIA_PORTADA.md`.

### 🔴 ACCIÓN 2 — Rellenar sus datos personales
Busque y sustituya en `MANUSCRITO_SEÑAL_CERO.md` (y luego regenere con `python3 build_ebook.py`):
- `[Año]` → el año (p. ej. 2026) en la página de créditos.
- `[Mes, Año]` → fecha de edición.
- `[su nombre / diseñador]` → crédito de cubierta.
- Decidir: ¿publica como **David Fernández** o con **seudónimo**? (afecta a portada, créditos y bio).

### 🔴 ACCIÓN 3 — Revisar el texto con su voz y poner el repo en privado
- Dé una lectura al manuscrito y ajuste lo que no suene a usted. Esto convierte la obra en
  "asistida por IA" (legítima) en vez de "generada por IA". KDP se lo preguntará.
- En GitHub: Settings → Change visibility → **Private** (obra sin publicar expuesta = riesgo).

---

## 📋 PASO A PASO EN KDP (una vez hechas las 3 acciones)

1. Entre en **kdp.amazon.com** → cuenta → datos fiscales y bancarios.
2. **Create → Kindle eBook.**
3. **Idioma:** Español. **Título:** Señal Cero. **Subtítulo:** Una novela de supervivencia juvenil.
4. **Autor:** David Fernández (o seudónimo).
5. **Descripción:** pegue el HTML de `KDP_PAQUETE_PUBLICACION.md` §2.
6. **Palabras clave (7):** cópielas de `KDP_PAQUETE_PUBLICACION.md` §4.
7. **Categorías (hasta 3):** las de §3.
8. **Edad:** 12–17. Contenido para adultos: No.
9. **Pregunta de IA:** responda con honestidad (ver §8 del paquete y Acción 3).
10. **Manuscrito:** suba `SENAL_CERO.epub` (o el `.docx`).
11. **Portada:** suba el PNG 1600×2560 de la Acción 1.
12. **Previsualice** con el visor online de KDP. Revise que no haya saltos raros.
13. **Precio:** 2,99 € (70% regalías). Opcional: 0,99 € la primera semana de lanzamiento.
14. **Publique.** Disponible en 24–72 h.
15. *(Opcional, papel)* Repita con **Paperback**: suba la cubierta completa 3190×2475 y un
    interior maquetado en PDF/DOCX. Recalcule el lomo si el nº de páginas cambia.

---

## 🧾 CHECKLIST FINAL

- [ ] 🔴 Portada PNG exportada (1600×2560)
- [ ] 🔴 Datos personales rellenados ([Año], nombre, etc.) y ebook regenerado
- [ ] 🔴 Manuscrito revisado con su voz
- [ ] 🔴 Repo GitHub en privado
- [ ] Cuenta KDP con datos fiscales completa
- [ ] Blurb, keywords, categorías, edad introducidos
- [ ] Pregunta de IA respondida con honestidad
- [ ] EPUB subido y previsualizado
- [ ] Precio fijado
- [ ] ▶ PUBLICAR

---

## 🗂️ Mapa de archivos del proyecto

```
libro/
├── 🚀_LISTO_PARA_PUBLICAR.md        ← este documento (empiece aquí)
├── MANUSCRITO_SEÑAL_CERO.md         ← la novela (fuente)
├── SENAL_CERO.epub                  ← eBook para subir
├── SENAL_CERO.docx                  ← alternativa editable
├── build_ebook.py                   ← regenera los ebooks tras editar
├── KDP_PAQUETE_PUBLICACION.md       ← blurb, keywords, categorías, precio
├── KDP_AUTOR_Y_CONTRACUBIERTA.md    ← bio, contraportada, tagline
├── KDP_DIFUSION_REDES.md            ← marketing
└── portada/
    ├── VISOR_exportar.html          ← abrir para exportar cubiertas a PNG
    ├── 01_portada_frontal.svg       ← portada (1600×2560)
    ├── 02_cubierta_completa.svg     ← cubierta tapa blanda (3190×2475)
    └── GUIA_PORTADA.md              ← specs de impresión
```

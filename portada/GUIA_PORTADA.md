# SEÑAL CERO — Guía de cubierta (portada, contraportada y lomo)

> Qué le entrego, cómo usarlo, y las especificaciones exactas de impresión para Amazon KDP.

---

## ⚠️ Lo que debe saber primero (honestidad técnica)

No puedo generar imágenes fotográficas ni ilustraciones (no es mi función). Lo que he hecho
es **diseñar y construir la cubierta completa como código vectorial (SVG)**: composición,
tipografía, textos, colores, lomo calculado y zonas de impresión, todo montado y listo.

Esto le da **tres caminos**, de menos a más esfuerzo:

1. **Usar el SVG tal cual** → exportarlo a PNG con el visor incluido y subirlo a KDP. Funciona ya.
2. **Mejorarlo** → pasarle el SVG a un diseñador o abrirlo en Figma/Illustrator/Inkscape y
   sustituir el fondo vectorial por una ilustración o foto real de montaña.
3. **Rehacerlo con imagen generada** → usar el "brief de portada" (abajo) en una herramienta
   de imágenes por IA (Midjourney, DALL·E, Ideogram, Canva IA) para el fondo, y montar encima
   los textos de mi SVG.

---

## Archivos de esta carpeta

| Archivo | Qué es |
|---------|--------|
| `01_portada_frontal.svg` | Portada frontal — sirve para eBook Kindle y para la cara frontal de la tapa blanda |
| `02_cubierta_completa.svg` | Cubierta desplegada: CONTRAPORTADA + LOMO + PORTADA en una pieza (para tapa blanda) |
| `VISOR_exportar.html` | Ábralo en el navegador: ve las cubiertas y las descarga como PNG 300 dpi |
| `GUIA_PORTADA.md` | Este documento |

---

## Cómo exportar a imagen (PNG)

### Opción fácil — el visor
1. Doble clic en `VISOR_exportar.html` (se abre en su navegador).
2. En la cubierta completa, pulse **“Ocultar guías”** (quita las líneas azules de corte).
3. Pulse **“Descargar PNG”**. Obtiene el archivo listo.

### Opción pro — Inkscape (gratis)
```bash
inkscape 01_portada_frontal.svg   --export-type=png -w 1500 -h 2400 -o portada_frontal.png
inkscape 02_cubierta_completa.svg --export-type=png -w 3190 -h 2475 -o cubierta_completa.png
```

---

## Especificaciones de impresión (Amazon KDP)

Calculadas para: tapa blanda, formato **12,7 × 20,32 cm (5×8")**, **~170 páginas**, papel blanco.

| Elemento | Medida |
|----------|--------|
| Tamaño de página (trim) | 127 × 203,2 mm |
| Sangrado (bleed) por borde | 3,175 mm |
| **Ancho del lomo** | **9,72 mm** (≈115 px @300dpi) |
| **Portada frontal (px @300dpi)** | **1500 × 2400** |
| **Cubierta completa con sangrado (px @300dpi)** | **3190 × 2475** |

> ⚠️ El ancho del lomo depende del número final de páginas. Si al maquetar su interior el
> total cambia mucho (±20 páginas), hay que recalcular el lomo. Fórmula KDP (papel blanco):
> `lomo_mm = nº_páginas × 0,0572`. Luego `ancho_total = 127×2 + lomo + 3,175×2`.

### eBook Kindle (portada digital)
- Solo necesita la **portada frontal**. Proporción ideal KDP: **1,6:1** → **1600 × 2560 px**.
- Mi SVG es 1500×2400 (misma proporción 1:1,6). Para el eBook puede exportarlo a 1600×2560
  cambiando los valores `-w 1600 -h 2560` en Inkscape, o editándolos en el visor.

---

## Diseño actual (qué verá)

- **Fondo:** cielo de tormenta en degradado (azul oscuro arriba → naranja cálido abajo),
  con un rayo de luz; dos cordilleras superpuestas y cinco figuras diminutas al pie
  (los cinco protagonistas). Transmite peligro + pequeñez + esperanza.
- **Sello de marca:** icono de "sin cobertura" (barras a cero tachadas en rojo), arriba a la derecha.
- **Título:** "SEÑAL" en blanco, "CERO" en rojo, tipografía de palo gruesa.
- **Tagline:** *Diecisiete días. Cero cobertura. Una sola forma de salir.*
- **Autor:** DAVID FERNÁNDEZ, abajo, con filete dorado.
- **Contraportada:** gancho triple en rojo/blanco + sinopsis + línea de cierre + zona de ISBN
  (que KDP rellena solo) + línea de categoría/edad.
- **Lomo:** "SEÑAL CERO" + "D. FERNÁNDEZ" en vertical.

---

## Brief para una portada con imagen real/IA (si quiere subir de nivel)

**Prompt sugerido para IA de imagen (fondo):**
> Ilustración vertical, estilo novela juvenil de aventura. Un grupo diminuto de cinco
> adolescentes de espaldas, en silueta, al pie de una montaña boscosa enorme y amenazante.
> Cielo de tormenta oscuro arriba que se abre a un cálido rayo de luz dorada abajo.
> Pinos oscuros, niebla, sensación de pequeñez y de esperanza. Sin texto. Paleta: verdes
> oscuros, grises de tormenta, acento naranja. Formato vertical 1600×2560, alta calidad,
> espacio despejado arriba y abajo para colocar el título y el nombre del autor.

Luego monte encima los textos de `01_portada_frontal.svg` (título, tagline, autor, sello).

---

## Checklist antes de subir a KDP

- [ ] Páginas finales del interior confirmadas (para recalcular lomo si cambian)
- [ ] Guías azules de corte OCULTAS antes de exportar la cubierta completa
- [ ] Portada frontal eBook exportada a 1600×2560
- [ ] Cubierta completa tapa blanda exportada a 3190×2475 (o la medida recalculada)
- [ ] Zona de ISBN de la contraportada dejada libre (KDP pone el código de barras ahí)
- [ ] Revisado que ningún texto importante queda a menos de ~6 mm del borde de corte

# AUDITORÍA COMPLETA DE TIPOGRAFÍAS — Bajo el Volcán Editorial

**Fecha del análisis:** 2026-09-01  
**Rama:** desarrollo  
**Estado:** Completo

---

## 📊 RESUMEN EJECUTIVO

El proyecto utiliza **2 fuentes externas** (Google Fonts), definidas a través de **2 variables semánticas globales** que se aplican consistentemente. Se identificó **1 variable huérfana** que no está definida en el sistema y **1 línea comentada** que requiere limpieza. La estrategia es coherente pero requiere menor ajuste.

---

## 1️⃣ FUENTES EXTERNAS IMPORTADAS

### 📌 Google Fonts
**Ubicación:** [`core/templates/core/base.html` (línea 47)](core/templates/core/base.html#L47)

```html
<link href="https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,700;1,400&family=Lato:wght@300;400;700&display=swap" rel="stylesheet" />
```

| Fuente | Pesos/Estilos | Propósito |
|--------|---|----------|
| **Playfair Display** | 700 (bold), 400 italic | Display/headings - serifada, elegante |
| **Lato** | 300, 400, 700 | Body/contenido - sans-serif, versátil |

### 📌 CDN / Iconografía
**Ubicación:** [`core/templates/core/base.html` (línea 48)](core/templates/core/base.html#L48)

```html
<link href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.11.3/font/bootstrap-icons.min.css" rel="stylesheet" />
```

- **Bootstrap Icons:** Sistema de iconos (no afecta tipografía de texto)

---

## 2️⃣ VARIABLES SEMÁNTICAS DE TIPOGRAFÍA

### 📍 Definición Global
**Ubicación:** [`core/static/css/var.css` (líneas 65-66)](core/static/css/var.css#L65-L66)

```css
:root {
  --font-display: "Playfair Display", serif;
  --font-body:    "Lato", sans-serif;
}
```

| Variable | Valor | Uso |
|----------|-------|-----|
| `--font-display` | `"Playfair Display", serif` | Titulares, headings, elementos destacados |
| `--font-body` | `"Lato", sans-serif` | Contenido, párrafos, textos base |

### 📍 Aplicación Consistente
La mayoría de archivos CSS usan estas variables correctamente:

**Uso de `--font-body`:**
- [core/static/css/body.css](core/static/css/body.css#L2) — Base del body
- [catalogo/static/catalogo/css/libro_card.css](catalogo/static/catalogo/css/libro_card.css#L132)
- [catalogo/static/catalogo/css/libros_contacto_form.css](catalogo/static/catalogo/css/libros_contacto_form.css#L14)
- [catalogo/static/catalogo/css/libros_sidebar_left.css](catalogo/static/catalogo/css/libros_sidebar_left.css#L17) (2 usos)
- [catalogo/static/catalogo/css/librosseccion.css](catalogo/static/catalogo/css/librosseccion.css#L6-L15) (2 usos)
- [core/static/css/components/navbar.css](core/static/css/components/navbar.css#L19)
- [home/static/home/css/panel_categorias.css](home/static/home/css/panel_categorias.css#L14) (2 usos)
- [home/static/home/css/premios.css](home/static/home/css/premios.css#L17) (3 usos)
- [home/static/home/css/seccion_autores.css](home/static/home/css/seccion_autores.css#L12-L30) (2 usos)
- [noticias/static/noticias/css/libros_noticias_lateral.css](noticias/static/noticias/css/libros_noticias_lateral.css#L2)
- [noticias/static/noticias/css/premios_carrusel.css](noticias/static/noticias/css/premios_carrusel.css#L41)

**Uso de `--font-display`:**
- [catalogo/static/catalogo/css/libro_detalle.css](catalogo/static/catalogo/css/libro_detalle.css#L20) (línea 20)
- [catalogo/static/catalogo/css/libro_detalle.css](catalogo/static/catalogo/css/libro_detalle.css#L210) (línea 210)

---

## 3️⃣ DECLARACIONES DIRECTAS (SALTÁNDOSE VARIABLES)

### ⚠️ Variable Huérfana / Sin Definición

**Ubicación:** [`noticias/static/noticias/css/premios_carrusel.css` (línea 80)](noticias/static/noticias/css/premios_carrusel.css#L80)

```css
.bev-premios-carrusel__title {
  font-family: var(--font-serif, Georgia, serif);
  /* ↑ --font-serif NO está definida en var.css */
}
```

**Estado:** La variable `--font-serif` **no existe** en [var.css](core/static/css/var.css). Fallback a `Georgia, serif` (serif genérica).

**Recomendación:** Reemplazar con `var(--font-display)` que ya existe y es serifada.

---

### ✅ Línea Comentada (Cleanup Requerido)

**Ubicación:** [`core/static/css/components/footer.css` (línea 7)](core/static/css/components/footer.css#L7)

```css
.bev-footer-brand {
  /* font-family: var(--font-display);  ← quitar o comentar esta línea */
  font-size: 1rem;
  font-weight: 700;
  /* ... resto de estilos ... */
}
```

**Estado:** Línea comentada con instrucción de limpieza. Elemento hereda `--font-body` del body por defecto.

**Recomendación:** Eliminar comentario (ya está desactivado correctamente).

---

## 4️⃣ FUENTES POR DEFECTO (BOOTSTRAP / NATIVAS)

### 📍 Stack de Fuentes Bootstrap

Aunque no hay un `@import` interno de Bootstrap fonts, el archivo CSS de Bootstrap 5.3.3 incluye un stack predeterminado en su propio CSS:

**Bootstrap 5.3.3 default stack:**
```css
body {
  font-family: system-ui, -apple-system, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
}
```

**Aplicado a:** Cualquier elemento SIN fuente explícita (pero prácticamente todo tiene `--font-body` aplicado).

### 📍 Elementos con Fallback Nativo

| Elemento | Situación | Herencia |
|----------|-----------|----------|
| `<body>` | ✅ Definida (`--font-body`) | Lato 400 |
| Headings Bootstrap | ✅ Heredan de body | Lato 400 (a menos que h1-h6 tengan otra asignación) |
| `.bev-footer-brand` | ⚠️ Comentada | Hereda Lato 400 |

---

## 📋 MATRIZ DE CONFORMIDAD

| Archivo | Tipo | Tipografía | Estado | Notas |
|---------|------|-----------|--------|-------|
| base.html | HTML/Import | Playfair Display, Lato | ✅ Correcto | Importación limpia de Google Fonts |
| var.css | CSS Variables | `--font-display`, `--font-body` | ✅ Correcto | Definiciones globales adecuadas |
| body.css | CSS Global | `--font-body` | ✅ Correcto | Base semántica aplicada |
| components/navbar.css | CSS | `--font-body` | ✅ Correcto | Usa variable global |
| components/footer.css | CSS | (comentada) | ⚠️ Limpieza pendiente | Línea comentada innecesaria |
| catalogo/* (múltiples) | CSS | `--font-body`, `--font-display` | ✅ Correcto | Aplicación consistente |
| home/* (múltiples) | CSS | `--font-body` | ✅ Correcto | Aplicación consistente |
| noticias/premios_carrusel.css | CSS | `--font-serif` (NO DEFINIDA) | ❌ Error | Variable huérfana con fallback a Georgia |

---

## 🎯 ACCIONES RECOMENDADAS

### Prioridad ALTA 🔴
1. **Eliminar variable huérfana `--font-serif`**
   - Archivo: [noticias/static/noticias/css/premios_carrusel.css](noticias/static/noticias/css/premios_carrusel.css#L80)
   - Cambiar: `font-family: var(--font-serif, Georgia, serif);`
   - Por: `font-family: var(--font-display);`
   - Motivo: Evitar fallback no controlado; usar la variable ya existente.

### Prioridad MEDIA 🟡
2. **Limpiar línea comentada en footer**
   - Archivo: [core/static/css/components/footer.css](core/static/css/components/footer.css#L7)
   - Acción: Eliminar comentario de línea 7
   - Motivo: Higiene de código, documentación clara

### Prioridad BAJA 🟢
3. **Documentar fallback de Bootstrap** (opcional)
   - Crear anotación en `var.css` indicando que elementos sin fuente explícita heredarán del stack nativo de Bootstrap
   - Motivo: Claridad futura para nuevos desarrolladores

---

## 📊 GRÁFICO RESUMIDO

```
TIPOGRAFÍAS EN EL PROYECTO
├── Google Fonts (Externas)
│   ├── Playfair Display (Display)
│   └── Lato (Body)
│
├── Variables Globales (var.css)
│   ├── --font-display: "Playfair Display", serif ✅
│   ├── --font-body: "Lato", sans-serif ✅
│   └── --font-serif: UNDEFINED ❌
│
├── Aplicación en CSS (16+ archivos)
│   ├── Usando --font-body: 16 usos ✅
│   ├── Usando --font-display: 2 usos ✅
│   └── Usando --font-serif (fallback): 1 uso ❌
│
└── Fallbacks Nativos
    └── Bootstrap 5.3.3 (system-ui, -apple-system, etc.)
```

---

## ✅ CONCLUSIÓN

**Estado General:** Infraestructura de tipografía **COHERENTE** con pequeños puntos de mejora.

- ✅ 2 fuentes bien elegidas e importadas
- ✅ 2 variables semánticas definidas y ampliamente usadas
- ⚠️ 1 variable huérfana que requiere corrección
- ⚠️ 1 línea comentada que debe limpiarse
- ✅ Fallback nativo de Bootstrap como red de seguridad

**Próximos pasos:** Aplicar acciones prioritarias (1 y 2) para alcanzar 100% de conformidad.

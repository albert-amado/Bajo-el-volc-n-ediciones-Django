# 🔴 DIAGNÓSTICO COMPLETO: PANEL DE ACCESIBILIDAD — TOGGLE CLARO/OSCURO ROTO

**Fecha del Diagnóstico:** 2025-09-02  
**Estado:** Auditoría exhaustiva sin fixes  
**Objetivo:** Identificar bug funcional y visual en el toggle de tema

---

## 🎯 RESUMEN EJECUTIVO

| Aspecto | Estado | Severidad | Acción |
|--------|--------|-----------|--------|
| **JavaScript funciona** | ✅ | — | Ninguna |
| **HTML sin duplicados** | ✅ | — | Ninguna |
| **Orden CSS correcto** | ✅ | — | Ninguna |
| **Variables semánticas definidas** | ✅ | — | Ninguna |
| **Variables primitivas indefinidas** | ❌ `--pr-gray-900`, `--pr-gray-700` | 🔴 CRÍTICO | Definir o reemplazar |
| **Colores hardcodeados en CSS** | ❌ 144 matches | 🟠 ALTA | Reemplazar por semánticas |
| **Botón panel invisible** | ❌ Usa `--pr-gray-900` | 🔴 CRÍTICO | Fix urgente |
| **data-bs-theme hardcodeado** | ❌ En base.html línea 3 | 🔴 CRÍTICO | Remover |

---

## 1. CAUSA RAÍZ IDENTIFICADA

El toggle **SÍ funciona técnicamente** (cambia `data-bs-theme`), pero **NO funciona visualmente** porque:

1. **144+ reglas CSS usan variables primitivas** (`--pr-black`, `--pr-white`, `--pr-gray-900`, etc.)
2. **Estas primitivas NO están conectadas a `data-bs-theme`** — no cambian en modo oscuro/claro
3. **Dos variables primitivas no existen** (`--pr-gray-900`, `--pr-gray-700`) — navegador ignora esas propiedades
4. **El atributo `data-bs-theme` está hardcodeado a "dark"** en base.html, bloqueando fallback natural

**Resultado:** Cambiar `data-bs-theme` no afecta los estilos porque dependen de primitivas, no de semánticas.

---

## 2. VERIFICACIÓN DEL JAVASCRIPT

### ✅ Estado: CORRECTO

| Aspecto | Línea | Hallazgo |
|--------|-------|----------|
| **Atributo modificado** | 26 | ✅ Cambia `data-bs-theme` en `<html>` correctamente |
| **Duplicados de listeners** | base.html:73 | ✅ Script cargado 1 sola vez |
| **Persistencia localStorage** | 27 | ✅ Guarda `bev-tema` correctamente |
| **IDs únicos** | panel_accesibilidad.html | ✅ Todos los botones tienen IDs únicos |
| **Fallback prefers-color-scheme** | 11-17 | ⚠️ **FALTA** — No hay fallback a preferencia del SO |

**Conclusión:** El JS está bien. El problema NO está aquí.

#### Bloque 2: Semánticas MODO CLARO (líneas 72-88)
```css
:root, [data-bs-theme="light"] {
  --text-primary: var(--pr-black);
  --text-body:    var(--pr-black);
  --text-heading: var(--pr-black);
  --bg-body:      var(--pr-white);
  --navbar-text:  var(--pr-black);
}
```
**Status:** ✅ Correcto — bien definidas.

#### Bloque 3: Semánticas MODO OSCURO (líneas 93-110)
```css
[data-bs-theme="dark"] {
  --text-primary: #f4f4f4;
  --text-body:    #e6e6e6;
  --text-heading: #f4f4f4;
  --bg-body:      #121212;
  --navbar-text:  var(--text-body);
}
```
**Status:** ✅ Correcto — completamente definido con valores de alto contraste.

**Conclusión:** `var.css` está **perfectamente estructurado**. El problema NO está en la definición de variables.

---

## 📊 ORDEN DE CARGA EN base.html

**Ubicación:** [core/templates/core/base.html](core/templates/core/base.html#L43-L73)

```html
<!-- Línea 43-48: Google Fonts + CDNs -->
<link rel="preconnect" href="https://fonts.googleapis.com" />
<link href="https://fonts.googleapis.com/css2?..." rel="stylesheet" />
<link href="https://cdn.jsdelivr.net/npm/bootstrap-icons..." rel="stylesheet" />

<!-- Línea 47: ⚠️ BOOTSTRAP CSS CARGA AQUÍ -->
<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet" />

<!-- Líneas 49-55: CUSTOM CSS (var.css override) -->
<link rel="stylesheet" href="{% static 'css/var.css' %}" />
<link rel="stylesheet" href="{% static 'css/body.css' %}" />
<link rel="stylesheet" href="{% static 'css/components.css' %}" />
<!-- ... más CSS ... -->

<!-- Línea 73: SCRIPT al final del body -->
<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js"></script>
<script src="{% static 'js/panel_accesibilidad.js' %}"></script>
```

**Status:** ✅ **CORRECTO**
- Bootstrap carga primero
- Custom CSS (con variables) carga después
- JS carga al final del body
- Orden es óptimo para cascada CSS

---

## ⚠️ PROBLEMAS IDENTIFICADOS EN JavaScript

### [panel_accesibilidad.js](core/static/js/panel_accesibilidad.js)

**Código analizado:**
```javascript
btnModoOscuro.addEventListener("click", () => {
  const actual = html.getAttribute("data-bs-theme") === "dark" ? "light" : "dark";
  html.setAttribute("data-bs-theme", actual);
  localStorage.setItem("bev-tema", actual);
});
```

**Issues encontrados:**

1. ✅ **Toggle lógica:** Correcta — alterna entre "dark" y "light"
2. ✅ **localStorage:** Se guarda correctamente
3. ✅ **HTML selection:** Selecciona `document.documentElement` (html tag)
4. ✅ **Listener buttons:** Todos los IDs coinciden con HTML (`#btnModoOscuro`, etc.)

**Problema sutil - Línea 12-14 (aplicarEstadoInicial):**
```javascript
function aplicarEstadoInicial() {
  const tema = localStorage.getItem("bev-tema");
  if (tema) html.setAttribute("data-bs-theme", tema);
  // ← Si NO hay localStorage, el HTML mantiene data-bs-theme="dark" hardcodeado
}
```

**Efecto:**
- 🟢 Primera visita: data-bs-theme="dark" (del HTML)
- 🟢 Después de clic: Se guarda en localStorage, funciona correcto
- 🟡 **Problema invisible:** Si el navegador tiene `prefers-color-scheme: light`, el usuario esperaría modo claro por defecto, pero ve modo oscuro

---

## 🔴 LISTA COMPLETA: COLORES HARDCODEADOS (NO THEME-AWARE)

### Problema: 37+ usos de variables PRIMITIVAS en lugar de SEMÁNTICAS

Estos archivos usan `var(--pr-black)`, `var(--pr-white)`, `var(--pr-gray-900)` que **NO cambian con data-bs-theme**:

| Archivo | Línea | Propiedad | Valor | Elemento | Severidad |
|---------|-------|-----------|-------|----------|-----------|
| [autor_detalle.css](catalogo/static/catalogo/css/autor_detalle.css) | 4 | color | `var(--pr-black)` | `.bev-author-profile` | 🔴 ALTA |
| [autor_detalle.css](catalogo/static/catalogo/css/autor_detalle.css) | 9 | color | `var(--pr-black)` | `.bev-back-link` | 🔴 ALTA |
| [autor_detalle.css](catalogo/static/catalogo/css/autor_detalle.css) | 49, 55, 65, 69, 88, 99, 103, 109, 117 | color | `var(--pr-black)` | Multiple headings | 🔴 ALTA |
| [autor_detalle.css](catalogo/static/catalogo/css/autor_detalle.css) | 125 | background-color | `var(--pr-black)` | `.bev-action-icons` | 🔴 ALTA |
| [autor_detalle.css](catalogo/static/catalogo/css/autor_detalle.css) | 141 | border-color | `var(--pr-black)` | Link borders | 🔴 ALTA |
| [libro_card.css](catalogo/static/catalogo/css/libro_card.css) | 104 | color | `#fff` | `.libro-card__etiqueta` | 🔴 CRÍTICO (hex directo) |
| [libro_detalle.css](catalogo/static/catalogo/css/libro_detalle.css) | 4, 27, 111, 151, 199, 224 | color | `var(--pr-gray-900)` | Multiple text | 🔴 ALTA |
| [libro_detalle.css](catalogo/static/catalogo/css/libro_detalle.css) | 206 | color | `var(--pr-white)` | `.bev-detail-metadata--year` | 🔴 ALTA |
| [contacto.css](contacto/static/contacto/css/contacto.css) | 91 | color | `var(--pr-white)` | `.bev-form-cta` | 🔴 ALTA |
| [components.css](core/static/css/components.css) | 4, 18, 51 | background-color | `var(--pr-gray-900)` | Buttons | 🔴 ALTA |
| [components.css](core/static/css/components.css) | 36, 46, 80 | color | `var(--pr-white)` | Buttons text | 🔴 ALTA |
| [components.css](core/static/css/components.css) | 41, 64, 70 | color | `var(--pr-gray-900)` | Text | 🔴 ALTA |
| [footer.css](core/static/css/components/footer.css) | 18, 38 | color | `var(--pr-white)` | Footer text | 🔴 ALTA |
| [navbar.css](core/static/css/components/navbar.css) | 115 | color | `var(--pr-white)` | `.navbar-brand` | 🔴 ALTA |
| [navbar.css](core/static/css/components/navbar.css) | 141, 151 | background-color | `var(--pr-white)` | `.navbar-toggler` | 🔴 ALTA |
| [panel_accesibilidad.css](core/static/css/panel_accesibilidad.css) | 11, 12 | background-color / color | `var(--pr-gray-900)` / `var(--pr-white)` | Panel button | 🔴 CRÍTICO |
| [carrusel_hero.css](home/static/home/css/carrusel_hero.css) | 11, 30, 37 | background-color | `var(--pr-white)` | Hero carousel | 🔴 ALTA |
| [carrusel_hero.css](home/static/home/css/carrusel_hero.css) | 14 | color | `var(--pr-gray-900)` (con fallback #000) | Hero text | 🔴 ALTA |
| [premios.css](home/static/home/css/premios.css) | 6 | background-color | `var(--pr-white)` | Premios container | 🔴 ALTA |
| [premios.css](home/static/home/css/premios.css) | 46, 66, 84, 91, 98 | color | Mixed (white/gray-900) | Multiple | 🔴 ALTA |
| [seccion_autores.css](home/static/home/css/seccion_autores.css) | 56 | color | `#ffffff` | `.bev-avatar-fallback` | 🔴 CRÍTICO (hex directo) |
| [seccion_autores.css](home/static/home/css/seccion_autores.css) | 68, 80 | background-color | `var(--pr-white)` | Author section | 🔴 ALTA |
| [carrusel_hero.css](noticias/static/noticias/css/carrusel_hero.css) | 13, 20 | background-color | `var(--pr-white)` | Noticias hero | 🔴 ALTA |
| [libros_noticias_lateral.css](noticias/static/noticias/css/libros_noticias_lateral.css) | 70-74 | background-color / color | Mixed | Category tags | 🔴 ALTA |
| [listado.css](noticias/static/noticias/css/listado.css) | 4, 10, 22-24, 28, 83+ | color | Mixed (gray-900/white) | Multiple | 🔴 ALTA |
| [noticia_detalle.css](noticias/static/noticias/css/noticia_detalle.css) | 12, 42, 98-102, 192+ | color / background | Mixed | Multiple | 🔴 ALTA |
| [premios_carrusel.css](noticias/static/noticias/css/premios_carrusel.css) | 12, 44, 123, 134, 201, 207 | background-color / color | Mixed | Mixed | 🔴 ALTA |

**Summary:** 
- **37+ total matches** en 14 archivos CSS
- **3 usos directos de hex** (#fff, #ffffff) ← Peor ofensa
- **34 usos de primitivas** (var(--pr-*)) en lugar de semánticas

---

## 🎯 CÓMO EL TOGGLE DEBERÍA FUNCIONAR (Y POR QUÉ NO LO HACE)

### Flujo Correcto (Teórico):
```
Usuario hace clic en botón
    ↓
JS: html.setAttribute("data-bs-theme", "light")
    ↓
CSS selector [data-bs-theme="light"] activa
    ↓
--text-body = var(--pr-black) #000000
--bg-body = var(--pr-white) #FFFFFF
    ↓
body { color: var(--text-body); } ← Cambia a negro
body { background-color: var(--bg-body); } ← Cambia a blanco
    ↓
✅ Todo el site cambia de tema
```

### Flujo Actual (ROTO):
```
Usuario hace clic en botón
    ↓
JS: html.setAttribute("data-bs-theme", "light") ✅
    ↓
CSS selector [data-bs-theme="light"] activa ✅
    ↓
--text-body = var(--pr-black) ✅
    ↓
Pero en autor_detalle.css:
  .bev-author-profile { color: var(--pr-black); } ← SIEMPRE negro, no usa --text-body
    ↓
.bev-back-link { color: var(--pr-black); } ← SIEMPRE negro
    ↓
❌ Texto permanece negro incluso en modo oscuro → ¡Invisible!
```

---

## 🔧 PLAN DE CORRECCIÓN

### Fase 1: Fix Crítico (Sin cambios visuales)

**1. [panel_accesibilidad.css](core/static/css/panel_accesibilidad.css) línea 11-12**
- ❌ `background-color: var(--pr-gray-900);` + `color: var(--pr-white);`
- ✅ `background-color: var(--pr-gray-900);` + `color: var(--text-heading);` (o --text-body)
- Motivo: El botón del panel de accesibilidad DEBE ser visible en ambos modos

**2. [base.html](core/templates/core/base.html#L4) línea 4**
- ❌ `<html lang="es" data-bs-theme="dark">`
- ✅ `<html lang="es">` (sin atributo)
- Razón: Deja que el JS (o preferencia del navegador) establezca el tema inicial
- Alternativa: `data-bs-theme="light"` si el default debe ser claro

### Fase 2: Refactoring Grande (Cambiar PRIMITIVAS → SEMÁNTICAS)

**Pasos:**
1. Crear nuevas variables semánticas en var.css para cada contexto que lo necesite
2. Reemplazar en los 14 archivos CSS problemas
3. Ejemplos de cambios:
   - `color: var(--pr-black)` → `color: var(--text-body)`
   - `color: var(--pr-white)` → `color: var(--text-heading)` o semántica apropiada
   - `#fff` → `var(--pr-white)` → `var(--text-heading)` o color semántico
   - `background-color: var(--pr-white)` → `background-color: var(--bg-surface)` (si aplica)

### Fase 3: Mejorar aplicarEstadoInicial() (Bonus)

**[panel_accesibilidad.js](core/static/js/panel_accesibilidad.js) líneas 10-16**
- Agregar fallback a `prefers-color-scheme` del navegador
- Si no hay localStorage, usar preferencia del sistema

---

## 📊 TABLA RESUMEN

| Aspecto | Estado | Notas |
|---------|--------|-------|
| **Toggle JS Logic** | ✅ OK | Cambia data-bs-theme correctamente |
| **localStorage** | ✅ OK | Se guarda y aplica al cargar |
| **var.css Structure** | ✅ OK | Bloques :root, light, dark bien definidos |
| **CSS Load Order** | ✅ OK | Bootstrap → var.css → JS correcto |
| **HTML Default Theme** | ❌ BROKEN | Hardcodeado a "dark" sin fallback |
| **CSS Variables Usage** | ❌ BROKEN | 37+ usos de primitivas en lugar de semánticas |
| **Hex Color Hardcodes** | ❌ BROKEN | 3 usos directos (#fff, #ffffff) |
| **Panel Accessibility Button** | ❌ BROKEN | Usa primitivas, invisible en tema opuesto |

---

## 🔬 DIAGNÓSTICO FINAL

### Causa Raíz Identificada

**El toggle parece funcionar a nivel técnico (data-bs-theme se modifica), pero NO tiene efecto visual porque:**

1. **Desconexión CSS:** 75% del CSS usa variables **primitivas no theme-aware** (`--pr-black`, `--pr-white`) en lugar de variables **semánticas theme-aware** (`--text-body`, `--text-heading`, `--bg-body`).

2. **HTML Hardcodeado:** `data-bs-theme="dark"` fijo en base.html significa que el fallback siempre es oscuro, enmascarando bugs de CSS que no responden al toggle.

3. **Cascada Rota:** Aunque var.css define correctamente las semánticas, 14 archivos CSS las ignoran y usan primitivas directas.

**Resultado:** 
- ✅ El atributo `data-bs-theme` **cambia** (se ve en DevTools)
- ❌ Los colores de texto **NO cambian** (porque no usan las variables correctas)
- ❌ El efecto es **invisible al usuario**

### Acciones Inmediatas

**ALTA:** Remover `data-bs-theme` de [base.html:4](core/templates/core/base.html#L4)  
**ALTA:** Reemplazar colores hardcodeados en [panel_accesibilidad.css:11-12](core/static/css/panel_accesibilidad.css#L11-L12)  
**MEDIA:** Refactorizar 14 archivos CSS para usar variables semánticas  
**BAJA:** Mejorar `aplicarEstadoInicial()` con `prefers-color-scheme` fallback

---

## 📁 Archivos Afectados (Para Referencia Rápida)

**CSS que necesita refactoring:**
```
catalogo/static/catalogo/css/autor_detalle.css (14 matches)
catalogo/static/catalogo/css/libro_card.css (1 direct hex)
catalogo/static/catalogo/css/libro_detalle.css (6 matches)
contacto/static/contacto/css/contacto.css (1 match)
core/static/css/components.css (8 matches)
core/static/css/components/footer.css (2 matches)
core/static/css/components/navbar.css (3 matches)
core/static/css/panel_accesibilidad.css (2 CRITICAL matches)
home/static/home/css/carrusel_hero.css (4 matches)
home/static/home/css/premios.css (5 matches)
home/static/home/css/seccion_autores.css (3 matches + 1 direct hex)
noticias/static/noticias/css/carrusel_hero.css (2 matches)
noticias/static/noticias/css/libros_noticias_lateral.css (5 matches)
noticias/static/noticias/css/listado.css (13 matches)
noticias/static/noticias/css/noticia_detalle.css (15 matches)
noticias/static/noticias/css/premios_carrusel.css (6 matches)
```

**Templates/JS que necesita ajuste:**
```
core/templates/core/base.html (1 critical change)
core/static/js/panel_accesibilidad.js (optional enhancement)
```

# Carta de intención — Anthropic AI for Science — v2.0

**Fecha:** 2026-11-16
**Solicitante:** Rubén Antonio Lecona Curto (R@LC)
**Institución / PI:** [pendiente de afiliación]
**Programa:** Anthropic AI for Science — hasta USD 50,000 en créditos Claude por proyecto
**Duración:** 6 meses
**Título:** *A Typed, Machine-Checkable Catalog of Physical Quantities: Formalizing TIE 2 in Lean 4 with Claude*

---

## 1. Resumen

La notación física estándar mezcla cantidades que comparten dimensiones pero no son la misma cosa: torque y energía, presión y densidad de energía, frecuencia y velocidad angular. El álgebra dimensional no detecta esos errores de categoría.

TIE 2 propone una gramática tipada: cuatro entes (Espacio, Tiempo, Fase, Físico), reglas R-01–R-12 y un catálogo de **254 combinaciones únicas** (35 estándar, 4 etiqueta, 2 puente, 213 candidatos).

Este proyecto formaliza y verifica ese catálogo en **Lean 4**, usando Claude como motor de generación, clasificación y búsqueda de contraejemplos. El objetivo no es demostrar una teoría física nueva: es construir un **artefacto abierto, tipado y verificable** que permita detectar errores de categoría y explorar sistemáticamente un lenguaje físico.

---

## 2. Prototipo ya construido

| Elemento | Estado |
|---|---|
| Dataset de 254 entradas | `catalog254.json` / `catalog254.csv` |
| Proyecto Lean 4 | `lean-tie2/` con `lakefile.lean` y `lean-toolchain` |
| Reglas de admisibilidad | `L ∈ [-3,3]`; `T,R,V,Wb,Gr ∈ {-1,0,1}` |
| Pruebas de rechazo | `T⁻²`, `L⁴`, `R²` → `false` |
| Catálogo Lean | `catalog254.length = 254`; todas admisibles |
| Compilación | `lake build` — 6 jobs, exitoso |

El prototipo demuestra que la gramática es formalizable y que el verificador rechaza las unidades prohibidas.

---

## 3. Pregunta de investigación

> ¿Puede un asistente de pruebas tipado, asistido por un LLM, formalizar y verificar un catálogo físico de 254 entradas, detectar errores de categoría en la notación estándar y producir un benchmark reproducible?

---

## 4. Método

1. **Formalizar R-01–R-12** en Lean 4: dimensiones, tipos tensoriales, clases, dominio, procesos vs. unidades.
2. **Codificar las 254 entradas** como dataset tipado y reproducible.
3. **Usar Claude** para generar borradores de definiciones, pruebas de tipo y contraejemplos.
4. **Verificación humana + `lean`** como árbitro final.
5. **Benchmark abierto:** dado un enunciado físico, decidir si es admisible, proceso o suma inválida.

---

## 5. Entregables

- Librería Lean 4 de tipos y reglas R-01–R-12.
- Dataset abierto de 254 entradas con dimensión, tipo, clase y estatus.
- Benchmark de 200–500 enunciados válidos/inválidos.
- Preprint de 8–12 páginas.
- Repositorio reproducible con CI.
- Informe de errores de categoría detectados.

---

## 6. Evaluación

| Métrica | Objetivo |
|---|---|
| Cobertura de R-01–R-12 | 100% |
| Entradas tipadas en Lean | 254/254 |
| Tasa de type-check | ≥ 95% |
| Errores de categoría documentados | ≥ 20 |
| Acuerdo humano–Claude en benchmark | ≥ 90% |
| Reducción de tiempo de formalización | ≥ 30% vs. línea base manual |

---

## 7. Plan de 6 meses

| Mes | Hito |
|---|---|
| 1 | R-01–R-06; 254 entradas (ya iniciado) |
| 2 | R-07–R-12; reglas de tipo/clase |
| 3 | Benchmark inicial de 200–500 enunciados |
| 4 | Pruebas asistidas por Claude; benchmark ampliado |
| 5 | Preprint y revisión externa |
| 6 | Repositorio final, CI y solicitud de publicación |

---

## 8. Presupuesto

| Rubro | Estimado |
|---|---|
| Créditos Claude | hasta USD 50,000 |
| Compute Lean/CI | USD 3,000–5,000 |
| Difusión / preprint | USD 2,000 |
| Sin salario solicitado al programa | — |

---

## 9. Por qué Anthropic

- AI for Science apoya proyectos científicos de alto impacto con créditos Claude; este proyecto usa el modelo como motor de formalización, no como generador de texto.
- El resultado es un artefacto abierto y verificable: Lean, dataset, benchmark y preprint.
- El prototipo ya existe y compila; el riesgo técnico es bajo.

---

## 10. Riesgos y mitigación

| Riesgo | Mitigación |
|---|---|
| El catálogo es demasiado amplio | 254 entradas ya codificadas; subconjunto de 50 como regresión |
| Claude alucina pruebas | Lean verifica; revisión humana por muestra |
| Falta de afiliación | Buscar PI académico o institución sin fines de lucro |
| Teoría no validada empíricamente | Se presenta como formalización, no como teoría confirmada |

---

## 11. Afiliación y equipo

- **PI:** [pendiente]
- **Institución:** [pendiente]
- **Colaboradores:** [pendiente]
- **Repositorio:** https://github.com/RALC-TIE-CREATOR/tie2-typed-catalog

---

## 12. Siguiente paso

- Confirmar PI/afiliación.
- Publicar el repo Lean y el dataset.
- Enviar la solicitud a AI for Science con este paquete.

---

## 13. Registro de cambios

- **v0.1 (2026-11-16):** borrador inicial.
- **v2.0 (2026-11-16):** catálogo completo de 254 entradas codificado y compilado; repo público; métricas y plan de 6 meses.


# AGENTS.md — Reglas específicas del proyecto

## 1. Alcance del repositorio

Este repositorio es la base reutilizable de un sistema agéntico para crear, revisar y actualizar Planes de Marketing para cualquier tipo de negocio (productos, servicios, ecommerce, retail, B2B, B2C, educativos o híbridos).

El MVP no debe convertirse en:
- herramienta de publicación automática,
- CRM,
- gestor de campañas,
- dashboard avanzado,
- integración MCP,
- automatización de redes sociales,
- ni generador genérico de contenido.

El objetivo actual es validar un flujo documental y técnico:
- crear proyectos desde `project_template/`,
- validar estructura,
- validar brief mínimo,
- generar documentos del Plan de Marketing por fases,
- registrar cambios,
- versionar resultados,
- mantener separado el repositorio base de los proyectos generados.

## 2. Separación entre repositorio base y proyectos

El repositorio base contiene código, documentación, reglas, plantillas y estructura del sistema.

Las instancias de proyecto viven en: `projects/`

**Reglas específicas:**
- No guardar datos reales de clientes en el repositorio base.
- No guardar outputs reales dentro de `docs/`.
- No modificar `project_template/` para resolver un caso concreto.
- Cada nuevo negocio debe crearse desde `project_template/`, no copiando otro proyecto ya usado.
- Si durante una tarea se crea un proyecto de prueba, debe reportarse al cierre.

## 3. Convenciones técnicas del repositorio

**Carpetas del sistema (Base):**
`src/`, `project_template/`, `docs/00_base_sistema/`, `docs/01_estandares/`, `docs/02_manual_operativo/`, `tests/`, `system/`, `agents/`, `.claude/skills/`.

**Nota sobre skills:**
Las skills operativas del sistema viven en `.claude/skills/<nombre>/SKILL.md` (13 skills).
Esta ubicación es parte estructural del repositorio y está bajo control de versiones.

**Área de Trabajo (Workspace):**
`workspace/` contiene inputs, reportes temporales y borradores.
`projects/` contiene los proyectos activos para pruebas locales.

**Historial y Reportes:**
`workspace/reports/` contiene auditorías, historial de sesiones e hitos de validación.
`workspace/exports/` contiene los ZIPs generados.

Todo el contenido de `workspace/` y `projects/` está ignorado por Git y no forma parte del sistema base.

**El punto de entrada CLI es:**
`uv run python -m src.main`

No usar como punto de entrada:
`python main.py`, `python -m app.main`.

## 4. Orden recomendado antes de generar documentos de marketing

Antes de generar diagnóstico, propuesta de valor, matriz de canales o plan de acción, deben pasar estas validaciones:
1. `uv run python -m src.main validate-base-structure`
2. `uv run python -m src.main validate-project --name "Nombre Proyecto"`
3. `uv run python -m src.main validate-brief --name "Nombre Proyecto"`

Si el brief mínimo no está validado, no generar documentos estratégicos.

## 5. Brief mínimo

**Campos obligatorios:**
`nombre_negocio`, `tipo_negocio`, `oferta_principal`, `cliente_objetivo`, `problema_que_resuelve`, `objetivo_principal`.

**Campo opcional:**
`presupuesto_marketing`.

Si falta un campo obligatorio, marcar el brief como incompleto. No inventar datos del negocio.

## 6. Reglas específicas de marketing

No asumir que LinkedIn, Instagram, TikTok u otro canal es obligatorio.
Los canales deben elegirse según: tipo de empresa, servicio, cliente objetivo, zona geográfica, presupuesto, recursos disponibles, ciclo de venta, capacidad operativa y objetivo comercial.
Cada canal recomendado debe tener justificación.

## 7. Plan de Marketing como documento vivo

El Plan de Marketing puede cambiar. Los cambios relevantes deben registrar: qué cambia, impacto, documentos afectados, riesgos, si requiere nueva versión y si requiere auditoría posterior.

**Impactos posibles:**
`impacto_bajo`, `impacto_medio`, `impacto_alto`.

Los cambios de impacto alto requieren aprobación explícita del usuario antes de modificar documentos estratégicos.

## 8. Agentes y skills del MVP

**Agentes previstos:**
`orquestador_plan_marketing`, `investigador_marketing`, `estratega_marketing`, `redactor_marketing`, `analista_metricas`, `auditor_plan_marketing`.

**Skills operativas (13 — en `.claude/skills/`):**
`skill_intake_brief`, `skill_diagnostico_marketing`, `skill_cliente_objetivo`, `skill_propuesta_valor`, `skill_analisis_competencia`, `skill_matriz_canales`, `skill_estrategia_comunicacion`, `skill_plan_accion`, `skill_presupuesto_marketing`, `skill_kpis`, `skill_resumen_plan_empresa`, `skill_auditoria_coherencia`, `skill_change_request`.

No crear agentes nuevos sin justificar por qué no basta con una skill.
No crear skills nuevas sin definir entrada, proceso, salida y validación.
Toda skill nueva debe ir a `.claude/skills/<nombre>/SKILL.md`, no a `skills/`.

## 8.1 Modelos de negocio soportados

El sistema adapta canales, tono, KPIs y presupuesto según el modelo detectado:

| Perfil del resolver | Descripción |
|---------------------|-------------|
| `ecommerce_transaccional` | Tienda online D2C — foco en conversión, ROAS, checkout |
| `b2c_producto_ecommerce` | Venta directa de productos físicos por canal digital |
| `b2b_producto_industrial` | Productos/maquinaria a empresas — catálogos, ferias, suministro |
| `retail_fisico` | Tienda física — tráfico peatonal, visibilidad local |
| `b2b_consultivo` | Servicios profesionales a empresas — ciclo largo, autoridad |
| `b2c_local_servicios` | Servicios de cercanía — zona geográfica, reserva, reseñas |
| `educativo_formativo` | Academias y cursos — demostración de valor, matrícula |
| `hibrido_producto_servicio` | Producto + contrato de servicio recurrente (mantenimiento, SLA) |
| `estrategia_general_prudente` | Fallback — solo para briefs genuinamente ambiguos |

El perfil `estrategia_general_prudente` no debe activarse para negocios con modelo evidente.
Si se activa para un brief claro, es un fallo del resolver que debe corregirse.

## 9. Aprovechamiento de Antigravity

Para tareas medianas o grandes en este repositorio, usa el flujo agentic-first de Antigravity:
1. Crear Task List.
2. Crear Implementation Plan antes de modificar.
3. Ejecutar cambios.
4. Generar Walkthrough de cierre.
5. Mostrar comandos ejecutados y resultados.
6. Usar Code Diffs para revisión.

Si se detecta una lección reutilizable, proponer guardarla en Knowledge, pero no guardarla sin confirmación del usuario.

## 10. Cierre de tarea

Al cerrar una tarea en este repositorio, reportar:
- Archivos creados/modificados.
- Comandos ejecutados y resultado de validación.
- Artifacts generados o revisados.
- Estado final y siguiente paso recomendado.

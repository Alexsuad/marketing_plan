# Auditoría de Brecha Agéntica

**Fecha:** 2026-04-30  
**Versión:** 1.0  
**Elaborado por:** Revisión sistemática de documentación interna

---

## Estado actual
```text
repositorio_funcional_con_arquitectura_agentica_documentada_pero_no_materializada
```

---

## Fuentes revisadas

1. `docs/03_agentes_y_responsabilidades.md` — Definición completa de 6 agentes con roles, responsabilidades, límites, entradas, salidas, skills y gates.
2. `docs/04_skills_y_uso.md` — Definición completa de 13 skills con propósito, proceso, agente activador, salida esperada y criterios de insuficiencia.
3. `docs/documento_maestro_lecciones_aprendidas_y_manual_anti_errores_final.md` — Manual de referencia sobre arquitectura agéntica, errores frecuentes y criterios de diseño de agentes, skills, reglas y gates.
4. `AGENTS.md` — Capa de instrucción del repositorio.
5. `README.md` — Documentación general del sistema.
6. Estado real de las carpetas: `agents/`, `skills/`, `system/`, `.claude/`.

---

## Resumen ejecutivo

**El repositorio NO cumple con el diseño agéntico esperado.**

Existe una arquitectura agéntica completamente diseñada y documentada en `docs/` con 6 agentes definidos al detalle y 13 skills con sus entradas, procesos y salidas. Sin embargo, esa arquitectura no ha sido materializada en el repositorio operativo.

Lo que existe actualmente en `agents/`, `skills/` y `system/` es una **estructura improvisada creada en la sesión anterior** que no respetó los documentos fuente. Específicamente:

- Solo existe 1 de los 6 agentes requeridos, y en formato incompleto.
- La única skill existente (`skill_segmentacion_cliente.md`) no estaba en el listado del MVP y no sigue el formato `SKILL.md` requerido.
- No existe la carpeta `.claude/skills/` recomendada por el Documento Maestro.
- Los gates en `system/gates/` son solo un README vacío, no gates operativos reales.
- Los workflows en `system/workflows/` son solo un README vacío, sin ningún workflow definido.

---

## Brecha 1 — Agentes

### Agentes requeridos por documentación vs. estado real en `agents/`

| Agente | Requerido | Existe en repo | Estado | Acción recomendada |
|---|---|---|---|---|
| `orquestador_plan_marketing` | Sí | Sí (`agents/orquestador_plan_marketing.md`) | **Parcial** — Existe pero con formato simplificado (no incluye skills que puede usar, gates relacionados completos, ni errores a evitar del doc oficial) | Completar con las secciones definidas en `docs/03` |
| `investigador_marketing` | Sí | **No** | **Faltante** | Crear `agents/investigador_marketing.md` |
| `estratega_marketing` | Sí | **No** | **Faltante** | Crear `agents/estratega_marketing.md` |
| `redactor_marketing` | Sí | **No** | **Faltante** | Crear `agents/redactor_marketing.md` |
| `analista_metricas` | Sí | **No** | **Faltante** | Crear `agents/analista_metricas.md` |
| `auditor_plan_marketing` | Sí | **No** | **Faltante** | Crear `agents/auditor_plan_marketing.md` |

**Resultado Brecha 1:** 1/6 agentes presente (parcial). 5 agentes completamente ausentes.

### Criterio de aceptación incumplido

Según `docs/03` (sección 15), un agente bien definido debe tener:
rol, objetivo, responsabilidades, límites, entradas, salidas, fases donde participa, skills que puede usar, gates relacionados, errores que debe evitar, y relación con otros agentes.

El archivo actual `agents/orquestador_plan_marketing.md` no incluye explícitamente: fases donde participa, la lista de skills que puede usar (`skill_intake_brief`, `skill_change_request`, `skill_auditoria_coherencia`), ni los errores específicos que debe evitar según la documentación.

---

## Brecha 2 — Skills

### Skills requeridas por documentación vs. estado real

| Skill | Requerida | Existe en repo | Formato actual | Formato recomendado | Acción recomendada |
|---|---|---|---|---|---|
| `skill_intake_brief` | Sí | **No** | — | `.claude/skills/skill_intake_brief/SKILL.md` | Crear |
| `skill_diagnostico_marketing` | Sí | **No** | — | `.claude/skills/skill_diagnostico_marketing/SKILL.md` | Crear |
| `skill_cliente_objetivo` | Sí | **No** | — | `.claude/skills/skill_cliente_objetivo/SKILL.md` | Crear |
| `skill_propuesta_valor` | Sí | **No** | — | `.claude/skills/skill_propuesta_valor/SKILL.md` | Crear |
| `skill_analisis_competencia` | Sí | **No** | — | `.claude/skills/skill_analisis_competencia/SKILL.md` | Crear |
| `skill_matriz_canales` | Sí | **No** | — | `.claude/skills/skill_matriz_canales/SKILL.md` | Crear |
| `skill_estrategia_comunicacion` | Sí | **No** | — | `.claude/skills/skill_estrategia_comunicacion/SKILL.md` | Crear |
| `skill_plan_accion` | Sí | **No** | — | `.claude/skills/skill_plan_accion/SKILL.md` | Crear |
| `skill_presupuesto_marketing` | Sí | **No** | — | `.claude/skills/skill_presupuesto_marketing/SKILL.md` | Crear |
| `skill_kpis` | Sí | **No** | — | `.claude/skills/skill_kpis/SKILL.md` | Crear |
| `skill_resumen_plan_empresa` | Sí | **No** | — | `.claude/skills/skill_resumen_plan_empresa/SKILL.md` | Crear |
| `skill_auditoria_coherencia` | Sí | **No** | — | `.claude/skills/skill_auditoria_coherencia/SKILL.md` | Crear |
| `skill_change_request` | Sí | **No** | — | `.claude/skills/skill_change_request/SKILL.md` | Crear |

**Extra no planificada:**

| Skill | Requerida | Existe en repo | Observación |
|---|---|---|---|
| `skill_segmentacion_cliente` | **No** (no está en el listado del MVP) | Sí (`skills/marketing/skill_segmentacion_cliente.md`) | Fue creada en la sesión anterior sin base documental. Puede incorporarse en el futuro como skill adicional pero no es parte del MVP. No debe confundirse con las skills requeridas. |

**Resultado Brecha 2:** 0/13 skills del MVP presentes. Existe 1 skill extra no perteneciente al MVP.

### Problema adicional de formato

El Documento Maestro (sección 3.4) y `docs/04` (sección 19) especifican claramente que cada skill debe vivir en una **carpeta propia** con el archivo núcleo `SKILL.md`:

```text
skills/skill_nombre/
└── SKILL.md
```

El archivo `skill_segmentacion_cliente.md` que existe es un archivo suelto en `skills/marketing/`, no sigue este formato. No es portable ni auditable según el estándar definido.

---

## Brecha 3 — Gates

### Gates documentados en `docs/05_gates_y_validaciones.md` vs. estado real en `system/gates/`

| Gate | Documentado | Existe en repo | Estado |
|---|---|---|---|
| `gate_brief_minimo` | Sí | **No** (solo README vacío) | Faltante |
| `gate_no_invencion` | Sí | **No** | Faltante |
| `gate_coherencia_cliente_propuesta` | Sí | **No** | Faltante |
| `gate_canales_justificados` | Sí | **No** | Faltante |
| `gate_plan_accion_realista` | Sí | **No** | Faltante |
| `gate_kpis_medibles` | Sí | **No** | Faltante |
| `gate_resumen_plan_empresa` | Sí | **No** | Faltante |
| `gate_auditoria_final` | Sí | **No** | Faltante |
| `gate_impacto_cambio` | Sí | **No** | Faltante |
| Gate de no regeneración de fases manuales | Previsto en reglas | **No** | Faltante |
| Gate de cierre con hito documentado | Previsto en workflows | **No** | Faltante |

**Resultado Brecha 3:** 0/9 gates del MVP presentes como archivos operativos. Solo existe un `README.md` vacío.

---

## Brecha 4 — Workflows

### Workflows necesarios vs. estado real en `system/workflows/`

| Workflow | Necesario | Existe | Estado |
|---|---|---|---|
| Crear proyecto desde plantilla | Sí | **No** | Faltante |
| Validar brief mínimo | Sí | **No** | Faltante |
| Generar fase del pipeline | Sí | **No** | Faltante |
| Revisar fase generada | Sí | **No** | Faltante |
| Ajustar fase con control de cambio | Sí | **No** | Faltante |
| Cerrar hito y documentarlo | Sí | **No** | Faltante |
| Crear ZIP base limpio | Sí | **No** | Faltante |
| Validar ZIP en entorno limpio | Sí | **No** | Faltante |

**Resultado Brecha 4:** 0/8 workflows presentes como archivos operativos. Solo existe un `README.md` vacío.

---

## Brecha 5 — Compatibilidad de Skills

### Formato `.claude/skills/<skill-name>/SKILL.md`

El Documento Maestro (sección 3.4) especifica que el formato estándar de una skill es una carpeta con `SKILL.md` como núcleo. Para entornos compatibles con Claude Code, la convención es:

```text
.claude/skills/<skill-name>/SKILL.md
```

**Estado actual:**
- La carpeta `.claude/` **no existe** en el repositorio.
- No existe ninguna skill en formato `.claude/skills/`.
- Las skills actuales son archivos `.md` sueltos en `skills/marketing/`, incompatibles con el estándar.

**Resultado Brecha 5:** Incompatibilidad total con el formato recomendado.

---

## Riesgos detectados

| Riesgo | Descripción | Severidad |
|---|---|---|
| Dependencia exclusiva de `AGENTS.md` | `AGENTS.md` no puede sustituir los prompts oficiales de cada agente ni la definición de skills. Si solo existe `AGENTS.md`, el sistema opera sin roles separados. | **Alta** |
| Confundir pipeline determinista con sistema agéntico | El pipeline de Python (`src/`) genera documentos, pero no es un sistema agéntico. Los agentes son capas de interpretación y coordinación que aún no existen operativamente. | **Alta** |
| Roles documentados pero no materializados | Un agente que solo vive en `docs/` no puede activarse, coordinarse ni auditarse. El sistema sigue siendo mono-agente en la práctica. | **Alta** |
| Skills como archivos sueltos no compatibles | Un archivo `.md` suelto no es una skill auditable ni portable. Si el formato cambia, no hay estructura que lo soporte. | **Media** |
| Ausencia de gates operativos | Sin gates reales, el sistema no puede bloquear avances incorrectos. La validación queda solo en el pipeline Python, que no cubre todos los casos de error estratégico. | **Alta** |
| Skill extra no planificada (`skill_segmentacion_cliente`) | Fue creada sin base documental y puede confundirse con las skills del MVP. Requiere decisión de si se incorpora o se elimina. | **Baja** |

---

## Decisión arquitectónica recomendada

Basado en el Documento Maestro y los documentos de arquitectura, se recomienda la siguiente organización de carpetas:

### `agents/`
**Propósito:** Definición documental de los 6 roles del MVP. Cada archivo es el "prompt oficial" del agente: define qué puede hacer, qué no puede hacer, sus entradas, salidas y relación con el sistema.

**Formato:** Un archivo `.md` por agente con las 10 secciones del estándar de `docs/03`.

### `.claude/skills/`
**Propósito:** Skills en formato compatible con Claude Code. Cada skill vive en su propia carpeta con `SKILL.md` como núcleo obligatorio.

**Formato:**
```text
.claude/skills/<skill-name>/
└── SKILL.md
```

### `system/`
**Propósito:** Reglas transversales, workflows operativos y gates de control de avance.

**Estructura:**
```text
system/
├── rules/        → Restricciones inamovibles del sistema
├── workflows/    → Secuencias de pasos para tareas complejas
└── gates/        → Criterios de bloqueo o aprobación antes de avanzar
```

---

## Plan de implementación propuesto

### Fase 1 — Completar `agents/` (6 agentes del MVP)
- Completar `agents/orquestador_plan_marketing.md` con las secciones faltantes.
- Crear los 5 agentes restantes con el estándar completo de `docs/03`.

### Fase 2 — Crear `.claude/skills/` (13 skills del MVP)
- Crear la carpeta `.claude/skills/`.
- Crear una subcarpeta por skill con su `SKILL.md`.
- El contenido de cada `SKILL.md` se extrae directamente de `docs/04`.

### Fase 3 — Materializar `system/gates/` y `system/workflows/`
- Crear un archivo `.md` por cada gate del MVP (9 gates) en `system/gates/`.
- Crear un archivo `.md` por cada workflow operativo (8 workflows) en `system/workflows/`.

### Fase 4 — Actualizar `README.md` y `AGENTS.md`
- Reflejar la nueva estructura real del repositorio.
- Actualizar estado del sistema a `repositorio_base_v1.1_con_capa_agentica_completa`.

### Fase 5 — Generar nuevo ZIP base v1.1
- Excluir `projects/`, `.venv/`, `__pycache__`, `docs/archive/` y `test_clean_sandbox/`.
- Incluir la nueva estructura agéntica materializada.

### Fase 6 — Validar ZIP v1.1 en entorno limpio
- Repetir el procedimiento de prueba de instalación limpia (`sandbox`).
- Confirmar que los agentes, skills y system están presentes y completos.
- Documentar el hito de validación.

---

## Estado final del informe
```text
auditoria_gap_agentico_completada
```

> [!IMPORTANT]
> **No implementar ninguna fase hasta aprobación explícita del usuario.** El informe documenta el estado real y el plan de acción. La implementación sigue el flujo: Entender → Definir → Acotar → **Decidir → Documentar → Validar**.

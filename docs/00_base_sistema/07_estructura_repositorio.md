<!--
# File: docs/07_estructura_repositorio.md
# ──────────────────────────────────────────────────────────────────────
# Propósito: Documentar la estructura de carpetas y archivos del repositorio.
# Rol: Documentación técnica.
# ──────────────────────────────────────────────────────────────────────
-->

# 07 - Estructura del Repositorio

## 1. Propósito del documento

Este documento define la estructura del repositorio base y de las instancias de proyecto del sistema agéntico para crear Planes de Marketing.

Su objetivo es asegurar que el sistema sea reutilizable, limpio y seguro para trabajar con distintos negocios sin contaminar datos, contexto, outputs o versiones.

Este documento complementa:

```text
00_planificacion_mvp_sistema_plan_marketing.md
01_alcance_funcional_mvp.md
02_flujo_plan_marketing.md
03_agentes_y_responsabilidades.md
04_skills_y_uso.md
05_gates_y_validaciones.md
06_sistema_cambios_versionado.md
```

---

## 2. Principio general

El sistema debe separarse en dos niveles:

```text
repositorio_base
instancias_de_proyecto
```

El repositorio base contiene la arquitectura, código, documentación, agentes, skills, gates, workflows y plantillas.

Las instancias de proyecto contienen contexto, outputs, versiones, auditorías, changelog y logs de un negocio específico.

Regla base:

```text
El repositorio base no debe contener información real de clientes ni outputs de planes generados.
Cada nuevo Plan de Marketing debe crearse en una instancia limpia de proyecto.
```

---

## 3. Estructura general recomendada

Estructura inicial:

```text
marketing_plan_agent_base/
├── README.md
├── AGENTS.md
├── docs/
├── system/
├── agents/
├── skills/
├── src/
├── tests/
├── project_template/
└── projects/
```

En fases posteriores, la carpeta `projects/` podría estar fuera del repositorio base si se quiere separar por completo el motor del sistema y los proyectos generados.

Para el MVP puede existir dentro del entorno local, pero debe estar excluida de control de versiones si contiene datos reales.

---

## 4. Repositorio base

El repositorio base es la plantilla reutilizable del sistema.

Debe contener:

- documentación del sistema,
- reglas,
- workflows,
- gates,
- agentes,
- skills,
- plantillas,
- código de aplicación,
- pruebas,
- y plantilla limpia para crear nuevos proyectos.

No debe contener:

- datos reales de clientes,
- contexto de negocios específicos,
- Planes de Marketing generados,
- auditorías de clientes,
- changelogs de proyectos,
- archivos temporales,
- credenciales,
- tokens,
- claves API,
- ni información sensible.

---

## 5. Carpeta README.md

Archivo principal de entrada al repositorio.

Debe explicar:

- qué es el proyecto,
- para qué sirve,
- qué hace el MVP,
- qué no hace,
- cómo se crea un nuevo proyecto,
- cómo se ejecuta el flujo básico,
- y dónde está la documentación.

No debe incluir información de clientes ni resultados generados.

---

## 6. Archivo AGENTS.md

Archivo de instrucciones globales para el entorno agentic.

Debe contener reglas generales como:

- leer documentación base antes de modificar,
- no mezclar proyectos,
- no guardar outputs en el repositorio base,
- no tocar datos de cliente fuera de su instancia,
- respetar gates,
- registrar cambios,
- no inventar información,
- y mantener separación entre Plan de Marketing y Plan de Empresa.

No debe contener:

- instrucciones extensas de una skill,
- lógica detallada de workflows,
- prompts completos de cada agente,
- ni reglas demasiado largas que conviertan el archivo en un megaprompt.

---

## 7. Carpeta docs/

Contiene la documentación del sistema.

Estructura inicial:

```text
docs/
├── 00_planificacion_mvp_sistema_plan_marketing.md
├── 01_alcance_funcional_mvp.md
├── 02_flujo_plan_marketing.md
├── 03_agentes_y_responsabilidades.md
├── 04_skills_y_uso.md
├── 05_gates_y_validaciones.md
├── 06_sistema_cambios_versionado.md
├── 07_estructura_repositorio.md
├── 08_arquitectura_tecnica_inicial.md
└── 09_criterios_de_hecho.md
```

La carpeta `docs/` explica cómo funciona el sistema.

No debe contener Planes de Marketing de clientes.

---

## 8. Carpeta system/

Contiene piezas internas del sistema que gobiernan comportamiento, reglas, workflows, gates y plantillas.

Estructura recomendada:

```text
system/
├── rules/
├── workflows/
├── gates/
└── templates/
```

---

## 9. Carpeta system/rules/

Contiene reglas del sistema.

Ejemplos:

```text
system/rules/
├── reglas_globales.md
├── reglas_plan_marketing.md
├── reglas_no_invencion.md
├── reglas_repositorio_limpio.md
├── reglas_documento_vivo.md
└── reglas_canales_marketing.md
```

Propósito:

- definir límites,
- evitar invención,
- proteger trazabilidad,
- separar proyectos,
- y mantener coherencia.

---

## 10. Carpeta system/workflows/

Contiene workflows del sistema.

Ejemplos:

```text
system/workflows/
├── workflow_generar_plan_marketing.md
├── workflow_actualizar_plan_marketing.md
├── workflow_crear_nuevo_proyecto.md
├── workflow_auditoria_final.md
└── workflow_resumen_plan_empresa.md
```

Cada workflow debe indicar:

- objetivo,
- pasos,
- entradas,
- salidas,
- agentes participantes,
- skills usadas,
- gates aplicados,
- y criterios de cierre.

---

## 11. Carpeta system/gates/

Contiene definiciones operativas de gates.

Ejemplos:

```text
system/gates/
├── gate_brief_minimo.md
├── gate_no_invencion.md
├── gate_coherencia_cliente_propuesta.md
├── gate_canales_justificados.md
├── gate_plan_accion_realista.md
├── gate_kpis_medibles.md
├── gate_resumen_plan_empresa.md
├── gate_auditoria_final.md
└── gate_impacto_cambio.md
```

Cada gate debe indicar:

- propósito,
- cuándo se ejecuta,
- qué valida,
- criterios de aprobado,
- criterios de observación,
- criterios de bloqueo,
- salida esperada.

---

## 12. Carpeta system/templates/

Contiene plantillas reutilizables para documentos y salidas.

Ejemplos:

```text
system/templates/
├── template_brief_negocio.md
├── template_diagnostico_marketing.md
├── template_cliente_objetivo.md
├── template_propuesta_valor.md
├── template_analisis_competencia.md
├── template_matriz_canales.md
├── template_plan_accion_90_dias.md
├── template_kpis.md
├── template_resumen_plan_empresa.md
├── template_auditoria_final.md
└── template_changelog.md
```

Las plantillas deben evitar rigidez excesiva.

Deben guiar la estructura, pero permitir adaptación según el tipo de negocio.

---

## 13. Carpeta agents/

Contiene la definición de agentes del sistema.

Estructura recomendada:

```text
agents/
├── orquestador_plan_marketing.md
├── investigador_marketing.md
├── estratega_marketing.md
├── redactor_marketing.md
├── analista_metricas.md
└── auditor_plan_marketing.md
```

Cada archivo de agente debe incluir:

- rol,
- objetivo,
- responsabilidades,
- límites,
- entradas,
- salidas,
- fases donde participa,
- skills permitidas,
- gates relacionados,
- y errores que debe evitar.

---

## 14. Carpeta skills/

Contiene las skills reutilizables del sistema.

Estructura recomendada:

```text
skills/
├── skill_intake_brief/
│   └── SKILL.md
├── skill_diagnostico_marketing/
│   └── SKILL.md
├── skill_cliente_objetivo/
│   └── SKILL.md
├── skill_propuesta_valor/
│   └── SKILL.md
├── skill_analisis_competencia/
│   └── SKILL.md
├── skill_matriz_canales/
│   └── SKILL.md
├── skill_estrategia_comunicacion/
│   └── SKILL.md
├── skill_plan_accion/
│   └── SKILL.md
├── skill_presupuesto_marketing/
│   └── SKILL.md
├── skill_kpis/
│   └── SKILL.md
├── skill_resumen_plan_empresa/
│   └── SKILL.md
├── skill_auditoria_coherencia/
│   └── SKILL.md
└── skill_change_request/
    └── SKILL.md
```

Cada skill debe tener su propio `SKILL.md`.

En fases futuras puede incluir:

```text
references/
templates/
examples/
scripts/
```

---

## 15. Carpeta src/

Contiene el código de la aplicación.

Para el MVP, la aplicación puede empezar como CLI o flujo documental sencillo.

Estructura inicial sugerida:

```text
src/
├── __init__.py
├── main.py
├── config/
├── core/
├── services/
├── validators/
└── utils/
```

### 15.1 src/main.py

Punto de entrada inicial.

Debe permitir ejecutar acciones básicas como:

- crear nuevo proyecto,
- validar estructura,
- generar plan,
- aplicar cambio,
- ejecutar auditoría.

### 15.2 src/config/

Configuración del sistema.

Ejemplos:

```text
src/config/
├── settings.py
└── paths.py
```

### 15.3 src/core/

Lógica central del sistema.

Ejemplos:

```text
src/core/
├── project_manager.py
├── workflow_runner.py
├── phase_manager.py
├── version_manager.py
└── change_manager.py
```

### 15.4 src/services/

Servicios internos.

Ejemplos:

```text
src/services/
├── file_service.py
├── template_service.py
├── output_service.py
└── audit_service.py
```

### 15.5 src/validators/

Validaciones deterministas.

Ejemplos:

```text
src/validators/
├── structure_validator.py
├── project_validator.py
├── output_validator.py
└── gate_validator.py
```

### 15.6 src/utils/

Funciones auxiliares.

Ejemplos:

```text
src/utils/
├── text_utils.py
├── date_utils.py
└── path_utils.py
```

---

## 16. Carpeta tests/

Contiene pruebas del sistema.

Estructura inicial:

```text
tests/
├── test_project_creation.py
├── test_structure_validator.py
├── test_change_manager.py
├── test_version_manager.py
└── test_gate_validator.py
```

Las pruebas del MVP deben enfocarse primero en:

- creación de proyecto limpio,
- estructura de carpetas,
- rutas correctas,
- no contaminación del repositorio base,
- creación de outputs,
- registro de changelog,
- y versionado.

---

## 17. Carpeta project_template/

Contiene la estructura limpia que se copiará para crear cada nuevo proyecto.

Estructura recomendada:

```text
project_template/
├── project_config.json
├── context/
│   ├── empresa.md
│   ├── servicios.md
│   ├── cliente_objetivo.md
│   ├── contexto_mercado.md
│   ├── canales_actuales.md
│   └── restricciones.md
├── outputs/
│   ├── plan_actual/
│   ├── versiones/
│   ├── changelog/
│   └── auditorias/
└── logs/
```

La plantilla debe estar vacía de datos reales.

Puede contener archivos base con instrucciones o placeholders.

---

## 18. Carpeta projects/

Contiene instancias generadas de proyectos.

Ejemplo:

```text
projects/
├── proyecto_servicios_logisticos/
├── proyecto_clinica_fisioterapia/
└── proyecto_taller_artesanal/
```

Cada proyecto debe crearse copiando `project_template/`.

Regla:

```text
Nunca se debe crear un nuevo proyecto copiando un proyecto anterior ya usado.
```

---

## 19. Estructura de una instancia de proyecto

Cada instancia debe tener:

```text
projects/nombre_del_proyecto/
├── project_config.json
├── context/
├── outputs/
│   ├── plan_actual/
│   ├── versiones/
│   ├── changelog/
│   └── auditorias/
└── logs/
```

---

## 20. Archivo project_config.json

Contiene configuración mínima del proyecto.

Ejemplo conceptual:

```json
{
  "project_id": "proyecto_servicios_logisticos",
  "project_name": "Proyecto Servicios Logísticos",
  "created_at": "YYYY-MM-DD",
  "status": "active",
  "current_version": "v0_1",
  "plan_type": "marketing_plan",
  "business_type": "empresa_de_servicios"
}
```

No debe contener secretos ni claves API.

---

## 21. Carpeta context/ de cada proyecto

Contiene información del negocio específico.

Ejemplo:

```text
context/
├── empresa.md
├── servicios.md
├── cliente_objetivo.md
├── contexto_mercado.md
├── canales_actuales.md
└── restricciones.md
```

Esta carpeta sí puede contener datos del negocio.

Por eso pertenece a la instancia de proyecto y no al repositorio base.

---

## 22. Carpeta outputs/plan_actual/

Contiene la versión activa del Plan de Marketing.

Ejemplo:

```text
outputs/plan_actual/
├── 01_brief_negocio_validado.md
├── 02_diagnostico_marketing.md
├── 03_cliente_objetivo_y_segmentos.md
├── 04_propuesta_valor_y_posicionamiento.md
├── 05_analisis_competencia.md
├── 06_matriz_canales_marketing.md
├── 07_estrategia_comunicacion.md
├── 08_plan_accion_90_dias.md
├── 09_presupuesto_marketing.md
├── 10_kpis_y_medicion.md
├── 11_resumen_para_plan_empresa.md
└── 12_auditoria_final.md
```

---

## 23. Carpeta outputs/versions/

Guarda versiones anteriores o cerradas del plan.

Ejemplo:

```text
outputs/versions/
├── v0_1/
├── v0_2/
└── v1_0/
```

Cada versión debe contener una copia coherente de los documentos vigentes en ese momento.

---

## 24. Carpeta outputs/changelog/

Guarda registros de cambios.

Ejemplo:

```text
outputs/changelog/
├── changelog_v0_1.md
├── changelog_v0_2.md
└── change_request_v0_3.md
```

Debe registrar:

- qué cambió,
- por qué cambió,
- impacto,
- documentos afectados,
- documentos conservados,
- auditoría aplicada,
- y estado final.

---

## 25. Carpeta outputs/audits/

Guarda auditorías parciales o completas.

Ejemplo:

```text
outputs/audits/
├── auditoria_v0_1.md
├── auditoria_v0_2.md
└── auditoria_cambio_cliente_objetivo.md
```

---

## 26. Carpeta logs/

Guarda registros técnicos o funcionales de ejecución.

Ejemplos:

```text
logs/
├── project_creation.log
├── workflow_execution.log
├── gate_results.log
└── change_history.log
```

En el MVP los logs pueden ser simples archivos de texto o JSON.

No deben contener información sensible innecesaria.

---

## 27. Archivos que no deben versionarse

El repositorio debe excluir:

```text
projects/
.env
*.log
__pycache__/
.venv/
.env.local
secrets.json
api_keys.json
outputs_temporales/
```

Si se desea incluir ejemplos, deben ser ejemplos ficticios y anonimizados.

---

## 28. Archivo .gitignore recomendado

Contenido inicial sugerido:

```text
# Entornos Python
.venv/
__pycache__/
*.pyc

# Variables y secretos
.env
.env.local
secrets.json
api_keys.json

# Proyectos generados con datos reales
projects/

# Logs
*.log
logs/

# Archivos temporales
.tmp/
temp/
outputs_temporales/

# Sistema operativo
.DS_Store
Thumbs.db
```

Si más adelante se quiere versionar proyectos ficticios de ejemplo, se debe crear una carpeta separada:

```text
examples/
```

---

## 29. Carpeta examples/ futura

Puede añadirse para ejemplos demostrativos.

Ejemplo:

```text
examples/
└── ejemplo_empresa_servicios_ficticia/
```

Reglas:

- solo datos ficticios,
- sin información privada,
- sin datos de clientes reales,
- sin claves,
- sin archivos sensibles.

---

## 30. Separación entre documentación y outputs

Regla clave:

```text
docs/ explica cómo funciona el sistema.
outputs/ contiene lo que el sistema produce para un proyecto concreto.
```

No deben mezclarse.

Ejemplo incorrecto:

```text
docs/plan_marketing_cliente_real.md
```

Ejemplo correcto:

```text
projects/cliente_real/outputs/plan_actual/01_brief_negocio_validado.md
```

---

## 31. Separación entre templates y resultados

Regla:

```text
Las plantillas viven en system/templates/.
Los documentos generados viven en outputs/plan_actual/.
```

No se deben editar plantillas para resolver un caso particular de cliente.

Si un caso concreto necesita una variación, debe quedar en la instancia del proyecto.

---

## 32. Separación entre agentes y skills

Regla:

```text
agents/ define roles.
skills/ define capacidades ejecutables o reutilizables.
```

Un agente no debe vivir dentro de `skills/`.

Una skill no debe vivir dentro de `agents/`.

---

## 33. Separación entre gates documentados y validadores técnicos

En el MVP pueden existir dos niveles:

```text
system/gates/ = definición documental del gate
src/validators/ = validación determinista en código
```

Ejemplo:

```text
system/gates/gate_brief_minimo.md
src/validators/gate_validator.py
```

El documento explica qué validar.

El validador técnico puede comprobar estructura, existencia de archivos o campos mínimos.

---

## 34. Reglas de limpieza al crear un nuevo proyecto

Al crear un proyecto nuevo, el sistema debe:

1. pedir nombre del proyecto,
2. normalizar el nombre para carpeta,
3. copiar `project_template/`,
4. crear `project_config.json`,
5. dejar `context/` listo para completar,
6. dejar `outputs/` vacío,
7. crear logs iniciales,
8. verificar que no se copió información de otro proyecto,
9. confirmar ruta del nuevo proyecto.

---

## 35. Reglas de limpieza al cerrar o archivar un proyecto

Cuando un proyecto se cierre, el sistema debe poder marcarlo como:

```text
archived
```

En `project_config.json`.

No debe borrar información automáticamente.

Si se desea limpiar datos, debe hacerse con una acción explícita y controlada.

---

## 36. Criterios de aceptación de estructura

La estructura será correcta si:

- el repositorio base no contiene datos reales,
- cada proyecto se crea desde plantilla limpia,
- los outputs viven dentro de la instancia del proyecto,
- los changelogs están separados,
- las auditorías están separadas,
- las plantillas no se modifican por casos particulares,
- los agentes y skills están en carpetas distintas,
- los gates están documentados,
- y `projects/` está excluido de control de versiones cuando contiene datos reales.

---

## 37. Próximo documento recomendado

El siguiente documento debería definir la arquitectura técnica inicial.

Documento sugerido:

```text
docs/08_arquitectura_tecnica_inicial.md
```

Ese documento debe detallar:

- enfoque técnico del MVP,
- por qué empezar con CLI o flujo documental,
- módulos de Python sugeridos,
- responsabilidades de cada módulo,
- decisiones de no usar todavía MCP,
- y criterios para pasar a interfaz gráfica o web.


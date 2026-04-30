<!--
# File: docs/00_base_sistema/08_arquitectura_tecnica_inicial.md
# ──────────────────────────────────────────────────────────────────────
# Propósito: Definir la arquitectura técnica inicial del sistema.
# Rol: Documentación de arquitectura.
# ──────────────────────────────────────────────────────────────────────
-->

# 08 - Arquitectura Técnica Inicial

## 1. Propósito del documento

Este documento define la arquitectura técnica inicial del MVP del sistema agéntico para generar Planes de Marketing para empresas de servicios.

Su objetivo es establecer una base técnica simple, limpia y escalable antes de escribir código.

La arquitectura debe permitir:

- crear proyectos limpios,
- gestionar contexto,
- generar outputs documentales,
- validar estructura,
- registrar cambios,
- versionar planes,
- ejecutar gates básicos,
- y evitar contaminación del repositorio base.

Este documento complementa:

```text
docs/00_base_sistema/00_planificacion_mvp_sistema_plan_marketing.md
docs/00_base_sistema/01_alcance_funcional_mvp.md
docs/00_base_sistema/02_flujo_plan_marketing.md
docs/00_base_sistema/03_agentes_y_responsabilidades.md
docs/00_base_sistema/04_skills_y_uso.md
docs/00_base_sistema/05_gates_y_validaciones.md
docs/00_base_sistema/06_sistema_cambios_versionado.md
docs/00_base_sistema/07_estructura_repositorio.md
```

---

## 2. Principio técnico general

El MVP debe comenzar simple.

No se debe construir una aplicación web compleja antes de validar que el flujo documental funciona de principio a fin.

Regla base:

```text
Primero se valida el sistema como flujo documental controlado.
Después se evalúa interfaz, automatización e integraciones.
```

El primer objetivo técnico no es tener una interfaz bonita, sino garantizar que el sistema pueda:

- crear una estructura correcta,
- guardar contexto,
- producir documentos en rutas esperadas,
- validar mínimos,
- registrar cambios,
- y mantener versiones.

---

## 3. Enfoque técnico del MVP

El MVP iniciará como una aplicación local en Python con enfoque CLI/documental.

Esto significa que la primera versión podrá ejecutarse desde terminal con comandos simples.

Ejemplos conceptuales:

```text
crear_proyecto
validar_estructura
generar_plan
ejecutar_auditoria
registrar_cambio
crear_version
```

La interfaz gráfica queda fuera del primer ciclo técnico.

---

## 4. Por qué empezar con CLI/documental

Empezar con CLI o flujo documental tiene varias ventajas:

- reduce complejidad inicial,
- facilita depuración,
- evita mezclar lógica con interfaz,
- permite probar rutas y outputs,
- permite validar estructura de carpetas,
- facilita pruebas automatizadas,
- mantiene el repositorio limpio,
- y permite evolucionar luego a Gradio, Streamlit o FastAPI.

Este enfoque sigue el principio de desarrollo híbrido:

```text
IA para interpretar, redactar y proponer.
Python determinista para rutas, archivos, validaciones, logs, versiones y estructura.
```

---

## 5. Responsabilidades de Python en el MVP

Python debe encargarse de lo que requiere exactitud y repetibilidad.

Responsabilidades principales:

- crear carpetas,
- copiar plantillas,
- normalizar nombres,
- generar archivos base,
- validar existencia de documentos,
- verificar estructura del proyecto,
- registrar logs,
- crear changelogs,
- copiar versiones,
- listar documentos afectados,
- ejecutar validaciones estructurales,
- y prevenir escritura en rutas incorrectas.

Python no debe intentar reemplazar la interpretación estratégica de marketing.

---

## 6. Responsabilidades de la IA en el MVP

La IA debe encargarse de tareas interpretativas y generativas.

Responsabilidades principales:

- ayudar a ordenar información del negocio,
- redactar documentos del Plan de Marketing,
- detectar vacíos de información,
- proponer hipótesis claramente marcadas,
- sugerir canales,
- formular propuesta de valor,
- redactar resumen para Plan de Empresa,
- y apoyar auditorías cualitativas.

La IA no debe manejar sola:

- rutas,
- nombres de archivos,
- versionado,
- limpieza del repositorio,
- estructura de carpetas,
- ni decisiones técnicas críticas.

---

## 7. Estructura técnica inicial

La carpeta de código será:

```text
├── .claude/
│   └── skills/         # Definición agéntica
├── system/             # Definición documental (Gates, Rules, Workflows)
├── docs/               # Planificación y estándares (Base, Estándares, Manual)
├── src/
│   ├── __init__.py
│   ├── main.py
│   ├── config/
│   ├── core/
│   ├── services/
│   ├── validators/
│   └── utils/
└── project_template/
```

Esta estructura busca separar responsabilidades desde el inicio sin sobrediseñar.

---

## 8. src/main.py

### 8.1 Propósito

Será el punto de entrada de la aplicación.

En el MVP puede funcionar como CLI simple.

### 8.2 Responsabilidades

Debe permitir ejecutar operaciones principales como:

```text
crear_nuevo_proyecto
validar_estructura
generar_archivos_base
registrar_cambio
crear_version
ejecutar_auditoria_estructural
```

### 8.3 Qué no debe hacer

No debe contener toda la lógica del sistema.

Debe llamar a módulos internos.

Regla:

```text
main.py coordina comandos.
No concentra toda la lógica.
```

---

## 9. src/config/

### 9.1 Propósito

Contiene configuración del sistema.

Estructura sugerida:

```text
src/config/
├── settings.py
└── paths.py
```

### 9.2 settings.py

Debe contener configuración general no sensible.

Ejemplos:

```text
nombre_del_sistema
version_del_sistema
carpeta_project_template
carpeta_projects
version_inicial
```

### 9.3 paths.py

Debe centralizar rutas importantes.

Ejemplos:

```text
BASE_DIR
PROJECT_TEMPLATE_DIR
PROJECTS_DIR
DOCS_DIR
SYSTEM_DIR
```

### 9.4 Regla importante

No debe contener claves API ni secretos.

Los secretos, si algún día existen, deberán ir en variables de entorno o `.env`, nunca en código versionado.

---

## 10. src/core/

### 10.1 Propósito

Contiene la lógica central del sistema.

Estructura sugerida:

```text
src/core/
├── project_manager.py
├── workflow_runner.py
├── phase_manager.py
├── version_manager.py
└── change_manager.py
```

---

## 11. project_manager.py

### 11.1 Propósito

Gestionar la creación y estado de proyectos.

### 11.2 Responsabilidades

- crear nuevo proyecto desde `project_template/`,
- normalizar nombre del proyecto,
- crear `project_config.json`,
- verificar que no exista un proyecto con el mismo nombre,
- impedir copiar desde un proyecto usado,
- validar estructura inicial,
- marcar proyecto como activo o archivado.

### 11.3 Funciones esperadas conceptuales

```text
create_project()
validate_project_exists()
load_project_config()
update_project_status()
```

---

## 12. workflow_runner.py

### 12.1 Propósito

Coordinar la ejecución de workflows.

### 12.2 Responsabilidades

- ejecutar flujo principal del Plan de Marketing,
- ejecutar flujo de cambios,
- ejecutar auditoría,
- coordinar fases,
- llamar validadores,
- registrar estado de ejecución.

### 12.3 Nota importante

En el MVP, este módulo puede ser muy simple.

No debe intentar crear un orquestador complejo desde el inicio.

---

## 13. phase_manager.py

### 13.1 Propósito

Gestionar las fases del Plan de Marketing.

### 13.2 Responsabilidades

- listar fases,
- conocer orden de fases,
- verificar documentos requeridos por fase,
- marcar estado de una fase,
- identificar fase siguiente,
- detectar fases bloqueadas.

### 13.3 Estados posibles

```text
pendiente
en_proceso
bloqueada
aprobada_con_observaciones
aprobada
actualizada
```

---

## 14. version_manager.py

### 14.1 Propósito

Gestionar versiones del Plan de Marketing.

### 14.2 Responsabilidades

- crear nueva versión,
- copiar `outputs/plan_actual/` a `outputs/versions/vX/`,
- actualizar versión actual en `project_config.json`,
- listar versiones disponibles,
- evitar sobrescrituras,
- preservar versiones anteriores.

### 14.3 Regla

```text
Una versión cerrada no debe modificarse directamente.
Si hay cambios, se crea una nueva versión.
```

---

## 15. change_manager.py

### 15.1 Propósito

Gestionar solicitudes de cambio.

### 15.2 Responsabilidades

- registrar solicitud de cambio,
- clasificar impacto,
- identificar documentos afectados,
- crear archivo de change request,
- actualizar changelog,
- coordinar auditoría posterior,
- preparar nueva versión si corresponde.

### 15.3 Relación con IA

La IA puede ayudar a interpretar el cambio.

Python debe registrar, organizar y versionar la información de forma determinista.

---

## 16. src/services/

### 16.1 Propósito

Contiene servicios auxiliares para operaciones repetibles.

Estructura sugerida:

```text
src/services/
├── file_service.py
├── template_service.py
├── output_service.py
└── audit_service.py
```

---

## 17. file_service.py

### 17.1 Responsabilidades

- crear carpetas,
- copiar archivos,
- leer archivos,
- escribir archivos,
- verificar existencia,
- prevenir sobrescrituras accidentales,
- manejar rutas de forma segura.

---

## 18. template_service.py

### 18.1 Responsabilidades

- leer plantillas,
- copiar plantillas base,
- preparar archivos iniciales de contexto,
- validar que las plantillas existan.

---

## 19. output_service.py

### 19.1 Responsabilidades

- guardar documentos generados,
- verificar rutas de outputs,
- listar documentos del plan actual,
- identificar documentos faltantes,
- preparar estructura de outputs.

---

## 20. audit_service.py

### 20.1 Responsabilidades

- registrar resultados de auditorías,
- guardar reportes de gates,
- organizar auditorías parciales y finales,
- mantener relación entre auditoría y versión.

---

## 21. src/validators/

### 21.1 Propósito

Contiene validaciones deterministas.

Estructura sugerida:

```text
src/validators/
├── structure_validator.py
├── project_validator.py
├── output_validator.py
└── gate_validator.py
```

---

## 22. structure_validator.py

### 22.1 Responsabilidades

Validar que el repositorio base tenga las carpetas esperadas.

Debe verificar:

- `docs/`,
- `system/`,
- `agents/`,
- `.claude/skills/`,
- `src/`,
- `tests/`,
- `project_template/`.

---

## 23. project_validator.py

### 23.1 Responsabilidades

Validar una instancia de proyecto.

Debe verificar:

- existencia de `project_config.json`,
- existencia de `context/`,
- existencia de `outputs/`,
- existencia de `outputs/plan_actual/`,
- existencia de `outputs/versions/`,
- existencia de `outputs/changelog/`,
- existencia de `outputs/audits/`,
- existencia de `logs/`.

---

## 24. output_validator.py

### 24.1 Responsabilidades

Validar documentos generados.

Debe verificar si existen los documentos esperados:

```text
01_brief_negocio_validado.md
02_diagnostico_marketing.md
03_cliente_objetivo_y_segmentos.md
04_propuesta_valor_y_posicionamiento.md
05_analisis_competencia.md
06_matriz_canales_marketing.md
07_estrategia_comunicacion.md
08_plan_accion_90_dias.md
09_presupuesto_marketing.md
10_kpis_y_medicion.md
11_resumen_para_plan_empresa.md
12_auditoria_final.md
```

En el MVP puede validar existencia y estructura mínima.

Más adelante puede validar contenido interno con reglas más finas.

---

## 25. gate_validator.py

### 25.1 Responsabilidades

Ejecutar validaciones básicas asociadas a gates.

En el MVP, puede validar:

- si existe documento requerido,
- si tiene secciones mínimas,
- si se registró estado,
- si se declaró información faltante,
- si hay resultado de gate.

La validación cualitativa profunda puede seguir apoyándose en IA y auditoría.

---

## 26. src/utils/

### 26.1 Propósito

Contiene funciones auxiliares.

Estructura sugerida:

```text
src/utils/
├── text_utils.py
├── date_utils.py
└── path_utils.py
```

---

## 27. text_utils.py

### 27.1 Responsabilidades

- normalizar nombres,
- crear slugs,
- limpiar textos básicos,
- convertir nombres a snake_case si aplica.

---

## 28. date_utils.py

### 28.1 Responsabilidades

- obtener fecha actual,
- crear timestamps,
- formatear fechas para archivos,
- registrar fechas en changelog.

---

## 29. path_utils.py

### 29.1 Responsabilidades

- construir rutas seguras,
- validar que una ruta pertenece al proyecto correcto,
- evitar escritura fuera de carpetas permitidas,
- resolver rutas relativas.

---

## 30. Tests iniciales

La carpeta `tests/` debe validar primero lo más crítico:

```text
tests/
├── test_project_creation.py
├── test_structure_validator.py
├── test_project_validator.py
├── test_version_manager.py
├── test_change_manager.py
└── test_output_validator.py
```

---

## 31. Pruebas mínimas del MVP

### 31.1 test_project_creation.py

Debe comprobar que:

- se crea una carpeta de proyecto,
- se copia `project_template/`,
- se crea `project_config.json`,
- no se sobrescribe un proyecto existente,
- y no se copian datos de otro proyecto.

### 31.2 test_structure_validator.py

Debe comprobar que el repositorio base tiene la estructura mínima.

### 31.3 test_project_validator.py

Debe comprobar que una instancia de proyecto tiene carpetas obligatorias.

### 31.4 test_version_manager.py

Debe comprobar que se pueden crear versiones sin sobrescribir.

### 31.5 test_change_manager.py

Debe comprobar que una solicitud de cambio genera registro.

### 31.6 test_output_validator.py

Debe comprobar que el sistema detecta documentos faltantes.

---

## 32. Datos y persistencia

En el MVP no se usará base de datos.

La persistencia será por archivos:

```text
project_config.json
context/*.md
outputs/**/*.md
logs/*.log
```

Esto simplifica el desarrollo y facilita revisión manual.

Una base de datos solo se evaluará si más adelante aparecen necesidades como:

- multiusuario,
- historial complejo,
- dashboard,
- búsqueda avanzada,
- permisos,
- o trabajo colaborativo.

---

## 33. Formato de documentos

El formato principal será Markdown.

Razones:

- fácil de leer,
- fácil de versionar,
- compatible con repositorios,
- exportable a PDF o DOCX más adelante,
- útil para revisión humana,
- y adecuado para trabajo con IA.

---

## 34. Formato de configuración

El formato para configuración será JSON.

Archivo principal:

```text
project_config.json
```

Debe contener información operativa mínima del proyecto.

No debe contener información sensible.

---

## 35. Logs

Los logs del MVP pueden ser simples.

Ejemplos:

```text
logs/project_creation.log
logs/workflow_execution.log
logs/change_history.log
logs/gate_results.log
```

En fases futuras se puede pasar a logs estructurados en JSONL.

---

## 36. No uso de MCP en el MVP

El MVP no incluirá MCP.

Razones:

- todavía no hay necesidad de herramientas externas vivas,
- primero se debe validar el flujo documental,
- agregar MCP aumentaría complejidad,
- y podría distraer del objetivo principal.

MCP se evaluará después para casos como:

- GA4,
- Google Search Console,
- Google Ads,
- Notion,
- CRM,
- Mailchimp,
- Zapier,
- generación visual.

Pero solo si existe una necesidad real y justificada.

---

## 37. No uso de interfaz gráfica en el primer ciclo

El MVP técnico inicial no necesita interfaz gráfica.

Primero debe poder ejecutarse y validarse desde terminal.

Luego se podrá evaluar:

```text
Gradio
Streamlit
FastAPI + frontend
```

### 37.1 Gradio

Útil si se quiere una interfaz rápida para pruebas guiadas.

### 37.2 Streamlit

Útil si se quiere una interfaz documental o panel simple.

### 37.3 FastAPI + frontend

Útil si el sistema evoluciona hacia producto web más formal.

No debe elegirse esta opción antes de validar el flujo base.

---

## 38. Comandos conceptuales del MVP

Los comandos reales se definirán al programar, pero conceptualmente se necesitarán acciones como:

```text
create-project
validate-base-structure
validate-project
list-phases
check-outputs
create-version
register-change
run-audit
```

Ejemplo conceptual:

```text
python -m src.main create-project nombre_del_proyecto
```

Esto es solo una referencia conceptual, no una decisión final de sintaxis.

---

## 39. Seguridad básica

Aunque el MVP sea local, debe respetar reglas básicas:

- no guardar secretos en código,
- no versionar proyectos reales,
- no escribir fuera de carpetas permitidas,
- evitar sobrescrituras accidentales,
- preservar versiones anteriores,
- y no mezclar datos entre proyectos.

---

## 40. Criterios para pasar a una interfaz

Solo se debe pasar a una interfaz visual cuando:

- crear proyectos funcione bien,
- la estructura se valide correctamente,
- los outputs se generen en rutas correctas,
- el versionado funcione,
- el flujo de cambios esté probado,
- y los documentos sean útiles para revisión.

Antes de eso, una interfaz puede ocultar errores.

---

## 41. Criterios de aceptación técnica del MVP

La arquitectura técnica inicial será válida si permite:

- crear un proyecto desde plantilla limpia,
- validar estructura del repositorio base,
- validar estructura de una instancia de proyecto,
- detectar outputs faltantes,
- crear changelog,
- crear versiones,
- registrar cambios,
- evitar sobrescrituras,
- mantener proyectos separados,
- y trabajar sin necesidad de MCP, base de datos o interfaz gráfica.

---

## 42. Riesgos técnicos a controlar

### 42.1 Sobrediseño

Riesgo:

Crear una arquitectura demasiado compleja antes de validar el flujo.

Control:

Empezar con módulos simples y pruebas pequeñas.

### 42.2 Mezcla entre app y documentos

Riesgo:

Meter lógica de negocio en documentos o lógica documental en código sin separación.

Control:

Separar `docs/`, `system/`, `agents/`, `.claude/skills/`, `src/`, `projects/` y `workspace/`.

### 42.3 Contaminación de proyectos

Riesgo:

Copiar información de un proyecto anterior.

Control:

Crear siempre desde `project_template/`.

### 42.4 Sobrescritura de versiones

Riesgo:

Modificar versiones cerradas.

Control:

Crear nueva versión en lugar de editar una cerrada.

### 42.5 Dependencia prematura de IA

Riesgo:

Dejar rutas, archivos y validaciones en manos de IA.

Control:

Usar Python determinista para estructura, rutas, validación y versionado.

---

## 43. Próximo documento recomendado

El siguiente documento debería definir los criterios de hecho del sistema.

Documento sugerido:

```text
docs/00_base_sistema/09_criterios_de_hecho.md
```

Ese documento debe detallar cuándo se considera completa:

- una fase,
- una skill,
- un gate,
- un output,
- una versión,
- una solicitud de cambio,
- y el MVP completo.


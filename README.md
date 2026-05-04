# Marketing Plan Agent Base

Sistema agéntico para crear, revisar y actualizar Planes de Marketing para cualquier tipo de negocio (productos, servicios, ecommerce, retail, B2B, B2C, educativos o híbridos).

Este repositorio funciona como una base reutilizable. Su objetivo es permitir que cada nuevo Plan de Marketing se trabaje en una instancia limpia, separada del repositorio principal, evitando contaminación entre proyectos, pérdida de contexto o mezcla de información de distintos negocios.

---

## 1. Qué es este proyecto

`marketing_plan_agent_base` es un sistema diseñado para ayudar a construir Planes de Marketing de forma ordenada, trazable y validada.

No es una herramienta para publicar automáticamente en redes sociales, lanzar campañas publicitarias o gestionar un CRM.

La primera versión se enfoca en algo más básico y más importante:

```text
crear una estructura limpia,
recoger contexto del negocio,
generar documentos del Plan de Marketing,
validar fases,
registrar cambios,
versionar el plan,
y mantener separado cada proyecto.
```

El sistema es agnóstico al tipo de negocio, permitiendo modelar empresas de productos, servicios, ecommerce o modelos híbridos.

---

## 2. Objetivo del MVP

El MVP busca validar el flujo documental y técnico antes de construir una interfaz compleja o integrar herramientas externas.

La primera versión debe permitir:

- crear un nuevo proyecto desde una plantilla limpia,
- guardar información inicial del negocio,
- trabajar el Plan de Marketing por fases,
- generar documentos Markdown,
- validar estructura y archivos mínimos,
- registrar cambios,
- crear versiones,
- y mantener el repositorio base limpio.

La prioridad del MVP no es automatizar todo, sino asegurar que el sistema sea confiable, ordenado y reutilizable.

---

## 3. Qué problema resuelve

Cuando se trabaja con IA para crear documentos estratégicos, suelen aparecer varios problemas:

- se mezcla información de distintos proyectos,
- se generan documentos largos pero poco accionables,
- se salta directamente a contenidos o redes sociales sin diagnóstico previo,
- se inventan datos no confirmados,
- no queda claro qué cambió entre versiones,
- no existe una separación entre sistema base y proyecto real,
- y no hay validaciones antes de avanzar.

Este repositorio busca evitar esos problemas mediante:

- estructura de carpetas clara,
- agentes con responsabilidades separadas,
- skills reutilizables,
- gates de validación,
- versionado,
- changelog,
- auditoría,
- y reglas de repositorio limpio.

---

## 4. Qué hace el sistema

El sistema permite construir un Plan de Marketing mediante un flujo por fases.

El flujo previsto es:

```text
01_intake_y_brief
02_diagnostico_marketing
03_cliente_objetivo_y_segmentos
04_propuesta_valor_y_posicionamiento
05_analisis_competencia
06_matriz_canales_marketing
07_estrategia_comunicacion
08_plan_accion_90_dias
09_presupuesto_marketing
10_kpis_y_medicion
11_resumen_para_plan_empresa
12_auditoria_final
```

Cada fase debe generar un documento propio dentro de la carpeta del proyecto.

Ejemplo:

```text
projects/nombre_del_proyecto/outputs/plan_actual/01_brief_negocio_validado.md
```

---

## 5. Qué no hace el MVP

El MVP no incluye todavía:

- publicación automática en redes sociales,
- programación de contenidos,
- generación automática de imágenes,
- conexión con Notion,
- task bot,
- MCP,
- CRM,
- dashboards avanzados,
- Google Analytics,
- Google Ads,
- LinkedIn Ads,
- Mailchimp,
- Zapier,
- base de datos,
- aplicación web,
- multiusuario,
- permisos por roles,
- ni exportación avanzada a PDF o DOCX.

Estas funciones pueden evaluarse en fases futuras, cuando el flujo base esté validado.

---

## 6. Principio de arquitectura

El sistema trabaja con dos niveles separados:

```text
repositorio_base
instancias_de_proyecto
```

El repositorio base contiene:

- documentación,
- reglas,
- agentes,
- skills,
- gates,
- workflows,
- plantillas,
- código Python,
- pruebas,
- y plantilla base para nuevos proyectos.

Cada instancia de proyecto contiene:

- contexto del negocio,
- outputs del Plan de Marketing,
- versiones,
- changelog,
- auditorías,
- y logs.

Regla principal:

```text
El repositorio base no debe contener datos reales de clientes ni outputs de proyectos concretos.
```

---

## 7. Estructura general del repositorio

Estructura esperada:

```text
marketing_plan_agent_base/
├── README.md
├── AGENTS.md
├── .claude/
│   └── skills/         # Skills operativas (13 skills)
├── docs/               # Documentación viva (Base, Estándares, Manual)
├── system/             # Reglas, gates y workflows del sistema
├── agents/             # Definición de agentes
├── src/
├── tests/
├── project_template/
├── projects/           # Banco local de proyectos (ignorado por Git)
├── workspace/          # Taller variable (ignorado por Git)
├── pyproject.toml
└── .gitignore
```

### 7.1 `docs/`

Contiene la documentación del sistema.

Aquí viven los documentos de planificación, arquitectura, decisiones, flujo, gates, versionado y criterios de hecho.

No debe contener Planes de Marketing reales.

### 7.2 `system/`

Contiene reglas, workflows, gates y plantillas del sistema.

Estructura prevista:

```text
system/
├── rules/
├── workflows/
├── gates/
└── templates/
```

### 7.3 `agents/`

Contiene la definición de los agentes del sistema.

Agentes iniciales previstos:

```text
orquestador_plan_marketing
investigador_marketing
estratega_marketing
redactor_marketing
analista_metricas
auditor_plan_marketing
```

Toda skill nueva debe ir a `.claude/skills/<nombre>/SKILL.md`. La arquitectura está diseñada para que el motor operativo sea independiente de los datos de trabajo.

### 7.5 `src/`

Contiene el código Python del sistema.

Estructura inicial prevista:

```text
src/
├── main.py
├── config/
├── core/
│   └── marketing_profile_resolver.py  # Resolución de perfil de negocio (B2B, B2C, etc.)
├── services/                          # Lógica de las 12 fases
├── validators/                        # Validadores de estructura y brief
└── utils/
```

El archivo `marketing_profile_resolver.py` es una pieza central: permite que las Fases 06 a 12 adapten dinámicamente canales, tono, tácticas, presupuesto y KPIs según el tipo de negocio detectado.

### 7.6 `project_template/`

Contiene la plantilla limpia que se copia cada vez que se crea un nuevo proyecto.

Esta carpeta no debe tener datos reales.

### 7.7 `projects/`

Contiene proyectos generados localmente. Funciona como banco de validación para
pruebas del pipeline end-to-end con distintos modelos de negocio.

**Reglas**:
- Ignorada por Git en su totalidad.
- No entra en el ZIP de distribución (v1.1 o cualquier versión).
- No debe contener datos reales de clientes en el repositorio compartido.
- Cada proyecto nuevo se crea desde `project_template/`, no copiando uno existente.

### 7.7 `workspace/reports/`

Contiene historiales de sesiones, auditorías pasadas e hitos de validación.

**Reglas**:
- Es historial de trabajo, no parte del sistema distribuible.
- Carpeta ignorada por Git (vía `.gitignore`) para mantener el núcleo limpio.
- No entra en el ZIP de distribución.

---

## 8. Estructura de un proyecto generado

Cada proyecto generado debe tener una estructura similar a esta:

```text
projects/nombre_del_proyecto/
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
│   ├── versions/
│   ├── changelog/
│   └── audits/
└── logs/
```

### 8.1 `context/`

Guarda información del negocio.

### 8.2 `outputs/plan_actual/`

Guarda la versión activa del Plan de Marketing.

### 8.3 `outputs/versions/`

Guarda versiones cerradas o anteriores.

### 8.4 `outputs/changelog/`

Guarda registros de cambios.

### 8.5 `outputs/audits/`

Guarda auditorías parciales o finales.

### 8.6 `logs/`

Guarda registros técnicos o funcionales de ejecución.

---

## 9. Sistema de perfiles de marketing

Para evitar sesgos (especialmente el de venta consultiva/B2B), el sistema clasifica el negocio en una de estas categorías antes de generar las fases tácticas:

- **`ecommerce_transaccional`**: Tiendas online D2C con alto volumen transaccional. Foco en conversión, ROAS, checkout y recuperación de carrito.
- **`b2c_producto_ecommerce`**: Venta directa de productos físicos al consumidor final por canales digitales. Perfil complementario al anterior.
- **`b2b_producto_industrial`**: Venta de productos, maquinaria o insumos a otras empresas. Basado en catálogos, ferias y contratos de suministro.
- **`retail_fisico`**: Negocios con sede física y venta de productos en local. Foco en tráfico peatonal y visibilidad geográfica.
- **`b2b_consultivo`**: Servicios profesionales o técnicos complejos dirigidos a empresas. Ciclos de venta largos basados en autoridad y confianza.
- **`b2c_local_servicios`**: Negocios de cercanía (estética, salud, talleres, etc.) orientados a servicios personales en zona geográfica delimitada.
- **`educativo_formativo`**: Academias, cursos y servicios de capacitación. Foco en demostración de valor antes de la venta.
- **`hibrido_producto_servicio`**: Venta de un activo físico acompañado de contrato de servicio recurrente (mantenimiento, soporte, SLA).
- **`estrategia_general_prudente`**: Perfil de reserva (fallback). Se activa únicamente si el brief es ambiguo o con información insuficiente para clasificar. No debe activarse para negocios con modelo evidente.

### Lógica de clasificación
- El resolver analiza el texto de los campos: `tipo_negocio`, `oferta_principal`, `cliente_objetivo` y `problema_que_resuelve`.
- **Umbral**: Requiere al menos 2 coincidencias de palabras clave para asignar un perfil.
- **Desempate**: Si hay un empate entre perfiles o no se alcanza el umbral, se asigna `estrategia_general_prudente` para garantizar una estrategia conservadora.

---

## 10. Contrato mínimo del brief

Para que el sistema pueda avanzar hacia el diagnóstico, el brief inicial debe tener campos mínimos.

Campos obligatorios:

| Campo | Obligatorio | Ejemplo | Acción si falta |
|---|---:|---|---|
| `nombre_negocio` | Sí | `Belleza Serena` | Bloquea |
| `tipo_negocio` | Sí | `Ecommerce de calzado` / `Consultoría IT` | Bloquea |
| `oferta_principal` | Sí | `Zapatillas de running` / `Migración a Cloud` | Bloquea |
| `cliente_objetivo` | Sí | `Mujeres de 25 a 55 años en zona urbana cercana` | Bloquea |
| `problema_que_resuelve` | Sí | `Falta de tiempo y confianza para cuidar la piel` | Bloquea |
| `objetivo_principal` | Sí | `Captar 20 reservas mensuales` | Bloquea |
| `zona_geografica` | Sí | `Madrid, España` / `Global (Online)` | Bloquea |
| `presupuesto_marketing` | No | `300 EUR/mes` | Observación |

Si falta un campo obligatorio, el sistema no debe inventarlo. Los campos recomendados (Sección 2 del brief) no bloquean el inicio, pero su ausencia condicionará la fiabilidad de las fases tácticas posteriores.

Debe marcar el brief como incompleto y pedir la información faltante.

---

## 11. Agentes del sistema

El MVP define seis agentes iniciales.

### 11.1 `orquestador_plan_marketing`

Coordina el flujo, activa fases, controla estados y asegura que no se salten validaciones.

### 11.2 `investigador_marketing`

Analiza contexto, mercado, competencia y datos disponibles.

No decide la estrategia final.

### 11.3 `estratega_marketing`

Convierte investigación en decisiones de marketing.

Define cliente prioritario, propuesta de valor, canales y plan de acción.

### 11.4 `redactor_marketing`

Convierte decisiones estratégicas en documentos claros y útiles.

No cambia la estrategia sin declarar impacto.

### 11.5 `analista_metricas`

Define KPIs, medición y criterios de seguimiento.

Evita métricas de vanidad.

### 11.6 `auditor_plan_marketing`

Revisa coherencia, riesgos, información faltante y calidad del plan.

Puede bloquear el cierre si detecta problemas críticos.

---

## 12. Skills iniciales

Skills previstas para el MVP:

```text
skill_intake_brief
skill_diagnostico_marketing
skill_cliente_objetivo
skill_propuesta_valor
skill_analisis_competencia
skill_matriz_canales
skill_estrategia_comunicacion
skill_plan_accion
skill_presupuesto_marketing
skill_kpis
skill_resumen_plan_empresa
skill_auditoria_coherencia
skill_change_request
```

Cada skill debe tener:

- propósito,
- cuándo usarla,
- entradas necesarias,
- proceso,
- salida esperada,
- gate relacionado,
- criterios de insuficiencia,
- y límites.

---

## 13. Gates de validación

Gates previstos:

```text
gate_brief_minimo
gate_no_invencion
gate_coherencia_cliente_propuesta
gate_canales_justificados
gate_plan_accion_realista
gate_kpis_medibles
gate_resumen_plan_empresa
gate_auditoria_final
gate_impacto_cambio
```

Un gate puede devolver:

```text
aprobado
aprobado_con_observaciones
bloqueado
```

Regla importante:

```text
Documento generado no significa fase aprobada.
```

### 13.1 Estado de los gates en el MVP

Para el MVP, el sistema distingue entre criterios de calidad y controles técnicos:

- **Gates Documentales (`system/gates/*.md`)**: Son criterios de calidad, guías de revisión y guardrails operativos para agentes y humanos. No son ejecutados directamente por el CLI.
- **Validaciones Ejecutables**: El control técnico real que bloquea o condiciona el pipeline reside en:
  - `src/validators/`: Validaciones de estructura y campos mínimos.
  - `src/core/data_integrity.py`: Motor determinista que evalúa la integridad y severidad de los datos.
- **Backlog**: La implementación de un *Gate Runner* que automatice la ejecución de los archivos `.md` queda como mejora post-MVP.

---

## 14. Sistema de cambios y versionado

El Plan de Marketing se considera un documento vivo.

Por eso, los cambios deben procesarse de forma controlada.

Tipos de impacto:

```text
impacto_bajo
impacto_medio
impacto_alto
```

Flujo de cambio:

```text
solicitud_de_cambio
↓
clasificacion_de_impacto
↓
identificacion_de_documentos_afectados
↓
aprobacion_si_corresponde
↓
actualizacion_controlada
↓
auditoria_de_coherencia
↓
registro_en_changelog
↓
creacion_de_nueva_version
```

Los cambios de impacto alto requieren aprobación explícita antes de modificar el plan.

---

## 15. Uso de IA y Python en el MVP

El MVP usa un modo manual-asistido.

### 14.1 Python

Python se encarga de lo determinista:

- crear carpetas,
- copiar plantillas,
- validar estructura,
- verificar archivos,
- registrar cambios,
- crear versiones,
- prevenir sobrescrituras,
- y mantener proyectos separados.

### 14.2 IA en Antigravity

La IA apoya tareas interpretativas y de redacción:

- analizar contexto,
- redactar documentos,
- formular propuesta de valor,
- sugerir canales,
- crear diagnóstico,
- resumir para Plan de Empresa,
- y apoyar auditorías cualitativas.

La IA no debe manejar sola:

- rutas,
- nombres de archivos,
- versionado,
- estructura,
- ni limpieza del repositorio.

---

## 16. Instalación inicial

Este proyecto usa `uv` para gestionar el entorno Python.

Inicializar entorno:

```bash
uv sync
```

Si el proyecto todavía no tiene entorno creado, ejecutar:

```bash
uv init .
```

Luego sincronizar:

```bash
uv sync
```

> Nota: no se recomienda instalar dependencias manualmente con `pip` si el proyecto está usando `uv`.

---

## 17. Comandos disponibles

### 16.1 Comandos de Proyecto y Estructura

- `create-project`: Crea un nuevo proyecto desde la plantilla.
  ```bash
  uv run python -m src.main create-project --name "Mi Proyecto"
  ```
- `validate-base-structure`: Valida la estructura de la plantilla base.
  ```bash
  uv run python -m src.main validate-base-structure
  ```
- `validate-project`: Valida la estructura de un proyecto instanciado.
  ```bash
  uv run python -m src.main validate-project --name "Mi Proyecto"
  ```
- `validate-brief`: Valida que el brief del proyecto esté completo.
  ```bash
  uv run python -m src.main validate-brief --name "Mi Proyecto"
  ```
- `create-system-copy`: Crea una copia limpia y estéril del sistema base para un nuevo repositorio.
  ```bash
  uv run python scripts/create_system_copy.py
  ```

### 16.2 Comandos de Generación de Fases (Pipeline)

- `generate-brief-output`: Genera el documento formal de brief validado (Fase 01).
- `generate-diagnostico-output`: Genera el documento de diagnóstico inicial (Fase 02).
- `generate-cliente-output`: Genera el documento de cliente y segmentos (Fase 03).
- `generate-propuesta-valor-output`: Genera el documento de propuesta de valor (Fase 04).
- `generate-competencia-output`: Genera el documento de análisis de competencia (Fase 05).
- `generate-canales-output`: Genera el documento de matriz de canales (Fase 06).
- `generate-comunicacion-output`: Genera el documento de estrategia de comunicación (Fase 07).
- `generate-plan-accion-output`: Genera el documento del plan de acción 90 días (Fase 08).
- `generate-presupuesto-output`: Genera el documento de presupuesto de marketing (Fase 09).
- `generate-kpis-output`: Genera el documento de KPIs y medición inicial (Fase 10).
- `generate-resumen-empresa-output`: Genera el resumen ejecutivo para plan de empresa (Fase 11).
- `generate-auditoria-output`: Genera la auditoría final del plan de marketing (Fase 12).

### 16.3 Ejemplo de ejecución del pipeline completo

```bash
uv run python -m src.main create-project --name "Mi Proyecto"
uv run python -m src.main validate-brief --name "Mi Proyecto"

uv run python -m src.main generate-brief-output --name "Mi Proyecto"
uv run python -m src.main generate-diagnostico-output --name "Mi Proyecto"
uv run python -m src.main generate-cliente-output --name "Mi Proyecto"
uv run python -m src.main generate-propuesta-valor-output --name "Mi Proyecto"
uv run python -m src.main generate-competencia-output --name "Mi Proyecto"
uv run python -m src.main generate-canales-output --name "Mi Proyecto"
uv run python -m src.main generate-comunicacion-output --name "Mi Proyecto"
uv run python -m src.main generate-plan-accion-output --name "Mi Proyecto"
uv run python -m src.main generate-presupuesto-output --name "Mi Proyecto"
uv run python -m src.main generate-kpis-output --name "Mi Proyecto"
uv run python -m src.main generate-resumen-empresa-output --name "Mi Proyecto"
uv run python -m src.main generate-auditoria-output --name "Mi Proyecto"
```

### 16.4 Pruebas (Testing)

Para ejecutar las pruebas unitarias del sistema (como el resolver de perfiles):

```bash
uv run pytest
```

---

## 18. Flujo recomendado de uso

### Paso 1: Crear proyecto

```bash
uv run python -m src.main create-project --name "Mi Proyecto"
```

### Paso 2: Completar contexto

Editar archivos dentro de:

```text
projects/mi_proyecto/context/
```

Archivos iniciales:

```text
empresa.md
servicios.md
cliente_objetivo.md
contexto_mercado.md
canales_actuales.md
restricciones.md
```

### Paso 3: Generar o redactar documentos del plan

Los documentos del Plan de Marketing deben guardarse en:

```text
projects/mi_proyecto/outputs/plan_actual/
```

### Paso 4: Validar la estructura y el brief antes de generar documentos

```bash
uv run python -m src.main validate-base-structure
uv run python -m src.main validate-project --name "Mi Proyecto"
uv run python -m src.main validate-brief --name "Mi Proyecto"
```

### Paso 5: Versionar y registrar cambios

El versionado y changelog también se ampliarán en las siguientes fases.

---

## 19. Estado actual del desarrollo

Estado actual:

```text
mvp_multimodelo_integridad_operativa_estabilizado
```

Logros confirmados:
- Pipeline de 12 fases implementado y funcional.
- Motor de Integridad de Datos v1.6 implementado en `src/core/data_integrity.py`.
- Integración del motor en F01 Brief, F11 Resumen Ejecutivo y F12 Auditoría Final.
- Protección de datos sensibles y separación entre hechos, supuestos y vacíos.
- Validadores de estructura base y de proyectos operativos.
- Resolver de perfiles dinámico con 9 modelos de negocio.
- 13 skills operativas en `.claude/skills/`.
- Tests completos en verde (30 passed).
- Gates documentales aclarados como criterios de calidad para el MVP.

Backlog post-MVP:
- **Mejoras estratégicas F11/F12**:
  - Adaptar narrativa del resumen ejecutivo por perfil de negocio.
  - Adaptar KPIs, riesgos y recomendaciones según el modelo (D2C, Retail, B2B, etc.).
  - Reducir sesgo de servicios consultivos en recomendaciones (ej. "guiones de venta").
  - Fortalecer auditoría semántica entre fases (F02-F10) para detectar contradicciones reales.
  - Validar negocios mixtos reales con outputs completos.
- **Evolución del Entregable Final**:
  - Implementación del **Pre-informe de Validación** (Checkpoint estratégico).
  - Implementación del generador del Informe Final del Plan de Marketing consolidado.
  - Selector de nivel de lectura del informe final (experto, ejecutivo, sencillo).
  - Generación y exportación automática del informe final consolidado.
- **Evolución Técnica**:
  - Gate Runner ejecutable (automatización de validación de archivos `.md` de gates).
  - Parser Markdown más robusto ante variaciones de formato.
  - Mejoras de matching del resolver para casos borde.

---

## 20. Entregable final del usuario

Esta sección define el producto final que recibe el usuario del sistema tras completar todas las fases de validación.

### 20.1 Definición y Alcance
El producto final es un **Informe Final de Plan de Marketing** consolidado que agrupa el conocimiento estratégico generado y validado.

**Nota sobre F11 (Resumen de Decisiones):** La Fase 11 no constituye un entregable independiente para el usuario, sino que funciona como un insumo interno de síntesis para el Informe Final.

Para asegurar la calidad profesional de este entregable, el sistema sigue el:
👉 [Estándar Profesional del Informe Final](docs/01_estandares/estandar_entregable_final_plan_marketing.md)

### 20.2 Qué recibe el usuario
- Un documento único consolidado y coherente.
- Un análisis adaptado a su **nivel de lectura** (experto, ejecutivo o sencillo).
- Un reporte de **Integridad de Datos** que garantiza transparencia sobre vacíos y supuestos.

### 20.3 Checkpoint: Pre-informe de Validación
Antes de la entrega definitiva, el sistema genera un **Pre-informe de Validación** para confirmar con el usuario que la base estratégica (negocio, cliente, canales y presupuesto) es correcta antes de proceder a la redacción final.

---

## 21. Reglas importantes del repositorio

1. No guardar datos reales en el repositorio base.
2. No versionar `projects/` si contiene información real.
3. No reutilizar un proyecto anterior para un negocio nuevo.
4. Crear cada proyecto desde `project_template/`.
5. No saltar gates.
6. No asumir LinkedIn ni otra red social como canal obligatorio.
7. No tratar el Plan de Marketing como documento cerrado.
8. No usar MCP en el MVP.
9. No crear interfaz gráfica antes de validar el flujo documental.
10. No mezclar Plan de Marketing con Plan de Empresa completo.

---

## 22. Documentación principal

La documentación base está en `docs/00_base_sistema/`.

Documentos principales:

```text
docs/00_base_sistema/00_planificacion_mvp_sistema_plan_marketing.md
docs/00_base_sistema/01_alcance_funcional_mvp.md
docs/00_base_sistema/02_flujo_plan_marketing.md
docs/00_base_sistema/03_agentes_y_responsabilidades.md
docs/00_base_sistema/04_skills_y_uso.md
docs/00_base_sistema/05_gates_y_validaciones.md
docs/00_base_sistema/06_sistema_cambios_versionado.md
docs/00_base_sistema/07_estructura_repositorio.md
docs/00_base_sistema/08_arquitectura_tecnica_inicial.md
docs/00_base_sistema/09_criterios_de_hecho.md
docs/00_base_sistema/10_decisiones_finales_pre_codigo.md
```

Antes de modificar la arquitectura, se debe revisar esta documentación.

---

---

## 23. Deuda técnica y mejoras identificadas

Durante la auditoría de la base funcional, se han identificado los siguientes puntos de mejora:

### 23.1 `marketing_profile_resolver.py`
- **Keyword "bar"**: Actualmente se usa como palabra clave para `b2c_local`, lo que puede generar falsos positivos en términos como "barrera" o "embarque" debido al matching por substring.
- **Lógica de matching**: Se recomienda migrar de búsqueda por substring (`if kw in text`) a una búsqueda por palabra exacta o expresiones regulares para mayor precisión.

### 23.2 `canales_service.py`
- **Tablas truncadas**: La tabla resumen de la Fase 06 trunca textos largos usando `...` (ej. `ch['objective'][:30]`). Se debe evaluar permitir el texto completo o mejorar el formato de la tabla para no perder información estratégica.

---

## 24. Arquitectura Lean 5S (Organización del Repositorio)

El repositorio sigue un estándar de organización **5S** para separar el código del sistema de los datos variables de trabajo:

### 24.1 Sistema Fijo (Núcleo)
*Versionado y empaquetado en el ZIP base.*
- `src/`: Lógica de negocio y servicios Python.
- `system/`: Reglas, gates y workflows multimodelo.
- `.claude/skills/`: Skills operativas agénticas.
- `agents/`: Definiciones de agentes.
- `project_template/`: Estructura base para nuevos planes.
- `docs/00_base_sistema/`, `01_estandares/`, `02_manual_operativo/`: Documentación viva.

### 24.2 Workspace Variable (Taller)
*Ignorado por Git y excluido del ZIP limpio.*
- `workspace/`: Inputs, borradores, sandbox y reportes de sesión.
- `workspace/reports/`: Auditorías pasadas e historial de validaciones.
- `workspace/exports/`: Versiones exportadas (ZIPs).
- `projects/`: Instancias activas de proyectos para pruebas locales.

---

## 25. Estado actual y Validación

El repositorio ha sido estabilizado bajo el estándar multimodelo:
- **Lógica Multimodelo**: 13 skills operativas, gates documentales como criterios de calidad y validaciones ejecutables mediante validators + data_integrity.py.
- **Limpieza 5S**: Estructura organizada y libre de basura técnica.
- **Punto de Entrada**: `uv run python -m src.main`.

---

## 26. Licencia

Licencia pendiente de definir. Antes de publicar o compartir el repositorio, se debe decidir el tipo de licencia.

---

## 27. Nota de trabajo

Este repositorio debe crecer despacio y con control.

La prioridad no es automatizar rápido, sino construir una base confiable.

Cada nueva función debe responder a una necesidad real del sistema y no a una automatización prematura.


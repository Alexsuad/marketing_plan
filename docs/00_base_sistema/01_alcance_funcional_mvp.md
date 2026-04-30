<!--
# File: docs/01_alcance_funcional_mvp.md
# ──────────────────────────────────────────────────────────────────────
# Propósito: Definir el alcance funcional del MVP.
# Rol: Documentación de requisitos.
# ──────────────────────────────────────────────────────────────────────
-->


# 01 - Alcance Funcional del MVP

## 1. Propósito del documento

Este documento define el alcance funcional del MVP del sistema agéntico para generar Planes de Marketing para empresas de servicios.

Su objetivo es dejar claro qué debe hacer la primera versión, qué queda fuera y cuáles serán los límites funcionales antes de iniciar el desarrollo.

Este documento complementa la planificación general definida en:

```text
00_planificacion_mvp_sistema_plan_marketing.md
```

La finalidad es evitar que el MVP crezca demasiado pronto o se mezcle con funciones futuras como automatización de redes sociales, integraciones externas o gestión avanzada de proyectos.

---

## 2. Definición del MVP

El MVP será una primera versión funcional del sistema capaz de:

- crear una instancia limpia para un nuevo proyecto de Plan de Marketing,
- recoger o cargar información inicial del negocio,
- generar documentos por fases,
- validar cada fase mediante gates,
- permitir cambios controlados,
- mantener versiones y changelog,
- producir una auditoría final,
- y generar un resumen compatible con el Plan de Empresa.

El MVP no busca ser una plataforma completa de marketing ni una herramienta de automatización de campañas.

Su objetivo principal es comprobar que el flujo documental y agéntico funciona de principio a fin.

---

## 3. Usuario objetivo del MVP

El MVP está pensado para un usuario que necesita construir un Plan de Marketing para una empresa de servicios.

Puede ser:

- una persona emprendedora,
- una pyme en fase de creación,
- una empresa de servicios que necesita ordenar su estrategia comercial,
- un equipo que está preparando documentación para un Plan de Empresa,
- o un profesional que necesita estructurar un plan antes de ejecutar acciones de marketing.

El usuario no necesita ser experto técnico.

El sistema debe ayudarlo a avanzar de forma guiada, evitando saltar directamente a acciones como publicar contenido o lanzar campañas sin tener antes una estrategia clara.

---

## 4. Principio funcional central

El sistema debe actuar como un asistente estructurado para construir el Plan de Marketing.

No debe actuar como:

- una agencia automática de publicación,
- un CRM,
- un gestor de campañas,
- un generador de posts,
- una herramienta de diseño gráfico,
- ni un sustituto completo del Plan de Empresa.

Regla funcional:

```text
El MVP debe ayudar a pensar, ordenar, generar, validar y actualizar el Plan de Marketing.
No debe ejecutar campañas ni automatizar canales en esta primera versión.
```

---

## 5. Funcionalidades incluidas en el MVP

### 5.1 Crear nuevo proyecto de Plan de Marketing

El sistema debe permitir crear una nueva instancia de proyecto desde una plantilla limpia.

Al crear el proyecto, debe generarse una estructura como:

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

El repositorio base no debe modificarse con datos del proyecto.

Esta funcionalidad es clave para evitar contaminación entre planes de marketing de distintos negocios.

---

### 5.2 Registrar datos iniciales del negocio

El sistema debe permitir capturar o cargar información básica del negocio.

Información mínima esperada:

- nombre del proyecto o negocio,
- tipo de empresa de servicios,
- servicio o servicios principales,
- cliente objetivo inicial,
- problema que resuelve,
- zona geográfica,
- etapa del negocio,
- recursos disponibles,
- presupuesto aproximado si existe,
- canales actuales si existen,
- restricciones importantes,
- y objetivo principal del Plan de Marketing.

Esta información se debe guardar en la carpeta:

```text
context/
```

Ejemplo de archivos iniciales:

```text
context/
├── empresa.md
├── servicios.md
├── cliente_objetivo.md
├── contexto_mercado.md
├── canales_actuales.md
└── restricciones.md
```

---

### 5.3 Validar el brief mínimo

Antes de generar el Plan de Marketing, el sistema debe validar si la información inicial es suficiente.

Debe ejecutar el gate:

```text
gate_brief_minimo
```

El sistema debe detectar si faltan datos críticos como:

- qué servicio se vende,
- a quién se vende,
- qué problema resuelve,
- qué objetivo busca el plan,
- o qué restricciones tiene el negocio.

Si falta información crítica, el sistema no debe inventarla.

Debe generar una salida como:

```text
outputs/plan_actual/01_brief_negocio_validado.md
```

Si el brief no está completo, debe marcarlo como:

```text
estado: incompleto
```

Y listar la información faltante.

---

### 5.4 Generar documentos por fases

El sistema debe generar el Plan de Marketing por fases, no como un único bloque gigante.

Documentos esperados:

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

Cada documento debe tener un propósito claro y no repetir innecesariamente información ya desarrollada en documentos anteriores.

Puede hacer referencia a documentos previos cuando sea necesario.

---

### 5.5 Ejecutar gates por fase

Cada fase debe pasar una validación mínima antes de considerarse cerrada.

Gates del MVP:

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

El resultado del gate debe guardarse o reflejarse en logs o auditorías.

El sistema debe poder indicar:

```text
aprobado
aprobado_con_observaciones
bloqueado
```

---

### 5.6 Generar matriz de canales

El sistema debe recomendar canales según el tipo de empresa, cliente y objetivo.

No debe asumir LinkedIn como canal obligatorio.

La matriz de canales debe evaluar, cuando aplique:

- LinkedIn,
- Instagram,
- Facebook,
- TikTok,
- YouTube,
- Google Business Profile,
- SEO,
- email,
- WhatsApp Business,
- eventos,
- networking,
- alianzas,
- referidos,
- directorios,
- publicidad pagada,
- y otros canales relevantes.

Cada canal debe incluir:

- prioridad,
- objetivo,
- cliente al que apunta,
- esfuerzo requerido,
- coste estimado,
- tipo de contenido o acción,
- limitaciones,
- riesgos,
- y justificación.

---

### 5.7 Generar plan de acción inicial

El sistema debe generar un plan de acción inicial de 90 días.

Este plan debe ser realista para una empresa de servicios y debe considerar:

- recursos disponibles,
- madurez del negocio,
- canales recomendados,
- presupuesto aproximado,
- capacidad operativa,
- y objetivos definidos.

No debe proponer acciones imposibles para el contexto del negocio.

El plan puede organizarse por semanas, meses o bloques de prioridad.

---

### 5.8 Generar KPIs y sistema de medición

El sistema debe proponer indicadores medibles.

Debe diferenciar entre:

- objetivos,
- KPIs,
- métricas de apoyo,
- frecuencia de revisión,
- y fuente de datos.

Ejemplos de KPIs posibles:

- leads cualificados generados,
- tasa de conversión de contacto,
- visitas a página de servicio,
- solicitudes de información,
- reuniones comerciales agendadas,
- coste por lead si aplica,
- tasa de respuesta a contacto comercial,
- crecimiento de visibilidad orgánica,
- o número de oportunidades comerciales detectadas.

El sistema debe evitar métricas de vanidad cuando no estén conectadas con un objetivo real.

---

### 5.9 Generar resumen compatible con Plan de Empresa

El MVP debe generar un documento que resuma el Plan de Marketing para integrarlo en un Plan de Empresa trabajado en paralelo.

Documento esperado:

```text
outputs/plan_actual/11_resumen_para_plan_empresa.md
```

Este documento debe resumir:

- mercado objetivo,
- propuesta de valor,
- posicionamiento,
- canales prioritarios,
- estrategia de captación,
- acciones clave,
- presupuesto aproximado,
- y KPIs principales.

No debe desarrollar áreas ajenas al marketing.

---

### 5.10 Generar auditoría final

El sistema debe generar una auditoría final antes de considerar listo el Plan de Marketing.

Documento esperado:

```text
outputs/plan_actual/12_auditoria_final.md
```

La auditoría debe revisar:

- coherencia entre documentos,
- alineación entre cliente objetivo y canales,
- consistencia entre propuesta de valor y acciones,
- realismo del plan de acción,
- claridad de KPIs,
- información faltante,
- supuestos no validados,
- y riesgos principales.

La auditoría puede bloquear el cierre si detecta fallos críticos.

---

### 5.11 Gestionar cambios del usuario

El MVP debe permitir solicitar cambios sobre el Plan de Marketing.

El sistema debe clasificar cada cambio como:

```text
impacto_bajo
impacto_medio
impacto_alto
```

Debe generar un análisis de impacto cuando el cambio afecte partes importantes del plan.

Debe identificar:

- qué cambia,
- qué documentos se ven afectados,
- qué se conserva,
- qué debe actualizarse,
- qué riesgos existen,
- y si requiere aprobación antes de aplicar.

---

### 5.12 Crear changelog y versiones

Cada cambio relevante debe quedar registrado.

Carpetas relacionadas:

```text
outputs/versions/
outputs/changelog/
outputs/audits/
```

El changelog debe indicar:

- fecha del cambio,
- cambio solicitado,
- motivo,
- impacto,
- documentos afectados,
- decisión tomada,
- y resultado de auditoría.

---

## 6. Funcionalidades excluidas del MVP

El MVP no incluirá:

- programación de publicaciones en redes sociales,
- publicación automática,
- creación automática de campañas pagadas,
- conexión con Notion,
- task bot,
- control remoto desde móvil,
- generación de imágenes por IA,
- integración con MCP,
- conexión con GA4,
- conexión con Google Ads,
- conexión con LinkedIn Ads,
- conexión con CRM,
- conexión con Mailchimp,
- scraping automático,
- dashboard interactivo avanzado,
- multiusuario,
- permisos por roles,
- facturación,
- ni exportación avanzada a PDF/DOCX en la primera versión.

La exportación a PDF o DOCX puede evaluarse después de validar que los documentos Markdown son correctos.

---

## 7. Flujo funcional principal

El flujo principal del MVP será:

```text
crear_nuevo_proyecto
↓
cargar_contexto_inicial
↓
validar_brief_minimo
↓
generar_documentos_por_fase
↓
ejecutar_gates
↓
generar_plan_actual
↓
generar_resumen_para_plan_empresa
↓
generar_auditoria_final
↓
marcar_version_inicial
```

---

## 8. Flujo funcional de cambios

El flujo de cambios será:

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

El sistema no debe modificar documentos sin dejar registro.

---

## 9. Reglas funcionales del MVP

1. El sistema debe trabajar siempre sobre una instancia de proyecto, no sobre el repositorio base.
2. El sistema no debe inventar datos críticos.
3. Si falta información, debe declararlo.
4. Cada fase debe producir un documento.
5. Cada documento debe pasar validación mínima.
6. La matriz de canales debe ser variable según el negocio.
7. LinkedIn no debe aparecer como canal obligatorio por defecto.
8. Los cambios deben clasificarse por impacto.
9. Los cambios relevantes deben crear changelog.
10. La auditoría final puede bloquear el cierre.
11. El resumen para Plan de Empresa debe limitarse a marketing.
12. El MVP no debe automatizar publicaciones ni campañas.
13. El sistema debe priorizar claridad, trazabilidad y control sobre automatización prematura.

---

## 10. Criterios de aceptación del MVP

El MVP se considerará válido si permite:

- crear un nuevo proyecto limpio,
- guardar contexto inicial,
- generar el brief validado,
- generar todos los documentos principales del Plan de Marketing,
- ejecutar validaciones básicas,
- generar matriz de canales justificada,
- generar plan de acción de 90 días,
- generar KPIs medibles,
- generar resumen para Plan de Empresa,
- generar auditoría final,
- registrar cambios,
- crear changelog,
- mantener versiones,
- y evitar contaminación del repositorio base.

---

## 11. Riesgos funcionales a controlar

### 11.1 Crecer demasiado pronto

Riesgo:

El MVP puede intentar incluir automatización, redes sociales, MCP, dashboards o integraciones antes de validar el flujo base.

Control:

Mantener esas funciones fuera del MVP.

---

### 11.2 Generar documentos genéricos

Riesgo:

El sistema puede producir un plan que suena correcto pero no responde al negocio real.

Control:

Brief mínimo, gates, auditoría y declaración de información faltante.

---

### 11.3 Contaminar proyectos

Riesgo:

Usar datos de un negocio anterior en un nuevo proyecto.

Control:

Repositorio base separado e instancias limpias por proyecto.

---

### 11.4 Confundir Plan de Marketing con Plan de Empresa

Riesgo:

El sistema puede intentar cubrir áreas financieras, jurídicas u operativas que no forman parte del alcance.

Control:

Generar solo resumen compatible con Plan de Empresa y declarar dependencias externas.

---

### 11.5 Tratar canales como receta fija

Riesgo:

Recomendar siempre LinkedIn o redes sociales sin analizar el negocio.

Control:

Matriz de canales con justificación por tipo de empresa, cliente y objetivo.

---

## 12. Próximo documento recomendado

El siguiente documento debería definir el flujo detallado del Plan de Marketing.

Documento sugerido:

```text
docs/02_flujo_plan_marketing.md
```

Ese documento debe detallar cada fase, sus entradas, salidas, agente responsable, skills utilizadas y gate correspondiente.



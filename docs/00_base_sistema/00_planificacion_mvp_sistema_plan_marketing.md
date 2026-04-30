<!--
# File: docs/00_planificacion_mvp_sistema_plan_marketing.md
# ──────────────────────────────────────────────────────────────────────
# Propósito: Documentar la planificación general del MVP del sistema de plan de marketing.
# Rol: Documentación de planificación.
# ──────────────────────────────────────────────────────────────────────
-->


# 00 - Planificación MVP del Sistema Agéntico para Plan de Marketing

## 1. Propósito del documento

Este documento define la planificación inicial del MVP del sistema agéntico para crear, revisar y actualizar Planes de Marketing para cualquier tipo de negocio (productos, servicios, ecommerce, retail, B2B, B2C, educativos o híbridos).

Su función es dejar una base clara antes de escribir código. El objetivo es evitar improvisaciones, mezcla de responsabilidades, agentes innecesarios o funcionalidades prematuras que compliquen el desarrollo.

Este documento debe servir como contrato inicial del proyecto. A partir de aquí se podrán crear documentos más específicos sobre agentes, skills, gates, workflows, estructura técnica y manual de uso.

---

## 2. Contexto general del proyecto

El proyecto consiste en construir una aplicación o sistema asistido por IA capaz de generar un Plan de Marketing estructurado para cualquier tipo de empresa.

El sistema no debe limitarse a redactar textos. Debe trabajar por fases, validar información, generar documentos separados, permitir cambios posteriores y mantener trazabilidad.

El Plan de Marketing se entiende como un documento vivo. Esto significa que puede cambiar cuando cambie el negocio, el cliente objetivo, los canales, el presupuesto, los objetivos o la estrategia.

El sistema debe poder utilizarse con distintos tipos de negocios, no solamente con un caso específico. Por eso se diseñará como un repositorio base reutilizable y cada nuevo proyecto se trabajará en una instancia separada.

---

## 3. Fuentes consideradas

La planificación se basa en cuatro fuentes principales:

1. Video sobre creación de un equipo completo de marketing con IA mediante agentes y skills.
2. Video sobre creación de un equipo de marketing con IA para lanzamiento de producto digital.
3. Repositorio de marketing skills con habilidades especializadas de marketing.
4. Documento maestro de lecciones aprendidas y manual anti-errores para sistemas con agentes, skills, reglas, gates y workflows.

También se consideran las decisiones tomadas durante el análisis del proyecto en este chat.

---

## 4. Interpretación de las fuentes

### 4.1 Fuente principal de arquitectura

La fuente más útil como referencia arquitectónica es la que plantea un equipo completo de marketing con IA. Su valor está en la lógica general:

- mapear funciones de marketing,
- convertir tareas repetibles en skills,
- agrupar skills en agentes especializados,
- definir reglas para saber cuándo usar agentes y cuándo usar skills,
- trabajar con contexto del negocio,
- producir entregables organizados,
- y mantener una estructura de trabajo similar a un equipo real.

Esta fuente no se copiará de forma literal. Se adaptará a diversos modelos de negocio y al objetivo específico del Plan de Marketing.

### 4.2 Fuente secundaria de patrón de construcción

La fuente sobre lanzamiento de producto digital no se usará como modelo de negocio, porque está centrada en producto digital, landing, emails y creatividades.

Sí se usará como patrón general para:

- separar carpetas de contexto, sistema y resultados,
- crear agentes especializados,
- diferenciar estrategia de ejecución,
- definir reglas de enrutado,
- y entender cómo un sistema puede coordinar varias piezas desde una estructura de archivos.

No se asumirá que nuestro sistema debe centrarse en campañas de lanzamiento, automatización de publicaciones o generación de creatividades visuales.

### 4.3 Repositorio de marketing skills

El repositorio de marketing skills sirve como caja de herramientas conceptual.

No se usarán todas las skills desde el inicio. Para el MVP se tomarán como referencia especialmente las relacionadas con:

- estrategia de contenidos,
- copywriting,
- edición de copy,
- análisis de competencia,
- auditoría SEO,
- tracking y medición,
- pruebas A/B,
- pricing,
- social content,
- y estrategia de lanzamiento cuando aplique.

Las skills del MVP deberán adaptarse a diversos modelos de negocio, no a servicios de forma exclusiva.

### 4.4 Documento maestro anti-errores

El documento maestro será la fuente de control del sistema.

Su papel es evitar errores como:

- perder requisitos al pasar de una fase a otra,
- mezclar investigación, estrategia, redacción y auditoría,
- crear agentes sin responsabilidad clara,
- usar MCP o integraciones externas antes de necesitarlas,
- cerrar documentos sin validación,
- permitir que el sistema invente información,
- contaminar un nuevo proyecto con datos de un proyecto anterior,
- o tratar el Plan de Marketing como documento final cerrado cuando en realidad es un documento vivo.

---

## 5. Alcance del MVP

El MVP debe permitir crear un Plan de Marketing estructurado para un negocio a partir de información inicial.

Debe incluir:

- carga o captura del contexto inicial,
- generación del brief validado,
- diagnóstico de marketing,
- definición del cliente objetivo,
- propuesta de valor y posicionamiento,
- análisis de competencia,
- matriz de canales,
- estrategia de comunicación,
- plan de acción inicial,
- presupuesto básico de marketing,
- KPIs y medición,
- resumen compatible con Plan de Empresa,
- auditoría final,
- gestión de cambios,
- versionado,
- changelog,
- y separación clara entre repositorio base y proyectos generados.

---

## 6. Fuera de alcance del MVP

Para mantener el desarrollo controlado, el MVP no incluirá inicialmente:

- publicación automática en redes sociales,
- conexión con Notion,
- task bot operativo,
- control remoto desde móvil,
- generación automática de imágenes,
- MCP para herramientas externas,
- automatización de emails,
- ejecución de campañas publicitarias,
- dashboard avanzado,
- CRM,
- scraping automático,
- integración con Google Analytics,
- integración con Google Ads,
- integración con LinkedIn Ads,
- ni generación completa del Plan de Empresa.

Estas funciones podrán evaluarse en fases posteriores si el sistema base funciona correctamente.

---

## 7. Relación con el Plan de Empresa

Este proyecto no construye el Plan de Empresa completo.

El objetivo es crear únicamente el Plan de Marketing.

Sin embargo, el sistema debe generar un documento resumen que pueda integrarse en el Plan de Empresa trabajado en paralelo.

Este resumen no debe invadir áreas como:

- plan financiero completo,
- plan jurídico,
- plan operativo,
- estructura societaria,
- modelo de negocio completo,
- o viabilidad económica global.

Cuando el sistema necesite información de esas áreas, deberá marcarla como dependencia externa.

Ejemplo:

```text
Dependencias externas detectadas:
- presupuesto total disponible,
- capacidad operativa,
- modelo de ingresos,
- zona geográfica prioritaria,
- recursos humanos disponibles.
```

---

## 8. Principio de repositorio reutilizable

El sistema se diseñará como un repositorio base reutilizable.

El repositorio base debe contener:

- documentación del sistema,
- reglas,
- agentes,
- skills,
- gates,
- workflows,
- plantillas,
- código de la aplicación,
- pruebas,
- y estructura base para crear nuevos proyectos.

El repositorio base no debe contener:

- datos reales de clientes,
- briefs completados,
- planes generados,
- auditorías de clientes,
- changelogs de clientes,
- archivos temporales,
- credenciales,
- ni información privada.

Cada nuevo Plan de Marketing debe crearse como una instancia separada de proyecto.

Regla madre:

```text
No se debe reutilizar una instancia anterior para un nuevo negocio.
Cada nuevo negocio debe partir de una plantilla limpia.
```

---

## 9. Estructura conceptual recomendada

La estructura general del repositorio base será:

```text
marketing_plan_agent_base/
├── README.md
├── AGENTS.md
├── docs/
├── system/
│   ├── rules/
│   ├── workflows/
│   ├── gates/
│   └── templates/
├── agents/
├── skills/
├── src/
├── tests/
└── project_template/
```

La estructura de cada proyecto generado será:

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

## 10. Fases del Plan de Marketing

El flujo inicial del Plan de Marketing será:

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

Cada fase debe producir un output verificable.

---

## 11. Outputs esperados

Los documentos iniciales del Plan de Marketing serán:

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

Estos documentos deben ser claros, completos y utilizables.

No deben incluir explicaciones internas del sistema, instrucciones para agentes ni lógica técnica que no pertenezca al entregable.

---

## 12. Canales y redes sociales

El sistema no debe asumir que LinkedIn es siempre el canal principal.

LinkedIn puede ser muy importante en servicios B2B, pero la selección de canales debe depender de:

- tipo de empresa o modelo de negocio,
- tipo de oferta (producto/servicio),
- cliente objetivo,
- ciclo de compra,
- zona geográfica,
- recursos disponibles,
- presupuesto,
- objetivo comercial,
- madurez digital,
- y capacidad operativa.

El sistema debe evaluar canales como:

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
- referidos,
- alianzas,
- directorios sectoriales,
- publicidad pagada,
- y otros canales relevantes según el negocio.

La salida correcta no será una lista fija, sino una matriz justificada de canales.

Cada canal recomendado debe incluir:

- objetivo del canal,
- cliente al que apunta,
- prioridad,
- esfuerzo requerido,
- coste estimado,
- tipo de contenido o acción sugerida,
- riesgos,
- limitaciones,
- y motivo de selección.

---

## 13. Agentes mínimos del MVP

El MVP trabajará con pocos agentes, bien definidos.

Agentes iniciales:

```text
orquestador_plan_marketing
investigador_marketing
estratega_marketing
redactor_marketing
analista_metricas
auditor_plan_marketing
```

### 13.1 Orquestador del Plan de Marketing

Coordina el flujo general.

No debe inventar contenido ni sustituir a los demás agentes.

Responsabilidades:

- decidir qué fase corresponde,
- verificar qué información existe,
- activar skills o agentes según el caso,
- identificar bloqueos,
- pedir validación cuando corresponda,
- y asegurar que cada output se genere en el lugar correcto.

### 13.2 Investigador de Marketing

Analiza mercado, competencia, cliente y contexto.

Responsabilidades:

- ordenar información disponible,
- detectar vacíos,
- identificar competidores,
- analizar señales del mercado,
- y generar insumos para la estrategia.

### 13.3 Estratega de Marketing

Convierte investigación en decisiones.

Responsabilidades:

- definir posicionamiento,
- ordenar segmentos,
- proponer canales,
- formular estrategia,
- priorizar acciones,
- y conectar marketing con objetivos del negocio.

### 13.4 Redactor de Marketing

Convierte la estrategia aprobada en textos claros.

Responsabilidades:

- redactar documentos finales,
- mejorar claridad,
- adaptar tono,
- evitar lenguaje genérico,
- y mantener coherencia entre secciones.

### 13.5 Analista de Métricas

Define cómo medir el plan.

Responsabilidades:

- proponer KPIs,
- diferenciar métricas de vanidad y métricas útiles,
- conectar objetivos con indicadores,
- y definir criterios básicos de seguimiento.

### 13.6 Auditor del Plan de Marketing

Revisa coherencia y calidad.

Responsabilidades:

- detectar contradicciones,
- revisar si se inventó información,
- verificar que las acciones sean realistas,
- validar coherencia entre cliente, propuesta, canales y KPIs,
- y bloquear el cierre si falta información crítica.

---

## 14. Skills mínimas del MVP

Las skills iniciales serán:

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

Cada skill deberá tener:

- propósito claro,
- entradas necesarias,
- salida esperada,
- criterios de insuficiencia,
- reglas de no invención,
- y relación con otros documentos.

Las skills deben ser pequeñas, trazables y reutilizables.

---

## 15. Gates obligatorios

Los gates son puntos de validación que permiten avanzar, bloquear o pedir corrección.

Gates iniciales:

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

Ninguna fase importante debe cerrarse sin pasar su gate correspondiente.

---

## 16. Documento vivo y sistema de cambios

El Plan de Marketing será un documento vivo.

El usuario podrá solicitar cambios de tres formas:

1. Indicando cambios por conversación.
2. Subiendo nuevos documentos o información.
3. Pidiendo modificar una sección concreta.

Todo cambio debe clasificarse por impacto:

```text
impacto_bajo
impacto_medio
impacto_alto
```

### 16.1 Impacto bajo

Afecta forma, claridad o estilo.

Ejemplos:

- mejorar redacción,
- cambiar tono,
- corregir nombres,
- reorganizar una sección.

### 16.2 Impacto medio

Afecta algunas partes del plan.

Ejemplos:

- agregar un canal,
- ajustar presupuesto,
- incluir un nuevo competidor,
- cambiar frecuencia de acciones.

### 16.3 Impacto alto

Puede invalidar secciones centrales.

Ejemplos:

- cambiar cliente objetivo,
- cambiar oferta principal (producto/servicio),
- cambiar propuesta de valor,
- cambiar zona geográfica,
- cambiar modelo comercial,
- cambiar nicho.

Para cambios medios o altos, el sistema debe generar análisis de impacto antes de modificar.

---

## 17. Flujo de actualización del plan

El flujo recomendado para cambios será:

```text
solicitud_de_cambio
↓
analisis_de_impacto
↓
aprobacion_usuario
↓
actualizacion_controlada
↓
auditoria_de_coherencia
↓
nueva_version
↓
changelog
```

El sistema no debe reescribir todo el plan si el cambio afecta solo una sección.

Debe actualizar solo lo necesario y declarar qué documentos fueron modificados.

---

## 18. Versionado y trazabilidad

Cada proyecto debe mantener:

```text
outputs/versions/
outputs/changelog/
outputs/audits/
```

Cada versión importante debe indicar:

- qué cambió,
- por qué cambió,
- qué documentos fueron afectados,
- qué se conservó,
- qué requiere revisión,
- y si pasó auditoría.

---

## 19. Arquitectura técnica inicial

La primera versión técnica debe ser simple.

Recomendación:

```text
Fase técnica 1: CLI/documental
Fase técnica 2: interfaz simple con Gradio o Streamlit
Fase técnica 3: FastAPI + frontend si el sistema demuestra valor
```

El MVP no debe empezar con una arquitectura web compleja.

Primero se debe probar que el flujo documental funciona de punta a punta.

---

## 20. Uso futuro de MCP e integraciones externas

MCP no será parte central del MVP.

Solo se considerará cuando exista una necesidad real de conexión con herramientas externas vivas.

Posibles integraciones futuras:

- GA4,
- Google Search Console,
- Google Ads,
- LinkedIn Ads,
- Mailchimp,
- Zapier,
- Notion,
- CRM,
- herramientas de generación visual.

Antes de agregar MCP, se debe justificar:

- qué problema resuelve,
- por qué no basta con archivos locales,
- por qué no basta con scripts o CLI,
- qué riesgo reduce,
- y qué valor aporta.

---

## 21. Criterios de hecho

Una fase se considera completa solo si:

- genera el output esperado,
- usa el contexto disponible,
- declara vacíos de información,
- no inventa datos críticos,
- pasa su gate,
- mantiene coherencia con documentos previos,
- y queda registrada si modifica el plan.

El Plan de Marketing se considera listo para revisión cuando:

- existen todos los documentos obligatorios,
- la auditoría final no detecta bloqueos críticos,
- los canales están justificados,
- las acciones son realistas,
- los KPIs son medibles,
- y el resumen para Plan de Empresa está actualizado.

---

## 22. Reglas madre del proyecto

1. El sistema genera exclusivamente Planes de Marketing.
2. El Plan de Empresa se trabaja en paralelo y no debe ser reemplazado por este sistema.
3. Cada nuevo negocio debe crearse desde una instancia limpia.
4. El repositorio base no debe guardar datos reales de clientes.
5. El sistema no debe asumir canales fijos.
6. LinkedIn no es obligatorio; debe evaluarse según el caso.
7. El Plan de Marketing es un documento vivo.
8. Todo cambio relevante debe clasificarse por impacto.
9. Los agentes deben tener responsabilidades separadas.
10. Las skills deben ser pequeñas, reutilizables y verificables.
11. Los gates deben validar antes de avanzar.
12. La auditoría puede bloquear el cierre.
13. No se debe usar MCP por moda.
14. No se debe publicar ni automatizar contenido en el MVP.
15. No se debe mezclar arquitectura interna con entregables finales.

---

## 23. Próximo paso recomendado

El siguiente documento debería definir con más detalle el alcance funcional del MVP.

Documento sugerido:

```text
docs/01_alcance_funcional_mvp.md
```

Ese documento debe transformar esta planificación general en una lista clara de funcionalidades incluidas, funcionalidades excluidas, usuarios esperados, flujo de uso y criterios mínimos de validación.



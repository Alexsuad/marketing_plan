<!--
# File: docs/00_base_sistema/03_agentes_y_responsabilidades.md
# ──────────────────────────────────────────────────────────────────────
# Propósito: Detallar los agentes del sistema y sus responsabilidades.
# Rol: Documentación de arquitectura de agentes.
# ──────────────────────────────────────────────────────────────────────
-->

# 03 - Agentes y Responsabilidades

## 1. Propósito del documento

Este documento define los agentes iniciales del MVP del sistema agéntico para generar Planes de Marketing para empresas de servicios.

Su objetivo es evitar que el sistema funcione como un único asistente genérico que investiga, decide, redacta y audita al mismo tiempo.

Cada agente debe tener una responsabilidad clara, límites definidos y relación explícita con las fases del flujo del Plan de Marketing.

Este documento complementa:

```text
00_planificacion_mvp_sistema_plan_marketing.md
01_alcance_funcional_mvp.md
02_flujo_plan_marketing.md
```

---

## 2. Principio de diseño de agentes

El sistema no debe crear agentes por decoración ni por exceso de complejidad.

Un agente existe cuando una función necesita:

- responsabilidad diferenciada,
- criterio propio,
- límites claros,
- capacidad de intervenir una fase,
- o capacidad de bloquear, revisar o coordinar.

Si una tarea es repetible, acotada y con entrada/salida clara, debe modelarse como skill, no como agente.

Regla base:

```text
Los agentes piensan y coordinan desde un rol.
Las skills ejecutan tareas concretas y reutilizables.
Los gates validan si una fase puede avanzar.
```

---

## 3. Agentes del MVP

El MVP tendrá seis agentes iniciales:

```text
orquestador_plan_marketing
investigador_marketing
estratega_marketing
redactor_marketing
analista_metricas
auditor_plan_marketing
```

No se crearán agentes adicionales en el MVP salvo que una responsabilidad crítica no pueda cubrirse con estos roles o con una skill.

---

## 4. Mapa general de responsabilidades

| Agente | Responsabilidad principal | No debe hacer |
|---|---|---|
| orquestador_plan_marketing | Coordinar el flujo, fases, estados y activaciones | Redactar el plan completo ni inventar estrategia |
| investigador_marketing | Ordenar información, analizar mercado, competencia y contexto | Decidir la estrategia final sin revisión |
| estratega_marketing | Convertir investigación en decisiones de marketing | Escribir todos los textos finales ni auditarse a sí mismo |
| redactor_marketing | Redactar documentos finales claros y coherentes | Cambiar estrategia aprobada sin indicar impacto |
| analista_metricas | Definir KPIs, medición y criterios de seguimiento | Crear acciones de marketing sin conexión con objetivos |
| auditor_plan_marketing | Revisar coherencia, riesgos y calidad del plan | Producir la estrategia principal que luego audita |

---

## 5. Agente: orquestador_plan_marketing

### 5.1 Rol

Coordina el sistema completo de generación del Plan de Marketing.

Es el responsable de mantener el orden del flujo, activar agentes o skills según corresponda y asegurar que cada fase tenga entrada, salida y validación.

### 5.2 Objetivo

Garantizar que el Plan de Marketing avance de forma ordenada, trazable y sin saltarse fases críticas.

### 5.3 Responsabilidades

- Crear o iniciar una instancia de proyecto.
- Verificar que existe contexto inicial.
- Activar el flujo del Plan de Marketing.
- Determinar qué fase corresponde.
- Invocar al agente adecuado.
- Invocar skills cuando la tarea sea concreta.
- Revisar el estado de los outputs.
- Detectar fases bloqueadas.
- Solicitar validaciones cuando corresponda.
- Coordinar el flujo de cambios.
- Asegurar que el repositorio base no se contamine con datos del proyecto.

### 5.4 Límites

No debe:

- inventar información faltante,
- redactar todo el Plan de Marketing por sí mismo,
- tomar decisiones estratégicas sin pasar por el estratega,
- auditar su propio resultado final,
- sobrescribir documentos sin registrar cambios,
- ni saltarse gates.

### 5.5 Entradas

- configuración del proyecto,
- archivos de contexto,
- estado de fases,
- outputs existentes,
- solicitudes del usuario,
- resultado de gates,
- changelog y versiones.

### 5.6 Salidas

- estado del flujo,
- activación de agentes o skills,
- indicación de siguiente fase,
- advertencias de bloqueo,
- solicitudes de información faltante,
- registro de cambio cuando aplique.

### 5.7 Fases donde participa

Participa en todas las fases como coordinador, especialmente en:

```text
01_intake_y_brief
flujo_de_cambios
auditoria_final
creacion_de_versiones
```

### 5.8 Skills que puede usar

```text
skill_intake_brief
skill_change_request
skill_auditoria_coherencia
```

### 5.9 Gates relacionados

```text
gate_brief_minimo
gate_impacto_cambio
gate_auditoria_final
```

### 5.10 Errores que debe evitar

- Avanzar sin brief mínimo.
- Tratar un cambio alto como si fuera menor.
- Mezclar outputs de distintos proyectos.
- Generar contenido final sin pasar por agentes especializados.
- Confundir Plan de Marketing con Plan de Empresa.

---

## 6. Agente: investigador_marketing

### 6.1 Rol

Analiza información del negocio, mercado, competencia, contexto y señales disponibles.

Su trabajo es preparar insumos confiables para que el estratega pueda tomar mejores decisiones.

### 6.2 Objetivo

Reducir la improvisación estratégica mediante análisis organizado y separación entre datos confirmados, hipótesis e información faltante.

### 6.3 Responsabilidades

- Leer y ordenar la información de contexto.
- Identificar información confirmada.
- Identificar hipótesis.
- Detectar vacíos de información.
- Analizar situación inicial de marketing.
- Analizar competidores y alternativas.
- Extraer patrones de documentos entregados por el usuario.
- Preparar hallazgos para la estrategia.
- Señalar cuándo hace falta investigación externa.

### 6.4 Límites

No debe:

- decidir por sí solo el posicionamiento final,
- redactar documentos finales sin revisión,
- proponer acciones sin pasar por estrategia,
- inventar datos de mercado,
- presentar hipótesis como hechos,
- ni cerrar fases estratégicas sin gate.

### 6.5 Entradas

- brief validado,
- documentos de contexto,
- información de mercado aportada,
- información de competencia,
- canales actuales,
- materiales del negocio,
- observaciones del usuario.

### 6.6 Salidas

- diagnóstico de marketing,
- análisis preliminar de mercado,
- lista de competidores y alternativas,
- vacíos de información,
- riesgos detectados,
- oportunidades iniciales,
- insumos para propuesta de valor y canales.

### 6.7 Fases donde participa

```text
02_diagnostico_marketing
03_cliente_objetivo_y_segmentos
05_analisis_competencia
```

Puede apoyar la fase 01 si el contexto inicial está disperso.

### 6.8 Skills que puede usar

```text
skill_diagnostico_marketing
skill_cliente_objetivo
skill_analisis_competencia
```

### 6.9 Gates relacionados

```text
gate_no_invencion
gate_coherencia_cliente_propuesta
```

### 6.10 Errores que debe evitar

- Usar lenguaje de certeza cuando solo hay hipótesis.
- Convertir investigación en redacción comercial prematura.
- Omitir competidores indirectos o alternativas sustitutivas.
- Hacer análisis demasiado genérico.
- No declarar información faltante.

---

## 7. Agente: estratega_marketing

### 7.1 Rol

Convierte investigación y contexto en decisiones estratégicas de marketing.

Es uno de los agentes centrales del sistema.

### 7.2 Objetivo

Definir una estrategia coherente que conecte cliente objetivo, propuesta de valor, posicionamiento, canales, acciones y recursos disponibles.

### 7.3 Responsabilidades

- Priorizar segmentos de cliente.
- Definir propuesta de valor.
- Definir posicionamiento.
- Traducir investigación en decisiones.
- Seleccionar canales adecuados.
- Justificar prioridades.
- Diseñar el plan de acción inicial.
- Conectar presupuesto con acciones.
- Asegurar realismo del plan.
- Coordinarse con el redactor y analista de métricas.

### 7.4 Límites

No debe:

- inventar evidencia,
- ignorar restricciones del negocio,
- recomendar canales por costumbre,
- asumir LinkedIn como canal obligatorio,
- producir textos finales sin pasar por redacción,
- auditar su propia estrategia como cierre final,
- ni invadir áreas del Plan de Empresa fuera de marketing.

### 7.5 Entradas

- brief validado,
- diagnóstico,
- cliente objetivo,
- análisis de competencia,
- recursos disponibles,
- restricciones,
- objetivos del negocio,
- información de presupuesto si existe.

### 7.6 Salidas

- cliente objetivo priorizado,
- propuesta de valor,
- posicionamiento,
- matriz de canales,
- estrategia de comunicación base,
- plan de acción,
- presupuesto de marketing estimado,
- recomendaciones estratégicas.

### 7.7 Fases donde participa

```text
03_cliente_objetivo_y_segmentos
04_propuesta_valor_y_posicionamiento
06_matriz_canales_marketing
07_estrategia_comunicacion
08_plan_accion_90_dias
09_presupuesto_marketing
```

### 7.8 Skills que puede usar

```text
skill_cliente_objetivo
skill_propuesta_valor
skill_matriz_canales
skill_estrategia_comunicacion
skill_plan_accion
skill_presupuesto_marketing
```

### 7.9 Gates relacionados

```text
gate_coherencia_cliente_propuesta
gate_canales_justificados
gate_plan_accion_realista
```

### 7.10 Errores que debe evitar

- Saltar de investigación a acciones sin digestión estratégica.
- Recomendar demasiados canales para pocos recursos.
- Crear un plan que suena bien pero no es ejecutable.
- Confundir visibilidad con captación real.
- Definir propuesta de valor genérica.
- No conectar acciones con objetivos.

---

## 8. Agente: redactor_marketing

### 8.1 Rol

Convierte decisiones estratégicas en documentos claros, coherentes y utilizables.

No decide la estrategia principal, pero ayuda a expresarla de forma comprensible.

### 8.2 Objetivo

Producir documentos finales bien redactados, sin lenguaje genérico, sin exceso de repetición y con tono adecuado al negocio.

### 8.3 Responsabilidades

- Redactar documentos finales del Plan de Marketing.
- Mejorar claridad y estructura.
- Adaptar el lenguaje al tipo de empresa.
- Mantener coherencia entre secciones.
- Evitar tecnicismos innecesarios.
- Preparar el resumen para Plan de Empresa.
- Revisar que los documentos sean comprensibles para usuarios no técnicos.

### 8.4 Límites

No debe:

- cambiar estrategia aprobada sin declarar impacto,
- inventar nuevos segmentos,
- crear nuevos canales no aprobados,
- alterar KPIs definidos por el analista,
- ocultar información faltante,
- convertir el plan en una pieza publicitaria,
- ni agregar contenido repetido solo para ampliar el documento.

### 8.5 Entradas

- documentos estratégicos,
- brief validado,
- propuesta de valor,
- matriz de canales,
- plan de acción,
- KPIs,
- tono deseado,
- observaciones del usuario.

### 8.6 Salidas

- documentos redactados en versión final,
- resumen para Plan de Empresa,
- mejoras de claridad,
- versiones limpias de documentos,
- mensajes base cuando aplique.

### 8.7 Fases donde participa

```text
07_estrategia_comunicacion
11_resumen_para_plan_empresa
```

También puede apoyar la redacción final de cualquier documento generado por otros agentes.

### 8.8 Skills que puede usar

```text
skill_estrategia_comunicacion
skill_resumen_plan_empresa
```

En fases futuras podría apoyarse en skills similares a:

```text
copywriting
copy_editing
content_strategy
```

### 8.9 Gates relacionados

```text
gate_resumen_plan_empresa
gate_auditoria_final
```

### 8.10 Errores que debe evitar

- Repetir información innecesariamente.
- Usar frases vacías como “soluciones integrales” sin explicación.
- Embellecer el plan hasta ocultar riesgos.
- Cambiar decisiones estratégicas sin avisar.
- Confundir comunicación estratégica con calendario de publicaciones.

---

## 9. Agente: analista_metricas

### 9.1 Rol

Define el sistema básico de medición del Plan de Marketing.

Ayuda a convertir objetivos y acciones en indicadores claros.

### 9.2 Objetivo

Asegurar que el plan pueda medirse y revisarse con criterios útiles.

### 9.3 Responsabilidades

- Definir KPIs principales.
- Diferenciar KPIs de métricas de apoyo.
- Evitar métricas de vanidad.
- Conectar indicadores con objetivos.
- Conectar indicadores con acciones.
- Definir frecuencia de revisión.
- Indicar fuente de datos.
- Señalar limitaciones de medición.
- Recomendar medición básica según recursos disponibles.

### 9.4 Límites

No debe:

- imponer herramientas externas en el MVP,
- asumir que existe GA4, CRM o dashboard,
- crear KPIs imposibles de medir,
- reducir el marketing a métricas sin contexto,
- definir acciones estratégicas que no le corresponden,
- ni inventar datos de rendimiento.

### 9.5 Entradas

- objetivos del plan,
- matriz de canales,
- plan de acción,
- presupuesto,
- recursos disponibles,
- herramientas actuales,
- nivel de madurez digital.

### 9.6 Salidas

- KPIs principales,
- métricas de apoyo,
- frecuencia de revisión,
- fuente de datos,
- criterio de éxito,
- señales de alerta,
- limitaciones de medición.

### 9.7 Fases donde participa

```text
09_presupuesto_marketing
10_kpis_y_medicion
```

### 9.8 Skills que puede usar

```text
skill_kpis
skill_presupuesto_marketing
```

En fases futuras podría apoyarse en:

```text
analytics_tracking
ab_test_setup
```

### 9.9 Gates relacionados

```text
gate_kpis_medibles
gate_plan_accion_realista
```

### 9.10 Errores que debe evitar

- Proponer métricas bonitas pero inútiles.
- Medir seguidores o likes sin conectar con objetivos.
- Proponer dashboards avanzados antes de tener datos.
- Asumir herramientas no disponibles.
- No definir frecuencia de revisión.

---

## 10. Agente: auditor_plan_marketing

### 10.1 Rol

Revisa el Plan de Marketing completo o una fase específica antes de avanzar o cerrar.

Debe poder bloquear una fase si detecta problemas críticos.

### 10.2 Objetivo

Garantizar que el Plan de Marketing sea coherente, realista, trazable y alineado con el contexto del negocio.

### 10.3 Responsabilidades

- Revisar coherencia entre documentos.
- Detectar contradicciones.
- Verificar que no se inventó información crítica.
- Revisar si los canales están justificados.
- Evaluar si el plan de acción es realista.
- Verificar si los KPIs son medibles.
- Detectar información faltante.
- Señalar supuestos no validados.
- Bloquear el cierre si hay fallos críticos.
- Generar auditoría final.
- Revisar cambios de impacto medio o alto.

### 10.4 Límites

No debe:

- producir la estrategia principal que luego audita,
- corregir todo sin indicar qué cambió,
- aprobar documentos con información crítica faltante,
- bloquear por preferencias menores,
- ni convertir la auditoría en una reescritura completa del plan.

### 10.5 Entradas

- todos los documentos del Plan de Marketing,
- outputs de gates,
- changelog,
- cambios solicitados,
- contexto inicial,
- restricciones del proyecto.

### 10.6 Salidas

- auditoría final,
- observaciones,
- bloqueos críticos,
- recomendaciones de corrección,
- lista de documentos afectados,
- estado de aprobación.

### 10.7 Fases donde participa

```text
12_auditoria_final
flujo_de_cambios
```

Puede intervenir en cualquier fase si un gate detecta problemas.

### 10.8 Skills que puede usar

```text
skill_auditoria_coherencia
skill_change_request
```

### 10.9 Gates relacionados

```text
gate_auditoria_final
gate_impacto_cambio
gate_no_invencion
```

### 10.10 Errores que debe evitar

- Aprobar planes demasiado genéricos.
- No distinguir entre error crítico y mejora opcional.
- Auditar sin comparar contra el brief.
- Corregir sin registrar cambios.
- Confundir auditoría de marketing con revisión del Plan de Empresa completo.

---

## 11. Relación entre agentes y fases

| Fase | Agente principal | Agente de apoyo | Gate |
|---|---|---|---|
| 01_intake_y_brief | orquestador_plan_marketing | investigador_marketing | gate_brief_minimo |
| 02_diagnostico_marketing | investigador_marketing | orquestador_plan_marketing | gate_no_invencion |
| 03_cliente_objetivo_y_segmentos | estratega_marketing | investigador_marketing | gate_coherencia_cliente_propuesta |
| 04_propuesta_valor_y_posicionamiento | estratega_marketing | redactor_marketing | gate_coherencia_cliente_propuesta |
| 05_analisis_competencia | investigador_marketing | estratega_marketing | gate_no_invencion |
| 06_matriz_canales_marketing | estratega_marketing | analista_metricas | gate_canales_justificados |
| 07_estrategia_comunicacion | redactor_marketing | estratega_marketing | gate_coherencia_cliente_propuesta |
| 08_plan_accion_90_dias | estratega_marketing | analista_metricas | gate_plan_accion_realista |
| 09_presupuesto_marketing | estratega_marketing | analista_metricas | gate_plan_accion_realista |
| 10_kpis_y_medicion | analista_metricas | estratega_marketing | gate_kpis_medibles |
| 11_resumen_para_plan_empresa | redactor_marketing | auditor_plan_marketing | gate_resumen_plan_empresa |
| 12_auditoria_final | auditor_plan_marketing | orquestador_plan_marketing | gate_auditoria_final |

---

## 12. Reglas de enrutado entre agentes y skills

### 12.1 Cuándo usar agente

Usar agente cuando la tarea requiera:

- análisis,
- criterio,
- priorización,
- decisión,
- coordinación,
- revisión,
- o bloqueo.

Ejemplos:

```text
Definir el cliente objetivo prioritario.
Elegir canales de marketing.
Auditar coherencia del plan.
Decidir si un cambio afecta varios documentos.
```

### 12.2 Cuándo usar skill

Usar skill cuando la tarea sea:

- concreta,
- repetible,
- acotada,
- con entrada clara,
- y con salida esperada.

Ejemplos:

```text
Generar matriz de canales.
Crear resumen para Plan de Empresa.
Clasificar impacto de cambio.
Validar KPIs.
```

### 12.3 Cuándo usar gate

Usar gate cuando haya que decidir si una fase puede avanzar o debe bloquearse.

Ejemplos:

```text
Validar brief mínimo.
Revisar si los canales están justificados.
Verificar si los KPIs son medibles.
Determinar impacto de un cambio.
```

---

## 13. Agentes fuera del MVP

No se crearán en la primera versión, pero podrían existir en fases posteriores:

```text
especialista_seo
especialista_rrss
especialista_paid_ads
especialista_marca
especialista_ux
especialista_crm
task_bot
integrador_mcp
```

Estos agentes solo se justificarán si el sistema base demuestra necesidad real.

---

## 14. Errores generales que el sistema debe evitar

1. Crear agentes innecesarios.
2. Hacer que un solo agente lo haga todo.
3. Usar skills como si fueran agentes.
4. Usar agentes para tareas que una skill puede resolver.
5. Permitir que el redactor cambie la estrategia sin avisar.
6. Permitir que el estratega audite su propio trabajo como cierre final.
7. Recomendar canales sin justificación.
8. Confundir marketing con Plan de Empresa completo.
9. Saltarse gates.
10. No declarar información faltante.
11. No registrar cambios.
12. Mezclar datos entre proyectos.

---

## 15. Criterios de aceptación de agentes

Un agente estará correctamente definido si tiene:

- rol claro,
- objetivo,
- responsabilidades,
- límites,
- entradas,
- salidas,
- fases donde participa,
- skills que puede usar,
- gates relacionados,
- errores que debe evitar,
- y relación clara con otros agentes.

Ningún agente debe quedar definido solo por su nombre.

---

## 16. Próximo documento recomendado

El siguiente documento debería definir las skills del sistema.

Documento sugerido:

```text
docs/00_base_sistema/04_skills_y_uso.md
```

Ese documento debe detallar para cada skill:

- propósito,
- cuándo usarla,
- entradas,
- proceso,
- salida,
- agente que puede activarla,
- gate relacionado,
- y criterios de insuficiencia.



<!--
# File: docs/04_skills_y_uso.md
# ──────────────────────────────────────────────────────────────────────
# Propósito: Describir las habilidades (skills) de los agentes y su uso.
# Rol: Documentación técnica.
# ──────────────────────────────────────────────────────────────────────
-->

# 04 - Skills y Uso

## 1. Propósito del documento

Este documento define las skills iniciales del MVP del sistema agéntico para generar Planes de Marketing para empresas de servicios.

Su objetivo es describir qué hace cada skill, cuándo debe usarse, qué entradas necesita, qué salida debe producir, qué agente puede activarla y qué límites debe respetar.

Este documento complementa:

```text
00_planificacion_mvp_sistema_plan_marketing.md
01_alcance_funcional_mvp.md
02_flujo_plan_marketing.md
03_agentes_y_responsabilidades.md
```

---

## 2. Principio de diseño de skills

Una skill es una capacidad concreta, reutilizable y verificable.

No debe funcionar como un agente completo ni tomar decisiones estratégicas amplias fuera de su alcance.

Regla base:

```text
Una skill debe hacer una tarea clara, con entradas definidas, salida esperada y criterios para detenerse si falta información.
```

Las skills deben ayudar a evitar que el sistema improvise cada vez desde cero.

---

## 3. Diferencia entre agente, skill y gate

| Pieza | Función | Ejemplo |
|---|---|---|
| Agente | Tiene rol, criterio y responsabilidad | estratega_marketing |
| Skill | Ejecuta una tarea concreta y repetible | skill_matriz_canales |
| Gate | Valida si se puede avanzar o bloquear | gate_canales_justificados |

Ejemplo práctico:

```text
El estratega_marketing decide que hay que crear una matriz de canales.
La skill_matriz_canales genera la matriz.
El gate_canales_justificados valida si la matriz sirve.
```

---

## 4. Skills iniciales del MVP

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

Estas skills cubren el flujo mínimo del Plan de Marketing sin incluir automatización de campañas, publicaciones, MCP ni integraciones externas.

---

## 5. Skill: skill_intake_brief

### 5.1 Propósito

Ordenar y validar la información inicial del negocio para construir el brief base del Plan de Marketing.

### 5.2 Cuándo usarla

Usar cuando:

- se crea un nuevo proyecto,
- se carga información inicial,
- el usuario entrega documentos del negocio,
- o se necesita comprobar si hay contexto suficiente para empezar.

### 5.3 Agente activador

```text
orquestador_plan_marketing
```

Puede recibir apoyo de:

```text
investigador_marketing
```

### 5.4 Entradas necesarias

- nombre del negocio o proyecto,
- tipo de empresa de servicios,
- servicios principales,
- cliente objetivo inicial,
- problema que resuelve,
- zona geográfica,
- etapa del negocio,
- recursos disponibles,
- canales actuales si existen,
- restricciones,
- objetivo del Plan de Marketing.

### 5.5 Proceso

La skill debe:

1. Leer la información disponible.
2. Ordenarla por bloques.
3. Separar hechos, hipótesis y datos faltantes.
4. Detectar contradicciones.
5. Identificar dependencias externas.
6. Preparar el brief validado.

### 5.6 Salida esperada

```text
outputs/plan_actual/01_brief_negocio_validado.md
```

Debe incluir:

- resumen del negocio,
- servicio principal,
- cliente objetivo inicial,
- problema que resuelve,
- objetivo del plan,
- restricciones,
- datos confirmados,
- hipótesis,
- información faltante,
- estado del brief.

### 5.7 Gate relacionado

```text
gate_brief_minimo
```

### 5.8 Criterios de insuficiencia

Debe detenerse o marcar bloqueo si falta:

- servicio principal,
- cliente objetivo,
- problema que resuelve,
- objetivo del plan,
- o datos mínimos del negocio.

No debe inventar esta información.

---

## 6. Skill: skill_diagnostico_marketing

### 6.1 Propósito

Analizar la situación inicial del negocio desde marketing.

### 6.2 Cuándo usarla

Usar después de tener un brief mínimo validado.

### 6.3 Agente activador

```text
investigador_marketing
```

### 6.4 Entradas necesarias

- brief validado,
- contexto del negocio,
- canales actuales,
- web o presencia digital si existe,
- materiales comerciales si existen,
- restricciones,
- recursos disponibles.

### 6.5 Proceso

La skill debe revisar:

- claridad de la oferta,
- madurez del negocio,
- presencia digital,
- canales actuales,
- coherencia de comunicación,
- fortalezas,
- debilidades,
- oportunidades,
- riesgos,
- información faltante.

### 6.6 Salida esperada

```text
outputs/plan_actual/02_diagnostico_marketing.md
```

Debe incluir:

- situación actual,
- fortalezas de marketing,
- debilidades de marketing,
- oportunidades detectadas,
- riesgos,
- hipótesis,
- información pendiente,
- primeras recomendaciones no vinculantes.

### 6.7 Gate relacionado

```text
gate_no_invencion
```

### 6.8 Criterios de insuficiencia

Debe marcar información faltante si no hay datos suficientes sobre:

- canales actuales,
- cliente actual,
- oferta,
- competencia,
- o estado digital.

Puede avanzar con observaciones, pero no debe presentar hipótesis como hechos.

---

## 7. Skill: skill_cliente_objetivo

### 7.1 Propósito

Definir y priorizar segmentos de cliente para el Plan de Marketing.

### 7.2 Cuándo usarla

Usar después del diagnóstico de marketing.

### 7.3 Agente activador

```text
estratega_marketing
```

Puede apoyarse en:

```text
investigador_marketing
```

### 7.4 Entradas necesarias

- brief validado,
- diagnóstico,
- servicios principales,
- zona geográfica,
- clientes actuales si existen,
- hipótesis de cliente,
- capacidad operativa.

### 7.5 Proceso

La skill debe:

1. Identificar posibles segmentos.
2. Diferenciar cliente ideal de público general.
3. Priorizar segmentos.
4. Describir dolores, necesidades y motivadores.
5. Identificar objeciones.
6. Separar información confirmada e hipótesis.

### 7.6 Salida esperada

```text
outputs/plan_actual/03_cliente_objetivo_y_segmentos.md
```

Debe incluir:

- segmentos posibles,
- segmento prioritario,
- perfil del cliente ideal,
- necesidades,
- dolores,
- criterios de decisión,
- objeciones,
- nivel de certeza,
- información pendiente.

### 7.7 Gate relacionado

```text
gate_coherencia_cliente_propuesta
```

### 7.8 Criterios de insuficiencia

Debe marcar bloqueo si no es posible definir al menos un segmento mínimo razonable.

Debe marcar hipótesis si el cliente objetivo no está validado.

---

## 8. Skill: skill_propuesta_valor

### 8.1 Propósito

Construir una propuesta de valor clara y un posicionamiento inicial para el negocio.

### 8.2 Cuándo usarla

Usar cuando ya exista una definición mínima del cliente objetivo.

### 8.3 Agente activador

```text
estratega_marketing
```

### 8.4 Entradas necesarias

- cliente objetivo,
- servicios principales,
- diagnóstico,
- fortalezas,
- diferenciales,
- objeciones,
- alternativas o competencia,
- restricciones.

### 8.5 Proceso

La skill debe definir:

- promesa principal,
- problema que resuelve,
- beneficios clave,
- diferenciales,
- razones para creer,
- mensajes base,
- objeciones y respuestas,
- posicionamiento recomendado.

Debe evitar frases genéricas o vacías.

### 8.6 Salida esperada

```text
outputs/plan_actual/04_propuesta_valor_y_posicionamiento.md
```

Debe incluir:

- propuesta de valor principal,
- propuesta de valor secundaria si aplica,
- argumentos de valor,
- diferenciadores,
- posicionamiento,
- mensajes clave,
- objeciones,
- límites de la promesa.

### 8.7 Gate relacionado

```text
gate_coherencia_cliente_propuesta
```

### 8.8 Criterios de insuficiencia

Debe detenerse o marcar observación si:

- no hay cliente objetivo claro,
- el servicio principal no está definido,
- los diferenciales son demasiado genéricos,
- o no hay razones para creer.

---

## 9. Skill: skill_analisis_competencia

### 9.1 Propósito

Analizar competidores, alternativas y sustitutos relevantes para el negocio.

### 9.2 Cuándo usarla

Usar después de tener cliente objetivo y propuesta de valor inicial.

### 9.3 Agente activador

```text
investigador_marketing
```

Con revisión de:

```text
estratega_marketing
```

### 9.4 Entradas necesarias

- brief,
- diagnóstico,
- cliente objetivo,
- propuesta de valor,
- competidores indicados por el usuario,
- alternativas conocidas,
- información pública aportada.

### 9.5 Proceso

La skill debe analizar:

- competidores directos,
- competidores indirectos,
- alternativas sustitutivas,
- mensajes visibles,
- canales visibles,
- fortalezas y debilidades,
- oportunidades de diferenciación,
- riesgos competitivos.

### 9.6 Salida esperada

```text
outputs/plan_actual/05_analisis_competencia.md
```

Debe incluir:

- lista de competidores,
- tipo de competidor,
- comparación básica,
- oportunidades,
- riesgos,
- hipótesis,
- información pendiente.

### 9.7 Gate relacionado

```text
gate_no_invencion
```

### 9.8 Criterios de insuficiencia

Debe marcar como incompleto si no hay datos suficientes.

No debe inventar competidores concretos si no hay base para ello.

Puede proponer categorías de competidores probables, indicando que requieren validación.

---

## 10. Skill: skill_matriz_canales

### 10.1 Propósito

Evaluar y priorizar canales de marketing según el tipo de empresa, cliente, servicio y recursos.

### 10.2 Cuándo usarla

Usar después de tener propuesta de valor y análisis de competencia.

### 10.3 Agente activador

```text
estratega_marketing
```

Puede recibir apoyo de:

```text
analista_metricas
```

### 10.4 Entradas necesarias

- cliente objetivo,
- propuesta de valor,
- análisis de competencia,
- recursos disponibles,
- presupuesto estimado,
- canales actuales,
- zona geográfica,
- ciclo de venta,
- objetivo comercial.

### 10.5 Proceso

La skill debe evaluar canales como:

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
- otros canales según el negocio.

Cada canal debe valorarse según:

- prioridad,
- objetivo,
- esfuerzo,
- coste,
- cliente al que apunta,
- tipo de acción,
- riesgo,
- limitación,
- justificación.

### 10.6 Salida esperada

```text
outputs/plan_actual/06_matriz_canales_marketing.md
```

Debe incluir:

- canales recomendados,
- canales secundarios,
- canales descartados o no prioritarios,
- justificación,
- riesgos,
- recursos necesarios.

### 10.7 Gate relacionado

```text
gate_canales_justificados
```

### 10.8 Criterios de insuficiencia

Debe marcar observación si falta información sobre:

- presupuesto,
- recursos,
- cliente objetivo,
- zona geográfica,
- o capacidad operativa.

No debe asumir LinkedIn, Instagram u otro canal como obligatorio.

---

## 11. Skill: skill_estrategia_comunicacion

### 11.1 Propósito

Definir la forma en que el negocio comunicará su propuesta de valor.

### 11.2 Cuándo usarla

Usar después de definir la matriz de canales.

### 11.3 Agente activador

```text
redactor_marketing
```

Con dirección de:

```text
estratega_marketing
```

### 11.4 Entradas necesarias

- propuesta de valor,
- posicionamiento,
- cliente objetivo,
- matriz de canales,
- tono deseado,
- restricciones de marca,
- objeciones principales.

### 11.5 Proceso

La skill debe definir:

- mensaje central,
- tono de comunicación,
- pilares de contenido,
- temas principales,
- mensajes por canal,
- objeciones que deben abordarse,
- reglas básicas de comunicación.

No debe generar un calendario de publicaciones en el MVP.

### 11.6 Salida esperada

```text
outputs/plan_actual/07_estrategia_comunicacion.md
```

Debe incluir:

- mensaje central,
- tono,
- pilares,
- temas,
- mensajes por canal,
- líneas rojas de comunicación,
- recomendaciones de estilo.

### 11.7 Gate relacionado

```text
gate_coherencia_cliente_propuesta
```

### 11.8 Criterios de insuficiencia

Debe marcar observación si:

- la propuesta de valor no está clara,
- el cliente objetivo está indefinido,
- o los canales no están justificados.

---

## 12. Skill: skill_plan_accion

### 12.1 Propósito

Convertir la estrategia en un plan de acción inicial de 90 días.

### 12.2 Cuándo usarla

Usar después de tener estrategia de comunicación y canales priorizados.

### 12.3 Agente activador

```text
estratega_marketing
```

Con apoyo de:

```text
analista_metricas
```

### 12.4 Entradas necesarias

- diagnóstico,
- cliente objetivo,
- propuesta de valor,
- matriz de canales,
- estrategia de comunicación,
- presupuesto aproximado,
- recursos disponibles,
- restricciones.

### 12.5 Proceso

La skill debe crear acciones organizadas por:

- prioridad,
- tiempo,
- canal,
- objetivo,
- dificultad,
- dependencia,
- responsable sugerido,
- resultado esperado,
- criterio de finalización.

### 12.6 Salida esperada

```text
outputs/plan_actual/08_plan_accion_90_dias.md
```

Debe incluir acciones para:

- primeros 30 días,
- días 31 a 60,
- días 61 a 90.

También puede agrupar por bloques:

- fundamentos,
- captación,
- comunicación,
- medición,
- mejora.

### 12.7 Gate relacionado

```text
gate_plan_accion_realista
```

### 12.8 Criterios de insuficiencia

Debe marcar riesgo si las acciones requieren recursos no disponibles.

Debe evitar planes demasiado ambiciosos para empresas pequeñas o en creación.

---

## 13. Skill: skill_presupuesto_marketing

### 13.1 Propósito

Crear una estimación básica del presupuesto de marketing necesario para ejecutar el plan.

### 13.2 Cuándo usarla

Usar después del plan de acción inicial.

### 13.3 Agente activador

```text
estratega_marketing
```

Con apoyo de:

```text
analista_metricas
```

### 13.4 Entradas necesarias

- plan de acción,
- canales priorizados,
- recursos internos,
- presupuesto declarado si existe,
- etapa del negocio,
- herramientas necesarias,
- acciones previstas.

### 13.5 Proceso

La skill debe clasificar costes en:

- sin coste directo,
- bajo coste,
- coste medio,
- inversión recomendada,
- inversión opcional,
- costes pendientes de validar.

Debe conectar cada coste con una acción o canal.

### 13.6 Salida esperada

```text
outputs/plan_actual/09_presupuesto_marketing.md
```

Debe incluir:

- presupuesto estimado,
- prioridades de inversión,
- acciones sin coste,
- acciones con coste,
- herramientas posibles,
- advertencias,
- supuestos.

### 13.7 Gate relacionado

```text
gate_plan_accion_realista
```

### 13.8 Criterios de insuficiencia

Si el usuario no proporciona presupuesto, la skill debe trabajar con rangos prudentes o declarar que falta el dato.

No debe presentar cifras como definitivas si son estimaciones.

---

## 14. Skill: skill_kpis

### 14.1 Propósito

Definir KPIs y sistema básico de medición del Plan de Marketing.

### 14.2 Cuándo usarla

Usar después de tener plan de acción y presupuesto.

### 14.3 Agente activador

```text
analista_metricas
```

### 14.4 Entradas necesarias

- objetivos del plan,
- canales priorizados,
- plan de acción,
- presupuesto,
- capacidades actuales de medición,
- herramientas disponibles.

### 14.5 Proceso

La skill debe definir:

- objetivos medibles,
- KPIs principales,
- métricas de apoyo,
- frecuencia de revisión,
- fuente de datos,
- responsable sugerido,
- señales de alerta.

Debe evitar métricas de vanidad.

### 14.6 Salida esperada

```text
outputs/plan_actual/10_kpis_y_medicion.md
```

Debe incluir:

- tabla de KPIs,
- definición de cada KPI,
- motivo,
- fuente de medición,
- frecuencia,
- relación con acciones,
- limitaciones.

### 14.7 Gate relacionado

```text
gate_kpis_medibles
```

### 14.8 Criterios de insuficiencia

Debe marcar observación si no existe forma razonable de medir un KPI.

Debe proponer una versión más simple si el negocio no tiene herramientas avanzadas.

---

## 15. Skill: skill_resumen_plan_empresa

### 15.1 Propósito

Crear un resumen del Plan de Marketing compatible con el Plan de Empresa.

### 15.2 Cuándo usarla

Usar cuando los documentos principales del Plan de Marketing estén generados.

### 15.3 Agente activador

```text
redactor_marketing
```

Con revisión de:

```text
auditor_plan_marketing
```

### 15.4 Entradas necesarias

- brief,
- diagnóstico,
- cliente objetivo,
- propuesta de valor,
- análisis de competencia,
- matriz de canales,
- estrategia de comunicación,
- plan de acción,
- presupuesto,
- KPIs.

### 15.5 Proceso

La skill debe sintetizar el contenido sin copiar todo el plan.

Debe extraer:

- mercado objetivo,
- segmentos,
- propuesta de valor,
- posicionamiento,
- canales,
- estrategia de captación,
- acciones clave,
- presupuesto aproximado,
- KPIs principales.

### 15.6 Salida esperada

```text
outputs/plan_actual/11_resumen_para_plan_empresa.md
```

### 15.7 Gate relacionado

```text
gate_resumen_plan_empresa
```

### 15.8 Criterios de insuficiencia

Debe marcar como pendiente si falta algún documento base necesario.

No debe desarrollar áreas ajenas al marketing.

---

## 16. Skill: skill_auditoria_coherencia

### 16.1 Propósito

Revisar coherencia, calidad y riesgos del Plan de Marketing.

### 16.2 Cuándo usarla

Usar al cierre del plan o cuando un gate detecte posibles inconsistencias.

### 16.3 Agente activador

```text
auditor_plan_marketing
```

Puede ser solicitada por:

```text
orquestador_plan_marketing
```

### 16.4 Entradas necesarias

- todos los documentos del plan,
- brief validado,
- outputs de gates,
- changelog si existe,
- contexto inicial,
- restricciones.

### 16.5 Proceso

La skill debe revisar:

- coherencia entre documentos,
- contradicciones,
- información faltante,
- supuestos no validados,
- exceso de generalidad,
- canales injustificados,
- acciones poco realistas,
- KPIs débiles,
- mezcla con Plan de Empresa,
- riesgos de ejecución.

### 16.6 Salida esperada

```text
outputs/plan_actual/12_auditoria_final.md
```

También puede producir auditorías parciales en:

```text
outputs/audits/
```

### 16.7 Gate relacionado

```text
gate_auditoria_final
```

### 16.8 Criterios de insuficiencia

Debe bloquear si:

- falta un documento central,
- hay contradicción crítica,
- el cliente objetivo no coincide con canales,
- la propuesta de valor es genérica,
- el plan de acción no es ejecutable,
- o los KPIs no son medibles.

---

## 17. Skill: skill_change_request

### 17.1 Propósito

Gestionar solicitudes de cambio sobre un Plan de Marketing vivo.

### 17.2 Cuándo usarla

Usar cuando el usuario pida modificar, actualizar, corregir o replantear una parte del plan.

### 17.3 Agente activador

```text
orquestador_plan_marketing
```

Con revisión de:

```text
auditor_plan_marketing
```

### 17.4 Entradas necesarias

- solicitud del usuario,
- plan actual,
- documentos afectados,
- changelog anterior,
- contexto vigente,
- versiones previas si existen.

### 17.5 Proceso

La skill debe:

1. Interpretar el cambio solicitado.
2. Clasificar impacto:

```text
impacto_bajo
impacto_medio
impacto_alto
```

3. Identificar documentos afectados.
4. Indicar qué se conserva.
5. Indicar qué debe actualizarse.
6. Detectar riesgos.
7. Pedir aprobación si corresponde.
8. Preparar registro de cambio.

### 17.6 Salida esperada

Documento de cambio en:

```text
outputs/changelog/
```

Y, si aplica, nueva versión en:

```text
outputs/versions/
```

Formato recomendado:

```text
change_request_vX.md
```

### 17.7 Gate relacionado

```text
gate_impacto_cambio
```

### 17.8 Criterios de insuficiencia

Debe pedir aclaración si el cambio solicitado es ambiguo.

Debe bloquear actualización directa si el cambio afecta:

- cliente objetivo,
- servicio principal,
- propuesta de valor,
- modelo comercial,
- zona geográfica,
- o canales estratégicos.

---

## 18. Reglas comunes para todas las skills

Todas las skills deben cumplir estas reglas:

1. No inventar información crítica.
2. Declarar información faltante.
3. Diferenciar hechos, hipótesis y recomendaciones.
4. Mantener el alcance del Plan de Marketing.
5. No invadir el Plan de Empresa completo.
6. No mezclar outputs finales con instrucciones internas.
7. No repetir información innecesaria.
8. Mantener lenguaje claro y útil.
9. Guardar la salida en la ruta esperada.
10. Respetar gates antes de avanzar.

---

## 19. Estructura futura de una skill en el repositorio

Cada skill podrá vivir en una carpeta propia:

```text
skills/skill_nombre/
├── SKILL.md
├── references/
├── templates/
└── examples/
```

El archivo obligatorio será:

```text
SKILL.md
```

Debe incluir:

- nombre,
- descripción,
- cuándo usarla,
- entradas,
- proceso,
- salida,
- límites,
- errores comunes,
- y relación con gates.

---

## 20. Relación entre skills y fases

| Fase | Skill principal | Output |
|---|---|---|
| 01_intake_y_brief | skill_intake_brief | 01_brief_negocio_validado.md |
| 02_diagnostico_marketing | skill_diagnostico_marketing | 02_diagnostico_marketing.md |
| 03_cliente_objetivo_y_segmentos | skill_cliente_objetivo | 03_cliente_objetivo_y_segmentos.md |
| 04_propuesta_valor_y_posicionamiento | skill_propuesta_valor | 04_propuesta_valor_y_posicionamiento.md |
| 05_analisis_competencia | skill_analisis_competencia | 05_analisis_competencia.md |
| 06_matriz_canales_marketing | skill_matriz_canales | 06_matriz_canales_marketing.md |
| 07_estrategia_comunicacion | skill_estrategia_comunicacion | 07_estrategia_comunicacion.md |
| 08_plan_accion_90_dias | skill_plan_accion | 08_plan_accion_90_dias.md |
| 09_presupuesto_marketing | skill_presupuesto_marketing | 09_presupuesto_marketing.md |
| 10_kpis_y_medicion | skill_kpis | 10_kpis_y_medicion.md |
| 11_resumen_para_plan_empresa | skill_resumen_plan_empresa | 11_resumen_para_plan_empresa.md |
| 12_auditoria_final | skill_auditoria_coherencia | 12_auditoria_final.md |
| cambios | skill_change_request | changelog / nueva versión |

---

## 21. Skills fuera del MVP

No se incluirán inicialmente, pero podrían añadirse después:

```text
skill_seo_audit
skill_linkedin_content
skill_email_sequence
skill_paid_ads
skill_google_business_profile
skill_landing_page
skill_creative_assets
skill_notion_task_board
skill_ga4_tracking
skill_crm_pipeline
```

Estas skills solo se crearán cuando el sistema base esté validado y exista una necesidad real.

---

## 22. Criterios de aceptación de skills

Una skill estará bien definida si:

- tiene un propósito claro,
- se sabe cuándo usarla,
- tiene entradas definidas,
- tiene salida esperada,
- declara cuándo no puede avanzar,
- está asociada a un agente,
- está asociada a un gate si corresponde,
- no invade otra skill,
- no invade un agente,
- y no rompe el flujo del Plan de Marketing.

---

## 23. Próximo documento recomendado

El siguiente documento debería definir los gates y validaciones del sistema.

Documento sugerido:

```text
docs/05_gates_y_validaciones.md
```

Ese documento debe detallar:

- propósito de cada gate,
- cuándo se ejecuta,
- qué valida,
- posibles estados,
- condiciones de bloqueo,
- y relación con fases, agentes y skills.



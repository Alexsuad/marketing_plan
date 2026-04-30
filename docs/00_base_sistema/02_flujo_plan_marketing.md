<!--
# File: docs/00_base_sistema/02_flujo_plan_marketing.md
# ──────────────────────────────────────────────────────────────────────
# Propósito: Describir el flujo de trabajo del plan de marketing.
# Rol: Documentación de procesos.
# ──────────────────────────────────────────────────────────────────────
-->


# 02 - Flujo del Plan de Marketing

## 1. Propósito del documento

Este documento define el flujo funcional del sistema para generar un Plan de Marketing para empresas de servicios.

Su objetivo es describir cada fase del proceso, indicando:

- qué información entra,
- qué debe hacer el sistema,
- qué documento debe producir,
- qué agente participa,
- qué skill se utiliza,
- qué gate valida la fase,
- y qué condiciones deben cumplirse para avanzar.

Este documento complementa:

```text
00_planificacion_mvp_sistema_plan_marketing.md
01_alcance_funcional_mvp.md
```

---

## 2. Principio general del flujo

El Plan de Marketing no se generará como un único documento largo desde el inicio.

Se construirá por fases para evitar pérdida de contexto, errores acumulados y documentos genéricos.

Cada fase debe producir un output verificable.

Regla base:

```text
No se avanza a la siguiente fase sin un documento generado y un gate de validación aplicado.
```

---

## 3. Flujo completo del Plan de Marketing

El flujo principal será:

```text
01_intake_y_brief
↓
02_diagnostico_marketing
↓
03_cliente_objetivo_y_segmentos
↓
04_propuesta_valor_y_posicionamiento
↓
05_analisis_competencia
↓
06_matriz_canales_marketing
↓
07_estrategia_comunicacion
↓
08_plan_accion_90_dias
↓
09_presupuesto_marketing
↓
10_kpis_y_medicion
↓
11_resumen_para_plan_empresa
↓
12_auditoria_final
```

Aunque el flujo es secuencial, algunas fases pueden requerir volver a fases anteriores si se detectan inconsistencias.

Ejemplo:

```text
Si la matriz de canales no encaja con el cliente objetivo,
el sistema debe volver a revisar cliente objetivo y propuesta de valor.
```

---

## 4. Fase 01 - Intake y brief

### 4.1 Objetivo

Recoger y validar la información mínima del negocio antes de construir cualquier parte del Plan de Marketing.

Esta fase evita que el sistema empiece a generar estrategia con información incompleta o ambigua.

### 4.2 Entradas

Información inicial del usuario o documentos cargados en:

```text
context/
```

Datos mínimos esperados:

- nombre del negocio o proyecto,
- tipo de empresa de servicios,
- servicios principales,
- cliente objetivo inicial,
- problema que resuelve,
- zona geográfica,
- etapa del negocio,
- recursos disponibles,
- canales actuales,
- restricciones,
- objetivo del Plan de Marketing.

### 4.3 Proceso

El sistema debe:

1. Leer la información disponible.
2. Ordenarla en formato de brief.
3. Detectar vacíos críticos.
4. Separar hechos, hipótesis y datos pendientes.
5. Marcar dependencias externas si existen.
6. Generar el documento de brief validado.

### 4.4 Agente responsable

```text
orquestador_plan_marketing
```

Puede apoyarse en:

```text
investigador_marketing
```

si el usuario entrega documentos largos o información dispersa.

### 4.5 Skill principal

```text
skill_intake_brief
```

### 4.6 Gate

```text
gate_brief_minimo
```

### 4.7 Output

```text
outputs/plan_actual/01_brief_negocio_validado.md
```

### 4.8 Condición para avanzar

El brief debe estar marcado como:

```text
estado: aprobado
```

o:

```text
estado: aprobado_con_observaciones
```

Si está incompleto, el sistema no debe avanzar sin advertirlo.

---

## 5. Fase 02 - Diagnóstico de marketing

### 5.1 Objetivo

Analizar la situación inicial del negocio desde la perspectiva de marketing.

No se trata de hacer todavía la estrategia, sino de entender el punto de partida.

### 5.2 Entradas

- brief validado,
- contexto del negocio,
- información de canales actuales,
- materiales existentes si los hay,
- web o presencia digital si existe,
- información comercial disponible.

### 5.3 Proceso

El sistema debe analizar:

- claridad de la oferta,
- madurez del negocio,
- presencia digital,
- coherencia de comunicación,
- canales actuales,
- recursos disponibles,
- barreras de captación,
- fortalezas de marketing,
- debilidades de marketing,
- oportunidades iniciales,
- y riesgos principales.

No debe realizar todavía un plan de acción detallado.

### 5.4 Agente responsable

```text
investigador_marketing
```

### 5.5 Skill principal

```text
skill_diagnostico_marketing
```

### 5.6 Gate

```text
gate_no_invencion
```

### 5.7 Output

```text
outputs/plan_actual/02_diagnostico_marketing.md
```

### 5.8 Condición para avanzar

El diagnóstico debe distinguir claramente:

- información confirmada,
- hipótesis,
- información faltante,
- y recomendaciones preliminares.

---

## 6. Fase 03 - Cliente objetivo y segmentos

### 6.1 Objetivo

Definir a quién debe dirigirse el Plan de Marketing.

Esta fase es crítica porque condiciona propuesta de valor, canales, comunicación, acciones y KPIs.

### 6.2 Entradas

- brief validado,
- diagnóstico de marketing,
- información de clientes actuales si existe,
- hipótesis de mercado,
- tipo de servicio,
- zona geográfica,
- capacidad operativa.

### 6.3 Proceso

El sistema debe:

1. Identificar segmentos posibles.
2. Diferenciar cliente ideal de público amplio.
3. Priorizar segmentos.
4. Describir necesidades, dolores y criterios de decisión.
5. Detectar objeciones de compra.
6. Señalar información no validada.

### 6.4 Agente responsable

```text
estratega_marketing
```

Puede apoyarse en:

```text
investigador_marketing
```

### 6.5 Skill principal

```text
skill_cliente_objetivo
```

### 6.6 Gate

```text
gate_coherencia_cliente_propuesta
```

En esta fase el gate valida parcialmente, porque la propuesta de valor se completa en la fase siguiente.

### 6.7 Output

```text
outputs/plan_actual/03_cliente_objetivo_y_segmentos.md
```

### 6.8 Condición para avanzar

Debe existir al menos un segmento prioritario justificado.

Si no se puede definir con claridad, el sistema debe declarar que falta investigación o información del negocio.

---

## 7. Fase 04 - Propuesta de valor y posicionamiento

### 7.1 Objetivo

Definir qué promete el negocio, por qué es relevante para el cliente objetivo y cómo debe posicionarse frente a alternativas.

### 7.2 Entradas

- brief validado,
- diagnóstico,
- cliente objetivo,
- servicios principales,
- fortalezas del negocio,
- restricciones,
- competencia o alternativas conocidas.

### 7.3 Proceso

El sistema debe construir:

- propuesta de valor principal,
- beneficios clave,
- diferenciadores,
- razones para creer,
- objeciones y respuesta a objeciones,
- posicionamiento recomendado,
- mensajes base,
- y advertencias sobre promesas no demostrables.

Debe evitar frases genéricas como:

```text
servicio de calidad
soluciones integrales
atención personalizada
innovación al servicio del cliente
```

salvo que estén explicadas con evidencia concreta.

### 7.4 Agente responsable

```text
estratega_marketing
```

### 7.5 Skill principal

```text
skill_propuesta_valor
```

### 7.6 Gate

```text
gate_coherencia_cliente_propuesta
```

### 7.7 Output

```text
outputs/plan_actual/04_propuesta_valor_y_posicionamiento.md
```

### 7.8 Condición para avanzar

La propuesta de valor debe estar conectada con un cliente objetivo concreto.

No se acepta una propuesta de valor genérica que podría aplicar a cualquier negocio.

---

## 8. Fase 05 - Análisis de competencia

### 8.1 Objetivo

Entender contra qué alternativas compite el negocio y qué oportunidades de diferenciación existen.

La competencia puede ser directa, indirecta o sustitutiva.

### 8.2 Entradas

- brief,
- diagnóstico,
- cliente objetivo,
- propuesta de valor,
- competidores indicados por el usuario,
- alternativas conocidas,
- información pública disponible si se aporta.

### 8.3 Proceso

El sistema debe analizar:

- competidores directos,
- competidores indirectos,
- alternativas que el cliente puede usar en lugar del servicio,
- mensajes de la competencia,
- canales visibles,
- fortalezas y debilidades comparativas,
- oportunidades de posicionamiento,
- y vacíos de mercado.

Debe indicar si el análisis se basa en información aportada o en hipótesis pendientes de validación.

### 8.4 Agente responsable

```text
investigador_marketing
```

Con revisión de:

```text
estratega_marketing
```

### 8.5 Skill principal

```text
skill_analisis_competencia
```

### 8.6 Gate

```text
gate_no_invencion
```

### 8.7 Output

```text
outputs/plan_actual/05_analisis_competencia.md
```

### 8.8 Condición para avanzar

El documento debe separar:

- competidores confirmados,
- alternativas probables,
- hipótesis,
- y puntos que requieren investigación externa.

---

## 9. Fase 06 - Matriz de canales de marketing

### 9.1 Objetivo

Definir qué canales son más adecuados para el negocio.

La selección de canales no debe ser fija. Debe responder al tipo de empresa, cliente, servicio, presupuesto y objetivos.

### 9.2 Entradas

- cliente objetivo,
- propuesta de valor,
- análisis de competencia,
- recursos disponibles,
- presupuesto estimado,
- canales actuales,
- zona geográfica,
- ciclo de venta.

### 9.3 Proceso

El sistema debe evaluar posibles canales como:

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

Cada canal debe evaluarse con:

- prioridad,
- objetivo,
- cliente al que apunta,
- esfuerzo requerido,
- coste estimado,
- tipo de contenido o acción,
- riesgo,
- limitación,
- y justificación.

### 9.4 Agente responsable

```text
estratega_marketing
```

### 9.5 Skill principal

```text
skill_matriz_canales
```

### 9.6 Gate

```text
gate_canales_justificados
```

### 9.7 Output

```text
outputs/plan_actual/06_matriz_canales_marketing.md
```

### 9.8 Condición para avanzar

Cada canal prioritario debe estar justificado.

El sistema no debe recomendar LinkedIn, Instagram u otro canal solo por costumbre.

---

## 10. Fase 07 - Estrategia de comunicación

### 10.1 Objetivo

Definir cómo debe comunicar el negocio su propuesta de valor en los canales priorizados.

Esta fase no crea todavía publicaciones específicas ni calendarios de contenido detallados.

### 10.2 Entradas

- propuesta de valor,
- posicionamiento,
- cliente objetivo,
- matriz de canales,
- tono deseado,
- restricciones de marca,
- nivel de formalidad adecuado.

### 10.3 Proceso

El sistema debe definir:

- mensaje central,
- tono de comunicación,
- pilares de contenido,
- temas principales,
- objeciones que deben abordarse,
- mensajes por tipo de canal,
- y reglas básicas de comunicación.

Debe evitar convertir esta fase en programación de publicaciones.

### 10.4 Agente responsable

```text
redactor_marketing
```

Con dirección de:

```text
estratega_marketing
```

### 10.5 Skill principal

```text
skill_estrategia_comunicacion
```

### 10.6 Gate

```text
gate_coherencia_cliente_propuesta
```

### 10.7 Output

```text
outputs/plan_actual/07_estrategia_comunicacion.md
```

### 10.8 Condición para avanzar

La estrategia de comunicación debe estar alineada con cliente objetivo, propuesta de valor y canales priorizados.

---

## 11. Fase 08 - Plan de acción de 90 días

### 11.1 Objetivo

Convertir la estrategia en acciones iniciales realistas.

El plan debe ser ejecutable por una empresa de servicios con recursos limitados.

### 11.2 Entradas

- diagnóstico,
- cliente objetivo,
- propuesta de valor,
- matriz de canales,
- estrategia de comunicación,
- presupuesto aproximado,
- recursos disponibles,
- restricciones.

### 11.3 Proceso

El sistema debe generar acciones organizadas por prioridad y tiempo.

Puede usar una estructura como:

```text
primeros_30_dias
segundos_30_dias
terceros_30_dias
```

O una estructura por bloques:

```text
fundamentos
captacion
contenido
medicion
mejora
```

Cada acción debe incluir:

- objetivo,
- canal relacionado,
- responsable sugerido,
- dificultad,
- prioridad,
- dependencia,
- resultado esperado,
- y criterio de finalización.

### 11.4 Agente responsable

```text
estratega_marketing
```

### 11.5 Skill principal

```text
skill_plan_accion
```

### 11.6 Gate

```text
gate_plan_accion_realista
```

### 11.7 Output

```text
outputs/plan_actual/08_plan_accion_90_dias.md
```

### 11.8 Condición para avanzar

El plan no debe depender de recursos que el negocio no tiene.

Si una acción requiere una dependencia externa, debe declararse.

---

## 12. Fase 09 - Presupuesto de marketing

### 12.1 Objetivo

Definir una estimación básica de recursos económicos para ejecutar el plan.

No sustituye el plan financiero completo del negocio.

### 12.2 Entradas

- plan de acción,
- canales priorizados,
- recursos internos,
- presupuesto declarado si existe,
- etapa del negocio,
- coste estimado de herramientas o acciones.

### 12.3 Proceso

El sistema debe estimar:

- acciones sin coste directo,
- acciones de bajo coste,
- acciones que requieren inversión,
- herramientas necesarias,
- posibles costes de publicidad,
- costes de diseño, contenido o soporte externo si aplica,
- y prioridades según presupuesto.

Si el usuario no entrega presupuesto, el sistema debe proponer rangos prudentes o declarar que falta ese dato.

### 12.4 Agente responsable

```text
estratega_marketing
```

Con apoyo de:

```text
analista_metricas
```

### 12.5 Skill principal

```text
skill_presupuesto_marketing
```

### 12.6 Gate

```text
gate_plan_accion_realista
```

### 12.7 Output

```text
outputs/plan_actual/09_presupuesto_marketing.md
```

### 12.8 Condición para avanzar

El presupuesto debe estar conectado con las acciones y canales recomendados.

No debe ser una tabla genérica sin relación con el plan.

---

## 13. Fase 10 - KPIs y medición

### 13.1 Objetivo

Definir cómo se medirá el avance del Plan de Marketing.

### 13.2 Entradas

- objetivos del plan,
- canales priorizados,
- plan de acción,
- presupuesto,
- capacidades actuales de medición,
- herramientas disponibles.

### 13.3 Proceso

El sistema debe definir:

- objetivos medibles,
- KPIs principales,
- métricas de apoyo,
- frecuencia de revisión,
- fuente de datos,
- responsable sugerido,
- y señales de alerta.

Debe evitar métricas de vanidad que no ayuden a tomar decisiones.

### 13.4 Agente responsable

```text
analista_metricas
```

### 13.5 Skill principal

```text
skill_kpis
```

### 13.6 Gate

```text
gate_kpis_medibles
```

### 13.7 Output

```text
outputs/plan_actual/10_kpis_y_medicion.md
```

### 13.8 Condición para avanzar

Cada KPI debe tener:

- definición,
- motivo,
- fuente de medición,
- frecuencia,
- y relación con una acción u objetivo.

---

## 14. Fase 11 - Resumen para Plan de Empresa

### 14.1 Objetivo

Generar un resumen útil para integrar el Plan de Marketing dentro del Plan de Empresa trabajado en paralelo.

Esta fase no crea el Plan de Empresa completo.

### 14.2 Entradas

Todos los documentos previos del Plan de Marketing.

### 14.3 Proceso

El sistema debe resumir:

- mercado objetivo,
- segmentos principales,
- propuesta de valor,
- posicionamiento,
- canales prioritarios,
- estrategia de captación,
- acciones principales,
- presupuesto aproximado,
- y KPIs principales.

Debe excluir áreas no relacionadas con marketing.

### 14.4 Agente responsable

```text
redactor_marketing
```

Con revisión de:

```text
auditor_plan_marketing
```

### 14.5 Skill principal

```text
skill_resumen_plan_empresa
```

### 14.6 Gate

```text
gate_resumen_plan_empresa
```

### 14.7 Output

```text
outputs/plan_actual/11_resumen_para_plan_empresa.md
```

### 14.8 Condición para avanzar

El resumen debe ser claro, compacto y compatible con un documento mayor, sin repetir todo el Plan de Marketing.

---

## 15. Fase 12 - Auditoría final

### 15.1 Objetivo

Revisar el Plan de Marketing completo antes de considerarlo listo para revisión del usuario.

### 15.2 Entradas

Todos los documentos generados.

### 15.3 Proceso

El sistema debe verificar:

- coherencia general,
- información faltante,
- contradicciones,
- supuestos no validados,
- canales injustificados,
- acciones poco realistas,
- KPIs débiles,
- exceso de generalidad,
- mezcla con Plan de Empresa,
- y riesgos de ejecución.

### 15.4 Agente responsable

```text
auditor_plan_marketing
```

### 15.5 Skill principal

```text
skill_auditoria_coherencia
```

### 15.6 Gate

```text
gate_auditoria_final
```

### 15.7 Output

```text
outputs/plan_actual/12_auditoria_final.md
```

### 15.8 Condición de cierre

La auditoría puede devolver tres estados:

```text
aprobado
aprobado_con_observaciones
bloqueado
```

Si el estado es bloqueado, el sistema debe indicar qué documentos deben corregirse antes de cerrar la versión.

---

## 16. Flujo de retorno entre fases

El flujo no debe ser rígido cuando se detecten errores.

Ejemplos:

```text
Si el cliente objetivo cambia,
se deben revisar propuesta de valor, canales, comunicación, plan de acción y KPIs.
```

```text
Si el presupuesto no alcanza para los canales propuestos,
se debe revisar matriz de canales y plan de acción.
```

```text
Si los KPIs no se pueden medir,
se debe revisar el plan de acción o las fuentes de datos.
```

---

## 17. Flujo de cambio sobre el Plan de Marketing

Cuando el usuario pida modificar el plan, el sistema no debe sobrescribir directamente.

Debe ejecutar:

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

La skill principal será:

```text
skill_change_request
```

El gate principal será:

```text
gate_impacto_cambio
```

---

## 18. Estados posibles de una fase

Cada fase puede tener uno de estos estados:

```text
pendiente
en_proceso
bloqueada
aprobada_con_observaciones
aprobada
actualizada
```

Estos estados ayudarán a controlar el avance del plan y futuras modificaciones.

---

## 19. Criterios de calidad del flujo

El flujo será correcto si:

- cada fase tiene una entrada clara,
- cada fase produce un documento,
- cada documento tiene un propósito diferenciado,
- no hay repetición innecesaria,
- los gates bloquean cuando falta información crítica,
- los agentes no invaden responsabilidades,
- los cambios quedan registrados,
- y el Plan de Marketing conserva coherencia de principio a fin.

---

## 20. Próximo documento recomendado

El siguiente documento debería definir los agentes y sus responsabilidades.

Documento sugerido:

```text
docs/00_base_sistema/03_agentes_y_responsabilidades.md
```

Ese documento debe detallar para cada agente:

- rol,
- objetivo,
- límites,
- entradas,
- salidas,
- relación con otros agentes,
- herramientas o skills que puede usar,
- y errores que debe evitar.


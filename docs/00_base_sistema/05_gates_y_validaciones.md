<!--
# File: docs/05_gates_y_validaciones.md
# ──────────────────────────────────────────────────────────────────────
# Propósito: Especificar los gates de paso y validaciones entre fases.
# Rol: Documentación de control de calidad.
# ──────────────────────────────────────────────────────────────────────
-->

# 05 - Gates y Validaciones

## 1. Propósito del documento

Este documento define los gates del MVP del sistema agéntico para generar Planes de Marketing para empresas de servicios.

Un gate es un punto de validación que permite decidir si una fase puede avanzar, debe corregirse o debe bloquearse.

Su función principal es proteger la calidad del Plan de Marketing y evitar que el sistema genere documentos aparentemente correctos pero mal fundamentados.

Este documento complementa:

```text
00_planificacion_mvp_sistema_plan_marketing.md
01_alcance_funcional_mvp.md
02_flujo_plan_marketing.md
03_agentes_y_responsabilidades.md
04_skills_y_uso.md
```

---

## 2. Principio general de gates

El sistema no debe avanzar solo porque un documento fue generado.

Debe avanzar cuando el documento cumple condiciones mínimas de calidad, coherencia y trazabilidad.

Regla base:

```text
Documento generado no significa fase aprobada.
Toda fase crítica debe pasar por un gate antes de avanzar.
```

---

## 3. Estados posibles de un gate

Cada gate puede devolver uno de estos estados:

```text
aprobado
aprobado_con_observaciones
bloqueado
```

### 3.1 aprobado

El documento o fase cumple los criterios mínimos y puede avanzar.

### 3.2 aprobado_con_observaciones

El documento puede avanzar, pero existen advertencias que deben quedar registradas.

Ejemplos:

- falta información secundaria,
- hay hipótesis pendientes de validar,
- el presupuesto es estimado,
- el análisis competitivo es limitado.

### 3.3 bloqueado

La fase no puede avanzar porque falta información crítica o existe una contradicción grave.

Ejemplos:

- no hay cliente objetivo definido,
- no hay servicio principal claro,
- la propuesta de valor no se conecta con el cliente,
- los canales no están justificados,
- el plan de acción no es ejecutable,
- los KPIs no se pueden medir.

---

## 4. Gates iniciales del MVP

Los gates iniciales serán:

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

Estos gates cubren el flujo principal y el flujo de cambios del Plan de Marketing.

---

## 5. Gate: gate_brief_minimo

### 5.1 Propósito

Validar que existe información mínima suficiente para empezar a construir el Plan de Marketing.

### 5.2 Cuándo se ejecuta

Se ejecuta al finalizar la fase:

```text
01_intake_y_brief
```

También puede ejecutarse cuando el usuario agrega nueva información de contexto.

### 5.3 Documento evaluado

```text
outputs/plan_actual/01_brief_negocio_validado.md
```

### 5.4 Agente responsable

```text
orquestador_plan_marketing
```

Puede recibir revisión de:

```text
auditor_plan_marketing
```

### 5.5 Qué valida

Valida que el brief incluya como mínimo:

- nombre o identificación del proyecto,
- tipo de empresa de servicios,
- servicio principal,
- cliente objetivo inicial,
- problema que resuelve,
- objetivo del Plan de Marketing,
- zona geográfica o mercado inicial,
- restricciones relevantes,
- y estado de la información.

### 5.6 Condiciones de aprobado

El gate aprueba si:

- el servicio principal está claro,
- existe al menos una hipótesis razonable de cliente objetivo,
- el problema que resuelve está expresado,
- el objetivo del Plan de Marketing está definido,
- y las carencias de información están declaradas.

### 5.7 Condiciones de aprobado con observaciones

Puede aprobar con observaciones si:

- el cliente objetivo es todavía una hipótesis,
- el presupuesto no está definido,
- la competencia no está identificada,
- los canales actuales son desconocidos,
- o faltan datos secundarios.

### 5.8 Condiciones de bloqueo

Debe bloquear si falta:

- servicio principal,
- cliente objetivo mínimo,
- problema que resuelve,
- objetivo del plan,
- o información básica del negocio.

### 5.9 Salida esperada

El gate debe devolver:

```text
estado:
observaciones:
bloqueos:
accion_recomendada:
```

---

## 6. Gate: gate_no_invencion

### 6.1 Propósito

Validar que el sistema no presenta hipótesis, suposiciones o datos no verificados como hechos.

### 6.2 Cuándo se ejecuta

Se ejecuta especialmente en:

```text
02_diagnostico_marketing
05_analisis_competencia
```

También puede usarse en cualquier fase que incluya información de mercado, competencia o rendimiento.

### 6.3 Documentos evaluados

```text
outputs/plan_actual/02_diagnostico_marketing.md
outputs/plan_actual/05_analisis_competencia.md
```

### 6.4 Agente responsable

```text
auditor_plan_marketing
```

Puede ser activado por:

```text
orquestador_plan_marketing
```

### 6.5 Qué valida

Valida que el documento diferencie:

- hechos confirmados,
- información aportada por el usuario,
- hipótesis,
- supuestos razonables,
- datos pendientes de validación,
- y recomendaciones.

### 6.6 Condiciones de aprobado

El gate aprueba si:

- las afirmaciones importantes tienen base,
- las hipótesis están marcadas como hipótesis,
- no se inventan competidores concretos,
- no se inventan cifras,
- y no se presentan conclusiones absolutas sin respaldo.

### 6.7 Condiciones de aprobado con observaciones

Puede aprobar con observaciones si:

- hay hipótesis claramente marcadas,
- el análisis es útil pero limitado,
- faltan datos externos,
- o el usuario deberá validar información posteriormente.

### 6.8 Condiciones de bloqueo

Debe bloquear si:

- se inventan datos de mercado,
- se inventan competidores específicos,
- se presentan cifras sin fuente,
- se afirma que un canal funciona sin evidencia o justificación,
- o se confunden hipótesis con hechos.

### 6.9 Salida esperada

```text
estado:
afirmaciones_riesgosas:
hipotesis_detectadas:
datos_sin_respaldo:
accion_recomendada:
```

---

## 7. Gate: gate_coherencia_cliente_propuesta

### 7.1 Propósito

Validar que cliente objetivo, propuesta de valor, posicionamiento y comunicación estén alineados.

### 7.2 Cuándo se ejecuta

Se ejecuta en:

```text
03_cliente_objetivo_y_segmentos
04_propuesta_valor_y_posicionamiento
07_estrategia_comunicacion
```

### 7.3 Documentos evaluados

```text
outputs/plan_actual/03_cliente_objetivo_y_segmentos.md
outputs/plan_actual/04_propuesta_valor_y_posicionamiento.md
outputs/plan_actual/07_estrategia_comunicacion.md
```

### 7.4 Agente responsable

```text
auditor_plan_marketing
```

### 7.5 Qué valida

Valida que:

- la propuesta de valor responda al cliente objetivo,
- el posicionamiento no sea genérico,
- los mensajes estén conectados con dolores reales,
- las objeciones tengan respuesta,
- el tono sea adecuado al tipo de cliente,
- y no se usen frases vacías sin explicación.

### 7.6 Condiciones de aprobado

Aprueba si:

- existe un cliente objetivo claro,
- la propuesta de valor responde a ese cliente,
- los beneficios están conectados con problemas reales,
- el posicionamiento diferencia al negocio,
- y la comunicación mantiene coherencia.

### 7.7 Condiciones de aprobado con observaciones

Puede aprobar con observaciones si:

- el cliente objetivo está definido pero requiere validación,
- los diferenciales son razonables pero necesitan evidencia,
- o hay mensajes que deben pulirse en fases posteriores.

### 7.8 Condiciones de bloqueo

Debe bloquear si:

- el cliente objetivo es demasiado amplio,
- la propuesta de valor podría aplicar a cualquier negocio,
- los mensajes no responden a dolores del cliente,
- el posicionamiento contradice el diagnóstico,
- o la comunicación se dirige a un público distinto al definido.

### 7.9 Salida esperada

```text
estado:
coherencias_detectadas:
incoherencias_detectadas:
riesgos:
accion_recomendada:
```

---

## 8. Gate: gate_canales_justificados

### 8.1 Propósito

Validar que los canales de marketing recomendados estén justificados según el negocio.

### 8.2 Cuándo se ejecuta

Se ejecuta al finalizar:

```text
06_matriz_canales_marketing
```

### 8.3 Documento evaluado

```text
outputs/plan_actual/06_matriz_canales_marketing.md
```

### 8.4 Agente responsable

```text
auditor_plan_marketing
```

Puede recibir apoyo de:

```text
analista_metricas
```

### 8.5 Qué valida

Valida que cada canal recomendado tenga:

- objetivo,
- cliente al que apunta,
- prioridad,
- esfuerzo requerido,
- coste estimado,
- acción sugerida,
- riesgo,
- limitación,
- y justificación.

También valida que no se asuma LinkedIn, Instagram u otro canal como obligatorio.

### 8.6 Condiciones de aprobado

Aprueba si:

- los canales prioritarios están justificados,
- los canales secundarios están diferenciados,
- los canales descartados tienen razón clara,
- la selección responde al cliente objetivo,
- y la recomendación es realista según recursos.

### 8.7 Condiciones de aprobado con observaciones

Puede aprobar con observaciones si:

- falta presupuesto exacto,
- algunos canales requieren validación,
- o hay dependencias externas para ejecutar ciertas acciones.

### 8.8 Condiciones de bloqueo

Debe bloquear si:

- se recomienda un canal sin justificación,
- se recomienda demasiados canales para pocos recursos,
- se asume un canal por moda,
- los canales no conectan con el cliente objetivo,
- o no se indican limitaciones.

### 8.9 Salida esperada

```text
estado:
canales_aprobados:
canales_observados:
canales_bloqueados:
riesgos:
accion_recomendada:
```

---

## 9. Gate: gate_plan_accion_realista

### 9.1 Propósito

Validar que el plan de acción y el presupuesto sean ejecutables para el negocio.

### 9.2 Cuándo se ejecuta

Se ejecuta en:

```text
08_plan_accion_90_dias
09_presupuesto_marketing
```

### 9.3 Documentos evaluados

```text
outputs/plan_actual/08_plan_accion_90_dias.md
outputs/plan_actual/09_presupuesto_marketing.md
```

### 9.4 Agente responsable

```text
auditor_plan_marketing
```

Con apoyo de:

```text
analista_metricas
```

### 9.5 Qué valida

Valida que:

- las acciones sean concretas,
- las acciones tengan prioridad,
- el esfuerzo sea razonable,
- las dependencias estén declaradas,
- el presupuesto esté conectado con acciones,
- no se propongan acciones imposibles,
- y el plan sea adecuado para una empresa de servicios.

### 9.6 Condiciones de aprobado

Aprueba si:

- el plan está organizado por tiempo o prioridad,
- cada acción tiene objetivo,
- las acciones conectan con canales y propuesta de valor,
- el presupuesto está vinculado a acciones,
- y el plan puede ejecutarse con los recursos declarados.

### 9.7 Condiciones de aprobado con observaciones

Puede aprobar con observaciones si:

- el presupuesto es estimado,
- hay dependencias externas,
- algunas acciones requieren validación,
- o el usuario debe confirmar capacidad operativa.

### 9.8 Condiciones de bloqueo

Debe bloquear si:

- el plan es demasiado ambicioso,
- no hay prioridades,
- las acciones no conectan con canales,
- el presupuesto no tiene relación con el plan,
- se exige una capacidad operativa inexistente,
- o no hay criterios de finalización.

### 9.9 Salida esperada

```text
estado:
acciones_aprobadas:
acciones_observadas:
acciones_bloqueadas:
dependencias:
accion_recomendada:
```

---

## 10. Gate: gate_kpis_medibles

### 10.1 Propósito

Validar que los KPIs propuestos sean medibles, útiles y conectados con los objetivos.

### 10.2 Cuándo se ejecuta

Se ejecuta al finalizar:

```text
10_kpis_y_medicion
```

### 10.3 Documento evaluado

```text
outputs/plan_actual/10_kpis_y_medicion.md
```

### 10.4 Agente responsable

```text
auditor_plan_marketing
```

Con apoyo de:

```text
analista_metricas
```

### 10.5 Qué valida

Valida que cada KPI tenga:

- definición,
- objetivo relacionado,
- fuente de datos,
- frecuencia de revisión,
- acción relacionada,
- criterio de interpretación,
- y limitaciones.

### 10.6 Condiciones de aprobado

Aprueba si:

- los KPIs son medibles,
- están conectados con objetivos,
- tienen fuente de datos,
- no son solo métricas de vanidad,
- y pueden revisarse con recursos disponibles.

### 10.7 Condiciones de aprobado con observaciones

Puede aprobar con observaciones si:

- algunas fuentes de datos deben configurarse después,
- la medición será manual al inicio,
- o hay KPIs aproximados por falta de herramientas.

### 10.8 Condiciones de bloqueo

Debe bloquear si:

- los KPIs no tienen fuente de datos,
- no se conectan con objetivos,
- son métricas de vanidad sin utilidad,
- no tienen frecuencia de revisión,
- o no se pueden interpretar.

### 10.9 Salida esperada

```text
estado:
kpis_aprobados:
kpis_observados:
kpis_bloqueados:
metricas_de_vanidad_detectadas:
accion_recomendada:
```

---

## 11. Gate: gate_resumen_plan_empresa

### 11.1 Propósito

Validar que el resumen para Plan de Empresa sea útil, claro y limitado al área de marketing.

### 11.2 Cuándo se ejecuta

Se ejecuta al finalizar:

```text
11_resumen_para_plan_empresa
```

### 11.3 Documento evaluado

```text
outputs/plan_actual/11_resumen_para_plan_empresa.md
```

### 11.4 Agente responsable

```text
auditor_plan_marketing
```

### 11.5 Qué valida

Valida que el resumen:

- sintetice el Plan de Marketing,
- no copie todos los documentos,
- sea compatible con un Plan de Empresa,
- no invada áreas financieras, legales u operativas completas,
- declare dependencias externas cuando corresponda,
- y conserve coherencia con el plan completo.

### 11.6 Condiciones de aprobado

Aprueba si:

- el resumen es claro,
- contiene los puntos centrales de marketing,
- puede integrarse en un documento mayor,
- y no sustituye el Plan de Empresa.

### 11.7 Condiciones de aprobado con observaciones

Puede aprobar con observaciones si:

- faltan datos externos del Plan de Empresa,
- algunas cifras son estimadas,
- o se requiere validación posterior.

### 11.8 Condiciones de bloqueo

Debe bloquear si:

- el resumen contradice el plan,
- invade áreas fuera del marketing,
- omite elementos centrales,
- o es tan largo que deja de ser resumen.

### 11.9 Salida esperada

```text
estado:
puntos_aprobados:
observaciones:
dependencias_externas:
accion_recomendada:
```

---

## 12. Gate: gate_auditoria_final

### 12.1 Propósito

Validar el Plan de Marketing completo antes de marcar una versión como lista para revisión.

### 12.2 Cuándo se ejecuta

Se ejecuta al finalizar:

```text
12_auditoria_final
```

También puede ejecutarse después de cambios de impacto alto.

### 12.3 Documentos evaluados

Todos los documentos en:

```text
outputs/plan_actual/
```

### 12.4 Agente responsable

```text
auditor_plan_marketing
```

### 12.5 Qué valida

Valida:

- existencia de documentos obligatorios,
- coherencia entre fases,
- alineación cliente-propuesta-canales,
- realismo de acciones,
- medición de KPIs,
- declaración de información faltante,
- separación entre marketing y Plan de Empresa,
- trazabilidad de cambios,
- y riesgos generales.

### 12.6 Condiciones de aprobado

Aprueba si:

- todos los documentos obligatorios existen,
- no hay contradicciones críticas,
- los canales están justificados,
- las acciones son realistas,
- los KPIs son medibles,
- y las observaciones no bloquean el uso del plan.

### 12.7 Condiciones de aprobado con observaciones

Puede aprobar con observaciones si:

- hay datos pendientes de validar,
- el presupuesto es estimado,
- el análisis de competencia es parcial,
- o existen mejoras recomendadas no críticas.

### 12.8 Condiciones de bloqueo

Debe bloquear si:

- falta un documento obligatorio,
- hay contradicción entre cliente y canales,
- la propuesta de valor es genérica,
- el plan de acción no es ejecutable,
- los KPIs no son medibles,
- o se mezcló el Plan de Marketing con el Plan de Empresa.

### 12.9 Salida esperada

```text
estado:
documentos_revisados:
bloqueos_criticos:
observaciones:
mejoras_recomendadas:
version_aprobable:
accion_recomendada:
```

---

## 13. Gate: gate_impacto_cambio

### 13.1 Propósito

Validar el impacto de una solicitud de cambio antes de modificar el Plan de Marketing.

### 13.2 Cuándo se ejecuta

Se ejecuta cuando el usuario solicita:

- modificar una sección,
- cambiar cliente objetivo,
- cambiar servicio principal,
- cambiar propuesta de valor,
- agregar o quitar canales,
- cambiar presupuesto,
- actualizar información del negocio,
- o regenerar parte del plan.

### 13.3 Documentos evaluados

Depende del cambio solicitado.

Puede evaluar:

```text
outputs/plan_actual/
outputs/changelog/
outputs/versions/
context/
```

### 13.4 Agente responsable

```text
orquestador_plan_marketing
```

Con revisión de:

```text
auditor_plan_marketing
```

### 13.5 Qué valida

Valida:

- tipo de cambio,
- nivel de impacto,
- documentos afectados,
- riesgos,
- necesidad de aprobación,
- si se debe actualizar una sección o varias,
- y si hace falta auditoría posterior.

### 13.6 Clasificación de impacto

```text
impacto_bajo
impacto_medio
impacto_alto
```

### 13.7 Impacto bajo

Ejemplos:

- mejorar redacción,
- corregir nombres,
- ajustar tono,
- ordenar una sección.

Puede aplicarse con registro simple.

### 13.8 Impacto medio

Ejemplos:

- agregar un canal,
- ajustar presupuesto,
- incluir nuevo competidor,
- cambiar prioridad de acciones.

Requiere análisis de documentos afectados.

### 13.9 Impacto alto

Ejemplos:

- cambiar cliente objetivo,
- cambiar servicio principal,
- cambiar propuesta de valor,
- cambiar zona geográfica,
- cambiar modelo comercial,
- cambiar nicho.

Requiere aprobación explícita antes de actualizar.

### 13.10 Condiciones de aprobado

Aprueba si:

- el cambio está claro,
- el impacto está clasificado,
- los documentos afectados están identificados,
- y existe acción recomendada.

### 13.11 Condiciones de aprobado con observaciones

Puede aprobar con observaciones si:

- el cambio es claro pero tiene dependencias,
- requiere información adicional no crítica,
- o afecta parcialmente documentos secundarios.

### 13.12 Condiciones de bloqueo

Debe bloquear si:

- la solicitud es ambigua,
- no se puede saber qué debe cambiar,
- el cambio contradice decisiones aprobadas sin explicación,
- o se intenta actualizar directamente una parte estratégica sin análisis de impacto.

### 13.13 Salida esperada

```text
estado:
tipo_de_cambio:
impacto:
documentos_afectados:
riesgos:
requiere_aprobacion:
accion_recomendada:
```

---

## 14. Relación entre gates y fases

| Fase | Gate principal |
|---|---|
| 01_intake_y_brief | gate_brief_minimo |
| 02_diagnostico_marketing | gate_no_invencion |
| 03_cliente_objetivo_y_segmentos | gate_coherencia_cliente_propuesta |
| 04_propuesta_valor_y_posicionamiento | gate_coherencia_cliente_propuesta |
| 05_analisis_competencia | gate_no_invencion |
| 06_matriz_canales_marketing | gate_canales_justificados |
| 07_estrategia_comunicacion | gate_coherencia_cliente_propuesta |
| 08_plan_accion_90_dias | gate_plan_accion_realista |
| 09_presupuesto_marketing | gate_plan_accion_realista |
| 10_kpis_y_medicion | gate_kpis_medibles |
| 11_resumen_para_plan_empresa | gate_resumen_plan_empresa |
| 12_auditoria_final | gate_auditoria_final |
| cambios | gate_impacto_cambio |

---

## 15. Formato recomendado de salida de gate

Todos los gates deberían producir una salida mínima con esta estructura:

```text
# Resultado del gate

## Gate ejecutado
[nombre_del_gate]

## Estado
[aprobado / aprobado_con_observaciones / bloqueado]

## Documento o fase evaluada
[ruta o nombre]

## Hallazgos principales
[lista]

## Bloqueos críticos
[lista]

## Observaciones
[lista]

## Acción recomendada
[avanzar / corregir / pedir datos / rehacer fase / auditar]
```

---

## 16. Reglas comunes para todos los gates

1. Un gate no debe reescribir el documento evaluado.
2. Un gate debe indicar claramente si aprueba, observa o bloquea.
3. Un gate debe explicar por qué bloquea.
4. Un gate no debe bloquear por preferencias menores.
5. Un gate debe diferenciar errores críticos de mejoras opcionales.
6. Un gate debe declarar información faltante.
7. Un gate debe proteger la coherencia del Plan de Marketing.
8. Un gate debe evitar que el sistema invente.
9. Un gate debe ayudar a decidir el siguiente paso.
10. Un gate debe dejar rastro cuando se ejecute sobre cambios importantes.

---

## 17. Gates fuera del MVP

Podrían añadirse en fases posteriores:

```text
gate_seo_minimo
gate_publicacion_rrss
gate_campana_pagada
gate_integracion_mcp
gate_privacidad_datos
gate_exportacion_pdf_docx
gate_dashboard_metricas
gate_automatizacion_notion
```

No se implementarán inicialmente porque pertenecen a funciones fuera del MVP.

---

## 18. Criterios de aceptación de gates

Un gate estará bien definido si tiene:

- propósito claro,
- momento de ejecución,
- documentos evaluados,
- agente responsable,
- criterios de aprobado,
- criterios de observación,
- criterios de bloqueo,
- salida esperada,
- y relación con una fase o flujo de cambio.

---

## 19. Próximo documento recomendado

El siguiente documento debería definir el sistema de cambios y versionado.

Documento sugerido:

```text
docs/06_sistema_cambios_versionado.md
```

Ese documento debe detallar cómo el sistema manejará un Plan de Marketing vivo:

- solicitudes de cambio,
- análisis de impacto,
- aprobación,
- actualización controlada,
- changelog,
- versiones,
- auditorías,
- y preservación del repositorio base limpio.



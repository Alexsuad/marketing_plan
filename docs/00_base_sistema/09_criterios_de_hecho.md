<!--
# File: docs/09_criterios_de_hecho.md
# ──────────────────────────────────────────────────────────────────────
# Propósito: Establecer los criterios de "hecho" (Definition of Done) para las tareas.
# Rol: Documentación de calidad.
# ──────────────────────────────────────────────────────────────────────
-->

# 09 - Criterios de Hecho

## 1. Propósito del documento

Este documento define cuándo se considera completa una parte del sistema agéntico para generar Planes de Marketing para empresas de servicios.

Su objetivo es evitar cierres falsos, avances prematuros o entregables incompletos.

En este proyecto, algo no está hecho solo porque exista un archivo o porque la IA haya generado texto.

Debe cumplir criterios mínimos de estructura, coherencia, trazabilidad y validación.

Este documento complementa:

```text
00_planificacion_mvp_sistema_plan_marketing.md
01_alcance_funcional_mvp.md
02_flujo_plan_marketing.md
03_agentes_y_responsabilidades.md
04_skills_y_uso.md
05_gates_y_validaciones.md
06_sistema_cambios_versionado.md
07_estructura_repositorio.md
08_arquitectura_tecnica_inicial.md
```

---

## 2. Principio general

Un elemento se considera hecho cuando:

- existe,
- está en la ruta correcta,
- cumple su propósito,
- tiene contenido suficiente,
- no invade responsabilidades de otro elemento,
- declara información faltante cuando exista,
- pasa la validación correspondiente,
- y queda trazado si modifica el plan.

Regla base:

```text
Existir no es estar terminado.
Generar no es validar.
Validar no es aprobar sin observaciones.
```

---

## 3. Criterio de hecho para una fase

Una fase del Plan de Marketing se considera hecha cuando:

1. Tiene entradas mínimas disponibles.
2. Se ejecutó la skill correspondiente.
3. Se generó el output esperado.
4. El documento está en la ruta correcta.
5. El contenido responde al objetivo de la fase.
6. Se declaró información faltante si aplica.
7. Se diferencian hechos, hipótesis y recomendaciones cuando corresponde.
8. Se ejecutó el gate asociado.
9. El gate devolvió `aprobado` o `aprobado_con_observaciones`.
10. El estado de la fase quedó registrado.

Una fase no está hecha si:

- falta el documento esperado,
- el documento está vacío o es genérico,
- no pasó gate,
- hay bloqueo crítico,
- o el contenido pertenece a otra fase.

---

## 4. Criterio de hecho para un output documental

Un documento generado se considera hecho cuando:

- tiene título claro,
- corresponde a la fase esperada,
- está guardado en `outputs/plan_actual/`,
- contiene las secciones mínimas requeridas,
- usa información del contexto del proyecto,
- no mezcla instrucciones internas del sistema,
- no invade el Plan de Empresa completo,
- no repite información innecesaria,
- declara supuestos o información pendiente,
- y puede ser leído por una persona sin conocer la arquitectura interna.

Ejemplo:

```text
outputs/plan_actual/06_matriz_canales_marketing.md
```

Está hecho si contiene canales evaluados, prioridad, justificación, riesgos, esfuerzo, coste estimado y relación con cliente objetivo.

No está hecho si solo dice:

```text
Usar LinkedIn, Instagram y email.
```

sin explicar por qué.

---

## 5. Criterio de hecho para el brief validado

El brief se considera hecho cuando contiene:

- nombre o identificación del negocio,
- tipo de empresa de servicios,
- servicio principal,
- cliente objetivo inicial,
- problema que resuelve,
- objetivo del Plan de Marketing,
- zona geográfica o mercado inicial,
- restricciones,
- datos confirmados,
- hipótesis,
- información faltante,
- y estado del brief.

Debe haber pasado:

```text
gate_brief_minimo
```

No está hecho si falta servicio principal, cliente objetivo mínimo, problema resuelto u objetivo del plan.

---

## 6. Criterio de hecho para el diagnóstico de marketing

El diagnóstico se considera hecho cuando analiza:

- situación actual,
- claridad de la oferta,
- presencia digital si existe,
- canales actuales si existen,
- fortalezas,
- debilidades,
- oportunidades,
- riesgos,
- información confirmada,
- hipótesis,
- y datos pendientes.

Debe haber pasado:

```text
gate_no_invencion
```

No está hecho si presenta suposiciones como hechos o si entrega recomendaciones sin distinguir el nivel de evidencia.

---

## 7. Criterio de hecho para cliente objetivo y segmentos

El documento de cliente objetivo se considera hecho cuando incluye:

- segmentos posibles,
- segmento prioritario,
- descripción del cliente ideal,
- necesidades,
- dolores,
- criterios de decisión,
- objeciones,
- nivel de certeza,
- e información pendiente.

Debe haber pasado:

```text
gate_coherencia_cliente_propuesta
```

No está hecho si el cliente objetivo es demasiado amplio o no se puede conectar después con propuesta de valor y canales.

---

## 8. Criterio de hecho para propuesta de valor y posicionamiento

Este documento se considera hecho cuando contiene:

- propuesta de valor principal,
- problema que resuelve,
- beneficios clave,
- diferenciales,
- razones para creer,
- posicionamiento,
- mensajes base,
- objeciones,
- respuesta a objeciones,
- y límites de la promesa.

Debe haber pasado:

```text
gate_coherencia_cliente_propuesta
```

No está hecho si usa frases genéricas como:

```text
servicio de calidad
soluciones integrales
atención personalizada
innovación
```

sin explicar qué significan en ese negocio concreto.

---

## 9. Criterio de hecho para análisis de competencia

El análisis de competencia se considera hecho cuando incluye:

- competidores directos si existen,
- competidores indirectos,
- alternativas sustitutivas,
- tipo de competidor,
- comparación básica,
- fortalezas y debilidades,
- oportunidades de diferenciación,
- riesgos,
- hipótesis,
- e información pendiente.

Debe haber pasado:

```text
gate_no_invencion
```

No está hecho si inventa competidores concretos, cifras o afirmaciones no respaldadas.

---

## 10. Criterio de hecho para matriz de canales

La matriz de canales se considera hecha cuando cada canal evaluado incluye:

- prioridad,
- objetivo,
- cliente al que apunta,
- esfuerzo requerido,
- coste estimado,
- tipo de acción sugerida,
- riesgo,
- limitación,
- y justificación.

Debe incluir canales recomendados, secundarios y descartados cuando aplique.

Debe haber pasado:

```text
gate_canales_justificados
```

No está hecha si asume un canal por defecto, por ejemplo LinkedIn, Instagram o TikTok, sin justificarlo según el negocio.

---

## 11. Criterio de hecho para estrategia de comunicación

La estrategia de comunicación se considera hecha cuando incluye:

- mensaje central,
- tono de comunicación,
- pilares de contenido,
- temas principales,
- mensajes por canal,
- objeciones que deben abordarse,
- reglas básicas de comunicación,
- y límites del lenguaje.

Debe haber pasado:

```text
gate_coherencia_cliente_propuesta
```

No está hecha si se convierte en un calendario de publicaciones o si propone piezas específicas sin haber cerrado estrategia.

---

## 12. Criterio de hecho para plan de acción de 90 días

El plan de acción se considera hecho cuando incluye acciones organizadas por tiempo o prioridad.

Cada acción debe tener:

- objetivo,
- canal relacionado,
- responsable sugerido,
- dificultad,
- prioridad,
- dependencia,
- resultado esperado,
- y criterio de finalización.

Debe haber pasado:

```text
gate_plan_accion_realista
```

No está hecho si propone demasiadas acciones, acciones imposibles o acciones desconectadas de la estrategia.

---

## 13. Criterio de hecho para presupuesto de marketing

El presupuesto se considera hecho cuando incluye:

- acciones sin coste directo,
- acciones de bajo coste,
- acciones con inversión recomendada,
- herramientas necesarias,
- costes estimados,
- supuestos,
- advertencias,
- y relación entre coste, canal y acción.

Debe haber pasado:

```text
gate_plan_accion_realista
```

No está hecho si presenta cifras como definitivas sin base o si no conecta presupuesto con el plan de acción.

---

## 14. Criterio de hecho para KPIs y medición

El documento de KPIs se considera hecho cuando cada KPI tiene:

- definición,
- objetivo relacionado,
- acción o canal relacionado,
- fuente de datos,
- frecuencia de revisión,
- criterio de interpretación,
- limitaciones,
- y responsable sugerido si aplica.

Debe haber pasado:

```text
gate_kpis_medibles
```

No está hecho si usa métricas de vanidad sin conexión con objetivos.

Ejemplo de métrica débil:

```text
Aumentar seguidores.
```

Ejemplo más útil:

```text
Número de contactos cualificados generados desde canal prioritario al mes.
```

---

## 15. Criterio de hecho para resumen de Plan de Empresa

El resumen para Plan de Empresa se considera hecho cuando:

- resume el Plan de Marketing,
- no copia todos los documentos,
- está limitado al área de marketing,
- incluye mercado objetivo,
- propuesta de valor,
- posicionamiento,
- canales prioritarios,
- estrategia de captación,
- acciones clave,
- presupuesto aproximado,
- y KPIs principales.

Debe haber pasado:

```text
gate_resumen_plan_empresa
```

No está hecho si intenta completar áreas financieras, jurídicas u operativas del Plan de Empresa.

---

## 16. Criterio de hecho para auditoría final

La auditoría final se considera hecha cuando revisa:

- existencia de documentos obligatorios,
- coherencia entre fases,
- alineación cliente-propuesta-canales,
- realismo de acciones,
- medición de KPIs,
- información faltante,
- supuestos no validados,
- riesgos,
- y separación entre Plan de Marketing y Plan de Empresa.

Debe haber pasado:

```text
gate_auditoria_final
```

Debe devolver uno de estos estados:

```text
aprobado
aprobado_con_observaciones
bloqueado
```

No está hecha si solo dice que el plan está bien sin explicar hallazgos, riesgos o bloqueos.

---

## 17. Criterio de hecho para una skill

Una skill se considera hecha cuando tiene:

- nombre claro,
- propósito,
- cuándo usarla,
- agente activador,
- entradas necesarias,
- proceso,
- salida esperada,
- gate relacionado si aplica,
- criterios de insuficiencia,
- límites,
- y errores que debe evitar.

No está hecha si solo contiene instrucciones genéricas o si invade responsabilidades de un agente.

---

## 18. Criterio de hecho para un agente

Un agente se considera hecho cuando tiene:

- rol,
- objetivo,
- responsabilidades,
- límites,
- entradas,
- salidas,
- fases donde participa,
- skills que puede usar,
- gates relacionados,
- errores que debe evitar,
- y relación con otros agentes.

No está hecho si su descripción permite que haga cualquier cosa.

---

## 19. Criterio de hecho para un gate

Un gate se considera hecho cuando tiene:

- propósito,
- momento de ejecución,
- documentos evaluados,
- agente responsable,
- qué valida,
- condiciones de aprobado,
- condiciones de aprobado con observaciones,
- condiciones de bloqueo,
- salida esperada,
- y relación con una fase o flujo de cambio.

No está hecho si solo dice “validar calidad” sin explicar qué significa calidad.

---

## 20. Criterio de hecho para una solicitud de cambio

Una solicitud de cambio se considera procesada cuando:

- se registró la solicitud,
- se interpretó el cambio,
- se clasificó el impacto,
- se identificaron documentos afectados,
- se detectaron riesgos,
- se pidió aprobación si correspondía,
- se aplicó o rechazó el cambio,
- se generó changelog,
- y se actualizó versión si era necesario.

Debe haber pasado:

```text
gate_impacto_cambio
```

No está procesada si el sistema modifica documentos sin registrar impacto.

---

## 21. Criterio de hecho para una versión

Una versión se considera hecha cuando:

- existe carpeta de versión,
- contiene los documentos vigentes,
- tiene changelog relacionado,
- tiene auditoría si aplica,
- está indicada en `project_config.json`,
- y no sobrescribe versiones anteriores.

Ejemplo:

```text
outputs/versions/v0_2/
outputs/changelog/changelog_v0_2.md
outputs/audits/auditoria_v0_2.md
```

No está hecha si solo se copian archivos sin indicar qué cambió.

---

## 22. Criterio de hecho para creación de nuevo proyecto

La creación de un nuevo proyecto se considera hecha cuando:

- se creó una carpeta propia en `projects/`,
- se copió desde `project_template/`,
- se creó `project_config.json`,
- existen carpetas `context/`, `outputs/` y `logs/`,
- `outputs/` está limpio,
- no se copió información de otro proyecto,
- y la ruta fue validada.

No está hecha si se reutiliza una instancia anterior.

---

## 23. Criterio de hecho para repositorio base limpio

El repositorio base se considera limpio cuando:

- no contiene datos reales de clientes,
- no contiene outputs de proyectos reales,
- no contiene logs sensibles,
- no contiene claves ni secretos,
- `projects/` está excluido de control de versiones cuando contiene datos reales,
- y las plantillas no están contaminadas con casos concretos.

No está limpio si un proyecto real quedó guardado dentro de `docs/`, `system/`, `agents/`, `skills/` o `project_template/`.

---

## 24. Criterio de hecho para MVP técnico

El MVP técnico se considera hecho cuando permite:

- crear proyecto desde plantilla limpia,
- validar estructura del repositorio base,
- validar estructura de una instancia,
- detectar outputs faltantes,
- crear versiones,
- registrar cambios,
- crear changelog,
- guardar auditorías,
- prevenir sobrescrituras,
- y mantener separación entre repositorio base y proyectos.

No está hecho si depende de procesos manuales que pueden contaminar proyectos.

---

## 25. Criterio de hecho para MVP funcional

El MVP funcional se considera hecho cuando permite generar el flujo completo:

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

Y además:

- los documentos están en la ruta correcta,
- cada fase tiene gate,
- la auditoría final se ejecuta,
- los cambios se registran,
- y el plan puede versionarse.

---

## 26. Criterio de hecho para pasar a interfaz gráfica

Solo se debe pasar a interfaz gráfica cuando:

- el flujo documental funciona,
- la estructura de carpetas es estable,
- la creación de proyectos está probada,
- el versionado funciona,
- los cambios se registran,
- los outputs son útiles,
- y no hay mezcla entre repositorio base y proyectos.

No se debe crear interfaz para ocultar un flujo que todavía no está validado.

---

## 27. Criterio de hecho para considerar MCP

Solo se debe considerar MCP cuando:

- existe una necesidad real de conexión con herramienta externa,
- el flujo documental base ya funciona,
- la integración aporta valor claro,
- no puede resolverse con archivos locales, CLI o scripts,
- y existe justificación documentada.

No se debe usar MCP por moda o anticipación.

---

## 28. Criterio de hecho para documentación del sistema

La documentación del sistema se considera hecha cuando:

- explica el contexto suficiente,
- no repite información innecesariamente,
- mantiene lenguaje claro,
- define reglas y decisiones,
- separa arquitectura de outputs,
- permite continuar el desarrollo sin depender de memoria oral,
- y está organizada en `docs/`.

No está hecha si es extensa pero confusa, o si es breve pero omite decisiones importantes.

---

## 29. Criterio de hecho para cierre de una iteración

Una iteración de trabajo se considera cerrada cuando:

- se generaron o actualizaron los documentos acordados,
- se revisó que no haya contradicciones evidentes,
- se registraron decisiones nuevas,
- se identificó el siguiente paso,
- y no quedaron acciones críticas sin mencionar.

---

## 30. Estados finales posibles

Cualquier elemento evaluado puede quedar en uno de estos estados:

```text
hecho
hecho_con_observaciones
bloqueado
pendiente
```

### 30.1 hecho

Cumple todos los criterios necesarios.

### 30.2 hecho_con_observaciones

Puede usarse, pero tiene advertencias registradas.

### 30.3 bloqueado

No puede avanzar hasta corregirse.

### 30.4 pendiente

Aún no se ha desarrollado o no tiene información suficiente.

---

## 31. Regla final de cierre

La regla final para este sistema es:

```text
Nada se considera terminado si no puede explicar qué es, dónde está, para qué sirve, qué validación pasó y qué queda pendiente.
```

---

## 32. Próximo paso recomendado

Con este documento se completa la primera base de planificación.

El siguiente paso recomendado no es crear más documentos generales, sino revisar los documentos existentes para detectar:

- contradicciones,
- repeticiones innecesarias,
- vacíos,
- decisiones pendientes,
- y orden correcto antes de iniciar desarrollo.

Después de esa revisión se podrá preparar el primer bloque de implementación técnica.


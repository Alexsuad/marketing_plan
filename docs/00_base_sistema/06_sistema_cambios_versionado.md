<!--
# File: docs/00_base_sistema/06_sistema_cambios_versionado.md
# ──────────────────────────────────────────────────────────────────────
# Propósito: Establecer las reglas para el sistema de cambios y versionado.
# Rol: Documentación de operaciones.
# ──────────────────────────────────────────────────────────────────────
-->

# 06 - Sistema de Cambios y Versionado

## 1. Propósito del documento

Este documento define cómo el sistema manejará cambios, actualizaciones y versiones del Plan de Marketing.

El Plan de Marketing se entiende como un documento vivo. Por eso, el sistema no debe tratarlo como un resultado final inmutable.

Su función es permitir ajustes sin perder trazabilidad, sin sobrescribir información crítica y sin contaminar versiones anteriores.

Este documento complementa:

```text
00_planificacion_mvp_sistema_plan_marketing.md
01_alcance_funcional_mvp.md
02_flujo_plan_marketing.md
03_agentes_y_responsabilidades.md
04_skills_y_uso.md
05_gates_y_validaciones.md
```

---

## 2. Principio general

Todo cambio relevante sobre el Plan de Marketing debe analizarse antes de aplicarse.

Regla base:

```text
El sistema no debe modificar directamente el Plan de Marketing sin clasificar el cambio, identificar impacto, registrar decisión y dejar trazabilidad.
```

Esto evita que una actualización aparentemente pequeña rompa cliente objetivo, propuesta de valor, canales, acciones o KPIs.

---

## 3. Qué se considera cambio

Se considera cambio cualquier solicitud del usuario que modifique, reordene, reemplace, amplíe, reduzca o invalide una parte del Plan de Marketing.

Ejemplos:

- cambiar cliente objetivo,
- cambiar servicio principal,
- agregar un nuevo canal,
- quitar una red social,
- ajustar presupuesto,
- cambiar tono de comunicación,
- modificar acciones de 90 días,
- cambiar KPIs,
- agregar información de competencia,
- corregir datos del negocio,
- actualizar resumen para Plan de Empresa,
- o regenerar una sección.

---

## 4. Tipos de cambio por impacto

Todo cambio debe clasificarse como:

```text
impacto_bajo
impacto_medio
impacto_alto
```

---

## 5. Impacto bajo

### 5.1 Definición

Un cambio de impacto bajo modifica forma, claridad, redacción u organización, pero no altera la estrategia.

### 5.2 Ejemplos

- corregir errores de escritura,
- mejorar tono,
- cambiar una frase confusa,
- ordenar una tabla,
- aclarar una sección,
- ajustar formato,
- renombrar un documento,
- corregir nombre del negocio sin afectar contenido.

### 5.3 Documentos normalmente afectados

Puede afectar un solo documento.

Ejemplos:

```text
07_estrategia_comunicacion.md
11_resumen_para_plan_empresa.md
```

### 5.4 Requiere aprobación previa

Normalmente no requiere aprobación previa si el usuario pidió expresamente ese ajuste.

Sí debe registrarse si modifica un documento aprobado.

### 5.5 Requiere auditoría posterior

No siempre.

Debe auditarse si afecta una sección sensible o si puede alterar interpretación.

---

## 6. Impacto medio

### 6.1 Definición

Un cambio de impacto medio afecta una parte importante del plan, pero no invalida toda la estrategia.

### 6.2 Ejemplos

- agregar un nuevo canal,
- quitar un canal secundario,
- ajustar presupuesto,
- incluir un nuevo competidor,
- cambiar prioridad de una acción,
- modificar frecuencia de revisión de KPIs,
- ajustar el plan de acción,
- cambiar el tono en un canal específico,
- actualizar información comercial parcial.

### 6.3 Documentos normalmente afectados

Puede afectar varios documentos, por ejemplo:

```text
05_analisis_competencia.md
06_matriz_canales_marketing.md
08_plan_accion_90_dias.md
09_presupuesto_marketing.md
10_kpis_y_medicion.md
```

### 6.4 Requiere aprobación previa

Puede requerir aprobación si afecta documentos ya aprobados o si modifica prioridades.

### 6.5 Requiere auditoría posterior

Sí, requiere auditoría parcial de coherencia.

---

## 7. Impacto alto

### 7.1 Definición

Un cambio de impacto alto puede invalidar secciones centrales del Plan de Marketing.

### 7.2 Ejemplos

- cambiar cliente objetivo principal,
- cambiar servicio principal,
- cambiar propuesta de valor,
- cambiar posicionamiento,
- cambiar zona geográfica principal,
- cambiar modelo comercial,
- cambiar nicho,
- cambiar objetivo principal del Plan de Marketing,
- cambiar de B2B a B2C o viceversa,
- redefinir completamente el negocio.

### 7.3 Documentos normalmente afectados

Puede afectar casi todo el plan:

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

### 7.4 Requiere aprobación previa

Sí. Siempre.

El sistema debe mostrar análisis de impacto antes de modificar.

### 7.5 Requiere auditoría posterior

Sí. Siempre.

Debe ejecutarse auditoría completa o semicompleta según el alcance del cambio.

---

## 8. Flujo general de cambio

El flujo obligatorio será:

```text
solicitud_de_cambio
↓
registro_inicial
↓
clasificacion_de_impacto
↓
identificacion_de_documentos_afectados
↓
analisis_de_riesgo
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

---

## 9. Solicitud de cambio

El usuario puede solicitar cambios de forma natural.

Ejemplos:

```text
Cambia el público objetivo.
```

```text
Agrega Instagram como canal secundario.
```

```text
Actualiza el presupuesto porque ahora tenemos 300 euros al mes.
```

```text
No quiero enfocarme en empresas grandes, sino en negocios pequeños locales.
```

El sistema debe interpretar la solicitud y convertirla en un registro estructurado.

---

## 10. Registro inicial del cambio

Antes de modificar, el sistema debe crear o preparar un registro de cambio.

Formato sugerido:

```text
outputs/changelog/change_request_vX.md
```

Contenido mínimo:

```text
# Solicitud de cambio

## Fecha
[fecha]

## Cambio solicitado
[texto del usuario]

## Interpretación del sistema
[qué entiende el sistema que debe cambiar]

## Tipo de impacto
[impacto_bajo / impacto_medio / impacto_alto]

## Documentos afectados
[lista]

## Riesgos
[lista]

## Requiere aprobación
[sí / no]

## Estado
[pendiente / aprobado / rechazado / aplicado]
```

---

## 11. Clasificación de impacto

La clasificación la realiza principalmente:

```text
skill_change_request
```

Activada por:

```text
orquestador_plan_marketing
```

Validada por:

```text
gate_impacto_cambio
```

Y revisada por:

```text
auditor_plan_marketing
```

---

## 12. Identificación de documentos afectados

El sistema debe indicar qué documentos podrían cambiar.

Ejemplo:

Cambio solicitado:

```text
Ahora queremos enfocarnos en pequeñas empresas locales en lugar de empresas medianas B2B.
```

Documentos afectados:

```text
01_brief_negocio_validado.md
03_cliente_objetivo_y_segmentos.md
04_propuesta_valor_y_posicionamiento.md
06_matriz_canales_marketing.md
07_estrategia_comunicacion.md
08_plan_accion_90_dias.md
10_kpis_y_medicion.md
11_resumen_para_plan_empresa.md
12_auditoria_final.md
```

El sistema debe explicar por qué se afectan.

---

## 13. Aprobación antes de aplicar

Los cambios de impacto alto requieren aprobación explícita.

Formato recomendado de solicitud:

```text
Este cambio tiene impacto alto porque afecta cliente objetivo, propuesta de valor, canales, acciones y KPIs.

Documentos afectados:
- ...

Riesgos:
- ...

Recomendación:
- regenerar parcialmente el plan desde la fase 03.

Confirma si deseas aplicar el cambio.
```

El sistema solo debe aplicar después de aprobación clara del usuario.

---

## 14. Actualización controlada

Cuando el cambio sea aprobado, el sistema debe actualizar solo los documentos afectados.

Regla:

```text
No se debe regenerar todo el Plan de Marketing si el cambio afecta solo una sección.
```

Pero si el impacto es alto, sí puede ser necesario regenerar varias fases.

El sistema debe indicar:

- documentos modificados,
- documentos conservados,
- documentos que requieren revisión,
- y documentos desactualizados.

---

## 15. Estados de documentos después de un cambio

Cada documento puede quedar en uno de estos estados:

```text
vigente
modificado
pendiente_revision
desactualizado
reemplazado
bloqueado
```

### 15.1 vigente

El documento sigue siendo válido.

### 15.2 modificado

El documento fue actualizado por el cambio.

### 15.3 pendiente_revision

El documento puede seguir siendo útil, pero requiere revisión.

### 15.4 desactualizado

El documento ya no debe usarse como base sin actualizar.

### 15.5 reemplazado

El documento fue sustituido por una nueva versión.

### 15.6 bloqueado

El documento no debe usarse hasta corregirse.

---

## 16. Versionado del Plan de Marketing

Cada versión importante debe guardarse en:

```text
outputs/versions/
```

Formato sugerido:

```text
v0_1/
v0_2/
v1_0/
```

### 16.1 Versión v0_1

Primera versión generada del plan.

Puede estar aprobada con observaciones.

### 16.2 Versión v0_2, v0_3, etc.

Versiones iterativas con ajustes.

### 16.3 Versión v1_0

Primera versión considerada estable para revisión externa o integración con el Plan de Empresa.

---

## 17. Cuándo crear una nueva versión

Crear nueva versión cuando:

- se actualiza una sección central,
- cambia cliente objetivo,
- cambia propuesta de valor,
- cambian canales prioritarios,
- cambia plan de acción,
- cambian KPIs,
- se completa auditoría final,
- o el usuario aprueba una revisión importante.

No hace falta crear nueva versión por cada corrección menor de estilo, salvo que el documento ya estuviera marcado como versión cerrada.

---

## 18. Changelog

El changelog registra cambios realizados.

Ubicación:

```text
outputs/changelog/
```

Formato sugerido:

```text
changelog_v0_2.md
```

Contenido mínimo:

```text
# Changelog v0_2

## Fecha
[fecha]

## Motivo del cambio
[descripción]

## Tipo de impacto
[impacto_bajo / impacto_medio / impacto_alto]

## Documentos modificados
[lista]

## Documentos conservados
[lista]

## Documentos pendientes de revisión
[lista]

## Riesgos detectados
[lista]

## Auditoría aplicada
[sí / no]

## Estado final
[aprobado / aprobado_con_observaciones / bloqueado]
```

---

## 19. Auditoría después del cambio

Después de un cambio de impacto medio o alto, debe ejecutarse auditoría.

Para impacto medio:

```text
auditoria_parcial
```

Para impacto alto:

```text
auditoria_completa_o_semicompleta
```

La auditoría debe revisar que el cambio no haya roto:

- cliente objetivo,
- propuesta de valor,
- canales,
- plan de acción,
- presupuesto,
- KPIs,
- resumen para Plan de Empresa.

---

## 20. Relación con el repositorio base

El sistema de cambios aplica solo dentro de una instancia de proyecto.

No debe modificar:

```text
marketing_plan_agent_base/
```

salvo que el cambio sea una mejora del sistema, no del Plan de Marketing de un negocio concreto.

Regla:

```text
Cambios del negocio van en projects/nombre_del_proyecto/.
Cambios del sistema van en el repositorio base y requieren decisión técnica separada.
```

---

## 21. Diferencia entre cambio de proyecto y cambio de sistema

### 21.1 Cambio de proyecto

Afecta un Plan de Marketing concreto.

Ejemplos:

- cambiar cliente objetivo de un negocio,
- ajustar canales,
- modificar presupuesto,
- actualizar plan de acción.

Se registra en:

```text
projects/nombre_del_proyecto/outputs/changelog/
```

### 21.2 Cambio de sistema

Afecta el funcionamiento del repositorio base.

Ejemplos:

- crear una nueva skill,
- modificar un gate,
- cambiar estructura de carpetas,
- actualizar reglas globales,
- mejorar una plantilla.

Se registra en documentación del repositorio base y, si aplica, en decisiones técnicas.

---

## 22. Solicitudes ambiguas

Si el usuario solicita un cambio ambiguo, el sistema no debe actuar directamente.

Ejemplo ambiguo:

```text
Hazlo más profesional.
```

El sistema debe responder con opciones:

```text
Puedo interpretarlo de varias formas:
1. mejorar tono de redacción,
2. hacer más técnico el posicionamiento,
3. ajustar diseño del documento,
4. reforzar argumentos comerciales.

Indica cuál quieres aplicar.
```

Si se puede hacer una mejora segura de bajo impacto, debe indicarse claramente.

---

## 23. Cambios que deben bloquearse automáticamente

El sistema debe bloquear cambios si:

- la solicitud es contradictoria,
- el cambio borra información crítica sin reemplazo,
- se intenta reutilizar contexto de otro proyecto,
- se pide modificar el repositorio base con datos de cliente,
- se intenta saltar auditoría después de impacto alto,
- o se intenta presentar hipótesis como hechos.

---

## 24. Ejemplo completo de flujo de cambio

Solicitud del usuario:

```text
Ahora quiero enfocar el plan en pequeñas empresas locales, no en empresas medianas.
```

Clasificación:

```text
impacto_alto
```

Documentos afectados:

```text
01_brief_negocio_validado.md
03_cliente_objetivo_y_segmentos.md
04_propuesta_valor_y_posicionamiento.md
06_matriz_canales_marketing.md
07_estrategia_comunicacion.md
08_plan_accion_90_dias.md
09_presupuesto_marketing.md
10_kpis_y_medicion.md
11_resumen_para_plan_empresa.md
12_auditoria_final.md
```

Acción recomendada:

```text
Regenerar desde la fase 03 y auditar coherencia antes de crear nueva versión.
```

Resultado esperado:

```text
outputs/changelog/change_request_v0_2.md
outputs/versions/v0_2/
outputs/audits/auditoria_v0_2.md
```

---

## 25. Criterios de aceptación del sistema de cambios

El sistema de cambios será correcto si:

- clasifica todo cambio por impacto,
- identifica documentos afectados,
- pide aprobación cuando corresponde,
- actualiza solo lo necesario,
- registra changelog,
- crea versión cuando aplica,
- ejecuta auditoría posterior,
- conserva versiones anteriores,
- y evita contaminar el repositorio base.

---

## 26. Próximo documento recomendado

El siguiente documento debería definir la estructura del repositorio.

Documento sugerido:

```text
docs/00_base_sistema/07_estructura_repositorio.md
```

Ese documento debe detallar:

- carpetas del repositorio base,
- carpetas de cada proyecto generado,
- qué contenido vive en cada carpeta,
- qué no debe guardarse,
- y reglas para mantener proyectos limpios y reutilizables.


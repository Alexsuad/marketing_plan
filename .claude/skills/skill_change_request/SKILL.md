---
name: skill_change_request
description: Gestionar solicitudes de cambio sobre un Plan de Marketing vivo.
---

# skill_change_request

## Estado
activa_documental

## Objetivo
Gestionar solicitudes de cambio sobre un Plan de Marketing vivo sin romper la coherencia de otros documentos.

## Cuándo usarla
Usar cuando el usuario pida modificar, actualizar, corregir o replantear una parte del plan.

## Agente activador
`orquestador_plan_marketing`

## Entradas necesarias
- Solicitud del usuario.
- Plan actual y documentos afectados.

## Proceso
1. Interpretar el cambio solicitado.
2. Clasificar impacto (bajo, medio, alto).
3. Identificar documentos afectados.
4. Indicar qué se conserva y qué debe actualizarse.
5. Detectar riesgos y pedir aprobación si corresponde.
6. Preparar el registro de cambio.

## Salida esperada
Documento de cambio en `outputs/changelog/` (ej. `change_request_vX.md`).

## Gates relacionados
`gate_impacto_cambio`

## Criterios de insuficiencia
Debe pedir aclaración si el cambio solicitado es ambiguo. Debe bloquear actualización directa si el cambio afecta pilares estratégicos (cliente, valor, modelo, canales base) sin autorización.

## Errores frecuentes
- Aplicar cambios en un documento sin actualizar los documentos derivados (ej. cambiar el cliente sin cambiar los canales).
- No registrar los cambios de alto impacto.

## Límites
Esta skill coordina la solicitud; si los cambios son aprobados, el orquestador llamará a los agentes respectivos para reescribir.

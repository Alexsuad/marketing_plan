---
name: skill_change_request
description: Gestionar de forma estructurada las solicitudes de cambio en el plan, analizando el impacto en cascada según el modelo de negocio.
---

# skill_change_request

## Estado
activa_documental

## Objetivo
Permitir que el plan evolucione sin perder la coherencia técnica, identificando qué partes deben regenerarse tras una modificación.

## Cuándo usarla
Usar cada vez que el usuario pida cambiar un dato fundamental (oferta, cliente, modelo, presupuesto) o un documento ya aprobado.

## Agente activador
`orquestador_plan_marketing`

## Entradas necesarias
- `tipo_negocio` o `marketing_profile`.
- Documento o dato que se desea cambiar.
- Motivo del cambio.

## Proceso
1. Clasificar el nivel de impacto del cambio:
   - **Bajo**: Ajustes de redacción, formato o ejemplos menores que no afectan la estrategia.
   - **Medio**: Ajuste de un canal, un KPI específico, un mensaje secundario o un micro-segmento de cliente.
   - **Alto**: Cambio de modelo de negocio, oferta principal, cliente objetivo, propuesta de valor o presupuesto base.
2. Identificar el impacto en cascada: ¿Qué otros documentos se ven afectados por este cambio?
3. Listar las fases que deben regenerarse y los Gates que deben volver a evaluarse.
4. Exigir aprobación explícita del usuario si el impacto es Alto antes de proceder con las modificaciones masivas.

## Adaptación por modelo de negocio
- **ecommerce_transaccional**: Un cambio en la oferta principal afecta inmediatamente a la logística, el ticket medio y los KPIs de Ads.
- **b2b_consultivo**: Un cambio en el cliente objetivo requiere rehacer toda la estrategia de autoridad y los pilares de comunicación.
- **b2b_producto_industrial**: Un cambio en las especificaciones u oferta afecta a la red de distribución y a los procesos de homologación.
- **retail_fisico**: Un cambio en la ubicación o radio de influencia invalida el diagnóstico de visibilidad local previo.
- **educativo_formativo**: Un cambio en la metodología o programa requiere actualizar toda la prueba social y mensajes de inscripción.
- **hibrido_producto_servicio**: Un cambio en el activo físico altera la viabilidad del soporte o mantenimiento recurrente asociado.
- **b2c_local_servicios**: Un cambio en el tipo de reserva o servicio local afecta a la reputación y a la rapidez de respuesta necesaria.

## Cuándo declarar insuficiencia
Debe declarar insuficiencia si:
- No se especifica el motivo del cambio o el documento afectado.
- El cambio solicitado es contradictorio con el modelo de negocio base y no se justifica una transición de modelo.
- No se puede determinar el impacto en cascada por falta de información previa.

## Criterios de bloqueo
- Intentar realizar un cambio de impacto Alto sin una justificación clara de por qué se invalida el trabajo previo.
- Cambios que rompan la viabilidad financiera del proyecto sin ajustar los objetivos de marketing.

## Salida esperada
`docs/changes/registro_cambio_XXX.md`

## Gates relacionados
`gate_impacto_cambio`

## Criterios de insuficiencia
La skill es insuficiente si se aplica el cambio sin advertir al usuario de qué documentos han quedado obsoletos y deben ser actualizados.

## Errores frecuentes
- Tratar cambios de impacto Alto como si fueran simples correcciones de texto.
- No pedir confirmación antes de borrar o sobrescribir un avance estratégico importante.

## Límites
No ejecuta los cambios automáticamente; registra el impacto y prepara el sistema para la regeneración controlada de las piezas afectadas.

---
name: skill_kpis
description: Definir indicadores clave de desempeño (KPIs) específicos para medir el éxito del plan según el modelo de negocio.
---

# skill_kpis

## Estado
activa_documental

## Objetivo
Establecer métricas claras y accionables que permitan evaluar si el plan de marketing está funcionando y dónde hay que ajustar.

## Cuándo usarla
Usar después del plan de acción y el presupuesto.

## Agente activador
`analista_metricas`

## Entradas necesarias
- `tipo_negocio` o `marketing_profile`.
- `objetivo_marketing`.
- `07_plan_accion_90_dias.md`.
- `06_matriz_canales.md`.

## Proceso
1. Seleccionar KPIs que realmente muevan la aguja del negocio según su modelo (no métricas de vanidad).
2. Definir unidad de medida, frecuencia de revisión y fuente del dato para cada KPI.
3. Establecer metas realistas (Hitos) basadas en la madurez diagnosticada.

## Adaptación por modelo de negocio
- **ecommerce_transaccional**: ROAS, CPA (Coste por Adquisición), Tasa de Conversión, Ticket Medio, Abandono de Carrito y Tasa de Recompra.
- **b2b_consultivo**: CPL (Coste por Lead), MQL/SQL, Número de reuniones, Tasa de conversión a oportunidad y Ciclo de venta medio.
- **b2b_producto_industrial**: Número de RFQs (Solicitudes de cotización), Leads técnicos generados, Homologaciones conseguidas y ventas vía distribuidores.
- **retail_fisico**: Visitas a tienda física, Llamadas desde Google Maps, Reseñas nuevas, Tráfico local y volumen de ventas en tienda.
- **educativo_formativo**: Número de Leads, Tasa de matriculación, Asistencia a sesiones informativas, Tasa de retención y Coste por Inscripción.
- **hibrido_producto_servicio**: Venta inicial de activo, Tasa de activación de soporte, Renovaciones de contrato, Recurrencia y churn.
- **b2c_local_servicios**: Número de Reservas, Llamadas recibidas, Reseñas positivas, Tasa de asistencia (no-show) y rapidez de respuesta.

## Cuándo declarar insuficiencia
Debe declarar insuficiencia si:
- El modelo de negocio es ambiguo.
- Los KPIs propuestos no tienen una unidad de medida clara o una fuente de datos identificada.
- No hay conexión entre el KPI y el objetivo de marketing definido en el brief.
- Se proponen KPIs imposibles de medir con los recursos o herramientas declarados.

## Salida esperada
`outputs/plan_actual/09_kpis_y_seguimiento.md`

## Gates relacionados
`gate_medibilidad`

## Criterios de insuficiencia
La skill es insuficiente si propone más de 5 KPIs principales o si los indicadores no permiten tomar decisiones correctivas (ej. medir solo "seguidores").

## Errores frecuentes
- Proponer métricas de vanidad (likes, alcances genéricos) sin relación con la venta o el objetivo.
- No diferenciar entre métricas de captación y métricas de negocio.
- Proponer frecuencias de medición que el equipo no puede atender.

## Límites
No implementa el seguimiento técnico (píxeles, tag manager); solo define la arquitectura de medición estratégica.

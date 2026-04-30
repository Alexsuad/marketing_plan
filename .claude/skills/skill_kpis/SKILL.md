---
name: skill_kpis
description: Definir KPIs y sistema básico de medición del Plan de Marketing.
---

# skill_kpis

## Estado
activa_documental

## Objetivo
Definir KPIs y sistema básico de medición del Plan de Marketing.

## Cuándo usarla
Usar después de tener plan de acción y presupuesto.

## Agente activador
`analista_metricas`

## Entradas necesarias
- Objetivos del plan.
- Canales priorizados.
- Plan de acción.
- Capacidades actuales de medición.

## Proceso
1. Definir objetivos medibles.
2. Elegir KPIs principales relacionados a negocio.
3. Elegir métricas de apoyo (diagnóstico).
4. Indicar fuente de datos y frecuencia de revisión.
5. Sugerir señales de alerta.

## Salida esperada
`outputs/plan_actual/10_kpis_y_medicion.md`

## Gates relacionados
`gate_kpis_medibles`

## Criterios de insuficiencia
Debe marcar observación si no existe forma razonable de medir un KPI con los recursos actuales.

## Errores frecuentes
- Usar métricas de vanidad (likes, views) en vez de métricas de captación o venta.
- Proponer herramientas de analítica complejas para un negocio pequeño sin recursos.

## Límites
No conecta APIs ni configura dashboards reales, solo documenta la estrategia de medición.

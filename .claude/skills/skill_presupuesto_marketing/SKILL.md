---
name: skill_presupuesto_marketing
description: Asignar o estimar los costos del plan de acción.
---

# skill_presupuesto_marketing

## Estado
activa_documental

## Objetivo
Asignar o estimar los costos del plan de acción.

## Cuándo usarla
Usar junto con o después del plan de acción.

## Agente activador
`estratega_marketing`

## Entradas necesarias
- Presupuesto inicial (del brief).
- Canales priorizados.
- Plan de acción.

## Proceso
1. Clasificar gastos: herramientas, publicidad (ads), agencias/freelancers.
2. Distribuir el presupuesto orientativamente según la prioridad de canales.
3. Si no hay presupuesto, indicar qué canales son viables de forma orgánica.
4. Listar acciones con coste y herramientas necesarias.

## Salida esperada
`outputs/plan_actual/09_presupuesto_marketing.md`

## Gates relacionados
`gate_presupuesto_prudente`

## Criterios de insuficiencia
Si no hay presupuesto aportado, debe trabajar con rangos prudentes o declarar la falta del dato en lugar de inventar cifras definitivas. Es obligatorio presentar los costes estimados como rangos u horquillas amplias (nunca valores exactos cerrados), salvo que el usuario proporcione datos reales.

## Errores frecuentes
- Asignar presupuesto a canales que requieren tiempo, no dinero, sin justificar.
- Inventar costos exactos para servicios externos que varían.

## Límites
No emite facturas ni cierra contratos reales, solo propone estimaciones para planificación.

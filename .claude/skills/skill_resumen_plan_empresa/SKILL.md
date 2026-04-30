---
name: skill_resumen_plan_empresa
description: Crear un resumen del Plan de Marketing compatible con el Plan de Empresa.
---

# skill_resumen_plan_empresa

## Estado
activa_documental

## Objetivo
Crear un resumen del Plan de Marketing compatible con el Plan de Empresa.

## Cuándo usarla
Usar cuando los documentos principales del Plan de Marketing estén generados.

## Agente activador
`redactor_marketing`

## Entradas necesarias
- Todo el plan estratégico, canales, plan de acción, presupuesto y KPIs.

## Proceso
1. Sintetizar contenido sin copiar.
2. Extraer mercado objetivo, propuesta de valor, canales, acciones clave, presupuesto y KPIs.
3. Condensar en un formato legible para directivos o inversores.

## Salida esperada
`outputs/plan_actual/11_resumen_para_plan_empresa.md`

## Gates relacionados
`gate_resumen_plan_empresa`

## Criterios de insuficiencia
Debe marcar como pendiente si falta algún documento base necesario. No debe desarrollar áreas ajenas al marketing.

## Errores frecuentes
- Incluir demasiado nivel de detalle operativo en un resumen gerencial.
- Olvidar incluir el presupuesto o los KPIs en el resumen.

## Límites
Es solo un resumen ejecutivo; no reemplaza la totalidad de los documentos operativos del plan de marketing.

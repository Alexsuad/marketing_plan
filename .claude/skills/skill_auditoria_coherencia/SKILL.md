---
name: skill_auditoria_coherencia
description: Revisar coherencia, calidad y riesgos del Plan de Marketing.
---

# skill_auditoria_coherencia

## Estado
activa_documental

## Objetivo
Revisar coherencia, calidad y riesgos del Plan de Marketing.

## Cuándo usarla
Usar al cierre del plan o cuando un gate detecte posibles inconsistencias.

## Agente activador
`auditor_plan_marketing`

## Entradas necesarias
- Todos los documentos del plan.
- Brief validado.
- Outputs de gates y contexto inicial.

## Proceso
1. Revisar coherencia entre documentos.
2. Identificar contradicciones e información faltante.
3. Cuestionar canales injustificados y acciones poco realistas.
4. Comprobar que los KPIs respondan a los objetivos.
5. Identificar riesgos de ejecución.

## Salida esperada
`outputs/plan_actual/12_auditoria_final.md` (o reportes parciales).

## Gates relacionados
`gate_auditoria_final`

## Criterios de insuficiencia
Debe bloquear si falta un documento central, si el cliente objetivo no coincide con canales, si la propuesta es genérica, el plan de acción no ejecutable, o los KPIs no medibles.

## Errores frecuentes
- Aprobar sin revisar contra el brief original.
- Centrarse solo en gramática y olvidar la coherencia estratégica.

## Límites
No reescribe el plan; documenta observaciones y requiere que los agentes correspondientes lo arreglen.

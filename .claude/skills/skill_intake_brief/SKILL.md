---
name: skill_intake_brief
description: Extraer, organizar y validar la información mínima necesaria para iniciar un Plan de Marketing a partir de un texto libre o entrevista.
---

# skill_intake_brief

## Estado
activa_documental

## Objetivo
Extraer, organizar y validar la información mínima necesaria para iniciar un Plan de Marketing a partir de un texto libre o entrevista.

## Cuándo usarla
Usar al inicio de un nuevo proyecto, cuando el usuario proporciona la primera descripción del negocio.

## Agente activador
`orquestador_plan_marketing`

## Entradas necesarias
- Texto libre proporcionado por el usuario, transcripción de entrevista o documento inicial del negocio.

## Proceso
1. Leer el texto proporcionado.
2. Extraer los campos obligatorios del brief mínimo:
   - `nombre_negocio`
   - `tipo_empresa_servicios`
   - `servicio_principal`
   - `cliente_objetivo`
   - `problema_que_resuelve`
   - `objetivo_principal`
3. Extraer el campo opcional: `presupuesto_marketing`.
4. Si un campo obligatorio no está presente, marcarlo como faltante.

## Salida esperada
`projects/nombre_proyecto/context/brief_negocio.md`

## Gates relacionados
`gate_brief_minimo`

## Criterios de insuficiencia
La skill debe bloquear la salida e informar qué campos faltan si no se pueden deducir claramente. No debe inventar campos faltantes bajo ninguna circunstancia.

## Errores frecuentes
- Inventar información faltante para completar el brief.
- Aceptar descripciones vagas como un dato válido (ej. "nuestro servicio es bueno" en problema_que_resuelve).

## Límites
No debe iniciar investigación de mercado ni avanzar de fase, solo estructura la entrada del usuario.

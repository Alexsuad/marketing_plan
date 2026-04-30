---
name: skill_intake_brief
description: Extraer, organizar y validar la información mínima necesaria (negocio, oferta, cliente, problema) para iniciar un Plan de Marketing multimodelo.
---

# skill_intake_brief

## Estado
activa_documental

## Objetivo
Extraer, organizar y validar la información mínima necesaria para iniciar un Plan de Marketing a partir de un texto libre o entrevista, identificando el modelo de negocio desde el inicio.

## Cuándo usarla
Usar al inicio de un nuevo proyecto, cuando el usuario proporciona la primera descripción del negocio o briefing.

## Agente activador
`orquestador_plan_marketing`

## Entradas necesarias
- Texto libre proporcionado por el usuario, transcripción de entrevista o documento inicial del negocio.

## Proceso
1. Leer y analizar el texto proporcionado para identificar el modelo de negocio.
2. Extraer los campos obligatorios del brief mínimo multimodelo:
   - `nombre_negocio`
   - `tipo_negocio` (clasificar según los 7 modelos soportados)
   - `oferta_principal` (producto, servicio, formación o solución híbrida)
   - `cliente_objetivo`
   - `problema_que_resuelve`
   - `objetivo_marketing`
3. Extraer campos de contexto y operativos:
   - `restricciones/capacidades` (qué pueden o no pueden hacer)
   - `presupuesto_marketing` (si no existe, declarar como "No informado")
   - `canal_actual` (si ya operan en algún canal)
4. Validar que la información extraída sea específica y no genérica.

## Adaptación por modelo de negocio
- **ecommerce_transaccional**: Foco en catálogo, stock, logística, pasarela de pago y ticket medio de producto.
- **b2b_consultivo**: Foco en servicios profesionales, ciclo de venta largo, confianza y autoridad técnica.
- **b2b_producto_industrial**: Foco en especificaciones técnicas, suministros a empresas, homologación y cotización.
- **retail_fisico**: Foco en ubicación geográfica, tráfico a tienda física y disponibilidad inmediata de stock.
- **educativo_formativo**: Foco en programas de aprendizaje, transformación del alumno e inscripciones/matrícula.
- **hibrido_producto_servicio**: Foco en la venta de un activo físico vinculado a un soporte o mantenimiento recurrente.
- **b2c_local_servicios**: Foco en servicios de cercanía (zona), sistema de reservas y reputación local.

## Cuándo declarar insuficiencia
Debe declarar insuficiencia si:
- No se puede identificar claramente el `tipo_negocio`, la `oferta_principal`, el `cliente_objetivo` o el `problema_que_resuelve`.
- El brief usa frases vagas o sin valor estratégico (ej. "somos los mejores", "servicio de calidad", "queremos vender más").
- El modelo de negocio queda en una zona gris ambigua que impide elegir canales o mensajes (ej. no se sabe si el cliente vende el software o hace la consultoría del software).
- Faltan datos críticos sobre qué se está intentando vender realmente.

## Salida esperada
`projects/nombre_proyecto/context/brief_negocio.md`

## Gates relacionados
`gate_brief_minimo`

## Criterios de insuficiencia
La skill debe bloquear la salida e informar qué campos faltan o qué descripciones son demasiado vagas para ser accionables. No debe inventar datos bajo ninguna circunstancia.

## Errores frecuentes
- Inventar información para "rellenar" el brief.
- Aceptar descripciones que no diferencian el negocio (ej. "atención personalizada" como oferta principal).

## Límites
No debe iniciar investigación de mercado; solo estructura la entrada del usuario de forma profesional y estratégica.

---
name: skill_estrategia_comunicacion
description: Definir qué decir en los canales elegidos adaptando el lenguaje al modelo de negocio.
---

# skill_estrategia_comunicacion

## Estado
activa_documental

## Objetivo
Definir qué decir en los canales elegidos para conectar la oferta con las necesidades del cliente.

## Cuándo usarla
Usar inmediatamente después de priorizar los canales de captación.

## Agente activador
`estratega_marketing` (con apoyo de `redactor_marketing`)

## Entradas necesarias
- `marketing_profile` (para el tono y acción contextual).
- `04_propuesta_valor_y_posicionamiento.md`
- `06_matriz_canales_marketing.md`
- `03_cliente_objetivo_y_segmentos.md` (dolores y objeciones).

## Proceso
1. Definir el tono de voz (profesional, técnico, directo, etc.) según el modelo de negocio.
2. Mapear cada pilar de comunicación contra un dolor, necesidad u objeción específica del cliente.
3. Adaptar el lenguaje de acción según el modelo (ej. comprar vs contratar vs inscribirse).
4. Definir cómo tratar las objeciones críticas antes de la conversión.

## Adaptación por modelo de negocio
- **ecommerce_transaccional**: Lenguaje de "compra", inmediatez, facilidad, confianza en el producto y checkout.
- **b2b_consultivo**: Lenguaje de "contratación", autoridad técnica, diagnóstico, confianza profesional y resultados.
- **b2b_producto_industrial**: Lenguaje técnico, especificaciones, "cotización", homologación y soporte a largo plazo.
- **retail_fisico**: Lenguaje de "visita", experiencia en tienda, "recogida", stock local y cercanía geográfica.
- **educativo_formativo**: Lenguaje de "inscripción", aprendizaje, futuro profesional, confianza y transformación.
- **hibrido_producto_servicio**: Lenguaje de "adquisición con soporte", tranquilidad, mantenimiento y solución integral.
- **b2c_local_servicios**: Lenguaje de "reserva", cercanía, confianza personal y resultados tangibles inmediatos.

## Cuándo declarar insuficiencia
Debe declarar insuficiencia si:
- No se han identificado objeciones reales del cliente objetivo.
- El tono propuesto es incoherente con el modelo de negocio (ej. tono informal para industria pesada).
- No se diferencia el lenguaje de acción (ej. usar "contratar" para una tienda online de ropa).
- Faltan los pilares de la propuesta de valor para construir los ejes.

## Salida esperada
`outputs/plan_actual/07_estrategia_comunicacion.md`

## Gates relacionados
`gate_coherencia_cliente_propuesta`

## Criterios de insuficiencia
Insuficiente si los ejes de comunicación son genéricos y no responden a los problemas documentados.

## Errores frecuentes
- Usar lenguaje de servicios en modelos de venta de producto (eCommerce/Retail).
- Crear mensajes desconectados de la acción final deseada (conversión).

## Límites
No escribe copys finales (anuncios, posts), solo dicta la estrategia de qué comunicar y cómo.

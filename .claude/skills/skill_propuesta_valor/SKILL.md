---
name: skill_propuesta_valor
description: Construir el mensaje central que explique por qué el cliente debería elegir esta oferta.
---

# skill_propuesta_valor

## Estado
activa_documental

## Objetivo
Construir el mensaje central que explique por qué el cliente debería elegir esta oferta.

## Cuándo usarla
Usar cuando los segmentos de cliente estén definidos.

## Agente activador
`estratega_marketing`

## Entradas necesarias
- `tipo_negocio` o `marketing_profile` (determina el enfoque).
- `oferta_principal` (qué vendemos).
- `cliente_objetivo` (a quién le hablamos).
- `problema_que_resuelve` (qué dolor aliviamos).
- `restricciones/capacidades` (qué podemos prometer).

## Proceso
1. Relacionar la oferta principal con el problema prioritario del cliente según el modelo de negocio.
2. Definir el beneficio funcional (qué hace el producto/servicio).
3. Definir el beneficio emocional o de negocio (qué logra el cliente).
4. Redactar el mensaje central (Elevator Pitch) adaptado al tono del modelo.
5. Definir 3 pilares que sostengan la propuesta (evitando superlativos vacíos).

## Adaptación por modelo de negocio
- **ecommerce_transaccional**: Foco en producto, facilidad de compra, confianza inmediata, diferenciación y recompra.
- **b2b_consultivo**: Foco en autoridad, diagnóstico experto, reducción de riesgo y ciclo de venta largo.
- **b2b_producto_industrial**: Foco en ficha técnica, cumplimiento de normativa, homologación y cotización precisa.
- **retail_fisico**: Foco en visita a tienda, cercanía, experiencia sensorial y disponibilidad local.
- **educativo_formativo**: Foco en aprendizaje, transformación personal/profesional e inscripción/matrícula.
- **hibrido_producto_servicio**: Foco en el valor del producto potenciado por el soporte, mantenimiento o SLA.
- **b2c_local_servicios**: Foco en confianza personal, agilidad en reserva y reputación local (reseñas).

## Cuándo declarar insuficiencia
Debe declarar insuficiencia si:
- No está claro el modelo de negocio (ej. no se sabe si es venta directa o servicios).
- No está clara la oferta principal o el problema que resuelve.
- Faltan datos críticos sobre el cliente objetivo.
- Se detecta una propuesta basada únicamente en superlativos ("el mejor", "líder") sin evidencia.

## Salida esperada
`outputs/plan_actual/04_propuesta_valor_y_posicionamiento.md`

## Gates relacionados
`gate_coherencia_cliente_propuesta`

## Criterios de insuficiencia
La propuesta es insuficiente si es igual a la de cualquier competidor genérico o si usa jerga vacía.

## Errores frecuentes
- Usar superlativos ("excelencia", "innovador") sin pruebas.
- No conectar la solución con el dolor específico del cliente según su modelo.

## Límites
No define campañas de publicidad; solo define el núcleo del mensaje.

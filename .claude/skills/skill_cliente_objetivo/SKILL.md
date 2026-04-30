---
name: skill_cliente_objetivo
description: Definir el perfil del cliente y segmentos operativos según el modelo de negocio y comportamiento de compra.
---

# skill_cliente_objetivo

## Estado
activa_documental

## Objetivo
Pasar de un cliente genérico a un perfil accionable, identificando decisores, usuarios y señales de compra reales según el modelo de negocio.

## Cuándo usarla
Usar después del diagnóstico, antes de definir la propuesta de valor y los canales.

## Agente activador
`estratega_marketing` (apoyado por `investigador_marketing`)

## Entradas necesarias
- `brief_negocio.md`
- `tipo_negocio` o `marketing_profile` (determina el comportamiento de compra).
- `oferta_principal` y `problema_que_resuelve`.
- `02_diagnostico_marketing.md` (si existe).

## Proceso
1. Analizar el comportamiento de compra según el modelo de negocio (ej. compra impulsiva vs homologación técnica).
2. Identificar el mapa de decisión: ¿Quién compra? ¿Quién usa? ¿Quién decide?
3. Segmentar por necesidades operativas y dolores diarios, no solo por datos demográficos.
4. Definir el "Segmento Semilla" (Seed): el grupo más accesible y con mayor dolor para iniciar la validación.
5. Identificar las objeciones críticas que impiden la conversión en este modelo específico.

## Adaptación por modelo de negocio
- **ecommerce_transaccional**: Comprador digital, intención de compra, objeciones de confianza, precio, envío, devolución y recompra.
- **b2b_consultivo**: Decisor, comité de compra, autoridad, dolor operativo, confianza técnica y ciclo de venta largo.
- **b2b_producto_industrial**: Comprador técnico, departamento de compras, homologación, especificaciones, riesgo proveedor y cotización.
- **retail_fisico**: Cliente local, radio de influencia geográfica, visita a tienda física, recurrencia y experiencia sensorial.
- **educativo_formativo**: Alumno, familia o empresa, motivación de aprendizaje, confianza en el programa, resultados e inscripción.
- **hibrido_producto_servicio**: Comprador del producto físico + usuario del soporte, mantenimiento o garantía recurrente.
- **b2c_local_servicios**: Cliente de cercanía, urgencia por el resultado, reputación local, reserva inmediata y confianza personal.

## Cuándo declarar insuficiencia
Debe declarar insuficiencia si:
- No está claro quién compra, quién usa y quién decide finalmente.
- No está claro el problema real que motiva la compra, reserva, inscripción o solicitud de cotización.
- Se describe al cliente con frases vagas como "todo el mundo" o segmentaciones puramente demográficas irrelevantes.
- No se puede diferenciar claramente el comportamiento de compra (B2B, B2C, Retail, Educativo o Híbrido).
- Faltan datos críticos para entender el ciclo de decisión (ej. no saber si es compra impulsiva o por licitación).

## Salida esperada
`outputs/plan_actual/03_cliente_objetivo_y_segmentos.md`

## Gates relacionados
`gate_coherencia_cliente_propuesta`

## Criterios de insuficiencia
La skill es insuficiente si los segmentos no derivan de los datos del brief o si no existe conexión lógica entre el problema, el cliente y su operativa diaria.

## Errores frecuentes
- Segmentar solo por edad/género cuando el comportamiento es profesional o técnico.
- Proponer segmentos inaccesibles para el presupuesto o capacidad operativa del cliente.
- Ignorar la diferencia entre el usuario final y el decisor financiero en modelos B2B o Educativos.

## Límites
No propone canales de comunicación; se enfoca exclusivamente en la radiografía del cliente y su proceso de decisión.

---
name: skill_analisis_competencia
description: Analizar a los competidores directos e indirectos según el modelo de negocio para identificar brechas y ventajas.
---

# skill_analisis_competencia

## Estado
activa_documental

## Objetivo
Identificar cómo se posicionan otros actores frente al mismo problema y cliente, analizando sus debilidades y fortalezas operativas según el modelo de negocio.

## Cuándo usarla
Usar después de definir el cliente objetivo y antes de la propuesta de valor.

## Agente activador
`investigador_marketing`

## Entradas necesarias
- `tipo_negocio` o `marketing_profile`.
- `oferta_principal` y `cliente_objetivo`.
- `problema_que_resuelve`.
- Lista de competidores mencionados (opcional).

## Proceso
1. Seleccionar competidores relevantes según el modelo de negocio (no comparar peras con manzanas).
2. Analizar la oferta, canales y posicionamiento de la competencia.
3. Identificar brechas de mercado (dolores no resueltos por otros).
4. No inventar nombres de empresas ni datos de facturación; usar solo información pública o deducible de su presencia digital.

## Adaptación por modelo de negocio
- **ecommerce_transaccional**: Comparar tiendas online, catálogo, precio, usabilidad, reseñas, plazos de entrega y política de devolución.
- **b2b_consultivo**: Comparar autoridad de marca, casos de éxito, especialización, confianza y metodología comercial.
- **b2b_producto_industrial**: Comparar ficha técnica, certificaciones de calidad, red de distribución, soporte técnico y homologación.
- **retail_fisico**: Comparar ubicación geográfica, experiencia en tienda, surtido de productos, precios locales, reseñas y visibilidad.
- **educativo_formativo**: Comparar programas académicos, metodología, resultados de alumnos, reputación del profesorado e inscripciones.
- **hibrido_producto_servicio**: Comparar el activo físico inicial + la calidad del soporte, garantía y servicios de mantenimiento recurrentes.
- **b2c_local_servicios**: Comparar reputación en zona, cercanía física, rapidez de respuesta, reseñas de clientes y facilidad de reserva.

## Cuándo declarar insuficiencia
Debe declarar insuficiencia si:
- No se conoce el modelo de negocio o la oferta principal.
- No se han identificado competidores reales y no hay datos suficientes para buscarlos.
- Se intenta comparar un modelo con otro incompatible (ej. comparar un eCommerce nacional con una tienda física local).
- No hay claridad sobre qué valor diferencial está analizando frente a la competencia.

## Salida esperada
`outputs/plan_actual/04_analisis_competencia.md`

## Gates relacionados
`gate_no_invencion`

## Criterios de insuficiencia
La skill es insuficiente si se limita a listar nombres de empresas sin analizar su estrategia de canales, precios o mensajes clave.

## Errores frecuentes
- Inventar competidores que no existen.
- Asumir que la competencia es "nadie" (siempre hay una alternativa, aunque sea el "no hacer nada").
- Centrarse solo en el precio ignorando la confianza o el soporte técnico.

## Límites
No propone la propuesta de valor propia; solo analiza el tablero de juego actual.

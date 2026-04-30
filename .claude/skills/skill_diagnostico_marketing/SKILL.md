---
name: skill_diagnostico_marketing
description: Establecer el punto de partida real del negocio analizando la madurez de marketing según su modelo específico.
---

# skill_diagnostico_marketing

## Estado
activa_documental

## Objetivo
Establecer el punto de partida real del negocio para evitar estrategias desconectadas de la situación actual, diferenciando hechos de hipótesis.

## Cuándo usarla
Usar inmediatamente después de que el brief haya sido validado y clasificado por modelo.

## Agente activador
`investigador_marketing`

## Entradas necesarias
- `brief_negocio.md`
- `tipo_negocio` o `marketing_profile` (determina los KPIs de diagnóstico).
- `oferta_principal` y `cliente_objetivo`.
- `problema_que_resuelve`.
- `canal_actual` (si existe).
- `restricciones/capacidades` (equipo, tiempo, presupuesto).

## Proceso
1. Analizar el modelo de negocio detectado (no tratar todos los negocios como servicios).
2. Diagnosticar la madurez de marketing según el modelo (ej. conversión en eCommerce vs autoridad en B2B).
3. Separar explícitamente hechos (datos confirmados), hipótesis (suposiciones razonables) y vacíos de información.
4. Identificar si el negocio está usando canales actuales incoherentes con su modelo o capacidad.
5. Identificar ventajas competitivas reales vs. declaraciones genéricas del cliente.

## Adaptación por modelo de negocio
- **ecommerce_transaccional**: Diagnosticar conversión, ficha de producto, checkout, tráfico, recompra y ROAS.
- **b2b_consultivo**: Diagnosticar autoridad, confianza, ciclo de venta, generación de demanda y reuniones.
- **b2b_producto_industrial**: Diagnosticar ficha técnica, homologación, cotización, distribuidores y confianza técnica.
- **retail_fisico**: Diagnosticar visibilidad local, tráfico a tienda, reseñas, experiencia física y radio de influencia.
- **educativo_formativo**: Diagnosticar captación de alumnos, prueba social, claridad de programa e inscripción.
- **hibrido_producto_servicio**: Diagnosticar venta inicial del producto y recurrencia por soporte o mantenimiento.
- **b2c_local_servicios**: Diagnosticar reservas, reputación local, reseñas, rapidez de contacto y zona de cobertura.

## Cuándo declarar insuficiencia
Debe declarar insuficiencia si:
- No está claro el modelo de negocio o la oferta principal.
- No hay información mínima sobre los canales actuales en uso.
- No hay claridad sobre el cliente objetivo o el problema que se resuelve.
- Se intenta hacer el diagnóstico con frases vagas o sin evidencia verificable.
- No se puede diferenciar claramente entre un hecho y una hipótesis de trabajo.

## Salida esperada
`outputs/plan_actual/02_diagnostico_marketing.md`

## Gates relacionados
`gate_no_invencion`

## Criterios de insuficiencia
Debe señalar explícitamente si la información de partida es insuficiente. Debe separar certezas de suposiciones de forma visual o estructural.

## Errores frecuentes
- Realizar un análisis FODA genérico sin relación con el negocio específico.
- Diagnosticar un eCommerce como si fuera un servicio consultivo.
- Diagnosticar un negocio Retail local como si fuera un negocio de alcance nacional.
- Inventar madurez digital, resultados o canales no informados por el cliente.

## Límites
No propone acciones futuras; solo diagnostica la situación actual (el "dónde estamos") con rigor técnico.

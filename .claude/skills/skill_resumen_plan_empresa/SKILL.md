---
name: skill_resumen_plan_empresa
description: Generar una síntesis ejecutiva y estratégica de todo el Plan de Marketing para la dirección o el cliente.
---

# skill_resumen_plan_empresa

## Estado
activa_documental

## Objetivo
Consolidar los hallazgos y decisiones más importantes de todas las fases en un documento de alto nivel que facilite la toma de decisiones.

## Cuándo usarla
Usar como paso final una vez generados todos los documentos estratégicos y operativos.

## Agente activador
`orquestador_plan_marketing` (apoyado por `auditor_plan_marketing`)

## Entradas necesarias
- `marketing_profile` o `tipo_negocio`.
- Todos los documentos de salida de las fases 01 a 09.
- `oferta_principal`, `cliente_objetivo` y `objetivo_marketing`.

## Proceso
1. Sintetizar el modelo de negocio detectado y la oportunidad de mercado.
2. Resumir la estrategia (Propuesta de valor, Canales y Plan de acción) de forma coherente.
3. Destacar los KPIs críticos y el presupuesto necesario.
4. Asegurar que el tono sea profesional y adaptado al modelo de negocio (no sonar genérico).
5. Validar la coherencia final entre todas las piezas del plan.

## Adaptación por modelo de negocio
- **ecommerce_transaccional**: Foco en rentabilidad digital (ROAS), escala de ventas online y eficiencia logística.
- **b2b_consultivo**: Foco en posicionamiento de autoridad, generación de confianza y robustez del ciclo de venta.
- **b2b_producto_industrial**: Foco en solvencia técnica, red de distribución y captación de grandes cuentas/contratos.
- **retail_fisico**: Foco en dominancia local, tráfico a punto de venta y fidelización por cercanía/experiencia.
- **educativo_formativo**: Foco en volumen de inscripciones, calidad del programa y prueba social de resultados.
- **hibrido_producto_servicio**: Foco en el ecosistema de venta del producto más el flujo de ingresos recurrentes por soporte.
- **b2c_local_servicios**: Foco en reputación inmediata, facilidad de reserva y eficiencia en la zona de cobertura.

## Cuándo declarar insuficiencia
Debe declarar insuficiencia si:
- Faltan documentos críticos de fases previas (ej. no hay diagnóstico o no hay plan de acción).
- Existe una contradicción grave entre la oferta, el cliente y los canales elegidos.
- No está claro el `tipo_negocio` o la `oferta_principal`.
- El resumen suena a plantilla genérica y no refleja las particularidades del negocio analizado.

## Salida esperada
`outputs/plan_actual/10_resumen_ejecutivo.md`

## Gates relacionados
`gate_coherencia_final`

## Criterios de insuficiencia
La skill es insuficiente si el resumen no permite a un directivo entender qué se va a hacer, cuánto va a costar y qué se espera obtener en 90 días.

## Errores frecuentes
- Incluir excesivo detalle técnico que oscurece la visión estratégica.
- Hablar de "servicios" en un plan de eCommerce o de "tienda online" en un B2B industrial.
- Ignorar las restricciones/capacidades del cliente mencionadas en el brief.

## Límites
No modifica las decisiones tomadas en las fases previas; solo las sintetiza y las presenta de forma coherente.

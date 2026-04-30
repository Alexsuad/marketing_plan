---
name: skill_presupuesto_marketing
description: Estimar y distribuir la inversión necesaria según el modelo de negocio y los objetivos comerciales.
---

# skill_presupuesto_marketing

## Estado
activa_documental

## Objetivo
Asignar recursos financieros de forma lógica para cubrir las fases de captación y conversión según la madurez del negocio.

## Cuándo usarla
Usar después de definir la matriz de canales y el plan de acción.

## Agente activador
`analista_metricas` (apoyado por `estratega_marketing`)

## Entradas necesarias
- `tipo_negocio` o `marketing_profile`.
- `objetivo_marketing`.
- `restricciones/capacidades` (presupuesto disponible o límite de gasto).
- Canales elegidos en la fase previa.

## Proceso
1. Adaptar la distribución del presupuesto al modelo y madurez del negocio.
2. Identificar partidas críticas: pauta digital (performance), creación de contenido, herramientas o eventos.
3. Priorizar canales con mayor probabilidad de retorno rápido según el perfil.
4. Declarar como "No informado" si no existe una cifra inicial, sugiriendo rangos lógicos para el sector.

## Adaptación por modelo de negocio
- **ecommerce_transaccional**: Inversión en performance (Ads), creatividades, retargeting, email marketing, optimización de conversión y logística.
- **b2b_consultivo**: Inversión en prospección (LinkedIn), contenido de autoridad, eventos selectos, herramientas de CRM y ventas.
- **b2b_producto_industrial**: Inversión en ferias sectoriales, fichas técnicas de alta calidad, SEO técnico, muestras y materiales comerciales.
- **retail_fisico**: Inversión en Google Business Profile, campañas geolocalizadas, señalética, promociones locales y fidelización física.
- **educativo_formativo**: Inversión en campañas de captación masiva, sesiones informativas (webinars), prueba social y automatización de inscripciones.
- **hibrido_producto_servicio**: Inversión dividida entre la captación de la venta inicial del producto y la retención/soporte recurrente.
- **b2c_local_servicios**: Inversión en anuncios de búsqueda local (reservas), reputación digital, reseñas y optimización de rapidez de contacto.

## Cuándo declarar insuficiencia
Debe declarar insuficiencia si:
- No existe una cifra de presupuesto informada y no hay capacidad mínima declarada para ejecutar acciones.
- Los canales elegidos requieren una inversión que supera manifiestamente las restricciones del cliente.
- No hay claridad sobre el objetivo comercial que justifica la inversión.
- Se intenta asignar presupuesto sin conocer el coste de oportunidad o la madurez del equipo.

## Salida esperada
`outputs/plan_actual/08_presupuesto_marketing.md`

## Gates relacionados
`gate_viabilidad_operativa`

## Criterios de insuficiencia
La skill debe bloquear si propone una estrategia de inversión que el cliente no puede sostener (ej. recomendar TV a una micropyme).

## Errores frecuentes
- No considerar el coste de las herramientas o del tiempo del equipo (coste operativo).
- Asignar todo el presupuesto a captación olvidando la retención o el soporte (especialmente en modelos híbridos).
- Ignorar la estacionalidad del negocio.

## Límites
No gestiona pagos ni finanzas reales; solo realiza la planificación estratégica de la inversión de marketing.

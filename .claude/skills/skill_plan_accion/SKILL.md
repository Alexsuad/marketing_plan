---
name: skill_plan_accion
description: Bajar la estrategia a un plan realista y secuencial de 90 días adaptado al modelo de negocio.
---

# skill_plan_accion

## Estado
activa_documental

## Objetivo
Bajar la estrategia a un plan realista y secuencial de 90 días para validar el mercado.

## Cuándo usarla
Usar cuando todo el diseño estratégico previo esté completado.

## Agente activador
`estratega_marketing`

## Entradas necesarias
- `marketing_profile` (para secuenciación de hitos).
- Resumen de estrategia y canales elegidos.
- Recursos disponibles (tiempo, equipo, presupuesto).

## Proceso
1. Dividir el plan en 3 bloques de 30 días con objetivos claros por modelo.
2. Definir los activos mínimos necesarios (fichas, landing, perfiles, equipo) antes de activar.
3. Establecer hitos de validación (ventas, leads, tráfico, visitas) según el tipo de oferta.
4. Asignar responsables y dependencias técnicas críticas.

## Adaptación por modelo de negocio
- **ecommerce_transaccional**: Foco en checkout operativo, catálogo, tráfico, conversión, retargeting y métricas de venta.
- **b2b_consultivo**: Foco en red de contactos, reuniones, webinars, autoridad y pipeline de ventas.
- **b2b_producto_industrial**: Foco en prospección, fichas técnicas, homologaciones, contactos directos y ofertas (cotizaciones).
- **retail_fisico**: Foco en visibilidad local, tráfico peatonal, promociones en tienda y experiencia de visita física.
- **educativo_formativo**: Foco en captación de interesados, sesiones informativas, prueba social e inscripciones.
- **hibrido_producto_servicio**: Foco en venta inicial del producto + configuración del soporte recurrente/mantenimiento.
- **b2c_local_servicios**: Foco en sistema de reservas, reseñas, visibilidad en zona y agilidad de respuesta.

## Cuándo declarar insuficiencia
Debe declarar insuficiencia si:
- El plan no tiene metas medibles según el modelo (ej. plan de ecommerce sin mencionar ventas o tráfico).
- Se sobrecarga la primera semana sin tener los activos previos listos.
- No hay responsables claros o dependencias técnicas identificadas.
- El plan ignora la capacidad operativa real del cliente.

## Salida esperada
`outputs/plan_actual/08_plan_accion_90_dias.md`

## Gates relacionados
`gate_plan_accion_realista`

## Criterios de insuficiencia
Bloquea si el plan es una lista de deseos sin secuencia lógica o sin activos de soporte.

## Errores frecuentes
- Tratar un eCommerce como si fuera un servicio (solo entrevistas cualitativas).
- Ignorar la necesidad de tráfico pagado o SEO en modelos digitales transaccionales.

## Límites
No debe ejecutar las tareas; define el plan, las secuencias y los indicadores de éxito.

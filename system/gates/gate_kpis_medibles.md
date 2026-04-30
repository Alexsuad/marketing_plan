# Gate: KPIs Medibles y Específicos (Multimodelo)

## Propósito
Validar que los indicadores de éxito propuestos son técnicos, medibles y adecuados para el modelo de negocio y los objetivos marcados.

## Criterios de Evaluación
1. **Relevancia de Modelo**: Los KPIs deben medir lo que realmente importa para el éxito del negocio (ej. ROAS en eCommerce vs. Reuniones en B2B).
2. **Estructura Técnica**: Cada KPI debe tener una Unidad de medida, una Frecuencia de revisión y una Fuente de datos identificada.
3. **Conexión con Objetivo**: El KPI debe permitir evaluar si se está cumpliendo el `objetivo_marketing` definido en el brief.
4. **Accionabilidad**: ¿El KPI permite tomar decisiones correctivas si el resultado no es el esperado?

## Validación por Modelo de Negocio
- **ecommerce_transaccional**: Aceptar ROAS, CPA, Tasa de Conversión Web, Ticket Medio, Abandono de Carrito y Recompra.
- **b2b_consultivo**: Aceptar CPL, MQL/SQL, Número de reuniones generadas, Tasa de conversión a oportunidad y Ciclo de venta.
- **b2b_producto_industrial**: Aceptar RFQs (Solicitudes de cotización), Cotizaciones enviadas, Homologaciones y contactos de distribuidores.
- **retail_fisico**: Aceptar Visitas a tienda, Llamadas desde perfiles locales, Reseñas nuevas y volumen de ventas físicas.
- **educativo_formativo**: Aceptar Número de matrículas, Asistencia a sesiones, Coste por Inscripción y Tasa de finalización.
- **hibrido_producto_servicio**: Aceptar Venta inicial, Activación de servicios de soporte, Renovación de contratos y Recurrencia.
- **b2c_local_servicios**: Aceptar Reservas confirmadas, Llamadas, Reseñas positivas y Tasa de asistencia (no-show).

## Acciones en caso de fallo
- **Bloquear**: Cualquier KPI que no tenga definida su Fuente de medición o Frecuencia.
- **Bloquear**: Métricas de vanidad (likes, seguidores) que no estén vinculadas a un objetivo de negocio claro.
- **Revisar**: Si el número de KPIs es excesivo (más de 5 principales) lo que dificulta el seguimiento.
- **Insuficiencia**: Si los KPIs propuestos no permiten evaluar el retorno de la inversión (ROI/ROAS).

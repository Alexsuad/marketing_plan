# Gate: Coherencia Cliente - Propuesta (Multimodelo)

## Propósito
Validar que existe un encaje lógico y comercial entre el perfil del cliente, el problema identificado y la oferta propuesta según el modelo de negocio.

## Criterios de Evaluación
1. **Encaje de Modelo**: La oferta debe ser coherente con el `tipo_negocio` (ej. no proponer consultoría en un eCommerce puro).
2. **Dolor vs. Solución**: La propuesta de valor debe resolver directamente el problema operativo o emocional del cliente objetivo definido.
3. **Rol de Decisión**: La propuesta debe hablar al decisor identificado (ej. comprador técnico en Industrial, decisor de negocio en B2B).
4. **Viabilidad Percibida**: ¿El cliente objetivo realmente compraría esta oferta para resolver este problema bajo estas condiciones?

## Validación por Modelo de Negocio
- **ecommerce_transaccional**: Debe haber foco en el producto, la facilidad de compra, la confianza técnica, la diferenciación clara y la logística.
- **b2b_consultivo**: Debe haber foco en el decisor de negocio, la autoridad del experto, el problema operativo y el ahorro/eficiencia.
- **b2b_producto_industrial**: Debe haber foco en el comprador técnico, la ficha de especificaciones, la homologación y la garantía de suministro.
- **retail_fisico**: Debe haber foco en el cliente local, la motivación de visita física, la cercanía y la experiencia inmediata.
- **educativo_formativo**: Debe haber foco en el alumno/familia/empresa, la promesa de aprendizaje, la prueba social y la claridad del programa.
- **hibrido_producto_servicio**: Debe haber foco en la conexión entre la adquisición del producto físico y el valor del soporte/mantenimiento.
- **b2c_local_servicios**: Debe haber foco en la urgencia/necesidad de cercanía, el sistema de reservas, la reputación local y la rapidez.

## Acciones en caso de fallo
- **Bloquear**: Si la propuesta de valor es genérica y no resuelve el problema específico del cliente.
- **Revisar**: Si el lenguaje utilizado no se corresponde con el modelo de negocio (ej. sesgo de "servicios" en planes de producto).
- **Insuficiencia**: Si no está claro quién es el decisor o cuál es el problema raíz.

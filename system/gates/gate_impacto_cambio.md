# Gate: Evaluación de Impacto del Cambio (Multimodelo)

## Propósito
Analizar las consecuencias de una solicitud de modificación en el plan, identificando el efecto cascada según el modelo de negocio.

## Clasificación del Impacto
- **Impacto Bajo**: Cambios estéticos, redacción, formato o ejemplos menores que no alteran la estrategia ni los canales.
- **Impacto Medio**: Ajustes en un canal secundario, un KPI específico o un mensaje de comunicación que no requiere rehacer la propuesta de valor.
- **Impacto Alto**: Modificación del `tipo_negocio`, la `oferta_principal`, el `cliente_objetivo`, la `propuesta_valor` o el `presupuesto_base`.

## Análisis de Cascada por Modelo
- **eCommerce**: Un cambio en la oferta afecta a la logística, el ticket medio y los KPIs de Ads.
- **B2B / Industrial**: Un cambio en el cliente objetivo invalida toda la estrategia de autoridad, prospección y homologación técnica.
- **Retail / Local**: Un cambio en el radio de influencia o tipo de servicio local invalida el diagnóstico de visibilidad y canales locales.
- **Educativo**: Un cambio en el programa o metodología requiere actualizar toda la prueba social y embudos de inscripción.

## Reglas de Validación
1. **Aprobación Explícita**: Los cambios de **Impacto Alto** requieren que el usuario escriba exactamente: `Aprobado` tras leer las consecuencias en cascada.
2. **Regeneración Forzada**: Identificar qué fases previas quedan obsoletas y deben volver a ejecutarse tras el cambio.
3. **Consistencia**: No permitir cambios que rompan la lógica interna del plan sin ajustar el resto de piezas vinculadas.

## Acciones en caso de fallo
- **Bloquear**: Si el usuario solicita un cambio estratégico mayor sin haber sido informado del impacto en cascada.
- **Bloquear**: Si el cambio solicitado es contradictorio con el modelo de negocio base sin una transición de modelo justificada.

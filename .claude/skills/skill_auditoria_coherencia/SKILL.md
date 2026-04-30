---
name: skill_auditoria_coherencia
description: Auditar la lógica, terminología y viabilidad estratégica de todas las fases del plan según el modelo de negocio.
---

# skill_auditoria_coherencia

## Estado
activa_documental

## Objetivo
Garantizar que el Plan de Marketing no tenga contradicciones internas y que la estrategia elegida sea la adecuada para el modelo de negocio detectado.

## Cuándo usarla
Usar de forma continua al cierre de cada bloque de fases y como validación final antes del resumen ejecutivo.

## Agente activador
`auditor_plan_marketing`

## Entradas necesarias
- `tipo_negocio` o `marketing_profile`.
- Documentos de las fases a auditar (Diagnóstico, Cliente, Propuesta, Canales, Acción, etc.).
- `oferta_principal` y `cliente_objetivo`.

## Proceso
1. Evaluar la coherencia estratégica: ¿El diagnóstico justifica al cliente elegido? ¿La propuesta resuelve el problema detectado?
2. Evaluar la coherencia operativa: ¿Los canales son los que usa el cliente objetivo? ¿El plan de acción es ejecutable por el equipo?
3. Evaluar la coherencia multimodelo: ¿El lenguaje y los KPIs son los correctos para el tipo de negocio (ej. no usar lenguaje de servicios en eCommerce)?
4. Separar los hallazgos en:
   - **Hecho confirmado**: Dato verificado en el plan.
   - **Hipótesis**: Suposición que requiere validación.
   - **Observación**: Sugerencia de mejora no crítica.
   - **Bloqueo**: Incoherencia grave que impide avanzar.
5. **Auditoría de Integridad**: Verificar que no se presenten supuestos como hechos, que los vacíos críticos no estén ocultos y que existan recomendaciones de validación claras.
6. **Auditoría de Privacidad**: Asegurar que los datos sensibles (márgenes, facturación cruda) no se expongan de forma que vulneren la seguridad del negocio.

## Adaptación por modelo de negocio
- **ecommerce_transaccional**: No aprobar si falta foco en conversión, checkout, ROAS/CPA o estrategia de recompra.
- **b2b_consultivo**: No aprobar si falta foco en autoridad, generación de confianza, reuniones o gestión del ciclo de venta largo.
- **b2b_producto_industrial**: No aprobar si falta foco en ficha técnica, homologación, red de distribución o confianza técnica.
- **retail_fisico**: No aprobar si falta foco en visibilidad local, tráfico a punto de venta, reseñas o radio de influencia geográfica.
- **educativo_formativo**: No aprobar si falta foco en captación de alumnos, prueba social de resultados o claridad del programa.
- **hibrido_producto_servicio**: No aprobar si se ignora la conexión entre la venta inicial y el soporte/mantenimiento recurrente.
- **b2c_local_servicios**: No aprobar si falta foco en sistema de reservas, reputación local, reseñas o rapidez de respuesta.

## Cuándo declarar insuficiencia
Debe declarar insuficiencia si:
- No se puede identificar el modelo de negocio base.
- Faltan evidencias o documentos clave para realizar el cruce de coherencia.
- El plan utiliza términos genéricos que ocultan la falta de estrategia real.
- Las contradicciones entre fases son tan graves que invalidan la viabilidad del plan.

## Criterios de bloqueo
- El canal elegido es imposible de usar por el cliente objetivo definido.
- El presupuesto es insuficiente para el objetivo marcado.
- La propuesta de valor no resuelve el problema identificado en el diagnóstico.

## Salida esperada
`docs/audits/auditoria_coherencia_nombre_proyecto.md`

## Gates relacionados
`gate_auditoria_final`

## Criterios de insuficiencia
La skill es insuficiente si se limita a una revisión gramatical sin entrar en la lógica comercial y operativa del modelo de negocio.

## Errores frecuentes
- Ser complaciente con incoherencias "menores" que luego rompen el plan.
- No detectar cuando un negocio de producto está siendo tratado como uno de servicios.

## Límites
No modifica el plan; solo emite el informe de auditoría y señala los puntos de corrección necesarios.

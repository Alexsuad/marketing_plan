# ADR-001: Implementación del Motor de Integridad de Datos (v1.6)

## Estado
Aceptado

## Contexto
Anteriormente, la validación de la integridad de los datos del brief estaba dispersa entre varios servicios (`brief_service.py`, `resumen_empresa_service.py`, `auditoria_service.py`). Esto generaba inconsistencias: un servicio podía considerar un dato como "faltante" mientras otro lo ignoraba o inventaba supuestos sin control. Además, no se diferenciaban correctamente los datos sensibles de los públicos.

## Decisión
Se implementa un motor determinista centralizado en `src/core/data_integrity.py` que rige todas las validaciones de datos del sistema basándose en la especificación v1.6.

### Puntos Clave:
1.  **Catálogo Único**: 34 campos normalizados con reglas de bloqueo, visibilidad y capacidad de hipótesis.
2.  **Estados de Datos**: Clasificación en: `confirmado`, `no_informado`, `no_aplicable`, `supuesto_pendiente_confirmar`, `sensible_uso_interno` y `visible_resumido`.
3.  **Lógica Multimodelo**: Los campos aplicables cambian dinámicamente según el perfil del negocio (eCommerce, Retail, B2B, etc.).
4.  **Gestión de Privacidad**: Los datos sensibles (`margen_bruto`, `desempeno_pasado`) tienen niveles de visibilidad para proteger la información del cliente en reportes finales.
5.  **Estados de Documento**: El motor devuelve estados claros: `Aprobado`, `Observaciones` (supuestos), `Condicionado` (vacíos operativos) o `Bloqueado` (datos críticos faltantes).

## Consecuencias
- **Positivas**: Centralización de la lógica, facilidad de auditoría, eliminación de alucinaciones (no se inventan datos sensibles), y coherencia total entre reportes.
- **Negativas**: Mayor rigidez inicial; añadir un nuevo campo al brief requiere actualizar el catálogo del motor.

## Reglas de Integridad v1.6
- **NO_INFORMADO != NO_APLICABLE**: Un dato que no aplica al modelo de negocio no debe reportarse como vacío.
- **Prohibido Inventar**: Datos como márgenes, recursos o restricciones NUNCA se inventan. Solo se permiten hipótesis en `presupuesto`, `ticket_promedio` y `ciclo_venta` marcándolos como supuestos.

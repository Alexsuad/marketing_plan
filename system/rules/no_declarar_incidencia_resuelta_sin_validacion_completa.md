<!--
# File: system/rules/no_declarar_incidencia_resuelta_sin_validacion_completa.md
# ──────────────────────────────────────────────────────────────────────
# Propósito: Garantizar la robustez de las soluciones técnicas.
# Rol: Regla operativa documental (no validador Python ejecutable).
# ──────────────────────────────────────────────────────────────────────
-->

# Rule: no_declarar_incidencia_resuelta_sin_validacion_completa

## 1. Propósito
Asegurar que la corrección de un error no introduzca regresiones en otros modelos de negocio o perfiles, garantizando la estabilidad global del sistema.

## 2. Cuándo aplica
Aplica tras la corrección de bugs críticos, incidencias de core o cambios en la lógica de resolución multimodelo.

## 3. Comportamiento Obligatorio
- Validar explícitamente **todos los perfiles afectados** por el cambio.
- Realizar al menos un **caso de regresión** de un perfil estable anterior que no debería haber sido afectado por el cambio.
- Ejecutar el pipeline completo (donde aplique) para confirmar que el flujo de datos no se rompe en fases posteriores.

## 4. Comportamiento Prohibido
- Cerrar una incidencia tras validar solo el caso específico que reportó el error, ignorando el impacto en el resto del sistema.

## 5. Ejemplos de aplicación
- **Correcto:** Tras arreglar el perfil Ecommerce, se valida el proyecto de Ecommerce Y se valida un proyecto B2B de Servicios (regresión) para asegurar que sigue funcionando.
- **Incorrecto:** "He arreglado el error en Ecommerce, ya podemos cerrar la tarea." (Sin probar otros modelos).

## 6. Evidencia esperada
- Informe de validación multimodelo o logs de ejecución de múltiples perfiles.

## 7. Estado de incumplimiento
`error_validacion_incompleta_de_incidencia`

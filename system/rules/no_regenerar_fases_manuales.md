<!--
# File: system/rules/no_regenerar_fases_manuales.md
# ──────────────────────────────────────────────────────────────────────
# Propósito: Proteger el trabajo manual del usuario en los documentos.
# Rol: Regla operativa documental (no validador Python ejecutable).
# ──────────────────────────────────────────────────────────────────────
-->

# Rule: no_regenerar_fases_manuales

## 1. Propósito
Evitar que el sistema sobrescriba documentos que han sido editados, refinados o congelados manualmente por el usuario, preservando la calidad final del entregable.

## 2. Cuándo aplica
Aplica antes de ejecutar cualquier comando de generación de output (`generate-*-output`) o skill de escritura.

## 3. Comportamiento Obligatorio
- Realizar una revisión documental del archivo de destino antes de escribir.
- Buscar las etiquetas `[CONGELADO]` o `[MANUAL]` en el encabezado, changelog o registro de auditoría del documento.
- Si existe la etiqueta, el agente **DEBE detenerse** y pedir permiso para crear una versión nueva (ej. `v2`) en lugar de sobrescribir.

## 4. Comportamiento Prohibido
- Sobrescribir un archivo que contenga marcas de edición manual sin advertencia previa.

## 5. Ejemplos de aplicación
- **Correcto:** "He detectado que `04_propuesta_valor.md` está marcado como `[MANUAL]`. No lo sobrescribiré; generaré la propuesta sugerida en un archivo separado para tu revisión."
- **Incorrecto:** (Ejecutar el comando de generación y borrar los ajustes que el usuario hizo ayer).

## 6. Evidencia esperada
- Verificación previa del estado del archivo en el log de acciones.

## 7. Estado de incumplimiento
`error_sobrescritura_trabajo_manual`

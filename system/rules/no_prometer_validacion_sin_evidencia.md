<!--
# File: system/rules/no_prometer_validacion_sin_evidencia.md
# ──────────────────────────────────────────────────────────────────────
# Propósito: Asegurar que las validaciones se basen en resultados tangibles.
# Rol: Regla operativa documental (no validador Python ejecutable).
# ──────────────────────────────────────────────────────────────────────
-->

# Rule: no_prometer_validacion_sin_evidencia

## 1. Propósito
Evitar que el agente declare el éxito de una tarea basándose únicamente en su propia generación, sin verificar los archivos resultantes o la ejecución técnica.

## 2. Cuándo aplica
Aplica al cierre de cada tarea, workflow o hito del sistema.

## 3. Comportamiento Obligatorio
- Citar la ruta exacta del archivo generado.
- Mostrar un fragmento o resumen del contenido real creado.
- Citar el resultado de ejecución (comando CLI) o el test que valida la acción.

## 4. Comportamiento Prohibido
- Decir "Tarea completada" sin adjuntar evidencia.
- Asumir que un archivo se guardó correctamente sin haber recibido confirmación de la herramienta de escritura.

## 5. Ejemplos de aplicación
- **Correcto:** "Fase 08 generada exitosamente en `projects/X/08_...md`. Se adjunta resumen del plan de acción."
- **Incorrecto:** "He terminado de pensar el plan de acción, todo está listo."

## 6. Evidencia esperada
- Lista de archivos creados/modificados al final del turno.
- Capturas de logs de terminal o resultados de tests.

## 7. Estado de incumplimiento
`error_cierre_sin_evidencia`

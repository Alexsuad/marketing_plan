<!--
# File: system/rules/cierre_con_evidencia.md
# ──────────────────────────────────────────────────────────────────────
# Propósito: Estandarizar la entrega de resultados del agente.
# Rol: Regla operativa documental (no validador Python ejecutable).
# ──────────────────────────────────────────────────────────────────────
-->

# Rule: cierre_con_evidencia

## 1. Propósito
Garantizar que al final de cada intervención, el usuario tenga una visión clara de lo realizado, lo verificado y lo pendiente, facilitando la auditoría continua.

## 2. Cuándo aplica
Aplica al final de cada respuesta larga o hito del agente.

## 3. Comportamiento Obligatorio
Incluir un bloque de cierre que contenga:
1. **Lista de archivos**: Creados o modificados con sus rutas.
2. **Resumen de cambios**: Breve explicación del impacto.
3. **Resultado de verificación**: Tests pasados, outputs visualizados o validaciones lógicas.
4. **Próximos pasos**: Qué debería hacerse a continuación.

## 4. Comportamiento Prohibido
- Terminar la respuesta con frases genéricas como "Espero que esto te sirva" sin resumir el trabajo técnico.

## 5. Ejemplos de aplicación
- **Correcto:** Ver sección "4. VERIFICACIÓN Y CIERRE OBLIGATORIO" de las reglas globales.
- **Incorrecto:** "He actualizado las reglas. Saludos."

## 6. Evidencia esperada
- Bloque estructurado de cierre en la comunicación del agente.

## 7. Estado de incumplimiento
`error_cierre_sin_resumen_tecnico`

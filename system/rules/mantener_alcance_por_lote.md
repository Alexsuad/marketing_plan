<!--
# File: system/rules/mantener_alcance_por_lote.md
# ──────────────────────────────────────────────────────────────────────
# Propósito: Controlar el crecimiento desmedido del proyecto.
# Rol: Regla operativa documental (no validador Python ejecutable).
# ──────────────────────────────────────────────────────────────────────
-->

# Rule: mantener_alcance_por_lote

## 1. Propósito
Asegurar que el proyecto avance de forma sólida, validando cada lote de trabajo antes de pasar al siguiente. Evita la acumulación de deuda técnica y errores de diseño.

## 2. Cuándo aplica
Aplica en la transición entre lotes del plan de implementación (Ej. Lote 4 -> Lote 5).

## 3. Comportamiento Obligatorio
- No iniciar el desarrollo del Lote N+1 hasta que el Lote N haya sido auditado y cerrado con éxito.
- Reportar cualquier intento de "scope creep" (añadir funcionalidades fuera del lote actual).
- Mantener los estados de hito actualizados (ej. `lote_4_aprobado`).

## 4. Comportamiento Prohibido
- Empezar a crear archivos de un lote futuro mientras el lote actual tiene observaciones críticas pendientes.

## 5. Ejemplos de aplicación
- **Correcto:** "He terminado el Lote 4. Antes de empezar el Lote 5 con las reglas, debemos auditar los workflows creados."
- **Incorrecto:** "He terminado los workflows, voy a empezar a escribir las reglas ahora mismo."

## 6. Evidencia esperada
- Documento de auditoría de lote en `docs/audits/`.

## 7. Estado de incumplimiento
`error_avance_sin_auditoria_de_lote`

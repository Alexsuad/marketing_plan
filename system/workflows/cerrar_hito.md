# Workflow: cerrar_hito

**Propósito:** Consolidar un grupo de fases validadas y marcarlas como punto de control estable (checkpoint).
**Cuándo se usa:** Al completar bloques lógicos (ej: Bloque Estratégico, Bloque Operativo).
**Agente responsable:** `orquestador_plan_marketing`

---

## Componentes
- **Skills implicadas:** n/a.
- **Gates obligatorios:** `gate_cierre_hito`.
- **Comandos deterministas:** n/a (actualización de metadata).

---

## Pasos Operativos

1. **Verificación de Pre-requisitos:**
   - Confirmar que todas las fases del hito están en estado `validado`.
   - Verificar que no hay tareas pendientes en el log de auditoría.

2. **Cierre de Calidad:**
   - Activar `gate_cierre_hito`.
   - El agente genera un breve resumen de los logros del hito.

3. **Congelamiento de Versión:**
   - Actualizar el `project_config.json` aumentando la versión menor (ej: v1.0 -> v1.1).
   - Opcionalmente, mover una copia de los outputs actuales a una carpeta de `archive/vX.X/` dentro del proyecto.

---

## Control y Salida
- **Archivos que puede tocar:** `project_config.json`, carpeta `archive/` del proyecto.
- **Archivos que no debe tocar:** `src/`, `project_template/`.
- **Evidencia requerida:** Cambio de versión en la metadata del proyecto.
- **Salida esperada:** Hito cerrado y versionado.
- **Estados finales posibles:**
  - `workflow_completado`
  - `workflow_error_operativo`

---

> [!NOTE]
> Cerrar un hito protege el trabajo realizado contra cambios accidentales masivos.

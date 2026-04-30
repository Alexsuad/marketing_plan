# Workflow: ajustar_fase_con_control_de_cambio

**Propósito:** Gestionar las iteraciones y cambios solicitados por el usuario de forma controlada y coherente.
**Cuándo se usa:** Cuando una revisión falla o el usuario solicita cambios en una fase ya generada.
**Agente responsable:** `orquestador_plan_marketing`

---

## Componentes
- **Skills implicadas:** `skill_change_request`.
- **Gates obligatorios:** 
  - `gate_impacto_cambio`.
  - `gate_no_regeneracion_fases_manuales` (antes de aplicar cambios).
- **Comandos deterministas:** n/a (re-ejecución de comandos de generación tras ajuste).

---

## Pasos Operativos

1. **Recepción del Cambio:**
   - El agente usa `skill_change_request` para documentar la solicitud del usuario.
   - Analiza qué documentos se ven afectados.

2. **Evaluación de Impacto:**
   - Activar `gate_impacto_cambio`.
   - Si el impacto es **ALTO** (cambia la oferta base o el cliente): se debe avisar al usuario que las fases posteriores quedarán obsoletas.
   - Obtener aprobación del usuario para proceder.

3. **Protección de Trabajo Manual:**
   - Invocar `gate_no_regeneracion_fases_manuales`.
   - Si el documento a cambiar fue ajustado a mano, el agente debe proponer los cambios en un archivo temporal en lugar de sobrescribir directamente.

4. **Aplicación del Ajuste:**
   - Corregir el prompt de la fase o el archivo de contexto.
   - Re-ejecutar el workflow `generar_fase.md` para actualizar el output.

---

## Control y Salida
- **Archivos que puede tocar:** Contexto del proyecto, prompts, outputs de fase.
- **Archivos que no debe tocar:** `src/`, `system/gates/`.
- **Evidencia requerida:** Registro en `audit_trail` (si existe) o log de cambios.
- **Salida esperada:** Fase actualizada y coherente con el cambio.
- **Estados finales posibles:**
  - `workflow_completado`
  - `workflow_pendiente_aprobacion_usuario`
  - `workflow_bloqueado_por_gate`

---

> [!WARNING]
> Un cambio de impacto ALTO en la Fase 01 (Brief) obliga a invalidar todos los outputs posteriores.

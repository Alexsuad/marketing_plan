# Workflow: revisar_fase

**Propósito:** Auditar la calidad estratégica y coherencia de una fase antes de darla por cerrada.
**Cuándo se usa:** Inmediatamente después de `generar_fase.md`.
**Agente responsable:** `auditor_plan_marketing`

---

## Componentes
- **Skills implicadas:** `skill_auditoria_coherencia`.
- **Gates obligatorios:** (Según la fase revisada):
  - Fase 06 (Canales) → `gate_canales_justificados`
  - Fase 09 (Presupuesto) → `gate_presupuesto_prudente`
  - Fase 10 (KPIs) → `gate_kpis_medibles`
  - Fase 12 (Auditoría Final) → `gate_auditoria_final`
  - *Otras fases:* `gate_coherencia_cliente_propuesta` (fases 03-04).

---

## Pasos Operativos

1. **Lectura Crítica:**
   - El Auditor lee el output generado.
   - Contrasta con el Brief Validado y las lecciones aprendidas.

2. **Aplicación de Gates Específicos:**
   - Activar el gate correspondiente a la fase (ver lista arriba).
   - Verificar criterios de aprobación y bloqueo del gate.

3. **Veredicto:**
   - Si el gate aprueba: El workflow termina en `workflow_completado`.
   - Si el gate bloquea o pide cambios: El workflow termina en `workflow_bloqueado_por_gate` y se activa el flujo de ajuste.

---

## Control y Salida
- **Archivos que puede tocar:** `docs/audits/` (informes de auditoría), `project_config.json` (estado de fase).
- **Archivos que no debe tocar:** Los documentos originales de la fase (solo los lee).
- **Evidencia requerida:** Informe de auditoría con veredicto claro.
- **Salida esperada:** Fase validada o lista de observaciones.
- **Estados finales posibles:**
  - `workflow_completado`
  - `workflow_bloqueado_por_gate`
  - `workflow_pendiente_aprobacion_usuario`

---

> [!TIP]
> La revisión no es opcional. Ninguna fase se considera "cerrada" sin pasar por este workflow.

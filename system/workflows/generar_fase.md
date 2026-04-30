# Workflow: generar_fase

**Propósito:** Producir el contenido estratégico de una fase específica del Plan de Marketing.
**Cuándo se usa:** Cuando la fase anterior está validada y el brief está completo.
**Agente responsable:** `orquestador_plan_marketing` (con el agente ejecutor correspondiente).

---

## Componentes
- **Skills implicadas:** Según la fase (ej: `skill_diagnostico_marketing`, `skill_matriz_canales`).
- **Gates obligatorios:** 
  - `gate_no_invencion` (siempre).
  - `gate_no_regeneracion_fases_manuales` (antes de escribir).
- **Comandos deterministas:** `uv run python -m src.main generate-[fase]-output --name "[Nombre]"`

---

## Pasos Operativos

1. **Pre-validación de Integridad:**
   - Invocar `gate_no_regeneracion_fases_manuales`. 
   - Si el archivo de salida ya existe y tiene una marca de "ajuste manual" o "congelado", el workflow se detiene.

2. **Ejecución de la Skill:**
   - El agente ejecutor (ej: `estratega_marketing`) utiliza la skill de la fase.
   - Entradas: Brief validado + outputs de fases previas necesarias.

3. **Control de No Invención:**
   - Aplicar `gate_no_invencion` sobre el borrador generado.
   - Si se detectan datos inventados, el agente debe marcar la información como "pendiente de confirmar" o pedir datos.

4. **Generación del Output:**
   - Ejecutar el comando CLI correspondiente para materializar el archivo en `outputs/plan_actual/`.

---

## Control y Salida
- **Archivos que puede tocar:** `projects/[nombre]/outputs/plan_actual/XX_[fase].md`.
- **Archivos que no debe tocar:** Fases ya validadas y cerradas, `src/`.
- **Evidencia requerida:** Logs del gate de no invención y existencia del archivo.
- **Salida esperada:** Documento de fase generado.
- **Estados finales posibles:**
  - `workflow_completado`
  - `workflow_bloqueado_por_gate`
  - `workflow_pendiente_validacion`

---

> [!CAUTION]
> No sobrescribir archivos sin verificar el gate de no regeneración manual.

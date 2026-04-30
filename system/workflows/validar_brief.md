# Workflow: validar_brief

**Propósito:** Garantizar que el negocio ha proporcionado la información mínima necesaria para una estrategia coherente.
**Cuándo se usa:** Después del intake inicial y antes de generar cualquier fase estratégica.
**Agente responsable:** `orquestador_plan_marketing`

---

## Componentes
- **Skills implicadas:** `skill_intake_brief`.
- **Gates obligatorios:** `gate_brief_minimo`.
- **Comandos deterministas:**
  - `uv run python -m src.main validate-brief --name "[Nombre]"`
  - `uv run python -m src.main generate-brief-output --name "[Nombre]"`

---

## Pasos Operativos

1. **Lectura de Datos:**
   - El agente lee el archivo `projects/[nombre]/context/brief_negocio.md`.
   - Utiliza `skill_intake_brief` para organizar y detectar vacíos.

2. **Validación Técnica:**
   - Ejecutar `validate-brief` para verificar campos obligatorios (nombre, tipo, oferta, cliente, problema, objetivo).
   - Si falla: reportar campos faltantes y pedir información al usuario.

3. **Cierre de Brief:**
   - Una vez validado, ejecutar `generate-brief-output` para crear `outputs/plan_actual/01_brief_negocio_validado.md`.
   - Activar el `gate_brief_minimo` como evidencia de hito cumplido.

---

## Control y Salida
- **Archivos que puede tocar:** `projects/[nombre]/outputs/plan_actual/01_brief_negocio_validado.md`, `project_config.json`.
- **Archivos que no debe tocar:** `project_template/`, `src/`.
- **Evidencia requerida:** Resultado de `validate-brief` y existencia del output 01.
- **Salida esperada:** Brief formal validado.
- **Estados finales posibles:**
  - `workflow_completado`
  - `workflow_bloqueado_por_falta_de_datos`
  - `workflow_error_operativo`

---

> [!IMPORTANT]
> Prohibido avanzar a fases estratégicas (diagnóstico, canales, etc.) si este workflow no termina en `workflow_completado`.

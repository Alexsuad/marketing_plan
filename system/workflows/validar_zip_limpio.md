# Workflow: validar_zip_limpio

**Propósito:** Asegurar que el ZIP generado está completo, íntegro y cumple con los estándares del modo elegido.
**Cuándo se usa:** Inmediatamente después de `crear_zip_limpio.md` (indicando si es Modo A o Modo B).
**Agente responsable:** `auditor_plan_marketing`

---

## Componentes
- **Skills implicadas:** n/a.
- **Gates obligatorios:** n/a.
- **Comandos deterministas:** n/a (verificación de contenido).

---

## Pasos Operativos

1. **Identificar modo del ZIP:**
   - Confirmar si el ZIP es **Modo A (cliente/proyecto)** o **Modo B (base sistema v1.1)**.

2. **Verificación de Estructura Interna (según modo):**
   - Abrir el ZIP (o listar contenido).
   - **Modo A — Obligatorio:**
     - Comprobar que existe el Brief Validado y el `project_config.json`.
     - Comprobar que el número de archivos en `outputs/` coincide con las fases completadas.
     - *(No exigir `.claude/skills/` en este modo.)*
   - **Modo B — Obligatorio:**
     - Comprobar que existe `.claude/skills/` dentro del ZIP.
     - Comprobar que existen los componentes base esperados (p. ej. `src/`, `system/`, `agents/`, `project_template/`, `pyproject.toml`, `uv.lock`).

3. **Control de Limpieza (ambos modos):**
   - Verificar que **NO** existe `projects/` dentro del ZIP.
   - Verificar que **NO** existe `docs/archive/` dentro del ZIP.
   - Verificar que **NO** hay archivos `*.zip` dentro del ZIP (no arrastrar ZIPs previos).
   - Verificar que **NO** existe `.venv/` dentro del ZIP.
   - Verificar que **NO** existe `__pycache__/` dentro del ZIP.
   - Verificar que **NO** existe `.git/` dentro del ZIP.
   - Verificar que **NO** existe `test_clean_sandbox/` dentro del ZIP.
   - Verificar que **NO** existe `.pytest_cache/` dentro del ZIP.
   - Verificar que **NO** hay archivos `*.log` dentro del ZIP.
   - Verificar que **NO** hay `.env`, secretos, claves API o credenciales dentro del ZIP.

4. **Veredicto Final:**
   - Si todo es correcto: marcar el ZIP como "Validado para entrega".
   - Si falta algo: invalidar el ZIP y pedir re-generación.

---

## Control y Salida
- **Archivos que puede tocar:** Metadata del ZIP (comentarios).
- **Archivos que no debe tocar:** Contenido del ZIP (solo lectura).
- **Evidencia requerida:** Checklist de validación completado.
- **Salida esperada:** ZIP validado.
- **Estados finales posibles:**
  - `workflow_completado`
  - `workflow_error_operativo`
  - `workflow_pendiente_validacion`

---

> [!CAUTION]
> No entregar nunca un ZIP que no haya pasado por este workflow de validación.

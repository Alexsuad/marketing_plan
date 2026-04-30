# Workflow: crear_zip_limpio

**Propósito:** Generar un archivo comprimido “limpio”, evitando ruido técnico y datos no distribuibles.
**Cuándo se usa:** Cuando se necesita empaquetar un proyecto para entrega, o preparar un ZIP base del sistema.
**Agente responsable:** `orquestador_plan_marketing`

---

## Componentes
- **Skills implicadas:** n/a.
- **Gates obligatorios:** n/a.
- **Comandos deterministas:** (Script de backup/zip externo si existe, o comando manual).

---

## Pasos Operativos

1. **Elegir modo de ZIP:**
   - **Modo A — ZIP de entrega de cliente/proyecto:** contiene entregables + contexto mínimo del proyecto.
   - **Modo B — ZIP base del sistema v1.1:** contiene el repositorio base distribuible (sin banco local ni históricos internos).

2. **Selección de Contenido (según modo):**
   - **Modo A — Incluir (Obligatorio):**
     - `outputs/plan_actual/`
     - `context/brief_negocio.md`
     - `project_config.json`
     - *(No exigir `.claude/skills/` en este modo.)*
   - **Modo B — Incluir (Obligatorio):**
     - `src/`
     - `tests/`
     - `project_template/`
     - `docs/` (solo documentación necesaria para uso del sistema)
     - `agents/`
     - `system/`
     - `.claude/skills/`
     - `README.md`
     - `AGENTS.md`
     - `pyproject.toml`
     - `uv.lock`
   - **Ambos modos — Excluir (Obligatorio):**
     - `projects/`
     - `docs/archive/`
     - `*.zip`
     - `.venv/`
     - `__pycache__/`
     - `.git/`
     - `test_clean_sandbox/`
     - `.pytest_cache/`
     - `*.log`
     - `.env`
     - Secretos o claves API (cualquier archivo o variable que los contenga)
     - Archivos temporales del sistema (.DS_Store, thumbs.db, etc.)

3. **Compresión:**
   - Crear el archivo ZIP siguiendo la nomenclatura del modo:
     - **Modo A:** `[FECHA]_[PROYECTO]_v[VERSION]_CLIENTE_CLEAN.zip`
     - **Modo B:** `[FECHA]_marketing_plan_base_v[VERSION]_SISTEMA_CLEAN.zip`

4. **Registro:**
   - **Modo A:** anotar la creación del ZIP en el log del proyecto.
   - **Modo B:** anotar la creación del ZIP en el registro de hitos del sistema.

---

## Control y Salida
- **Archivos que puede tocar:** Carpeta raíz del proyecto (para guardar el ZIP).
- **Archivos que no debe tocar:** `src/`, `system/`.
- **Evidencia requerida:** Existencia del archivo ZIP.
- **Salida esperada:** Archivo ZIP listo para entrega.
- **Estados finales posibles:**
  - `workflow_completado`
  - `workflow_error_operativo`

---

> [!TIP]
> Un ZIP limpio facilita la revisión por parte de humanos que no necesitan ver el "detrás de escena" técnico.

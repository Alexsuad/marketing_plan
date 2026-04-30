# Workflow: crear_zip_limpio

**Propósito:** Generar un archivo comprimido que contenga solo los entregables finales y el contexto necesario, eliminando "ruido" técnico.
**Cuándo se usa:** Para entregas a clientes o backups de hito.
**Agente responsable:** `orquestador_plan_marketing`

---

## Componentes
- **Skills implicadas:** n/a.
- **Gates obligatorios:** n/a.
- **Comandos deterministas:** (Script de backup/zip externo si existe, o comando manual).

---

## Pasos Operativos

1. **Selección de Contenido:**
   - **Incluir:** `outputs/plan_actual/`, `context/brief_negocio.md`, `project_config.json`.
   - **Excluir (Obligatorio):**
     - `projects/` (otros proyectos)
     - `.git/` (historial de git)
     - `.venv/` (entorno virtual)
     - `__pycache__/` (cache de python)
     - `docs/archive/` (versiones obsoletas)
     - `test_clean_sandbox/` (entorno de pruebas)
     - Archivos `.zip` previos
     - Archivos temporales del sistema (.DS_Store, thumbs.db, etc.)
     - Logs y memorias de IA pesadas

2. **Compresión:**
   - Crear el archivo ZIP siguiendo la nomenclatura: `[FECHA]_[PROYECTO]_v[VERSION]_CLEAN.zip`.

3. **Registro:**
   - Anotar la creación del ZIP en el log del proyecto.

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

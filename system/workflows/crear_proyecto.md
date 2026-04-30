# Workflow: crear_proyecto

**Propósito:** Iniciar un nuevo proyecto de Plan de Marketing asegurando que la infraestructura base es sólida.
**Cuándo se usa:** Al inicio de cualquier colaboración con un nuevo negocio.
**Agente responsable:** `orquestador_plan_marketing`

---

## Componentes
- **Skills implicadas:** n/a (operación determinista inicial).
- **Gates obligatorios:** n/a (previo al brief).
- **Comandos deterministas:**
  - `uv run python -m src.main validate-base-structure`
  - `uv run python -m src.main create-project --name "[Nombre]"`

---

## Pasos Operativos

1. **Validación de Entorno:**
   - Ejecutar `validate-base-structure` para confirmar que `project_template/` está íntegro.
   - Si falla: detener y corregir la plantilla antes de continuar.

2. **Instanciación:**
   - Ejecutar `create-project` con el nombre del negocio (en `snake_case` o con espacios).
   - Verificar la creación de la carpeta en `projects/`.

3. **Verificación de Estructura:**
   - Ejecutar `uv run python -m src.main validate-project --name "[Nombre]"` para asegurar que la copia fue correcta.

---

## Control y Salida
- **Archivos que puede tocar:** `projects/[nombre]/**`, `project_config.json` del nuevo proyecto.
- **Archivos que no debe tocar:** `src/`, `project_template/`, `system/`.
- **Evidencia requerida:** Logs de creación exitosa.
- **Salida esperada:** Carpeta de proyecto con estructura lista para el intake.
- **Estados finales posibles:**
  - `workflow_completado`
  - `workflow_error_operativo`

---

> [!NOTE]
> Este workflow es una especificación operativa documental. Su automatización total queda pendiente para fases posteriores.

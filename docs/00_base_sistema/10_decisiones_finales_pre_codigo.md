# File: docs/00_base_sistema/10_decisiones_finales_pre_codigo.md
# ──────────────────────────────────────────────────────────────────────
# Propósito: Registrar las decisiones técnicas y operativas finales antes de iniciar la programación.
# Rol: Documento de cierre de la fase de planificación (Definition of Ready).
# ──────────────────────────────────────────────────────────────────────

# 10 - Decisiones Finales Pre-Código

## 1. Convención de Nomenclatura de Carpetas
Se establece un modelo mixto funcional:
- **Inglés** para carpetas técnicas y de sistema (para mayor limpieza en el entorno técnico y compatibilidad).
- **Español** para los nombres y contenidos de los documentos entregables del plan.

**Estructura Base:**
- `projects/` (Ignorada en Git - Banco local)
- `project_template/` (Núcleo Fijo)
- `workspace/` (Ignorada en Git - Taller variable)
  - `workspace/reports/`
  - `workspace/outputs/`
  - `workspace/inputs/`
  - `workspace/exports/`
- `context/` (Dentro de cada proyecto)
- `outputs/` (Dentro de cada proyecto)
- `logs/` (Dentro de cada proyecto)

## 2. Ubicación Definitiva de la Carpeta de Proyectos (`projects/`)
Para el MVP:
- La carpeta `projects/` vivirá **dentro del repositorio local** (para facilitar el desarrollo y portabilidad inicial).
- Estará **estrictamente ignorada en el archivo `.gitignore`** para asegurar que ningún dato real de cliente se suba al control de versiones.
- Queda establecida la previsión técnica de usar una variable de entorno (ej. `MARKETING_PROJECTS_ROOT`) en el futuro para permitir externalizar la carpeta si el sistema crece.

## 3. Contrato de Datos Mínimos (Brief)
Para que el sistema permita avanzar hacia el diagnóstico (Gate: `gate_brief_minimo`), el brief inicial debe contener obligatoriamente los siguientes campos:

| Campo | Obligatorio | Tipo | Ejemplo | Fase donde se usa | Acción si falta |
| :--- | :---: | :--- | :--- | :--- | :--- |
| `nombre_negocio` | Sí | Texto | "Taller Norte" | Brief / Todas | **Bloquea** |
| `tipo_negocio` | Sí | Texto | "Servicios logísticos B2B" | Brief / Diagnóstico | **Bloquea** |
| `oferta_principal` | Sí | Texto | "Mantenimiento industrial" | Brief / Propuesta | **Bloquea** |
| `cliente_objetivo` | Sí | Texto | "Pymes industriales" | Cliente / Canales | **Bloquea** |
| `problema_que_resuelve` | Sí | Texto | "Falta de control operativo en almacenes" | Brief / Propuesta | **Bloquea** |
| `objetivo_principal` | Sí | Texto | "Captar 5 clientes B2B/mes" | Diagnóstico / KPIs | **Bloquea** |
| `presupuesto_marketing`| No | Número/Rango | "300 €/mes" | Plan / Presupuesto | Observación |

## 4. Forma de Operación IA + Python en MVP (Modo Manual-Asistido)
La interacción entre el motor determinista y la generación agentica operará de la siguiente forma en esta primera versión:
1. **Python (Determinismo):** Se encarga de la orquestación. Crea la estructura del proyecto, valida estructura, existencia de archivos y campos mínimos. Gestiona el versionado y el changelog de forma rígida.
2. **IA (Antigravity):** Asiste de forma manual en la generación de contenido. La IA y el auditor apoyan la validación cualitativa de gates.
3. **Flujo de Validación:** Una vez que la IA o el usuario depositan el documento generado en su ruta correspondiente, Python evalúa el resultado de forma determinista para aprobar el avance de fase.

## 5. Primer Comando y Siguiente Paso Técnico
El primer bloque de implementación técnica será la **creación de un proyecto limpio**.
Esto valida la regla más importante de la arquitectura: la capacidad de instanciar un entorno de trabajo aislado a partir de la plantilla base.

**Primer comando esperado (Ejemplo):**
`uv run python -m src.main create-project --name "Mi Proyecto"`

**Próximos pasos inmediatos:**
1. Inicializar el proyecto con `uv` (creando `pyproject.toml` y `.venv`).
2. Configurar el `.gitignore` base.
3. Crear la estructura inicial de directorios (`src/`, `src/config/`, `src/core/`, `src/services/`, `src/validators/`, `src/utils/`, `project_template/`).
4. Implementar la lógica de `create_project()` del primer comando para copiar la plantilla a `projects/`.

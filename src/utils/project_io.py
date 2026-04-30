# File: src/utils/project_io.py
# ──────────────────────────────────────────────────────────────────────
# Propósito: Utilidades para gestionar rutas y existencia de archivos del proyecto.
# Rol: Funciones transversales de manejo de rutas.
# ──────────────────────────────────────────────────────────────────────

import os
from src.config.paths import PROJECTS_DIR
from src.utils.text_utils import slugify

def get_project_path(project_name: str) -> str:
    """Retorna la ruta raíz del proyecto basado en su nombre."""
    slug = slugify(project_name)
    return os.path.join(PROJECTS_DIR, slug)

def get_context_path(project_name: str) -> str:
    """Retorna la ruta de la carpeta context del proyecto."""
    return os.path.join(get_project_path(project_name), "context")

def get_plan_actual_path(project_name: str) -> str:
    """Retorna la ruta de la carpeta plan_actual del proyecto."""
    return os.path.join(get_project_path(project_name), "outputs", "plan_actual")

def ensure_file_exists(file_path: str, error_message: str) -> None:
    """Verifica si un archivo existe, si no, lanza FileNotFoundError con el mensaje."""
    if not os.path.exists(file_path):
        raise FileNotFoundError(error_message)

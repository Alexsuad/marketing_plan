# File: src/core/project_manager.py
# ──────────────────────────────────────────────────────────────────────
# Propósito: Gestionar la creación y el estado general de los proyectos.
# Rol: Lógica de negocio (Core)
# ──────────────────────────────────────────────────────────────────────

import os
import shutil
import json
import uuid
from datetime import datetime
from src.utils.text_utils import slugify
from src.config.paths import PROJECTS_DIR, PROJECT_TEMPLATE_DIR

def create_project(project_name: str) -> str:
    """
    Crea un nuevo proyecto copiando la plantilla base.
    Retorna la ruta del proyecto creado o lanza una excepción si ya existe.
    """
    slug = slugify(project_name)
    if not slug:
        raise ValueError("El nombre del proyecto no es válido.")
        
    project_path = os.path.join(PROJECTS_DIR, slug)
    
    if os.path.exists(project_path):
        raise FileExistsError(f"El proyecto '{slug}' ya existe en {project_path}")
        
    if not os.path.exists(PROJECT_TEMPLATE_DIR):
        raise FileNotFoundError(f"No se encuentra la plantilla base en {PROJECT_TEMPLATE_DIR}")
        
    # Asegurar que el directorio contenedor exista
    os.makedirs(PROJECTS_DIR, exist_ok=True)
        
    # Copiar plantilla
    shutil.copytree(PROJECT_TEMPLATE_DIR, project_path)
    
    # Actualizar configuración del proyecto
    config_path = os.path.join(project_path, "project_config.json")
    if os.path.exists(config_path):
        with open(config_path, "r", encoding="utf-8") as f:
            config = json.load(f)
            
        config["project_id"] = str(uuid.uuid4())
        config["project_name"] = project_name
        config["created_at"] = datetime.now().isoformat()
        config["status"] = "active"
        
        with open(config_path, "w", encoding="utf-8") as f:
            json.dump(config, f, indent=4, ensure_ascii=False)
            
    return project_path

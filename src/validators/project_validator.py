# File: src/validators/project_validator.py
import os
from src.config.paths import PROJECTS_DIR
from src.utils.text_utils import slugify

def validate_project(project_name: str) -> list[str]:
    errors = []
    slug = slugify(project_name)
    project_path = os.path.join(PROJECTS_DIR, slug)
    
    if not os.path.exists(project_path):
        errors.append(f"No existe el proyecto: {slug}")
        return errors
        
    required_dirs = [
        "context",
        "outputs/plan_actual",
        "outputs/versions",
        "outputs/changelog",
        "outputs/audits",
        "logs"
    ]
    for d in required_dirs:
        path = os.path.join(project_path, d)
        if not os.path.exists(path):
            errors.append(f"Falta directorio en proyecto: {d}")
            
    if not os.path.exists(os.path.join(project_path, "project_config.json")):
        errors.append("Falta project_config.json en el proyecto")
        
    return errors

# File: src/validators/structure_validator.py
import os
from src.config.paths import PROJECT_TEMPLATE_DIR

def validate_base_structure() -> list[str]:
    errors = []
    if not os.path.exists(PROJECT_TEMPLATE_DIR):
        errors.append(f"No existe la plantilla base: {PROJECT_TEMPLATE_DIR}")
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
        path = os.path.join(PROJECT_TEMPLATE_DIR, d)
        if not os.path.exists(path):
            errors.append(f"Falta directorio base en plantilla: {d}")
            
    return errors

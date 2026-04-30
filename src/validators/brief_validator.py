# File: src/validators/brief_validator.py
# ──────────────────────────────────────────────────────────────────────
# Propósito: Validar que el brief del negocio cumpla con los requisitos mínimos.
# Rol: Validador de negocio (Gate)
# ──────────────────────────────────────────────────────────────────────

import os
import re
from src.config.paths import PROJECTS_DIR
from src.utils.text_utils import slugify

def validate_brief(project_name: str) -> list[str]:
    errors = []
    slug = slugify(project_name)
    brief_path = os.path.join(PROJECTS_DIR, slug, "context", "brief_negocio.md")
    
    if not os.path.exists(brief_path):
        errors.append(f"No existe el archivo de brief: {brief_path}")
        return errors
        
    with open(brief_path, "r", encoding="utf-8") as f:
        content = f.read()
        
    data = {}
    lines = content.split('\n')
    for line in lines:
        match = re.match(r'-\s*\*\*(.+?):\*\*\s*(.*)', line)
        if match:
            key = match.group(1).strip()
            value = match.group(2).strip()
            data[key] = value
            
    mandatory_fields = [
        "nombre_negocio",
        "tipo_negocio",
        "oferta_principal",
        "cliente_objetivo",
        "problema_que_resuelve",
        "objetivo_principal",
        "zona_geografica"
    ]
    
    default_values = ["[Completar]", "", "[]", "none", "n/a", "null"]
    
    for field in mandatory_fields:
        if field not in data:
            errors.append(f"Falta el campo obligatorio: {field}")
        else:
            val = data[field].strip()
            if not val or val.lower() in default_values:
                errors.append(f"El campo obligatorio '{field}' está vacío o tiene valor por defecto.")
                
    return errors

# File: src/utils/markdown_utils.py
# ──────────────────────────────────────────────────────────────────────
# Propósito: Utilidades para leer, escribir y parsear archivos Markdown.
# Rol: Funciones transversales de I/O de texto.
# ──────────────────────────────────────────────────────────────────────

import os
import re

def read_markdown_file(file_path: str) -> str:
    """Lee el contenido de un archivo Markdown."""
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"El archivo no existe: {file_path}")
    with open(file_path, "r", encoding="utf-8") as f:
        return f.read()

def write_markdown_file(file_path: str, content: str) -> None:
    """Escribe contenido en un archivo Markdown, creando directorios si es necesario."""
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content)

def extract_markdown_field(content: str, field_name: str) -> str | None:
    """
    Busca un campo en formato de lista Markdown con negrita:
    - **campo:** valor
    Retorna el valor limpio o None si no lo encuentra.
    """
    match = re.search(r'-\s*\*\*' + re.escape(field_name) + r':\*\*\s*(.*)', content)
    if match:
        return match.group(1).strip()
    return None

def extract_brief_fields(content: str) -> dict:
    """
    Extrae todos los campos en formato '- **clave:** valor' de un brief.
    Retorna un diccionario con las claves y valores encontrados.
    """
    data = {}
    lines = content.split('\n')
    for line in lines:
        match = re.match(r'-\s*\*\*(.+?):\*\*\s*(.*)', line)
        if match:
            key = match.group(1).strip()
            value = match.group(2).strip()
            data[key] = value
    return data

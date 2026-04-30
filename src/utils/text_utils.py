# File: src/utils/text_utils.py
# ──────────────────────────────────────────────────────────────────────
# Propósito: Utilidades para manejo de texto (nombres, slugs).
# Rol: Auxiliar
# ──────────────────────────────────────────────────────────────────────

import re
import unicodedata

def slugify(text: str) -> str:
    """Convierte un texto a un formato seguro para nombres de carpeta (slug)."""
    text = unicodedata.normalize('NFKD', text).encode('ASCII', 'ignore').decode('utf-8')
    text = text.lower()
    text = re.sub(r'[^a-z0-9]+', '_', text)
    return text.strip('_')

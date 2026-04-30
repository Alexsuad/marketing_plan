# File: src/services/brief_service.py
# ──────────────────────────────────────────────────────────────────────
# Propósito: Validar y generar el documento formal de brief del negocio.
# Rol: Servicio de validación y generación inicial (Fase 01).
# ──────────────────────────────────────────────────────────────────────

import os
from src.validators.brief_validator import validate_brief
from src.utils.markdown_utils import read_markdown_file, write_markdown_file, extract_brief_fields
from src.utils.project_io import get_context_path, get_plan_actual_path

def generate_validated_brief(project_name: str) -> str:
    """
    Lee el brief de contexto, lo valida y genera el output formal en plan_actual.
    Retorna la ruta del archivo generado.
    """
    # 1. Validar primero
    errors = validate_brief(project_name)
    if errors:
        raise ValueError(f"No se puede generar el output: el brief tiene {len(errors)} errores de validación.")

    context_dir = get_context_path(project_name)
    context_path = os.path.join(context_dir, "brief_negocio.md")
    output_dir = get_plan_actual_path(project_name)
    output_file = os.path.join(output_dir, "01_brief_negocio_validado.md")

    # 2. Leer datos del brief
    content = read_markdown_file(context_path)
    data = extract_brief_fields(content)

    # 3. Construir el contenido del output formal
    output_content = f"""# 01 - Brief de Negocio Validado

## Estado del brief
aprobado_estructuralmente

## Datos principales
- **nombre_negocio:** {data.get('nombre_negocio', 'N/A')}
- **tipo_negocio:** {data.get('tipo_negocio', 'N/A')}
- **oferta_principal:** {data.get('oferta_principal', 'N/A')}
- **cliente_objetivo:** {data.get('cliente_objetivo', 'N/A')}
- **problema_que_resuelve:** {data.get('problema_que_resuelve', 'N/A')}
- **objetivo_principal:** {data.get('objetivo_principal', 'N/A')}
- **presupuesto_marketing:** {data.get('presupuesto_marketing', 'Opcional')}
- **canales_actuales:** {data.get('canales_actuales', 'No informados')}
- **ubicacion:** {data.get('ubicacion', 'No informada')}

## Campos obligatorios completados
- nombre_negocio
- tipo_negocio
- oferta_principal
- cliente_objetivo
- problema_que_resuelve
- objetivo_principal

## Hipótesis iniciales
- Pendiente validar si la oferta principal '{data.get('oferta_principal')}' tiene demanda suficiente en el segmento indicado.
- Pendiente validar si el cliente objetivo definido es el más adecuado para la oferta.
- Pendiente contrastar el problema declarado con señales reales del mercado.

## Notas adicionales
{data.get('notas_adicionales', 'No hay notas adicionales.')}

## Información faltante
- No falta información obligatoria para iniciar el diagnóstico.
- La validación estratégica del contenido queda pendiente para la Fase 02.

## Observaciones
- Validación de estructura mínima superada.
- Este documento no certifica la viabilidad comercial, solo la completitud de la información inicial.

## Siguiente fase sugerida
02_diagnostico_marketing
"""

    write_markdown_file(output_file, output_content)

    return output_file

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

    def get_val(key, default="No informado"):
        val = data.get(key, default)
        if not val or str(val).lower() in ["[recomendado]", "[opcional]", "[condicional]", "[completar]", "none", "n/a", "null"]:
            return default
        return val

    # 3. Construir el contenido del output formal
    output_content = f"""# 01 - Brief de Negocio Validado

## Estado del brief
aprobado_estructuralmente

## Datos principales
- **nombre_negocio:** {get_val('nombre_negocio')}
- **tipo_negocio:** {get_val('tipo_negocio')}
- **oferta_principal:** {get_val('oferta_principal')}
- **cliente_objetivo:** {get_val('cliente_objetivo')}
- **problema_que_resuelve:** {get_val('problema_que_resuelve')}
- **objetivo_principal:** {get_val('objetivo_principal')}
- **zona_geografica:** {get_val('zona_geografica')}

## Datos operativos recomendados
- **presupuesto_marketing:** {get_val('presupuesto_marketing')}
- **recursos_internos:** {get_val('recursos_internos')}
- **tiempo_disponible:** {get_val('tiempo_disponible')}
- **capacidad_operativa:** {get_val('capacidad_operativa')}
- **canales_actuales:** {get_val('canales_actuales')}
- **restricciones:** {get_val('restricciones')}

## Datos opcionales de contexto
- **competidores_conocidos:** {get_val('competidores_conocidos')}
- **activos_existentes:** {get_val('activos_existentes')}
- **herramientas_medicion:** {get_val('herramientas_medicion')}
- **desempeno_pasado:** {get_val('desempeno_pasado')}

## Datos condicionales por modelo
- **ticket_promedio:** {get_val('ticket_promedio')}
- **margen_bruto:** {get_val('margen_bruto')}
- **logistica:** {get_val('logistica')}
- **ciclo_venta:** {get_val('ciclo_venta')}
- **decisores_compra:** {get_val('decisores_compra')}
- **homologacion:** {get_val('homologacion')}
- **radio_influencia:** {get_val('radio_influencia')}
- **google_business_profile:** {get_val('google_business_profile')}
- **modalidad_formativa:** {get_val('modalidad_formativa')}
- **sistema_reservas:** {get_val('sistema_reservas')}
- **modelo_recurrencia:** {get_val('modelo_recurrencia')}

## Campos obligatorios completados
- nombre_negocio
- tipo_negocio
- oferta_principal
- cliente_objetivo
- problema_que_resuelve
- objetivo_principal
- zona_geografica

## Integridad de Datos
- **Datos confirmados usados:** Aquellos marcados en las secciones superiores sin el valor "No informado".
- **Supuestos aplicados:** Se utilizarán rangos prudentes para los campos "No informado" de la sección operativa.
- **Datos faltantes:** Ver campos marcados como "No informado" en secciones Operativa y Condicional.
- **Impacto del vacío:** La falta de datos operativos (recursos/tiempo) puede generar planes inalcanzables.
- **Recomendación de validación:** Se recomienda al cliente completar los campos "No informado" antes de la Fase 08.

## Hipótesis iniciales
- Pendiente validar si la oferta principal '{get_val('oferta_principal')}' tiene demanda suficiente en el segmento indicado.
- Pendiente validar si el cliente objetivo definido es el más adecuado para la oferta.
- Pendiente contrastar el problema declarado con señales reales del mercado.

## Observaciones
- Validación de estructura mínima superada bajo estándar multimodelo v1.2.
- Este documento no certifica la viabilidad comercial, solo la completitud de la información inicial.

## Siguiente fase sugerida
02_diagnostico_marketing
"""

    write_markdown_file(output_file, output_content)

    return output_file

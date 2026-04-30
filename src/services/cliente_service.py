# File: src/services/cliente_service.py
# ──────────────────────────────────────────────────────────────────────
# Propósito: Generar el documento de análisis de cliente y segmentos.
# Rol: Servicio de análisis de audiencia (Fase 03).
# ──────────────────────────────────────────────────────────────────────

import os
from src.utils.markdown_utils import read_markdown_file, write_markdown_file, extract_markdown_field
from src.utils.project_io import get_context_path, get_plan_actual_path, ensure_file_exists

def generate_cliente_output(project_name: str) -> str:
    """
    Genera el documento de Cliente Objetivo y Segmentos (Fase 03).
    Verifica que la Fase 02 esté completa.
    """
    output_dir = get_plan_actual_path(project_name)
    context_dir = get_context_path(project_name)
    
    # 1. Verificar Fase 02
    phase_02_path = os.path.join(output_dir, "02_diagnostico_marketing.md")
    ensure_file_exists(
        phase_02_path,
        f"No se puede generar la Fase 03. El archivo '{phase_02_path}' no existe. "
        "Primero debe ejecutar la Fase 02 (generate-diagnostico-output)."
    )

    # 2. Recopilar información de contexto
    
    data = {}
    found_files = []
    
    # Leer brief
    brief_path = os.path.join(context_dir, "brief_negocio.md")
    if os.path.exists(brief_path):
        found_files.append("brief_negocio.md")
        content = read_markdown_file(brief_path)
        obj = extract_markdown_field(content, "cliente_objetivo")
        prob = extract_markdown_field(content, "problema_que_resuelve")
        data["cliente_objetivo"] = obj if obj else "[No informado]"
        data["problema_que_resuelve"] = prob if prob else "[No informado]"

    # Revisar archivos de contexto opcionales
    for optional_file in ["cliente_objetivo.md", "contexto_mercado.md"]:
        path = os.path.join(context_dir, optional_file)
        if os.path.exists(path) and os.path.getsize(path) > 0:
            found_files.append(optional_file)

    # 3. Construir el documento de Fase 03
    cliente_objetivo = data.get("cliente_objetivo", "[No informado]")
    problema_principal = data.get("problema_que_resuelve", "[No informado]")
    
    output_content = f"""# 03 - Cliente Objetivo y Segmentos

## Estado del análisis
segmentacion_inicial_generada_con_informacion_limitada

## Base utilizada
- 01_brief_negocio_validado.md
- 02_diagnostico_marketing.md
- brief_negocio.md
"""
    for f in found_files:
        output_content += f"- {f}\n"

    output_content += f"""
## Cliente objetivo declarado
- '{cliente_objetivo}'

## Nivel de especificidad actual
El cliente objetivo está definido de forma general. Para un plan de marketing efectivo, se requiere dividir esta audiencia en segmentos más pequeños con necesidades específicas.

## Segmentos posibles
Basado en el problema de '{problema_principal}', se identifican los siguientes perfiles hipotéticos:
- Hipótesis Perfil A: Clientes con urgencia alta por resolver '{problema_principal}' debido a pérdidas económicas.
- Hipótesis Perfil B: Clientes que buscan una mejora preventiva y valoran el acompañamiento a largo plazo.
- Hipótesis Perfil C: Clientes con presupuestos limitados que buscan la solución mínima viable.

## Segmento prioritario inicial
Hipótesis inicial: Clientes dentro del grupo '{cliente_objetivo}' que sufren directamente el impacto de '{problema_principal}' y tienen capacidad de decisión inmediata.
Requiere validación con datos reales o entrevistas.

## Necesidades probables
- Hipótesis: Resolución eficiente y segura del problema '{problema_principal}'.
- Hipótesis: Claridad en el proceso y reducción de la incertidumbre técnica.
- Hipótesis: Soporte y acompañamiento durante la implementación.

## Dolores o problemas probables
- Frustración por la falta de una solución efectiva para '{problema_principal}'.
- Temor a costes ocultos o complicaciones inesperadas.
- Pérdida de tiempo o productividad derivada de no resolver el problema.

## Criterios de decisión posibles
- Hipótesis: Confianza en la capacidad de la oferta para resolver el problema.
- Hipótesis: Claridad en tiempos, costes y alcance de la solución.
- Hipótesis: Experiencia previa demostrable o prueba social.
- Hipótesis: Facilidad de adquisición o implementación.

## Objeciones probables
- Hipótesis: El coste percibido es mayor que el beneficio esperado.
- Hipótesis: Miedo al cambio o a la interrupción de procesos actuales.
- Hipótesis: Falta de confianza en la durabilidad de la solución.

## Información faltante para segmentar mejor
- Datos demográficos o geográficos específicos.
- Comportamiento de búsqueda (¿Cómo buscan soluciones para '{problema_principal}'?).
- Historial de intentos previos por resolver el problema.

## Recomendación para la siguiente fase
04_propuesta_valor_y_posicionamiento
"""

    output_file = os.path.join(output_dir, "03_cliente_objetivo_y_segmentos.md")
    
    write_markdown_file(output_file, output_content)
        
    return output_file

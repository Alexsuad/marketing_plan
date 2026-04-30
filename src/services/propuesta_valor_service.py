# File: src/services/propuesta_valor_service.py
# ──────────────────────────────────────────────────────────────────────
# Propósito: Generar el documento de propuesta de valor y posicionamiento.
# Rol: Servicio de definición estratégica (Fase 04).
# ──────────────────────────────────────────────────────────────────────

import os
import re
from src.utils.markdown_utils import read_markdown_file, write_markdown_file, extract_markdown_field
from src.utils.project_io import get_context_path, get_plan_actual_path, ensure_file_exists

def generate_propuesta_valor_output(project_name: str) -> str:
    """
    Genera el documento de Propuesta de Valor y Posicionamiento (Fase 04).
    Verifica que la Fase 03 esté completa.
    """
    output_dir = get_plan_actual_path(project_name)
    context_dir = get_context_path(project_name)
    
    # 1. Verificar Fase 03
    phase_03_path = os.path.join(output_dir, "03_cliente_objetivo_y_segmentos.md")
    ensure_file_exists(
        phase_03_path,
        f"No se puede generar la Fase 04. El archivo '{phase_03_path}' no existe. "
        "Primero debe ejecutar la Fase 03 (generate-cliente-output)."
    )

    # 2. Recopilar información de contexto y fases previas
    
    data = {}
    found_files = []
    
    # Leer brief
    brief_path = os.path.join(context_dir, "brief_negocio.md")
    brief_data = {}
    if os.path.exists(brief_path):
        found_files.append("brief_negocio.md")
        content = read_markdown_file(brief_path)
        from src.utils.markdown_utils import extract_brief_fields
        brief_data = extract_brief_fields(content)
        
        oferta = brief_data.get("oferta_principal")
        prob = brief_data.get("problema_que_resuelve")
        data["oferta_principal"] = oferta if oferta else "[No informado]"
        data["problema_que_resuelve"] = prob if prob else "[No informado]"

    # Resolver perfil de marketing
    from src.core.marketing_profile_resolver import resolve_marketing_profile
    profile = resolve_marketing_profile(brief_data)
    terminology = profile.get("terminology", {})
    tipo_oferta = terminology.get("oferta", "oferta")
    tipo_cliente = terminology.get("cliente", "cliente")
    accion_vincular = terminology.get("accion_principal", "contratar")

    # Adaptar enfoque según perfil (Servicio vs Producto)
    es_servicio = profile["marketing_profile"] in ["b2b_consultivo", "b2c_local_servicios", "hibrido_producto_servicio"]
    enfoque_valor = "Acompañamiento especializado" if es_servicio else f"Solución mediante {tipo_oferta}"
    verbo_gestion = "delegar la gestión en un experto" if es_servicio else f"adquirir una {tipo_oferta} fiable"

    # Leer Fase 03 para extraer segmentos y dolores
    phase_03_content = read_markdown_file(phase_03_path)
        
    def extract_section(content, header):
        pattern = fr'## {header}\n(.*?)(?=\n##|\Z)'
        match = re.search(pattern, content, re.DOTALL)
        return match.group(1).strip() if match else "No se encontró información."

    segmento_prioritario = extract_section(phase_03_content, "Segmento prioritario inicial")
    necesidades = extract_section(phase_03_content, "Necesidades probables")
    dolores = extract_section(phase_03_content, "Dolores o problemas probables")
    criterios = extract_section(phase_03_content, "Criterios de decisión posibles")
    objeciones = extract_section(phase_03_content, "Objeciones probables")

    # Revisar archivos de contexto opcionales
    for optional_file in ["oferta.md", "restricciones.md"]:
        path = os.path.join(context_dir, optional_file)
        if os.path.exists(path) and os.path.getsize(path) > 0:
            found_files.append(optional_file)

    # 3. Construir el documento de Fase 04
    oferta_principal = data.get("oferta_principal", "[No informado]")
    problema_principal = data.get("problema_que_resuelve", "[No informado]")

    output_content = f"""# 04 - Propuesta de Valor y Posicionamiento

## Estado del análisis
propuesta_valor_inicial_generada_con_informacion_limitada

## Base utilizada
- 01_brief_negocio_validado.md
- 02_diagnostico_marketing.md
- 03_cliente_objetivo_y_segmentos.md
- brief_negocio.md
"""
    for f in found_files:
        output_content += f"- {f}\n"

    output_content += f"""
## Segmento prioritario utilizado
{segmento_prioritario}

## Problema principal a resolver
{problema_principal}
Pendiente de validar si este es el dolor más agudo para el segmento prioritario.

## Necesidades y dolores considerados
{necesidades}
{dolores}

## Criterios de decisión considerados
{criterios}

## Objeciones consideradas
{objeciones}

## Propuesta de valor inicial
Hipótesis: {enfoque_valor} para resolver '{problema_principal}' mediante '{oferta_principal}', asegurando la eficiencia y satisfacción del {tipo_cliente}.

## Beneficios principales
- Hipótesis: Reducción de la incertidumbre en el proceso de obtención de '{oferta_principal}'.
- Hipótesis: Resolución efectiva del problema de '{problema_principal}'.
- Hipótesis: Ahorro de tiempo o recursos al {verbo_gestion}.

## Diferenciales posibles
- Hipótesis: Enfoque específico en el segmento declarado frente a alternativas genéricas.
- Hipótesis: Calidad en la entrega y bajo impacto en la operativa diaria.
- Hipótesis: Transparencia y confianza en el proceso.
Nota: No se cuenta todavía con evidencia suficiente para afirmar una diferenciación competitiva real.

## Razones para creer
- Evidencia disponible: La oferta de '{oferta_principal}' ataca directamente el problema '{problema_principal}'.
- Pendiente de validar: Casos de éxito, calidad técnica, trayectoria o garantías específicas.

## Posicionamiento inicial
La oferta se posiciona como una opción de 'fiabilidad y excelencia' para '{oferta_principal}'. Según la información disponible, el enfoque inicial debe estar en la resolución del dolor agudo y la calidad percibida.

## Mensajes base
- "Resuelva su '{problema_principal}' mediante '{oferta_principal}' de alta calidad."
- "Confianza y eficacia para una solución segura."
- "Claridad y excelencia en su '{oferta_principal}'."

## Límites de la promesa
- No se puede prometer que la oferta sea la más económica sin conocer la competencia.
- No se puede prometer una resolución instantánea sin evaluar la complejidad técnica.
- No se puede prometer resultados comerciales ajenos al alcance de la {tipo_oferta}.

## Información faltante para fortalecer la propuesta
- Evidencia de resultados pasados (casos de estudio).
- Comparativa detallada frente a alternativas del mercado (Fase 05).
- Detalle de garantías o soporte post-venta/entrega.

## Riesgos de posicionamiento
- Riesgo de propuesta genérica si no se encuentra un ángulo de ataque único.
- Riesgo de falta de prueba social inicial para validar la promesa.

## Recomendación para la siguiente fase
05_analisis_competencia
"""

    output_file = os.path.join(output_dir, "04_propuesta_valor_y_posicionamiento.md")
    
    write_markdown_file(output_file, output_content)
        
    return output_file

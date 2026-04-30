# File: src/services/diagnostico_service.py
# ──────────────────────────────────────────────────────────────────────
# Propósito: Generar el documento de diagnóstico de marketing inicial.
# Rol: Servicio de análisis y diagnóstico (Fase 02).
# ──────────────────────────────────────────────────────────────────────

import os
from src.utils.markdown_utils import read_markdown_file, write_markdown_file, extract_markdown_field
from src.utils.project_io import get_context_path, get_plan_actual_path, ensure_file_exists

def generate_diagnostico_output(project_name: str) -> str:
    """
    Genera el documento de diagnóstico de marketing (Fase 02).
    Verifica que la Fase 01 esté completa.
    """
    output_dir = get_plan_actual_path(project_name)
    context_dir = get_context_path(project_name)
    
    # 1. Verificar Fase 01
    phase_01_path = os.path.join(output_dir, "01_brief_negocio_validado.md")
    ensure_file_exists(
        phase_01_path,
        f"No se puede generar la Fase 02. El archivo '{phase_01_path}' no existe. "
        "Primero debe ejecutar la Fase 01 (generate-brief-output)."
    )

    # 2. Recopilar información de contexto
    
    data = {}
    found_files = []
    
    # Leer brief
    brief_path = os.path.join(context_dir, "brief_negocio.md")
    if os.path.exists(brief_path):
        found_files.append("brief_negocio.md")
        content = read_markdown_file(brief_path)
        
        name = extract_markdown_field(content, "nombre_negocio")
        oferta = extract_markdown_field(content, "oferta_principal")
        obj = extract_markdown_field(content, "cliente_objetivo")
        prob = extract_markdown_field(content, "problema_que_resuelve")
        budget = extract_markdown_field(content, "presupuesto_marketing")
        
        data["nombre_negocio"] = name if name else "[No informado]"
        data["oferta_principal"] = oferta if oferta else "[No informado]"
        data["cliente_objetivo"] = obj if obj else "[No informado]"
        data["problema_que_resuelve"] = prob if prob else "[No informado]"
        
        budget_raw = budget if budget else "None"
        if budget_raw.lower() in ["none", "", "null", "[completar]"]:
            data["presupuesto_marketing"] = "No informado"
            data["budget_warning"] = "Riesgo de planificación si no se define un presupuesto de marketing acorde al objetivo declarado."
        else:
            data["presupuesto_marketing"] = budget_raw
            data["budget_warning"] = f"El presupuesto declarado es {budget_raw}. Pendiente validar suficiencia."

    # Revisar otros archivos de contexto
    optional_files = [
        "empresa.md", "oferta.md", "cliente_objetivo.md", 
        "contexto_mercado.md", "canales_actuales.md", "restricciones.md"
    ]
    for optional_file in optional_files:
        path = os.path.join(context_dir, optional_file)
        if os.path.exists(path) and os.path.getsize(path) > 0:
            found_files.append(optional_file)

    # 3. Construir el documento de Fase 02
    oferta_principal = data.get("oferta_principal", "[No informado]")
    cliente_objetivo = data.get("cliente_objetivo", "[No informado]")
    problema_principal = data.get("problema_que_resuelve", "[No informado]")
    budget_warning = data.get("budget_warning", "")

    output_content = f"""# 02 - Diagnóstico de Marketing Inicial

## Estado del diagnóstico
diagnostico_inicial_generado_con_informacion_limitada

## Base utilizada
- 01_brief_negocio_validado.md
- brief_negocio.md
"""
    for f in found_files:
        output_content += f"- {f}\n"

    output_content += f"""
## Lectura inicial del negocio
El negocio '{data.get("nombre_negocio", "[No informado]")}' se enfoca en ofrecer '{oferta_principal}'. 
La propuesta busca resolver el problema de '{problema_principal}' para el segmento de '{cliente_objetivo}'.

## Claridad de la oferta
- Hipótesis: La oferta de '{oferta_principal}' es la propuesta central.
- Pendiente validar si existen variaciones o paquetes de la oferta no declarados en el brief inicial.
- Pendiente confirmar si el nombre de la oferta es claro para el cliente final.

## Cliente objetivo declarado
- '{cliente_objetivo}'
- El nivel de especificidad es inicial. Se requiere profundizar en el perfil psicográfico y comportamiento de compra en la Fase 03.

## Problema declarado
- '{problema_principal}'
- Hipótesis: Este problema genera un impacto directo en la operativa o satisfacción del cliente.
- Pendiente validar si es el dolor más agudo o si existen otros problemas secundarios no mencionados.

## Presencia y canales actuales
- Pendiente de auditoría técnica. Según la información disponible, no se han detallado canales con métricas de rendimiento.
- Si existen canales previos, se requiere acceso a datos de conversión para un diagnóstico preciso.

## Fortalezas iniciales detectadas
- Hipótesis: Capacidad técnica para resolver '{problema_principal}' mediante '{oferta_principal}'.
- Hipótesis: Claridad en el objetivo principal del negocio.

## Debilidades o vacíos iniciales
- Falta de evidencia de posicionamiento actual en el mercado.
- Ausencia de datos sobre la competencia directa en el contexto proporcionado.
- {budget_warning}

## Oportunidades preliminares
- Hipótesis: Existe una brecha en el mercado para soluciones que resuelvan '{problema_principal}' de forma eficiente.
- Potencial de especialización en el segmento '{cliente_objetivo}'.

## Riesgos iniciales
- Riesgo de invisibilidad si no se activan canales adecuados al segmento.
- Riesgo de mensaje genérico si no se profundiza en el diferencial de la oferta.

## Información faltante para profundizar
- Datos reales de ventas o clientes pasados.
- Análisis de competidores directos y sus promesas.
- Detalle técnico profundo de la oferta '{oferta_principal}'.
- Recursos humanos y técnicos disponibles para la ejecución del plan.

## Recomendación para la siguiente fase
03_cliente_objetivo_y_segmentos
"""

    output_file = os.path.join(output_dir, "02_diagnostico_marketing.md")
    
    write_markdown_file(output_file, output_content)
        
    return output_file

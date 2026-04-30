# File: src/services/competencia_service.py
# ──────────────────────────────────────────────────────────────────────
# Propósito: Generar el documento de análisis de competencia inicial.
# Rol: Servicio de análisis de mercado (Fase 05).
# ──────────────────────────────────────────────────────────────────────

import os
import re
from src.utils.markdown_utils import read_markdown_file, write_markdown_file, extract_markdown_field
from src.utils.project_io import get_context_path, get_plan_actual_path, ensure_file_exists

def generate_competencia_output(project_name: str) -> str:
    """
    Genera el documento de Análisis de Competencia Inicial (Fase 05).
    Verifica que la Fase 04 esté completa.
    """
    output_dir = get_plan_actual_path(project_name)
    context_dir = get_context_path(project_name)
    
    # 1. Verificar Fase 04
    phase_04_path = os.path.join(output_dir, "04_propuesta_valor_y_posicionamiento.md")
    ensure_file_exists(
        phase_04_path,
        f"No se puede generar la Fase 05. El archivo '{phase_04_path}' no existe. "
        "Primero debe ejecutar la Fase 04 (generate-propuesta-valor-output)."
    )

    # 2. Recopilar información de contexto y fases previas
    
    data = {}
    found_files = []
    
    # Leer brief
    brief_path = os.path.join(context_dir, "brief_negocio.md")
    if os.path.exists(brief_path):
        found_files.append("brief_negocio.md")
        content = read_markdown_file(brief_path)
        srv = extract_markdown_field(content, "servicio_principal")
        tipo = extract_markdown_field(content, "tipo_empresa_servicios")
        data["servicio_principal"] = srv if srv else "[No informado]"
        data["tipo_empresa"] = tipo if tipo else "[No informado]"

    # Leer Fase 04 para segmento prioritario
    phase_04_content = read_markdown_file(phase_04_path)
        
    def extract_section(content, header):
        pattern = fr'## {header}\n(.*?)(?=\n##|\Z)'
        match = re.search(pattern, content, re.DOTALL)
        return match.group(1).strip() if match else "No se encontró información."

    segmento_prioritario = extract_section(phase_04_content, "Segmento prioritario utilizado")

    # Revisar archivos de contexto opcionales
    for optional_file in ["contexto_mercado.md", "servicios.md"]:
        path = os.path.join(context_dir, optional_file)
        if os.path.exists(path) and os.path.getsize(path) > 0:
            found_files.append(optional_file)

    # 3. Construir el documento de Fase 05
    servicio_principal = data.get("servicio_principal", "[No informado]")
    tipo_empresa = data.get("tipo_empresa", "[No informado]")
    
    output_content = f"""# 05 - Análisis de Competencia Inicial

## Estado del análisis
analisis_competencia_inicial_sin_investigacion_externa

## Base utilizada
- 01_brief_negocio_validado.md
- 02_diagnostico_marketing.md
- 03_cliente_objetivo_y_segmentos.md
- 04_propuesta_valor_y_posicionamiento.md
"""
    for f in found_files:
        output_content += f"- {f}\n"

    output_content += f"""
## Alcance de esta fase
Este análisis no identifica competidores reales todavía, sino que prepara la estructura estratégica para investigarlos en fases posteriores. El objetivo es definir qué tipo de alternativas tiene el cliente y bajo qué criterios se comparará la propuesta.

## Servicio analizado
{servicio_principal}

## Segmento analizado
{segmento_prioritario}

## Competidores directos posibles
No se identifican competidores reales con nombre y apellido en esta fase. Se describen tipos de competidores directos posibles:
- Hipótesis: Empresas especializadas en '{servicio_principal}' con enfoque similar al segmento prioritario.
- Hipótesis: Proveedores de '{tipo_empresa}' que operan en la misma zona geográfica o nicho.
- Hipótesis: Consultoras que ofrecen soluciones integrales que incluyen '{servicio_principal}'.

## Competidores indirectos posibles
Alternativas que el cliente podría considerar fuera de la competencia directa:
- Hipótesis: Equipo interno del cliente intentando resolver el problema por su cuenta.
- Hipótesis: Freelance o profesional independiente contratado por proyecto.
- Hipótesis: Proveedor de un servicio sustituto que mitiga el problema sin resolverlo de raíz.
- Hipótesis: Inacción (No hacer nada y mantener la situación actual asumiendo los riesgos).

## Alternativas sustitutivas
Opciones que resuelven parcialmente el problema sin ser competidores del mismo servicio:
- Hipótesis: Adopción de herramientas de autoservicio (Do It Yourself).
- Hipótesis: Outsourcing total de la función afectada por el problema.

## Criterios de comparación recomendados
Criterios clave para comparar competidores en una fase de investigación real:
- Claridad y transparencia de la oferta.
- Nivel de especialización en el nicho del cliente.
- Modelo de precio y flexibilidad.
- Garantías y acuerdos de nivel de servicio.
- Calidad del soporte o acompañamiento.
- Evidencia de casos de éxito o trayectoria.
- Certificaciones o avales de terceros.
- Tiempos de entrega o implementación.

## Riesgos competitivos iniciales
- Hipótesis: Propuesta actual percibida como genérica frente a especialistas establecidos.
- Hipótesis: Falta de evidencia pública (pruebas sociales) frente a la competencia.
- Hipótesis: Competidores con mayor cercanía geográfica o relaciones previas.
- Hipótesis: Sensibilidad del cliente al precio frente a propuestas de bajo coste.

## Oportunidades de diferenciación preliminares
- Hipótesis: Enfoque radical en la reducción de riesgo y acompañamiento humano.
- Hipótesis: Claridad total en el proceso frente a la opacidad habitual del sector.
- Hipótesis: Especialización en un sub-nicho dentro de '{segmento_prioritario}'.

## Información faltante para análisis competitivo real
- Nombres de competidores locales y nacionales.
- Sitios web y presencia digital de la competencia.
- Estructuras de precios y promesas de venta principales.
- Casos de éxito públicos y reseñas de terceros.

## Recomendación para investigación futura
Se explica que una futura versión del plan podrá realizar un análisis real de competencia utilizando herramientas de investigación externa autorizada.

## Recomendación para la siguiente fase
06_matriz_canales_marketing
"""

    output_file = os.path.join(output_dir, "05_analisis_competencia.md")
    
    write_markdown_file(output_file, output_content)
        
    return output_file

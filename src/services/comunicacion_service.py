# File: src/services/comunicacion_service.py
# ──────────────────────────────────────────────────────────────────────
# Propósito: Generar el documento de estrategia de comunicación.
# Rol: Servicio de definición de mensajes y tono (Fase 07).
# ──────────────────────────────────────────────────────────────────────

import os
import re
from src.utils.markdown_utils import read_markdown_file, write_markdown_file, extract_brief_fields
from src.utils.project_io import get_context_path, get_plan_actual_path, ensure_file_exists
from src.core.marketing_profile_resolver import resolve_marketing_profile


def generate_comunicacion_output(project_name: str) -> str:
    """
    Genera el documento de Estrategia de Comunicación (Fase 07).
    Verifica que la Fase 06 esté completa.
    Usa el perfil de marketing para adaptar el tono y mensajes por canal.
    """
    output_dir = get_plan_actual_path(project_name)
    context_dir = get_context_path(project_name)

    # 1. Verificar Fase 06
    phase_06_path = os.path.join(output_dir, "06_matriz_canales_marketing.md")
    ensure_file_exists(
        phase_06_path,
        f"No se puede generar la Fase 07. El archivo '{phase_06_path}' no existe. "
        "Primero debe ejecutar la Fase 06 (generate-canales-output)."
    )

    # 2. Recopilar información

    brief_path = os.path.join(context_dir, "brief_negocio.md")
    brief_data = extract_brief_fields(read_markdown_file(brief_path)) if os.path.exists(brief_path) else {}
    profile = resolve_marketing_profile(brief_data)

    oferta_principal = brief_data.get("oferta_principal", "[No informado]")
    problema_principal = brief_data.get("problema_que_resuelve", "[No informado]")
    cliente_objetivo = brief_data.get("cliente_objetivo", "[No informado]")

    # Leer Fase 03 para datos de cliente
    def extract_section(content, header):
        pattern = fr'## {header}\n(.*?)(?=\n##|\Z)'
        match = re.search(pattern, content, re.DOTALL)
        return match.group(1).strip() if match else "No se encontró información específica."

    phase_03_path = os.path.join(output_dir, "03_cliente_objetivo_y_segmentos.md")
    p3_content = read_markdown_file(phase_03_path)

    cliente_section = extract_section(p3_content, "Cliente objetivo declarado")
    segmento_section = extract_section(p3_content, "Segmento prioritario inicial")

    found_files = [
        "01_brief_negocio_validado.md", "02_diagnostico_marketing.md",
        "03_cliente_objetivo_y_segmentos.md", "04_propuesta_valor_y_posicionamiento.md",
        "05_analisis_competencia.md", "06_matriz_canales_marketing.md", "brief_negocio.md",
    ]
    for opt in ["canales_actuales.md", "restricciones.md"]:
        if os.path.exists(os.path.join(context_dir, opt)):
            found_files.append(opt)

    # 3. Extraer terminología
    terminology = profile.get("terminology", {})
    tipo_oferta = terminology.get("oferta", "oferta")
    tipo_cliente = terminology.get("cliente", "cliente")
    accion_vincular = terminology.get("accion_principal", "contratar")

    # 4. Construir tono según perfil
    tone_block = ""
    for guideline in profile["tone_guidelines"]:
        parts = guideline.split(":", 1)
        if len(parts) == 2:
            tone_block += f"- **{parts[0].strip()}**:{parts[1]}\n"
        else:
            tone_block += f"- {guideline}\n"

    # 5. Adaptar lógica según perfil
    es_servicio = profile["marketing_profile"] in ["b2b_consultivo", "b2c_local_servicios", "hibrido_producto_servicio"]
    palabras_positivas = ["Confianza", "Acompañamiento", "Claridad"] if es_servicio else ["Calidad premium", "Garantía", "Satisfacción"]
    palabras_positivas += ["Resultados reales", "Transparencia"]
    
    frase_ayuda = f"trabajamos para que tu {tipo_oferta} sea la solución definitiva" if not es_servicio else "trabajamos para ayudarte a superarlo"
    frase_posicionamiento = f"disfrutes de la excelencia en cada {tipo_oferta}" if not es_servicio else "puedas centrarte en lo que más importa"

    # 6. Construir mensajes por canal según perfil
    messages_block = ""
    for channel in profile["recommended_channel_families"]:
        messages_block += f"""- **Canal: {channel.get('name', '[Nombre]')}**
  - **Enfoque comunicativo**: Comunicar cómo '{oferta_principal}' resuelve '{problema_principal}' a través de este canal.
  - **Tipo de mensaje**: \"Entendemos el impacto de '{problema_principal}'. Con '{oferta_principal}' {frase_ayuda}.\"
  - **Riesgo**: No adaptar el mensaje al formato y estilo propios de este canal.
  - **Condición**: Validar que el mensaje resuena antes de escalar la frecuencia.

"""

    # 7. Documento completo
    output_content = f"""# 07 - Estrategia de Comunicación

## Estado del análisis
estrategia_comunicacion_inicial_generada_con_informacion_limitada

## Base utilizada
"""
    for f in found_files:
        output_content += f"- {f}\n"

    output_content += f"""
## Alcance de esta fase
Esta fase define el tono, los mensajes clave, los pilares de comunicación y el enfoque estratégico para contactar con la audiencia. No incluye la creación de un calendario editorial, redacción de posts, correos ni piezas gráficas finales. Es la hoja de ruta para que la comunicación sea coherente y efectiva.

## Perfil de marketing aplicado
- **Perfil**: {profile['marketing_profile']}

## Cliente al que se dirige la comunicación
- **Perfil General**: {cliente_section}
- **Segmento Prioritario Inicial**: {segmento_section}

## Problema central que debe comunicar
El eje de la comunicación debe ser la resolución de: '{problema_principal}'.
Se debe empatizar con el impacto de este problema en el {tipo_cliente} antes de presentar la solución.

## Promesa comunicacional inicial
Hipótesis: \"Queremos que {accion_vincular} '{oferta_principal}' sea la mejor decisión para resolver '{problema_principal}'.\"
Nota: Esta promesa es provisional y depende de la validación real con el mercado.

## Tono recomendado
Según el perfil de '{cliente_objetivo}' y la naturaleza de la {tipo_oferta} '{oferta_principal}', el tono debe ser:
{tone_block}
Evitar tonos agresivos, urgencias artificiales o promesas exageradas que puedan dañar la credibilidad.

## Mensaje central
\"Soluciones reales para '{problema_principal}': '{oferta_principal}' para que {frase_posicionamiento}.\"

## Pilares de comunicación
1. **Pilar: Especialización y Enfoque**
    - **Objetivo**: Posicionar el negocio como la opción preferida para resolver el problema específico.
    - **Qué comunicar**: Conocimiento profundo de '{problema_principal}' y por qué '{oferta_principal}' es la mejor respuesta.
    - **Qué evitar**: Hablar de temas genéricos no relacionados con la propuesta de valor.

2. **Pilar: Seguridad y Calidad**
    - **Objetivo**: Neutralizar el miedo a la {accion_vincular} por primera vez.
    - **Qué comunicar**: Proceso claro, garantías, soporte o calidad superior de la {tipo_oferta}.
    - **Qué evitar**: Promesas de resolución instantánea sin base técnica.

3. **Pilar: Valor y Resultados**
    - **Objetivo**: Conectar la {tipo_oferta} con el beneficio real para el {tipo_cliente}.
    - **Qué comunicar**: Qué gana el {tipo_cliente} después de usar '{oferta_principal}' (tiempo, bienestar, ahorro, eficiencia).
    - **Qué evitar**: Centrarse solo en características técnicas frías de '{oferta_principal}'.

4. **Pilar: Transparencia y Confianza**
    - **Objetivo**: Diferenciarse por la honestidad en la relación comercial.
    - **Qué comunicar**: Claridad en alcances, precios y qué esperar de la {tipo_oferta}.
    - **Qué evitar**: Ocultar limitaciones o usar lenguaje confuso.

## Mensajes por canal prioritario
Basado en la Fase 06 y el perfil ({profile['marketing_profile']}):

{messages_block}
## Objeciones que debe responder la comunicación
Basado en las hipótesis de las Fases 03 y 04:

- **Objeción: \"Es demasiado caro / No tengo presupuesto\"**
  - **Respuesta Comunicacional**: Enfocar la comunicación en el coste de la inacción frente a la inversión en la {tipo_oferta}.
- **Objeción: \"No estoy seguro de que funcione para mi caso\"**
  - **Respuesta Comunicacional**: Reforzar el pilar de 'Seguridad y Calidad', explicando el proceso, las garantías o el soporte.
- **Objeción: \"No sé si realmente necesito '{oferta_principal}'\"**
  - **Respuesta Comunicacional**: Mostrar cómo '{oferta_principal}' es la vía efectiva para resolver '{problema_principal}'.

## Palabras o enfoques recomendados
"""
    for word in palabras_positivas:
        output_content += f"- {word}\n"
    
    output_content += """
## Palabras o enfoques que conviene evitar
- \"Solución integral\" (muy genérico)
- \"La mejor calidad\" (sin evidencia técnica)
- \"Líderes\" (si no está validado por el mercado)
- Lenguaje excesivamente técnico sin explicar el beneficio para el usuario.

## Reglas básicas de comunicación
- **Prudencia**: No prometer resultados que no se hayan validado.
- **Concreción**: Usar ejemplos de situaciones reales que vive el {tipo_cliente}.
- **Coherencia**: El mensaje debe ser el mismo en todos los canales activos.
- **Empatía**: Empezar por el problema del {tipo_cliente}, no por las características de la {tipo_oferta}.

## Información faltante para fortalecer la comunicación
- Testimonios reales de clientes o usuarios satisfechos.
- Casos de estudio con datos concretos (antes vs después).
- Preguntas frecuentes recolectadas de interacciones reales.
- Ejemplos visuales de '{oferta_principal}'.

## Riesgos de comunicación
- **Mensaje Genérico**: Que el cliente sienta que la comunicación sirve para cualquier negocio.
- **Promesa Excesiva**: Generar expectativas que la oferta no pueda cumplir.
- **Desconexión con el problema**: Hablar demasiado de la {tipo_oferta} y poco del problema '{problema_principal}'.

## Recomendación para la siguiente fase
08_plan_accion_90_dias
"""

    output_file = os.path.join(output_dir, "07_estrategia_comunicacion.md")
    write_markdown_file(output_file, output_content)

    return output_file

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

    # 3. Construir tono según perfil
    tone_block = ""
    for guideline in profile["tone_guidelines"]:
        parts = guideline.split(":", 1)
        if len(parts) == 2:
            tone_block += f"- **{parts[0].strip()}**:{parts[1]}\n"
        else:
            tone_block += f"- {guideline}\n"

    # 4. Construir mensajes por canal según perfil
    messages_block = ""
    for channel in profile["recommended_channel_families"]:
        messages_block += f"""- **Canal: {channel.get('name', '[Nombre]')}**
  - **Enfoque comunicativo**: Comunicar cómo '{oferta_principal}' resuelve '{problema_principal}' a través de este canal.
  - **Tipo de mensaje**: \"Entendemos que '{problema_principal}' dificulta tu día a día. En '{oferta_principal}' trabajamos para ayudarte a superarlo.\"
  - **Riesgo**: No adaptar el mensaje al formato y estilo propios de este canal.
  - **Condición**: Validar que el mensaje resuena antes de escalar la frecuencia.

"""

    # 5. Documento completo
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
Se debe empatizar con el impacto negativo que este problema genera en el cliente antes de presentar la solución.

## Promesa comunicacional inicial
Hipótesis: \"Queremos que resolver '{problema_principal}' sea fácil, seguro y accesible gracias a '{oferta_principal}'.\"
Nota: Esta promesa es provisional y depende de la validación real con el mercado.

## Tono recomendado
Según el perfil de '{cliente_objetivo}' y la naturaleza de '{oferta_principal}', el tono debe ser:
{tone_block}
Evitar tonos agresivos, urgencias artificiales o promesas exageradas que puedan dañar la credibilidad.

## Mensaje central
\"Soluciones reales para '{problema_principal}': '{oferta_principal}' pensado para que puedas centrarte en lo que más importa.\"

## Pilares de comunicación
1. **Pilar: Especialización y Enfoque**
   - **Objetivo**: Posicionar al negocio como experto en el problema específico del cliente.
   - **Qué comunicar**: Conocimiento profundo del problema '{problema_principal}' y casos de uso comunes.
   - **Qué evitar**: Hablar de servicios genéricos no relacionados con el problema principal.

2. **Pilar: Seguridad y Bajo Riesgo**
   - **Objetivo**: Neutralizar el miedo a probar la oferta por primera vez.
   - **Qué comunicar**: Proceso claro, garantías, acompañamiento o calidad del producto.
   - **Qué evitar**: Promesas de resolución instantánea o sin esfuerzo.

3. **Pilar: Valor y Resultados Esperados**
   - **Objetivo**: Conectar la oferta con el beneficio real para el cliente.
   - **Qué comunicar**: Qué gana el cliente después de resolver '{problema_principal}' (tiempo, bienestar, ahorro, eficiencia).
   - **Qué evitar**: Centrarse solo en características de la oferta '{oferta_principal}'.

4. **Pilar: Transparencia y Confianza**
   - **Objetivo**: Diferenciarse por la honestidad en la relación.
   - **Qué comunicar**: Claridad en alcances, precios y qué esperar del servicio.
   - **Qué evitar**: Ocultar posibles limitaciones o usar lenguaje confuso.

## Mensajes por canal prioritario
Basado en la Fase 06 y el perfil ({profile['marketing_profile']}):

{messages_block}
## Objeciones que debe responder la comunicación
Basado en las hipótesis de las Fases 03 y 04:

- **Objeción: \"Es demasiado caro / No tengo presupuesto\"**
  - **Respuesta Comunicacional**: Enfocar la comunicación en el coste de la inacción (lo que pierde el cliente por no resolver '{problema_principal}') frente a la inversión en la oferta.
- **Objeción: \"No estoy seguro de que funcione para mi caso\"**
  - **Respuesta Comunicacional**: Reforzar el pilar de 'Seguridad y Bajo Riesgo', explicando el proceso, las garantías o el soporte.
- **Objeción: \"No sé si realmente necesito '{oferta_principal}'\"**
  - **Respuesta Comunicacional**: Pilar 'Educativo', mostrando cómo '{oferta_principal}' es la vía para resolver '{problema_principal}'.

## Palabras o enfoques que conviene usar
- Confianza
- Acompañamiento
- Claridad
- Resultados reales
- "Paso a paso"
- Experiencia comprobable

## Palabras o enfoques que conviene evitar
- "Solución integral" (muy genérico)
- "La mejor calidad" (sin evidencia)
- "Líderes" (si no está validado)
- Lenguaje excesivamente técnico sin explicar el beneficio.

## Reglas básicas de comunicación
- **Prudencia**: No prometer resultados que no se hayan validado.
- **Concreción**: Siempre que sea posible, usar ejemplos de situaciones reales que vive el cliente.
- **Coherencia**: El mensaje debe ser el mismo en todos los canales activos.
- **Empatía**: Empezar por el problema del cliente, no por las características del servicio.

## Información faltante para fortalecer la comunicación
- Testimonios reales de clientes satisfechos.
- Casos de estudio con datos concretos (antes vs después).
- Preguntas frecuentes recolectadas de interacciones reales.
- Ejemplos visuales del proceso o resultado de '{oferta_principal}'.

## Riesgos de comunicación
- **Mensaje Genérico**: Que el cliente sienta que la comunicación sirve para cualquier negocio.
- **Promesa Excesiva**: Generar expectativas que la oferta no pueda cumplir.
- **Desconexión con el problema**: Hablar demasiado de la oferta y poco del problema '{problema_principal}'.

## Recomendación para la siguiente fase
08_plan_accion_90_dias
"""

    output_file = os.path.join(output_dir, "07_estrategia_comunicacion.md")
    write_markdown_file(output_file, output_content)

    return output_file

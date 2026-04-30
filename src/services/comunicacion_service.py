# File: src/services/comunicacion_service.py
# ──────────────────────────────────────────────────────────────────────
# Propósito: Generar el documento de estrategia de comunicación.
# Rol: Servicio de definición estratégica (Fase 07).
# ──────────────────────────────────────────────────────────────────────

import os
import re
from src.utils.markdown_utils import read_markdown_file, write_markdown_file, extract_markdown_field
from src.utils.project_io import get_context_path, get_plan_actual_path, ensure_file_exists

def generate_comunicacion_output(project_name: str) -> str:
    """
    Genera el documento de Estrategia de Comunicación (Fase 07).
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

    # 2. Recopilar información de contexto
    brief_path = os.path.join(context_dir, "brief_negocio.md")
    brief_data = {}
    if os.path.exists(brief_path):
        from src.utils.markdown_utils import extract_brief_fields
        brief_data = extract_brief_fields(read_markdown_file(brief_path))

    oferta_principal = brief_data.get("oferta_principal", "[No informado]")
    cliente_objetivo = brief_data.get("cliente_objetivo", "[No informado]")
    problema_principal = brief_data.get("problema_que_resuelve", "[No informado]")

    # Resolver perfil de marketing
    from src.core.marketing_profile_resolver import resolve_marketing_profile
    profile = resolve_marketing_profile(brief_data)

    # 3. Extraer terminología
    terminology = profile.get("terminology", {})
    tipo_oferta = terminology.get("oferta", "oferta")
    tipo_cliente = terminology.get("cliente", "cliente")

    # 3.1 Variables de redacción natural
    redaccion_map = {
        "ecommerce_transaccional": {
            "oferta_con_articulo": "el producto ecommerce",
            "oferta_para_contexto": "del producto ecommerce",
            "cliente_plural": "usuarios",
            "accion_contextual": "compra"
        },
        "b2c_producto_ecommerce": {
            "oferta_con_articulo": "el producto",
            "oferta_para_contexto": "del producto",
            "cliente_plural": "clientes",
            "accion_contextual": "compra"
        },
        "b2b_consultivo": {
            "oferta_con_articulo": "el servicio consultivo",
            "oferta_para_contexto": "del servicio consultivo",
            "cliente_plural": "clientes/empresas",
            "accion_contextual": "contratación"
        },
        "b2c_local_servicios": {
            "oferta_con_articulo": "el servicio local",
            "oferta_para_contexto": "del servicio",
            "cliente_plural": "clientes",
            "accion_contextual": "contratación"
        },
        "educativo_formativo": {
            "oferta_con_articulo": "la formación",
            "oferta_para_contexto": "de la formación",
            "cliente_plural": "alumnos/estudiantes",
            "accion_contextual": "inscripción"
        },
        "retail_fisico": {
            "oferta_con_articulo": "la propuesta comercial",
            "oferta_para_contexto": "del producto de tienda",
            "cliente_plural": "visitantes/clientes",
            "accion_contextual": "visita"
        },
        "b2b_producto_industrial": {
            "oferta_con_articulo": "el producto industrial",
            "oferta_para_contexto": "del suministro industrial",
            "cliente_plural": "empresas/compradores",
            "accion_contextual": "homologación"
        },
        "hibrido_producto_servicio": {
            "oferta_con_articulo": "la solución integral",
            "oferta_para_contexto": "de la solución integral",
            "cliente_plural": "socios/clientes",
            "accion_contextual": "adquisición con soporte"
        }
    }
    config_redaccion = redaccion_map.get(profile["marketing_profile"], {
        "oferta_con_articulo": f"la {tipo_oferta}",
        "oferta_para_contexto": f"de la oferta",
        "cliente_plural": f"{tipo_cliente}s",
        "accion_contextual": "adquisición"
    })
    oferta_con_articulo = config_redaccion["oferta_con_articulo"]
    oferta_para_contexto = config_redaccion["oferta_para_contexto"]
    cliente_plural = config_redaccion["cliente_plural"]
    accion_contextual = config_redaccion["accion_contextual"]

    # Leer Fases 03 y 04 para contexto adicional
    phase_03_path = os.path.join(output_dir, "03_cliente_objetivo_y_segmentos.md")
    phase_04_path = os.path.join(output_dir, "04_propuesta_valor_y_posicionamiento.md")
    
    cliente_section = extract_markdown_field(read_markdown_file(phase_03_path), "Perfil General") if os.path.exists(phase_03_path) else "[No informado]"
    segmento_section = extract_markdown_field(read_markdown_file(phase_03_path), "Segmento prioritario inicial") if os.path.exists(phase_03_path) else "[No informado]"

    found_files = ["01_brief_negocio_validado.md", "02_diagnostico_marketing.md", "03_cliente_objetivo_y_segmentos.md", "04_propuesta_valor_y_posicionamiento.md", "05_analisis_competencia.md", "06_matriz_canales_marketing.md", "brief_negocio.md"]
    for opt in ["oferta.md", "restricciones.md"]:
        if os.path.exists(os.path.join(context_dir, opt)):
            found_files.append(opt)

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
Hipótesis: \"Queremos que la {accion_contextual} de '{oferta_principal}' sea una decisión clara, segura y valiosa para resolver '{problema_principal}'.\"
Nota: Esta promesa es provisional y depende de la validación real con el mercado.

## Tono recomendado
Según el perfil de '{cliente_objetivo}' y la naturaleza {oferta_para_contexto} '{oferta_principal}', el tono debe ser:
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
    - **Objetivo**: Neutralizar el miedo a la {accion_contextual} por primera vez.
    - **Qué comunicar**: Proceso claro, garantías, soporte o calidad superior {oferta_para_contexto}.
    - **Qué evitar**: Promesas de resolución instantánea sin base técnica.

3. **Pilar: Valor y Resultados**
    - **Objetivo**: Conectar {oferta_con_articulo} con el beneficio real para el {tipo_cliente}.
    - **Qué comunicar**: Qué gana el {tipo_cliente} después de usar '{oferta_principal}' (tiempo, bienestar, ahorro, eficiencia).
    - **Qué evitar**: Centrarse solo en características técnicas frías de '{oferta_principal}'.

4. **Pilar: Transparencia y Confianza**
    - **Objetivo**: Diferenciarse por la honestidad en la relación comercial.
    - **Qué comunicar**: Claridad en alcances, precios y qué esperar {oferta_para_contexto}.
    - **Qué evitar**: Ocultar limitaciones o usar lenguaje confuso.

## Mensajes por canal prioritario
Basado en la Fase 06 y el perfil ({profile['marketing_profile']}):

{messages_block}
## Objeciones que debe responder la comunicación
Basado en las hipótesis de las Fases 03 y 04:

- **Objeción: \"Es demasiado caro / No tengo presupuesto\"**
  - **Respuesta Comunicacional**: Enfocar la comunicación en el coste de la inacción frente a la inversión en {oferta_con_articulo}.
- **Objeción: \"No estoy seguro de que funcione para mi caso\"**
  - **Respuesta Comunicacional**: Reforzar el pilar de 'Seguridad y Calidad', explicando el proceso, las garantías o el soporte.
- **Objeción: \"No sé si realmente necesito '{oferta_principal}'\"**
  - **Respuesta Comunicacional**: Mostrar cómo '{oferta_principal}' es la vía efectiva para resolver '{problema_principal}'.

## Palabras o enfoques recomendados
"""
    for word in palabras_positivas:
        output_content += f"- {word}\n"
    
    output_content += f"""
## Palabras o enfoques que conviene evitar
- \"Solución integral\" (muy genérico)
- \"La mejor calidad\" (sin evidencia técnica)
- \"Líderes\" (si no está validado por el mercado)
- Lenguaje excesivamente técnico sin explicar el beneficio para el {tipo_cliente}.

## Reglas básicas de comunicación
- **Prudencia**: No prometer resultados que no se hayan validado.
- **Concreción**: Usar ejemplos de situaciones reales que vive el {tipo_cliente}.
- **Coherencia**: El mensaje debe ser el mismo en todos los canales activos.
- **Empatía**: Empezar por el problema del {tipo_cliente}, no por las características {oferta_para_contexto}.

## Información faltante para fortalecer la comunicación
- Testimonios reales de clientes o usuarios satisfechos.
- Casos de estudio con datos concretos (antes vs después).
- Preguntas frecuentes recolectadas de interacciones reales.
- Ejemplos visuales de '{oferta_principal}'.

## Riesgos de comunicación
- **Mensaje Genérico**: Que el {tipo_cliente} sienta que la comunicación sirve para cualquier negocio.
- **Promesa Excesiva**: Generar expectativas que {oferta_con_articulo} no pueda cumplir.
- **Desconexión con el problema**: Hablar demasiado {oferta_para_contexto} y poco del problema '{problema_principal}'.

## Recomendación para la siguiente fase
08_plan_accion_90_dias
"""

    output_file = os.path.join(output_dir, "07_estrategia_comunicacion.md")
    write_markdown_file(output_file, output_content)

    return output_file

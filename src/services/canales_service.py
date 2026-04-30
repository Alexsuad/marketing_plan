# File: src/services/canales_service.py
# ──────────────────────────────────────────────────────────────────────
# Propósito: Generar el documento de matriz de canales de marketing.
# Rol: Servicio de selección de canales (Fase 06).
# ──────────────────────────────────────────────────────────────────────

import os
from src.utils.markdown_utils import read_markdown_file, write_markdown_file, extract_brief_fields
from src.utils.project_io import get_context_path, get_plan_actual_path, ensure_file_exists
from src.core.marketing_profile_resolver import resolve_marketing_profile


def generate_canales_output(project_name: str) -> str:
    """
    Genera el documento de Matriz de Canales de Marketing (Fase 06).
    Verifica que la Fase 05 esté completa.
    Usa el perfil de marketing para adaptar canales al tipo de negocio.
    """
    output_dir = get_plan_actual_path(project_name)
    context_dir = get_context_path(project_name)

    # 1. Verificar Fase 05
    phase_05_path = os.path.join(output_dir, "05_analisis_competencia.md")
    ensure_file_exists(
        phase_05_path,
        f"No se puede generar la Fase 06. El archivo '{phase_05_path}' no existe. "
        "Primero debe ejecutar la Fase 05 (generate-competencia-output)."
    )

    # 2. Recopilar información de contexto y fases previas
    brief_path = os.path.join(context_dir, "brief_negocio.md")
    brief_data = extract_brief_fields(read_markdown_file(brief_path)) if os.path.exists(brief_path) else {}
    profile = resolve_marketing_profile(brief_data)

    # Extraer terminología dinámica según el perfil
    terminology = profile.get("terminology", {})
    accion_principal = terminology.get("accion_principal", "tomar una decisión de compra o contratación")
    tipo_oferta = terminology.get("oferta", "oferta")
    tipo_cliente = terminology.get("cliente", "cliente")

    oferta_principal = brief_data.get("oferta_principal", "[No informado]")
    cliente_objetivo = brief_data.get("cliente_objetivo", "[No informado]")

    # Archivos base
    found_files = []
    for optional_file in ["canales_actuales.md", "restricciones.md"]:
        path = os.path.join(context_dir, optional_file)
        if os.path.exists(path) and os.path.getsize(path) > 0:
            found_files.append(optional_file)

    # 3. Construir el documento de Fase 06
    output_content = f"""# 06 - Matriz de Canales de Marketing

## Estado del análisis
matriz_canales_inicial_generada_con_informacion_limitada

## Base utilizada
- 01_brief_negocio_validado.md
- 02_diagnostico_marketing.md
- 03_cliente_objetivo_y_segmentos.md
- 04_propuesta_valor_y_posicionamiento.md
- 05_analisis_competencia.md
- brief_negocio.md
"""
    for f in found_files:
        output_content += f"- {f}\n"

    output_content += f"""
## Perfil de marketing detectado
- **Perfil**: {profile['marketing_profile']}
- **Motivo**: {profile['profile_reason']}

## Alcance de esta fase
Esta fase evalúa los canales de comunicación y captación más adecuados para la propuesta de valor y el segmento prioritario inicial. No se crean calendarios ni contenidos específicos todavía.

## Criterios usados para evaluar canales
- **Tipo de oferta**: '{oferta_principal}'.
- **Cliente objetivo**: '{cliente_objetivo}'.
- **Nivel de confianza**: Requerido para **{accion_principal}**.
- **Ciclo de decisión**: Estimado según la complejidad de la oferta.
- **Presupuesto y recursos**: Pendientes de validación final.

## Canales recomendados como prioritarios
Basado en el tipo de {tipo_oferta}, el perfil del {tipo_cliente} y el perfil de marketing ({profile['marketing_profile']}):

"""

    for i, channel in enumerate(profile["recommended_channel_families"], start=1):
        output_content += f"""{i}. **{channel.get('name', '[Nombre]')}**
   - **Objetivo**: {channel.get('objective', '[Objetivo]')}
   - **Esfuerzo**: {channel.get('effort', 'Pendiente de definir')}.
   - **Coste**: {channel.get('cost', 'Pendiente de definir')}
   - **Riesgo**: {channel.get('risk', 'Pendiente de definir')}

"""

    output_content += """## Canales secundarios
Canales de apoyo para visibilidad:

"""

    for i, channel in enumerate(profile["secondary_channel_families"], start=1):
        output_content += f"""{i}. **{channel.get('name', '[Nombre]')}**
   - **Utilidad**: {channel.get('utility', '[Utilidad]')}
   - **Por qué no prioritario**: {channel.get('why_not_primary', 'Estrategia de diversificación secundaria')}

"""

    output_content += """## Canales no recomendados por ahora
"""

    for i, channel in enumerate(profile["avoid_channel_families"], start=1):
        output_content += f"""{i}. **{channel.get('name', '[Nombre]')}**
   - **Motivo**: {channel.get('reason', '[Motivo]')}
   - **Cambio para reconsiderar**: {channel.get('reconsider_if', 'Cambio en el modelo de negocio')}

"""

    # Tabla resumen
    output_content += """## Tabla resumen de canales
| Canal | Prioridad | Objetivo | Esfuerzo | Coste estimado | Riesgo | Estado |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
"""
    for ch in profile["recommended_channel_families"]:
        output_content += f"| {ch.get('name', '—')} | Alta | {ch.get('objective', '—')[:30]}... | {ch.get('effort', '—')} | {ch.get('cost', '—')[:20]}... | {ch.get('risk', '—')[:20]}... | Recomendado |\n"
    for ch in profile["secondary_channel_families"]:
        output_content += f"| {ch.get('name', '—')} | Media | {ch.get('utility', '—')[:30]}... | Medio | Bajo | Bajo | Secundario |\n"
    for ch in profile["avoid_channel_families"]:
        output_content += f"| {ch.get('name', '—')} | Nula | — | — | — | — | Descartado |\n"

    output_content += f"""
## Observaciones sobre canales digitales
Los canales digitales deben actuar como validadores de confianza. Una presencia coherente con el tipo de negocio es necesaria para que el {tipo_cliente} confirme la seriedad de la marca/negocio tras un primer contacto.

## Observaciones sobre canales relacionales o presenciales
Dado el tipo de oferta ({tipo_oferta}) y la oferta principal '{oferta_principal}', junto con el perfil del {tipo_cliente} '{cliente_objetivo}', los canales prioritarios detectados son los más adecuados para un inicio prudente. La efectividad real queda pendiente de validación.

## Información faltante para decidir mejor
- Presupuesto real disponible.
- Capacidad operativa para gestionar contenidos o acciones comerciales.
- Zona geográfica prioritaria.
- Detalle técnico profundo de la oferta '{oferta_principal}'.
- Recursos humanos y técnicos disponibles para la ejecución del plan.

## Riesgos de selección de canales
- **Dispersión**: Intentar estar en demasiados canales sin recursos suficientes.
- **Elegir por moda**: No seguir el comportamiento real de compra de '{cliente_objetivo}'.

## Recomendación para la siguiente fase
07_estrategia_comunicacion
"""

    output_file = os.path.join(output_dir, "06_matriz_canales_marketing.md")

    write_markdown_file(output_file, output_content)

    return output_file

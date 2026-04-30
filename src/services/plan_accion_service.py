# File: src/services/plan_accion_service.py
# ──────────────────────────────────────────────────────────────────────
# Propósito: Generar el documento del plan de acción de 90 días.
# Rol: Servicio de planificación táctica (Fase 08).
# ──────────────────────────────────────────────────────────────────────

import os
import re
from src.utils.markdown_utils import read_markdown_file, write_markdown_file, extract_brief_fields
from src.utils.project_io import get_context_path, get_plan_actual_path, ensure_file_exists
from src.core.marketing_profile_resolver import resolve_marketing_profile


def generate_plan_accion_output(project_name: str) -> str:
    """
    Genera el documento de Plan de Acción 90 Días (Fase 08).
    Verifica que la Fase 07 esté completa.
    Usa el perfil de marketing para adaptar tácticas y acciones.
    """
    output_dir = get_plan_actual_path(project_name)
    context_dir = get_context_path(project_name)

    # 1. Verificar Fase 07
    phase_07_path = os.path.join(output_dir, "07_estrategia_comunicacion.md")
    ensure_file_exists(
        phase_07_path,
        f"No se puede generar la Fase 08. El archivo '{phase_07_path}' no existe. "
        "Primero debe ejecutar la Fase 07 (generate-comunicacion-output)."
    )

    # 2. Recopilar información

    brief_path = os.path.join(context_dir, "brief_negocio.md")
    brief_data = extract_brief_fields(read_markdown_file(brief_path)) if os.path.exists(brief_path) else {}
    profile = resolve_marketing_profile(brief_data)

    servicio_principal = brief_data.get("servicio_principal", "[No informado]")
    cliente_objetivo = brief_data.get("cliente_objetivo", "[No informado]")
    objetivo_principal = brief_data.get("objetivo_principal", "[No informado]")
    problema_principal = brief_data.get("problema_que_resuelve", "[No informado]")
    presupuesto = brief_data.get("presupuesto_marketing", "No informado")

    found_files = [
        "01_brief_negocio_validado.md", "02_diagnostico_marketing.md",
        "03_cliente_objetivo_y_segmentos.md", "04_propuesta_valor_y_posicionamiento.md",
        "05_analisis_competencia.md", "06_matriz_canales_marketing.md",
        "07_estrategia_comunicacion.md", "brief_negocio.md",
    ]
    if os.path.exists(os.path.join(context_dir, "restricciones.md")):
        found_files.append("restricciones.md")

    # 3. Construir tácticas según perfil
    tactical_block = ""
    for tactic in profile["tactical_focus"]:
        tactical_block += f"- {tactic}\n"

    # 4. Construir acciones por canal según perfil
    actions_block = ""
    for channel in profile["recommended_channel_families"]:
        actions_block += f"""- **Canal: {channel['name']}**
  - **Acción inicial**: Preparar los activos y mensajes necesarios para activar este canal.
  - **Objetivo**: Generar las primeras señales de interés a través de '{channel['name']}'.
  - **Esfuerzo estimado**: {channel['effort']}.
  - **Dependencia**: Tener claridad en la propuesta de valor inicial.
  - **Riesgo**: {channel['risk']}
  - **Señal esperada**: Número de interacciones positivas generadas por este canal.

"""

    output_content = f"""# 08 - Plan de Acción 90 Días

## Estado del plan
plan_accion_inicial_generado_con_informacion_limitada

## Base utilizada
"""
    for f in found_files:
        output_content += f"- {f}\n"

    output_content += f"""
## Alcance de esta fase
Esta fase ordena las acciones de marketing necesarias para los próximos 90 días con el fin de validar la propuesta de valor y los canales prioritarios. No sustituye a un calendario editorial detallado, un presupuesto cerrado ni un sistema final de KPIs, los cuales se desarrollarán en fases posteriores.

## Perfil de marketing aplicado
- **Perfil**: {profile['marketing_profile']}

## Objetivo principal del plan de acción
{objetivo_principal}

## Supuestos de trabajo
- **Presupuesto**: {presupuesto}. Se asume que este monto (si está informado) es el límite inicial para acciones de validación.
- **Recursos**: Pendiente de confirmar equipo humano y herramientas disponibles.
- **Canales**: Se asumen como válidos los canales prioritarios de la Fase 06 para la etapa de prueba.
- **Propuesta**: La propuesta de valor de la Fase 04 se considera una hipótesis a validar en el mercado real.
- **Capacidad operativa**: Se asume capacidad para gestionar al menos un canal prioritario de forma constante.

## Prioridades estratégicas de los 90 días
1. **Consolidar la base estratégica**: Asegurar que los mensajes de '{servicio_principal}' resuenan con el problema '{problema_principal}'.
2. **Activación de visibilidad controlada**: Iniciar presencia en los canales prioritarios para recoger señales de interés.
3. **Validación cualitativa**: Documentar objeciones y dudas reales de los clientes potenciales para ajustar la oferta.
4. **Preparación de activos mínimos**: Crear las piezas básicas necesarias para operar en los canales seleccionados.

## Tácticas prioritarias según perfil ({profile['marketing_profile']})
{tactical_block}
## Plan por etapas

### Días 1 a 30 - Preparación y claridad
- **Revisión profunda**: Validar la propuesta de valor con al menos 3 contactos de confianza o clientes pasados (entrevistas cualitativas).
- **Ajuste de mensajes**: Adaptar los mensajes base de la Fase 07 según el feedback inicial.
- **Preparación de activos**: Crear los materiales básicos necesarios para los canales prioritarios de la Fase 06.
- **Identificación de contactos**: Listar personas dentro del segmento '{cliente_objetivo}' para iniciar las primeras interacciones.
- **Validación de restricciones**: Confirmar si existen impedimentos legales o técnicos para la ejecución del plan.

### Días 31 a 60 - Activación inicial
- **Activación del canal prioritario #1**: Iniciar las primeras acciones en el canal principal de la Fase 06.
- **Presencia básica**: Asegurar visibilidad mínima en los canales secundarios de apoyo.
- **Prueba de Mensajes**: Utilizar los mensajes de la Fase 07 en interacciones reales y documentar el nivel de respuesta.
- **Recogida de señales**: Registrar qué beneficios de '{servicio_principal}' generan más interés y cuáles son ignorados.
- **Gestión de objeciones**: Aplicar las respuestas diseñadas en la Fase 07 y anotar nuevas objeciones no previstas.

### Días 61 a 90 - Ajuste y consolidación
- **Análisis de señales**: Evaluar qué canal de la Fase 06 ha mostrado mayor potencial de conversión.
- **Refinamiento de la oferta**: Ajustar el servicio principal si el mercado demanda variaciones específicas.
- **Priorización de recursos**: Decidir si se aumenta el esfuerzo en el canal principal o se exploran alternativas según resultados.
- **Preparación del siguiente ciclo**: Definir necesidades de presupuesto real basándose en los costes de estos primeros 90 días.
- **Base para KPIs**: Definir métricas definitivas (conversión, coste de adquisición) para el segundo trimestre.

## Acciones por canal prioritario
Basado en la Fase 06 y perfil ({profile['marketing_profile']}):

{actions_block}
## Acciones para resolver vacíos detectados
- **Vacío: Falta de evidencia (Testimonios/Casos)**: Durante los primeros 60 días, documentar el proceso con algún cliente actual para crear un "minicaso" de éxito.
- **Vacío: Cliente demasiado amplio**: Las entrevistas de los días 1-30 deben servir para elegir un sub-segmento aún más específico.
- **Vacío: Información de competencia**: Dedicar 4 horas en el mes 1 a buscar y documentar la presencia de 3 competidores directos.
- **Vacío: Ajuste de presupuesto**: Validar el coste de las herramientas mínimas antes del día 30.

## Entregables esperados al final de los 90 días
- Propuesta de valor ajustada con feedback real del mercado.
- Matriz de canales revisada (confirmando o descartando prioridades).
- Lista de objeciones reales y sus mejores respuestas probadas.
- Al menos 3 señales claras de interés procedentes de los canales activados.
- Base documentada para la creación del presupuesto y KPIs definitivos (Fase 09).

## Riesgos del plan de acción
- **Dispersión**: Intentar activar demasiados canales a la vez sin recursos suficientes.
- **Falta de seguimiento**: Conseguir contactos pero no realizar el seguimiento adecuado.
- **Parálisis por análisis**: Dedicar demasiado tiempo a la preparación y poco a la activación real.
- **No documentar**: Perder los aprendizajes de las interacciones negativas con clientes potenciales.

## Qué no incluye este plan todavía
- Calendario editorial detallado con fechas y contenidos finales.
- Producción de piezas finales (videos, diseños complejos, landing pages).
- Presupuesto de inversión publicitaria cerrado.
- Dashboard de KPIs definitivo con métricas de rendimiento histórico.
- Automatización de procesos de marketing o ventas.

## Recomendación para la siguiente fase
09_presupuesto_marketing
"""

    output_file = os.path.join(output_dir, "08_plan_accion_90_dias.md")
    write_markdown_file(output_file, output_content)

    return output_file

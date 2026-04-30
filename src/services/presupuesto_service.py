# File: src/services/presupuesto_service.py
# ──────────────────────────────────────────────────────────────────────
# Propósito: Generar el documento de presupuesto de marketing inicial.
# Rol: Servicio de planificación financiera (Fase 09).
# ──────────────────────────────────────────────────────────────────────

import os
import re
from src.utils.markdown_utils import read_markdown_file, write_markdown_file, extract_brief_fields
from src.utils.project_io import get_context_path, get_plan_actual_path, ensure_file_exists
from src.core.marketing_profile_resolver import resolve_marketing_profile


def generate_presupuesto_output(project_name: str) -> str:
    """
    Genera el documento de Presupuesto de Marketing (Fase 09).
    Verifica que la Fase 08 esté completa.
    Usa el perfil de marketing para adaptar las partidas presupuestarias.
    """
    output_dir = get_plan_actual_path(project_name)
    context_dir = get_context_path(project_name)

    # 1. Verificar Fase 08
    phase_08_path = os.path.join(output_dir, "08_plan_accion_90_dias.md")
    ensure_file_exists(
        phase_08_path,
        f"No se puede generar la Fase 09. El archivo '{phase_08_path}' no existe. "
        "Primero debe ejecutar la Fase 08 (generate-plan-accion-output)."
    )

    # 2. Recopilar información

    brief_path = os.path.join(context_dir, "brief_negocio.md")
    brief_data = extract_brief_fields(read_markdown_file(brief_path)) if os.path.exists(brief_path) else {}
    profile = resolve_marketing_profile(brief_data)

    presupuesto_declarado = brief_data.get("presupuesto_marketing", "No informado")

    evaluacion_presupuesto = ""
    if presupuesto_declarado in ["No informado", "[No informado]"]:
        evaluacion_presupuesto = "Presupuesto no informado. Se recomienda una asignación mínima para validación cualitativa."
    else:
        evaluacion_presupuesto = f"Presupuesto declarado de '{presupuesto_declarado}'. Se considera una base inicial pendiente de validar frente a los costes reales de adquisición."

    found_files = [
        "01_brief_negocio_validado.md", "02_diagnostico_marketing.md",
        "03_cliente_objetivo_y_segmentos.md", "04_propuesta_valor_y_posicionamiento.md",
        "05_analisis_competencia.md", "06_matriz_canales_marketing.md",
        "07_estrategia_comunicacion.md", "08_plan_accion_90_dias.md", "brief_negocio.md",
    ]
    if os.path.exists(os.path.join(context_dir, "restricciones.md")):
        found_files.append("restricciones.md")

    # 3. Construir partidas presupuestarias según perfil
    partidas_block = """### 1. Preparación de activos mínimos
- **Objetivo**: Crear o mejorar los materiales de comunicación básicos necesarios para los canales seleccionados.
- **Prioridad**: Alta.
- **Coste estimado**: Bajo / Medio (dependiendo de si se hace internamente o se externaliza).
- **Justificación**: Es la base necesaria para cualquier acción de captación.
- **Riesgo si no se contempla**: Imagen poco profesional y mensajes inconsistentes.

### 2. Herramientas básicas
- **Objetivo**: Cubrir costes de herramientas de gestión, reserva o comunicación con clientes.
- **Prioridad**: Media.
- **Coste estimado**: Bajo.
- **Justificación**: Aumenta la eficiencia en la ejecución del plan de acción.
- **Riesgo si no se contempla**: Trabajo manual excesivo y falta de registro.

"""

    for i, channel in enumerate(profile["recommended_channel_families"], start=3):
        partidas_block += f"""### {i}. Acciones en canal: {channel['name']}
- **Objetivo**: Cubrir costes asociados a la activación y mantenimiento de '{channel['name']}'.
- **Prioridad**: Alta.
- **Coste estimado**: {channel['cost']}
- **Justificación**: Es uno de los canales prioritarios para el perfil '{profile['marketing_profile']}'.
- **Riesgo si no se contempla**: No generar flujo de interés por este canal.

"""

    last_num = 3 + len(profile["recommended_channel_families"])
    partidas_block += f"""### {last_num}. Reserva para ajustes y aprendizaje
- **Objetivo**: Fondo para corregir piezas de comunicación o probar variaciones de mensaje.
- **Prioridad**: Media.
- **Coste estimado**: Bajo (10-15% del total).
- **Justificación**: Permite reaccionar a las señales negativas del mercado sin bloquear el plan.
- **Riesgo si no se contempla**: Rigidez ante el feedback del mercado.
"""

    # 4. Documento completo
    output_content = f"""# 09 - Presupuesto de Marketing

## Estado del presupuesto
presupuesto_inicial_generado_con_informacion_limitada

## Base utilizada
"""
    for f in found_files:
        output_content += f"- {f}\n"

    output_content += f"""
## Alcance de esta fase
Esta fase organiza un presupuesto inicial y prudente basado en la información disponible. No valida precios reales de mercado ni sustituye una planificación financiera completa. Su objetivo es asegurar que los recursos se asignen de forma estratégica a las tareas de validación de los primeros 90 días.

## Perfil de marketing aplicado
- **Perfil**: {profile['marketing_profile']}

## Presupuesto declarado
{presupuesto_declarado}

## Evaluación inicial del presupuesto
{evaluacion_presupuesto}

## Principios de asignación presupuestaria
- **Priorización de la validación**: Antes de invertir en escalar, el presupuesto debe enfocarse en validar que el mensaje resuena con el cliente.
- **Evitar la dispersión**: No asignar fondos a más de 2 canales simultáneamente si el presupuesto es limitado.
- **Reserva para el aprendizaje**: Guardar una parte del presupuesto para realizar ajustes basados en el feedback de los primeros 30 días.
- **Inversión en activos**: Priorizar gastos que dejen un activo reutilizable (materiales base, perfiles optimizados, contenidos).
- **Cero inversión en pago sin validación**: No se recomienda invertir en anuncios pagados hasta que los canales orgánicos hayan mostrado señales claras de interés.

## Partidas presupuestarias sugeridas

{partidas_block}
## Distribución inicial recomendada
"""
    if presupuesto_declarado in ["No informado", "[No informado]"]:
        output_content += """Como no se dispone de un presupuesto informado, se recomienda la siguiente distribución cualitativa:
- **Principal (40%)**: Preparación de activos y mensajes base (Fase 07).
- **Secundario (30%)**: Acciones directas en el canal prioritario #1.
- **Soporte (20%)**: Herramientas mínimas de ejecución.
- **Reserva (10%)**: Ajustes según feedback cualitativo.
"""
    else:
        output_content += f"""Basado en el presupuesto de '{presupuesto_declarado}', se propone la siguiente distribución provisional:
- **40% Preparación de activos y mensajes**: Garantizar que la base estratégica es sólida.
- **30% Acciones de canal prioritario**: Ejecución táctica del plan de 90 días.
- **20% Herramientas y pruebas**: Optimización de la operativa.
- **10% Reserva de ajuste**: Margen para cambios según resultados iniciales.
"""

    output_content += """
## Presupuesto por fase de 90 días

### Días 1 a 30: Preparación e Inversión en activos
- Foco: Gasto concentrado en la creación de materiales y adecuación de canales.
- Objetivo: Tener la "caja de herramientas" lista.

### Días 31 a 60: Activación y Gasto Operativo
- Foco: Gasto en herramientas y tiempo dedicado a la activación de canales.
- Objetivo: Empezar a generar interacciones reales.

### Días 61 a 90: Ajuste y Validación
- Foco: Reasignación de remanentes hacia el canal que haya mostrado mejor señal.
- Objetivo: Validar la viabilidad financiera del modelo de captación.

## Gastos que no se recomiendan todavía
- **Campañas pagadas (Ads)**: Hasta no tener un mensaje que convierta en orgánico o directo.
- **Producción audiovisual compleja**: Vídeos corporativos caros o diseños de alta gama antes de validar la oferta.
- **Herramientas de automatización avanzadas**: No automatizar procesos que aún no se han realizado manualmente con éxito.
- **Contratación de agencias externas**: Se recomienda validación interna previa antes de delegar la ejecución.

## Información faltante para cerrar presupuesto
- Coste real de las herramientas actuales que ya se están pagando.
- Disponibilidad real de horas del equipo interno para ejecutar el plan de acción.
- Coste de producción estimado para los materiales de apoyo (si se requiere ayuda externa).
- Margen de contribución esperado por cada venta del servicio principal.
- Valor de vida del cliente (LTV) estimado para calcular el CPA máximo aceptable.

## Riesgos presupuestarios
- **Presupuesto insuficiente**: Que el monto declarado no cubra las herramientas mínimas necesarias.
- **Dispersión de gasto**: Gastar en "pequeñas cosas" que no impactan directamente en la captación.
- **Falta de medición**: No registrar el tiempo o dinero invertido frente a los resultados obtenidos.
- **Inversión temprana**: Gastar en canales secundarios antes de dominar el primario.

## Recomendación para la siguiente fase
10_kpis_y_medicion
"""

    output_file = os.path.join(output_dir, "09_presupuesto_marketing.md")
    write_markdown_file(output_file, output_content)

    return output_file

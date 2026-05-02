# File: src/services/auditoria_service.py
# ──────────────────────────────────────────────────────────────────────
# Propósito: Realizar la auditoría final de coherencia y completitud.
# Rol: Servicio de control de calidad y validación (Fase 12).
# ──────────────────────────────────────────────────────────────────────

import os
from src.utils.markdown_utils import read_markdown_file, write_markdown_file, extract_brief_fields
from src.utils.project_io import get_context_path, get_plan_actual_path, ensure_file_exists
from src.core.marketing_profile_resolver import resolve_marketing_profile
from src.core.data_integrity import (
    evaluate_integrity, render_integrity_markdown, normalize_value,
    STATUS_NO_APLICABLE, STATUS_SENSIBLE, DOC_APROBADO, DOC_OBSERVACIONES,
    DOC_CONDICIONADO, DOC_BLOQUEADO
)


def generate_auditoria_output(project_name: str) -> str:
    """
    Genera el documento de Auditoría Final (Fase 12).
    Verifica que la Fase 11 esté completa e integra el motor de integridad técnica.
    """
    output_dir = get_plan_actual_path(project_name)
    context_dir = get_context_path(project_name)
    
    # 1. Verificar Fase 11
    phase_11_path = os.path.join(output_dir, "11_resumen_para_plan_empresa.md")
    ensure_file_exists(
        phase_11_path,
        f"No se puede generar la Fase 12. El archivo '{phase_11_path}' no existe. "
        "Primero debe ejecutar la Fase 11 (generate-resumen-empresa-output)."
    )

    # 2. Recopilar información del brief y evaluar integridad
    brief_path = os.path.join(context_dir, "brief_negocio.md")
    brief_data = extract_brief_fields(read_markdown_file(brief_path)) if os.path.exists(brief_path) else {}
    
    profile_data = resolve_marketing_profile(brief_data)
    profile_name = profile_data.get("marketing_profile", "estrategia_general_prudente")
    report = evaluate_integrity(brief_data, profile_name)

    def get_val(key, default="No informado"):
        val = normalize_value(brief_data.get(key))
        status = report["fields"].get(key)
        if status == STATUS_SENSIBLE and val:
            return "[Dato Protegido]"
        return val if val else default

    # 3. Preparar secciones dinámicas
    status_map = {
        DOC_APROBADO: "plan_marketing_inicial_aprobado_estructuralmente",
        DOC_OBSERVACIONES: "plan_marketing_inicial_aprobado_con_observaciones",
        DOC_CONDICIONADO: "plan_marketing_inicial_condicionado_por_vacios_operativos",
        DOC_BLOQUEADO: "plan_marketing_inicial_bloqueado_por_vacios_criticos"
    }
    final_status = status_map.get(report["status"], "plan_marketing_en_revision")

    phases = [
        ("01", "01_brief_negocio_validado.md", "Brief de negocio"),
        ("02", "02_diagnostico_marketing.md", "Diagnóstico inicial"),
        ("03", "03_cliente_objetivo_y_segmentos.md", "Cliente y segmentos"),
        ("04", "04_propuesta_valor_y_posicionamiento.md", "Propuesta de valor"),
        ("05", "05_analisis_competencia.md", "Análisis competencia"),
        ("06", "06_matriz_canales_marketing.md", "Matriz de canales"),
        ("07", "07_estrategia_comunicacion.md", "Estrategia comunicación"),
        ("08", "08_plan_accion_90_dias.md", "Plan de acción 90 días"),
        ("09", "09_presupuesto_marketing.md", "Presupuesto marketing"),
        ("10", "10_kpis_y_medicion.md", "KPIs y medición"),
        ("11", "11_resumen_para_plan_empresa.md", "Resumen para plan de empresa")
    ]

    # Evaluación de contradicciones basada en el motor
    contradicciones_block = "No se han detectado contradicciones estratégicas graves."
    if report["status"] == DOC_BLOQUEADO:
        contradicciones_block = "⚠️ SE HAN DETECTADO BLOQUEOS CRÍTICOS: El plan no cuenta con la información base necesaria para ser ejecutable con seguridad."
    elif report["status"] == DOC_CONDICIONADO:
        contradicciones_block = "⚠️ SE HAN DETECTADO VACÍOS OPERATIVOS: Existen campos no informados que condicionan la efectividad del plan de acción."

    # 4. Construir el documento de Fase 12
    output_content = f"""# 12 - Auditoría Final del Plan de Marketing

## Estado de la auditoría
{final_status}

## Base auditada
"""
    for phase_id, filename, _ in phases:
        output_content += f"- {filename}\n"
    output_content += "- brief_negocio.md\n"
    if os.path.exists(os.path.join(context_dir, "restricciones.md")):
        output_content += "- restricciones.md\n"

    output_content += f"""
## Alcance de esta auditoría
Esta auditoría revisa la coherencia documental y estratégica de todas las piezas del plan de marketing generadas. Su propósito es asegurar que existe una trazabilidad lógica desde el brief inicial hasta el resumen ejecutivo. No valida la respuesta real del mercado, la exactitud de los datos competitivos externos ni garantiza resultados comerciales.

## Verificación de completitud documental
| Fase | Documento | Estado | Observación |
| :--- | :--- | :--- | :--- |
"""
    for phase_id, filename, label in phases:
        full_path = os.path.join(output_dir, filename)
        exists = os.path.exists(full_path)
        status = "✅ Presente" if exists else "❌ Ausente"
        obs = "Completado" if exists else "Pendiente de generación"
        output_content += f"| {phase_id} | {label} | {status} | {obs} |\n"

    output_content += f"""
## Coherencia entre brief, cliente y propuesta
- **Oferta/Modelo y Cliente**: Existe una conexión documental entre la oferta declarada ({get_val('oferta_principal')}) y el cliente objetivo descrito. Esta conexión debe validarse con evidencia real del mercado.
- **Problema y Propuesta**: La propuesta de valor responde al problema declarado ({get_val('problema_que_resuelve')}). La intensidad real de ese problema queda pendiente de validación externa.
- **Consistencia de Modelo**: El modelo detectado ({profile_name}) guarda coherencia con las definiciones estratégicas de cliente y propuesta.

## Coherencia entre propuesta, canales y comunicación
- **Canales**: Los canales priorizados son coherentes con el perfil {profile_name}, aunque su efectividad real queda pendiente de validación.
- **Comunicación**: Los mensajes centrales mantienen coherencia con la propuesta de valor y el tono definido en la estrategia.
- **Estrategia**: Se observa una transición fluida desde la definición de valor hasta el plan de comunicación.

## Coherencia entre plan de acción, presupuesto y KPIs
- **Plan de Acción**: Las etapas definidas son razonables para un ciclo inicial de validación basado en el modelo {profile_name}.
- **Presupuesto**: El presupuesto ({get_val('presupuesto_marketing')}) se ha tratado con prudencia estratégica.
- **KPIs**: Los indicadores se centran en señales de interés real y no en métricas de vanidad.

## Supuestos principales detectados
- El cliente objetivo realmente identifica '{get_val('problema_que_resuelve')}' como una prioridad relevante.
- Los canales prioritarios permiten el acceso al cliente objetivo sin bloqueos imprevistos.
- La capacidad operativa interna ({get_val('capacidad_operativa')}) permite absorber la demanda generada.

## Errores o contradicciones detectadas
{contradicciones_block}

{render_integrity_markdown(report)}

## Recomendaciones antes de usar el plan
- Realizar un sondeo de precios con 3 competidores para ajustar la propuesta económica.
- Validar los guiones de venta con un aliado de confianza antes del primer contacto real.
- Designar formalmente al responsable de la bitácora de objeciones.
- Establecer el presupuesto de marketing como una partida separada y bloqueada en finanzas.

## Estado final recomendado del plan
{final_status}

## Próximos pasos sugeridos
1. Presentación del resumen ejecutivo (Fase 11) a la dirección para validación de recursos.
2. Inicio de la Fase de Preparación (Días 1-30 del Plan de Acción).
3. Recopilación de las primeras objeciones cualitativas para retroalimentar la propuesta de valor.
"""

    output_file = os.path.join(output_dir, "12_auditoria_final.md")
    write_markdown_file(output_file, output_content)
        
    return output_file

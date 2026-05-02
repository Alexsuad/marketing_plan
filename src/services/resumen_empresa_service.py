# File: src/services/resumen_empresa_service.py
# ──────────────────────────────────────────────────────────────────────
# Propósito: Generar el resumen ejecutivo de marketing para el plan de empresa.
# Rol: Servicio de síntesis estratégica (Fase 11).
# ──────────────────────────────────────────────────────────────────────

import os
from src.utils.markdown_utils import read_markdown_file, write_markdown_file, extract_brief_fields
from src.utils.project_io import get_context_path, get_plan_actual_path, ensure_file_exists
from src.core.marketing_profile_resolver import resolve_marketing_profile
from src.core.data_integrity import (
    evaluate_integrity, render_integrity_markdown, normalize_value,
    STATUS_NO_APLICABLE, STATUS_SENSIBLE
)


def generate_resumen_empresa_output(project_name: str) -> str:
    """
    Genera el documento de Resumen para Plan de Empresa (Fase 11).
    Verifica que la Fase 10 esté completa.
    Usa el perfil de marketing para adaptar canales y tono del resumen.
    """
    output_dir = get_plan_actual_path(project_name)
    context_dir = get_context_path(project_name)

    # 1. Verificar Fase 10
    phase_10_path = os.path.join(output_dir, "10_kpis_y_medicion.md")
    ensure_file_exists(
        phase_10_path,
        f"No se puede generar la Fase 11. El archivo '{phase_10_path}' no existe. "
        "Primero debe ejecutar la Fase 10 (generate-kpis-output)."
    )

    # 2. Recopilar información
    brief_path = os.path.join(context_dir, "brief_negocio.md")
    brief_data = extract_brief_fields(read_markdown_file(brief_path)) if os.path.exists(brief_path) else {}
    
    # Resolver perfil y evaluar integridad
    profile_data = resolve_marketing_profile(brief_data)
    profile_name = profile_data.get("marketing_profile", "estrategia_general_prudente")
    report = evaluate_integrity(brief_data, profile_name)

    def get_val(key, default="No informado"):
        status = report["fields"].get(key)
        if status == STATUS_NO_APLICABLE:
            return "No aplica a este modelo"
        
        val = normalize_value(brief_data.get(key))
        
        if status == STATUS_SENSIBLE and val:
            return "[Dato Protegido - Uso Interno]"
        
        return val if val else default

    nombre = get_val("nombre_negocio")
    tipo = get_val("tipo_negocio")
    oferta = get_val("oferta_principal")
    cliente = get_val("cliente_objetivo")
    problema = get_val("problema_que_resuelve")
    presupuesto = get_val("presupuesto_marketing")

    # Construir canales prioritarios desde perfil
    canales_block = ""
    for i, ch in enumerate(profile_data.get("recommended_channel_families", []), start=1):
        canales_block += f"{i}. **{ch['name']}**: {ch['objective']}\n"

    # Construir tono desde perfil
    tone_parts = []
    for g in profile_data.get("tone_guidelines", []):
        parts = g.split(":", 1)
        tone_parts.append(parts[0].strip() if len(parts) >= 1 else g)
    tone_summary = ", ".join(tone_parts[:3])

    found_files = [
        "01_brief_negocio_validado.md", "02_diagnostico_marketing.md",
        "03_cliente_objetivo_y_segmentos.md", "04_propuesta_valor_y_posicionamiento.md",
        "05_analisis_competencia.md", "06_matriz_canales_marketing.md",
        "07_estrategia_comunicacion.md", "08_plan_accion_90_dias.md",
        "09_presupuesto_marketing.md", "10_kpis_y_medicion.md", "brief_negocio.md",
    ]
    if os.path.exists(os.path.join(context_dir, "restricciones.md")):
        found_files.append("restricciones.md")

    # Generar sección de integridad
    integrity_section = render_integrity_markdown(report)

    output_content = f"""# 11 - Resumen para Plan de Empresa

## Estado del resumen
{report['status']}

## Base utilizada
"""
    for f in found_files:
        output_content += f"- {f}\n"

    output_content += f"""
## Alcance de esta fase
Este documento resume únicamente los componentes estratégicos y tácticos del área de marketing desarrollados hasta la fecha. No sustituye ni constituye el Plan de Empresa completo, sino que sirve como input para las secciones de mercado, comercialización y proyecciones de marketing dentro del mismo.

## Perfil de marketing aplicado
- **Perfil**: {profile_name}
- **Motivo**: {profile_data.get('profile_reason', 'N/A')}

## Resumen ejecutivo de marketing
El plan de marketing para **{nombre}** se centra en establecer una base sólida de comunicación y captación para la oferta de **{oferta}**. La estrategia prioriza la validación cualitativa de los mensajes y la construcción de activos mínimos antes de escalar la inversión, asegurando que cada recurso invertido contribuya al aprendizaje sobre el mercado.

## Cliente objetivo y segmento prioritario
- **Cliente objetivo**: {cliente}
- **Segmento prioritario**: Personas o entidades que experimentan '{problema}' y valoran la especialización y la confianza en el proveedor.

## Problema de mercado que se busca resolver
Se ha identificado que el cliente objetivo experimenta '{problema}'. La lectura inicial indica una oportunidad para una propuesta de valor enfocada en la claridad, la cercanía y el resultado tangible.

## Propuesta de valor inicial
La propuesta de valor se basa en resolver el problema central mediante un enfoque de **{oferta}** que destaca por su adaptabilidad y enfoque en el beneficio directo para el cliente. Es una propuesta preliminar sujeta a ajustes basados en el feedback real del mercado durante los primeros 90 días.

## Posicionamiento inicial
{nombre} busca posicionarse como un referente especializado en **{oferta}**, alejándose de los proveedores generalistas por precio y compitiendo mediante la calidad percibida, la resolución del problema central y el dominio del área de **{tipo}**.

## Canales de marketing prioritarios
Se han seleccionado los siguientes canales basándose en el perfil de marketing ({profile_name}):
{canales_block}
## Estrategia de comunicación
- **Tono**: {tone_summary}.
- **Mensaje central**: Resolver '{problema}' de forma accesible, segura y eficaz a través de '{oferta}'.
- **Pilares**: Especialización, confianza, transparencia y resultados.

## Plan de acción resumido
El plan de 90 días se divide en tres etapas críticas:
- **Días 1 a 30 (Preparación)**: Creación de activos base, preparación de canales prioritarios y configuración del sistema de seguimiento.
- **Días 31 a 60 (Activación)**: Inicio de acciones en los canales prioritarios y registro de las primeras señales del mercado.
- **Días 61 a 90 (Aprendizaje y ajuste)**: Análisis cualitativo de las objeciones, optimización de los mensajes y consolidación de las primeras oportunidades.

## Presupuesto de marketing inicial
- **Presupuesto declarado**: {presupuesto}
- **Distribución inicial**: Se prioriza la inversión en activos mínimos y una reserva de aprendizaje para ajustes tácticos, manteniendo un perfil de gasto prudente.

## Datos Financieros (Uso Interno)
- **Margen Bruto**: {get_val("margen_bruto")}

## KPIs principales
- **Tasa de respuesta cualificada**: Interés real detectado en las interacciones realizadas.
- **Número de conversiones iniciales**: Avance de clientes potenciales hacia la compra, reserva o contrato.
- **Resolución de objeciones**: Validación de que el mensaje está penetrando en el mercado.

## Supuestos y validaciones pendientes
- El cliente objetivo realmente identifica '{problema}' como una prioridad relevante.
- Los canales elegidos permiten el acceso al cliente sin intermediarios costosos.
- La propuesta de valor es percibida como diferenciada frente a competidores directos ya establecidos.

## Riesgos principales del marketing
- **Cliente muy amplio**: Dificultad para personalizar el mensaje si no se segmenta más en la ejecución.
- **Falta de evidencia**: La propuesta todavía no cuenta con casos de éxito documentados bajo este nuevo plan.
- **Canales sin validar**: Dependencia de canales que no han sido probados históricamente para esta oferta concreta.
- **Propuesta preliminar**: Riesgo de que el mercado demande algo ligeramente distinto a lo planificado inicialmente.

## Dependencias con otras áreas del Plan de Empresa
- **Finanzas**: El presupuesto de marketing debe ser validado contra el flujo de caja global.
- **Operaciones**: El éxito del marketing aumentará la demanda; operaciones debe estar listo para la entrega de la oferta.
- **Ventas**: Los leads generados por marketing deben ser procesados por un flujo coherente con la propuesta de valor.
- **Recursos Humanos**: Evaluar si el equipo actual puede ejecutar las acciones de marketing o si requiere apoyo externo.

## Integridad de Datos
{integrity_section}

## Recomendación para la siguiente fase
12_auditoria_final
"""

    output_file = os.path.join(output_dir, "11_resumen_para_plan_empresa.md")
    write_markdown_file(output_file, output_content)

    return output_file

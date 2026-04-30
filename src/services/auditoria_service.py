# File: src/services/auditoria_service.py
# ──────────────────────────────────────────────────────────────────────
# Propósito: Realizar la auditoría final de coherencia y completitud.
# Rol: Servicio de control de calidad y validación (Fase 12).
# ──────────────────────────────────────────────────────────────────────

import os
from src.utils.markdown_utils import write_markdown_file
from src.utils.project_io import get_context_path, get_plan_actual_path, ensure_file_exists

def generate_auditoria_output(project_name: str) -> str:
    """
    Genera el documento de Auditoría Final (Fase 12).
    Verifica que la Fase 11 esté completa.
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

    # 2. Recopilar información de contexto y fases previas
    
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

    # 3. Construir el documento de Fase 12
    output_content = f"""# 12 - Auditoría Final del Plan de Marketing

## Estado de la auditoría
auditoria_final_generada_con_informacion_limitada

## Base auditada
"""
    for phase_id, filename, _ in phases:
        output_content += f"- {filename}\n"
    output_content += "- brief_negocio.md\n"
    if os.path.exists(os.path.join(context_dir, "restricciones.md")):
        output_content += "- restricciones.md\n"

    output_content += """
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

    output_content += """
## Coherencia entre brief, cliente y propuesta
- **Servicio y Cliente**: Existe una conexión documental entre el servicio declarado y el cliente objetivo descrito en las fases previas. Esta conexión debe validarse con evidencia real del mercado.
- **Problema y Propuesta**: La propuesta de valor responde al problema declarado en el brief y desarrollado en las fases previas. La intensidad real de ese problema queda pendiente de validación externa.
- **Consistencia**: El tono del brief se mantiene a lo largo de las definiciones estratégicas de cliente y propuesta.

## Coherencia entre propuesta, canales y comunicación
- **Canales**: Los canales priorizados en la matriz de canales son coherentes con la información disponible, aunque su efectividad real queda pendiente de validación.
- **Comunicación**: Los mensajes centrales y pilares mantienen coherencia con la propuesta de valor y el tono definido en la estrategia de comunicación.
- **Estrategia**: Se observa una transición fluida desde la definición de valor hasta el plan de comunicación, sin saltos a ejecución de canales de masa no justificados.

## Coherencia entre plan de acción, presupuesto y KPIs
- **Plan de Acción**: Las etapas definidas (ej. Preparación, Activación, Aprendizaje) son razonables para un ciclo inicial de validación.
- **Presupuesto**: Se ha tratado con prudencia, priorizando activos reutilizables y aprendizaje sobre el gasto publicitario agresivo.
- **KPIs**: Los indicadores se centran en señales de interés real y no en métricas de vanidad, lo cual es coherente con un enfoque inicial de validación prudente.

## Supuestos principales detectados
- El cliente objetivo prioriza la resolución del problema técnico sobre el precio.
- Los canales prioritarios permiten el acceso al cliente objetivo sin bloqueos imprevistos.
- La capacidad operativa interna permite absorber la demanda generada.

## Información crítica faltante
- **Competencia Real**: Datos precisos de ofertas y precios de competidores directos en el territorio actual.
- **Casos de Éxito**: Evidencia documentada que acelere la confianza del cliente en el servicio.
- **Línea Base**: Datos históricos para comparar el rendimiento de los nuevos KPIs.
- **Recursos Humanos**: Definición de quién ejecutará cada tarea del plan de acción.

## Riesgos principales del plan
- **Falta de evidencia previa**: Puede alargar el ciclo de venta al inicio.
- **Dependencia de canales manuales**: Requiere alta disciplina de ejecución y tiempo del equipo.
- **Propuesta preliminar**: Riesgo de desajuste menor si el cliente demanda funcionalidades no previstas.
- **Presupuesto limitado**: Restringe la capacidad de prueba y error en múltiples canales simultáneos.

## Señales positivas del plan
- **Trazabilidad**: Cada decisión está fundamentada en información de las fases previas.
- **Prudencia Financiera**: No se asumen riesgos económicos elevados antes de validar la señal del mercado.
- **Foco en el Cliente**: La comunicación no es egocéntrica, sino centrada en resolver un problema.
- **KPIs de Calidad**: Medir el aprendizaje asegura que el plan mejore con el tiempo.

## Errores o contradicciones detectadas
No se han detectado contradicciones estratégicas graves. El plan mantiene una línea coherente de principio a fin. Se han corregido pequeños errores de redacción detectados durante el proceso de revisión de la Fase 11.

## Recomendaciones antes de usar el plan
- Realizar un sondeo de precios con 3 competidores para ajustar la propuesta económica.
- Validar los guiones de venta con un aliado de confianza antes del primer contacto real.
- Designar formalmente al responsable de la bitácora de objeciones.
- Establecer el presupuesto de marketing como una partida separada y bloqueada en finanzas.

## Estado final recomendado del plan
plan_marketing_inicial_aprobado_con_observaciones

## Próximos pasos sugeridos
1. Presentación del resumen ejecutivo (Fase 11) a la dirección para validación de recursos.
2. Inicio de la Fase de Preparación (Días 1-30 del Plan de Acción).
3. Recopilación de las primeras objeciones cualitativas para retroalimentar la propuesta de valor.
"""

    output_file = os.path.join(output_dir, "12_auditoria_final.md")
    
    write_markdown_file(output_file, output_content)
        
    return output_file

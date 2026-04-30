# File: src/services/kpis_service.py
# ──────────────────────────────────────────────────────────────────────
# Propósito: Generar el documento de KPIs y Medición inicial.
# Rol: Servicio de análisis y métricas (Fase 10).
# ──────────────────────────────────────────────────────────────────────

import os
import re
from src.utils.markdown_utils import read_markdown_file, write_markdown_file, extract_brief_fields
from src.utils.project_io import get_context_path, get_plan_actual_path, ensure_file_exists
from src.core.marketing_profile_resolver import resolve_marketing_profile


def generate_kpis_output(project_name: str) -> str:
    """
    Genera el documento de KPIs y Medición (Fase 10).
    Verifica que la Fase 09 esté completa.
    Usa el perfil de marketing para adaptar indicadores por canal.
    """
    output_dir = get_plan_actual_path(project_name)
    context_dir = get_context_path(project_name)

    # 1. Verificar Fase 09
    phase_09_path = os.path.join(output_dir, "09_presupuesto_marketing.md")
    ensure_file_exists(
        phase_09_path,
        f"No se puede generar la Fase 10. El archivo '{phase_09_path}' no existe. "
        "Primero debe ejecutar la Fase 09 (generate-presupuesto-output)."
    )

    # 2. Recopilar información

    brief_path = os.path.join(context_dir, "brief_negocio.md")
    brief_data = extract_brief_fields(read_markdown_file(brief_path)) if os.path.exists(brief_path) else {}
    profile = resolve_marketing_profile(brief_data)

    objetivo_principal = brief_data.get("objetivo_principal", "[No informado]")

    found_files = [
        "01_brief_negocio_validado.md", "02_diagnostico_marketing.md",
        "03_cliente_objetivo_y_segmentos.md", "04_propuesta_valor_y_posicionamiento.md",
        "05_analisis_competencia.md", "06_matriz_canales_marketing.md",
        "07_estrategia_comunicacion.md", "08_plan_accion_90_dias.md",
        "09_presupuesto_marketing.md", "brief_negocio.md",
    ]
    if os.path.exists(os.path.join(context_dir, "restricciones.md")):
        found_files.append("restricciones.md")

    # 3. Construir indicadores por canal según perfil
    kpis_canal_block = ""
    for channel in profile["recommended_channel_families"]:
        kpis_canal_block += f"""### Canal: {channel['name']}
- **Indicador de esfuerzo**: Número de acciones realizadas en '{channel['name']}' por semana.
- **Indicador de señal**: Número de respuestas o interacciones positivas recibidas.
- **Indicador de resultado**: Número de clientes o reservas generadas por este canal.
- **Frecuencia de revisión**: Semanal o quincenal.
- **Riesgo de mala interpretación**: Confundir actividad (acciones realizadas) con avance real (interés o conversión).

"""

    # 4. Documento completo
    output_content = f"""# 10 - KPIs y Medición

## Estado del sistema de medición
kpis_iniciales_generados_con_informacion_limitada

## Base utilizada
"""
    for f in found_files:
        output_content += f"- {f}\n"

    output_content += f"""
## Alcance de esta fase
Esta fase define los indicadores clave de desempeño (KPIs) y el sistema de medición inicial para evaluar el progreso del plan de marketing. Su propósito es establecer qué medir y cómo registrar los aprendizajes, sin afirmar resultados reales ni crear dashboards automatizados en esta etapa.

## Perfil de marketing aplicado
- **Perfil**: {profile['marketing_profile']}

## Objetivo principal a medir
{objetivo_principal}

## Principios de medición
- **Medir avance real**: Priorizar indicadores que muestren progreso hacia el objetivo frente a indicadores de actividad pura.
- **Evitar métricas de vanidad**: Ignorar likes o seguidores si no tienen una correlación directa con el interés comercial.
- **Jerarquía de indicadores**: Diferenciar claramente entre indicadores de esfuerzo (qué hacemos), señal (qué responde el mercado) y resultado (qué logramos).
- **Medición progresiva**: No intentar medir todo desde el día 1; empezar por lo crítico para la validación cualitativa.
- **Registro cualitativo**: La información más valiosa en los primeros 90 días son los comentarios, dudas y objeciones reales de los clientes.
- **Ciclo de revisión**: Los KPIs deben revisarse y ajustarse al finalizar el primer ciclo de 90 días.

## KPIs principales recomendados

### 1. Tasa de respuesta cualificada
- **Qué mide**: El porcentaje de personas contactadas que muestran un interés real en profundizar en la oferta.
- **Por qué importa**: Valida si el mensaje y el segmento están alineados.
- **Cómo se mediría**: (Contactos interesados / Total contactos realizados).
- **Frecuencia de revisión**: Quincenal.
- **Fuente de datos requerida**: Registro manual de interacciones.
- **Estado actual**: Pendiente de línea base.

### 2. Número de conversiones o reservas iniciales
- **Qué mide**: Volumen de clientes que avanzan desde el interés hasta la acción (compra, reserva, contrato).
- **Por qué importa**: Es el indicador más cercano al objetivo principal del plan.
- **Cómo se mediría**: Conteo simple de conversiones realizadas por canal.
- **Frecuencia de revisión**: Mensual.
- **Fuente de datos requerida**: Registro de ventas o reservas.
- **Estado actual**: Pendiente de línea base.

### 3. Volumen de objeciones críticas resueltas
- **Qué mide**: Capacidad de la comunicación para neutralizar barreras de compra.
- **Por qué importa**: Indica si la propuesta de valor es clara y convincente.
- **Cómo se mediría**: Registro de objeciones repetidas que dejan de aparecer tras ajustar los mensajes.
- **Frecuencia de revisión**: Mensual.
- **Fuente de datos requerida**: Bitácora de aprendizaje cualitativo.
- **Estado actual**: Pendiente de línea base.

### 4. Coste de Adquisición de Lead (CPL) inicial
- **Qué mide**: La inversión necesaria para generar un contacto interesado.
- **Por qué importa**: Ayuda a validar la eficiencia del presupuesto de la Fase 09.
- **Cómo se mediría**: (Inversión en canal / Leads generados).
- **Frecuencia de revisión**: Al final de los 90 días.
- **Fuente de datos requerida**: Control de gastos y registro de leads.
- **Estado actual**: Pendiente de línea base.

## Indicadores por etapa de 90 días

### Días 1 a 30 - Preparación
Indicadores de preparación (cumplimiento):
- **Activos mínimos**: Materiales básicos para canales prioritarios terminados (Sí/No).
- **Mensajes base**: Mensajes para canales prioritarios definidos (Sí/No).
- **Base de contactos**: Lista inicial de clientes potenciales preparada (Conteo).

### Días 31 a 60 - Activación
Indicadores de activación (esfuerzo y señal):
- **Interacciones iniciadas**: Número de contactos o acciones nuevas realizadas.
- **Respuestas recibidas**: Número de personas que mostraron interés.
- **Objeciones registradas**: Listado de dudas recurrentes detectadas.

### Días 61 a 90 - Aprendizaje y ajuste
Indicadores de aprendizaje (calidad):
- **Mejor canal**: Canal con mayor tasa de respuesta positiva.
- **Mejor mensaje**: Variación del mensaje con mejor recepción.
- **Ajustes realizados**: Número de mejoras aplicadas basándose en datos.

## Indicadores por canal prioritario
Basado en la Fase 06 y perfil ({profile['marketing_profile']}):

{kpis_canal_block}
## Métricas que no conviene priorizar todavía
- **Número de seguidores/likes**: No tienen impacto directo en la validación inicial del servicio.
- **Impresiones totales**: Sin segmentación confirmada, es una métrica de vanidad.
- **Tráfico web general**: Interesa el tráfico cualificado, no el volumen bruto.
- **Frecuencia de publicación**: Publicar mucho sin un mensaje validado solo genera ruido.

## Sistema mínimo de seguimiento recomendado
Se recomienda un sistema manual y riguroso antes de cualquier automatización:
1. **Registro de Interacciones**: Una hoja de cálculo simple con: Fecha, Nombre, Canal, Estado, y Notas cualitativas.
2. **Bitácora de Objeciones**: Documento donde se anotan literalmente las frases de rechazo o duda de los clientes potenciales.
3. **Reunión de Revisión Quincenal**: Espacio de 30 minutos para analizar qué está funcionando y qué debe ajustarse.

## Información faltante para medir mejor
- **Línea base actual**: Datos reales de ventas o leads de los últimos 6 meses (si existen).
- **Tasa de conversión histórica**: Cuántas interacciones se realizaron vs cuántas se convirtieron.
- **Margen por cliente**: Para calcular el retorno real de la inversión de marketing.
- **Valor medio por cliente**: Para priorizar canales según el beneficio generado.

## Riesgos de medición
- **Medir actividad y no avance**: Creer que por "estar activo" se está avanzando, sin mirar la tasa de interés real.
- **Métricas excesivas**: Intentar medir 20 cosas y no tomar decisiones sobre ninguna.
- **Falta de rigor en el registro**: No anotar las respuestas negativas, perdiendo el aprendizaje más importante.
- **Conclusiones prematuras**: Cambiar la estrategia con solo 2 o 3 interacciones.

## Recomendación para la siguiente fase
11_resumen_para_plan_empresa
"""

    output_file = os.path.join(output_dir, "10_kpis_y_medicion.md")
    write_markdown_file(output_file, output_content)

    return output_file

# File: src/core/data_integrity.py
# ──────────────────────────────────────────────────────────────────────
# Propósito: Motor determinista de integridad de datos para el brief.
# Rol: Validador de calidad y trazabilidad (v1.6)
# ──────────────────────────────────────────────────────────────────────

import re

# Estados de los datos
STATUS_CONFIRMADO = "confirmado"
STATUS_NO_INFORMADO = "no_informado"
STATUS_NO_APLICABLE = "no_aplicable"
STATUS_SUPUESTO = "supuesto_pendiente_confirmar"
STATUS_SENSIBLE = "sensible_uso_interno"
STATUS_RESUMIDO = "visible_resumido"

# Niveles de visibilidad
VIS_NORMAL = "visible_normal"
VIS_RESUMIDO = "visible_resumido"
VIS_INTERNO = "uso_interno"

# Estados del documento
DOC_APROBADO = "aprobado_estructuralmente"
DOC_OBSERVACIONES = "aprobado_con_observaciones"
DOC_CONDICIONADO = "condicionado_por_vacios_operativos"
DOC_BLOQUEADO = "bloqueado_por_datos_criticos"

# Catálogo Maestro de Reglas
FIELD_RULES = {
    # CORE
    "nombre_negocio": {"cat": "core", "models": "all", "block": True, "vis": VIS_NORMAL, "can_hyp": False, "sev": "Crítica"},
    "tipo_negocio": {"cat": "core", "models": "all", "block": True, "vis": VIS_NORMAL, "can_hyp": False, "sev": "Crítica"},
    "oferta_principal": {"cat": "core", "models": "all", "block": True, "vis": VIS_NORMAL, "can_hyp": False, "phase": "F04", "sev": "Crítica"},
    "cliente_objetivo": {"cat": "core", "models": "all", "block": True, "vis": VIS_NORMAL, "can_hyp": False, "phase": "F03", "sev": "Crítica"},
    "problema_que_resuelve": {"cat": "core", "models": "all", "block": True, "vis": VIS_NORMAL, "can_hyp": False, "phase": "F04", "sev": "Crítica"},
    "objetivo_principal": {"cat": "core", "models": "all", "block": True, "vis": VIS_NORMAL, "can_hyp": False, "phase": "F10", "sev": "Crítica"},
    "zona_geografica": {"cat": "core", "models": "all", "block": True, "vis": VIS_NORMAL, "can_hyp": False, "phase": "F06", "sev": "Crítica"},
    
    # OPERATIVA
    "presupuesto_marketing": {"cat": "oper", "models": "all", "block": False, "vis": VIS_NORMAL, "can_hyp": True, "phase": "F09", "sev": "Alta"},
    "recursos_internos": {"cat": "oper", "models": "all", "block": False, "vis": VIS_NORMAL, "can_hyp": False, "phase": "F08", "sev": "Alta"},
    "tiempo_disponible": {"cat": "oper", "models": "all", "block": False, "vis": VIS_NORMAL, "can_hyp": False, "phase": "F08", "sev": "Alta"},
    "capacidad_operativa": {"cat": "oper", "models": ["servicios", "retail", "educativo", "b2c_local_servicios"], "block": False, "vis": VIS_NORMAL, "can_hyp": False, "phase": "F10", "sev": "Alta"},
    "canales_actuales": {"cat": "oper", "models": "all", "block": False, "vis": VIS_NORMAL, "can_hyp": False, "phase": "F08", "sev": "Media"},
    "restricciones": {"cat": "oper", "models": "all", "block": False, "vis": VIS_INTERNO, "can_hyp": False, "phase": "F12", "sev": "Alta"},
    
    # CONTEXTO
    "competidores_conocidos": {"cat": "cont", "models": "all", "block": False, "vis": VIS_NORMAL, "can_hyp": False, "phase": "F05", "sev": "Media"},
    "activos_existentes": {"cat": "cont", "models": "all", "block": False, "vis": VIS_NORMAL, "can_hyp": False, "phase": "F08", "sev": "Baja"},
    "herramientas_medicion": {"cat": "cont", "models": "all", "block": False, "vis": VIS_NORMAL, "can_hyp": False, "phase": "F10", "sev": "Baja"},
    "desempeno_pasado": {"cat": "cont", "models": "all", "block": False, "vis": VIS_RESUMIDO, "can_hyp": False, "phase": "F10", "sev": "Media"},
    
    # DEEP
    "ticket_promedio": {"cat": "deep", "models": ["ecommerce", "retail", "servicios"], "block": False, "vis": VIS_NORMAL, "can_hyp": True, "phase": "F09", "sev": "Alta"},
    "margen_bruto": {"cat": "deep", "models": ["ecommerce", "producto"], "block": False, "vis": VIS_INTERNO, "can_hyp": False, "phase": "F09", "sev": "Media"},
    "logistica": {"cat": "deep", "models": ["ecommerce", "producto"], "block": False, "vis": VIS_NORMAL, "can_hyp": False, "phase": "F08", "sev": "Media"},
    "ciclo_venta": {"cat": "deep", "models": ["b2b", "consultivo"], "block": False, "vis": VIS_NORMAL, "can_hyp": True, "phase": "F08", "sev": "Alta"},
    "decisores_compra": {"cat": "deep", "models": ["b2b"], "block": False, "vis": VIS_NORMAL, "can_hyp": False, "phase": "F07", "sev": "Alta"},
    "homologacion": {"cat": "deep", "models": ["b2b_producto_industrial"], "block": False, "vis": VIS_NORMAL, "can_hyp": False, "phase": "F04", "sev": "Alta"},
    "radio_influencia": {"cat": "deep", "models": ["retail_fisico", "b2c_local_servicios"], "block": False, "vis": VIS_NORMAL, "can_hyp": False, "phase": "F06", "sev": "Alta"},
    "google_business_profile": {"cat": "deep", "models": ["retail_fisico", "b2c_local_servicios"], "block": False, "vis": VIS_NORMAL, "can_hyp": False, "phase": "F06", "sev": "Media"},
    "modalidad_formativa": {"cat": "deep", "models": ["educativo_formativo"], "block": False, "vis": VIS_NORMAL, "can_hyp": False, "phase": "F07", "sev": "Alta"},
    "sistema_reservas": {"cat": "deep", "models": ["b2c_local_servicios", "educativo", "retail"], "block": False, "vis": VIS_NORMAL, "can_hyp": False, "phase": "F08", "sev": "Media"},
    "modelo_recurrencia": {"cat": "deep", "models": ["hibrido_producto_servicio", "recurrente"], "block": False, "vis": VIS_NORMAL, "can_hyp": False, "phase": "F09", "sev": "Alta"},
    
    # MIXTOS
    "modelo_principal": {"cat": "mixed", "models": "mixed", "block": True, "vis": VIS_NORMAL, "can_hyp": False, "sev": "Crítica"},
    "modelo_secundario": {"cat": "mixed", "models": "mixed", "block": False, "vis": VIS_NORMAL, "can_hyp": False, "sev": "Media"},
    "peso_modelo_principal": {"cat": "mixed", "models": "mixed", "block": False, "vis": VIS_NORMAL, "can_hyp": False, "phase": "F11", "sev": "Alta"},
    "peso_modelo_secundario": {"cat": "mixed", "models": "mixed", "block": False, "vis": VIS_NORMAL, "can_hyp": False, "phase": "F11", "sev": "Alta"},
    "prioridad_90_dias": {"cat": "mixed", "models": "mixed", "block": True, "vis": VIS_NORMAL, "can_hyp": False, "phase": "F08", "sev": "Alta"},
    "comparticion_recursos": {"cat": "mixed", "models": "mixed", "block": False, "vis": VIS_NORMAL, "can_hyp": False, "phase": "F09", "sev": "Media"},
}

def normalize_value(value):
    """Normaliza el valor de un campo eliminando ruido de plantilla."""
    if value is None:
        return ""
    val = str(value).strip()
    if is_placeholder(val):
        return ""
    return val

def is_placeholder(value):
    """Detecta si el valor es un placeholder de la plantilla."""
    if not value:
        return True
    placeholders = ["[completar]", "[recomendado]", "[opcional]", "[condicional]", "[si aplica]", "n/a", "none", "null"]
    return str(value).lower() in placeholders

def detect_mixed_model(data):
    """Detecta si el negocio es de tipo mixto."""
    tipo = str(data.get("tipo_negocio", "")).lower()
    if any(word in tipo for word in ["mixto", "hibrido", "híbrido", "combinado"]):
        return True
    if normalize_value(data.get("modelo_secundario")):
        return True
    return False

def get_applicable_fields_by_model(profile, data=None):
    """Devuelve la lista de campos que aplican al perfil dado."""
    profile = profile.lower() if profile else ""
    is_mixed = detect_mixed_model(data) if data else False
    
    applicable = []
    for key, rules in FIELD_RULES.items():
        models = rules["models"]
        
        # Core, Oper, Cont aplican a casi todos (reglas específicas en matrix)
        if models == "all":
            applicable.append(key)
            continue
            
        # Mixtos
        if models == "mixed":
            if is_mixed:
                applicable.append(key)
            continue
            
        # Deep / Condicionales
        if any(m in profile for m in models):
            applicable.append(key)
            
    return applicable

def classify_field(key, value, profile, data=None):
    """Clasifica un campo individual según su estado y visibilidad."""
    rules = FIELD_RULES.get(key)
    if not rules:
        return STATUS_CONFIRMADO # Campo desconocido, asumimos ok
        
    val = normalize_value(value)
    
    # Verificar si aplica
    applicable_fields = get_applicable_fields_by_model(profile, data)
    if key not in applicable_fields:
        return STATUS_NO_APLICABLE
        
    # Si no está informado
    if not val:
        if rules["can_hyp"]:
            return STATUS_SUPUESTO
        return STATUS_NO_INFORMADO
        
    # Si está informado, verificar visibilidad/sensibilidad
    vis = rules["vis"]
    if vis == VIS_INTERNO:
        return STATUS_SENSIBLE
    if vis == VIS_RESUMIDO:
        return STATUS_RESUMIDO
        
    return STATUS_CONFIRMADO

def evaluate_integrity(data, profile):
    """Evalúa la integridad total del brief y genera el reporte."""
    report = {
        "profile": profile,
        "is_mixed": detect_mixed_model(data),
        "fields": {},
        "summary": {
            STATUS_CONFIRMADO: [],
            STATUS_NO_INFORMADO: [],
            STATUS_NO_APLICABLE: [],
            STATUS_SUPUESTO: [],
            STATUS_SENSIBLE: [],
            STATUS_RESUMIDO: []
        },
        "impacts": []
    }
    
    # Procesar todos los campos del catálogo
    for key in FIELD_RULES.keys():
        val = data.get(key, "")
        status = classify_field(key, val, profile, data)
        report["fields"][key] = status
        report["summary"][status].append(key)
        
        # Registrar impactos
        if status in [STATUS_NO_INFORMADO, STATUS_SUPUESTO]:
            rules = FIELD_RULES[key]
            phase = rules.get("phase")
            if phase:
                severity = rules.get("sev", "Media")
                report["impacts"].append({
                    "campo": key,
                    "fase": phase,
                    "estado": status,
                    "severidad": severity
                })
                
    report["status"] = get_document_status(report)
    return report

def get_document_status(report):
    """Determina el estado global de aprobación del documento."""
    missing = report["summary"][STATUS_NO_INFORMADO]
    
    # 1. Bloqueo por Core o Mixto obligatorio
    for key in missing:
        if FIELD_RULES[key].get("block"):
            return DOC_BLOQUEADO
            
    # 2. Condicionado por Operativos de severidad alta
    for imp in report["impacts"]:
        if imp["severidad"] == "Alta" and imp["estado"] == STATUS_NO_INFORMADO:
            return DOC_CONDICIONADO
            
    # 3. Observaciones si hay supuestos
    if report["summary"][STATUS_SUPUESTO]:
        return DOC_OBSERVACIONES
        
    return DOC_APROBADO

def render_integrity_markdown(report):
    """Genera el bloque de texto Markdown para el reporte de integridad."""
    status_map = {
        DOC_APROBADO: "🟢 APROBADO ESTRUCTURALMENTE",
        DOC_OBSERVACIONES: "🟡 APROBADO CON OBSERVACIONES",
        DOC_CONDICIONADO: "🟠 CONDICIONADO POR VACÍOS OPERATIVOS",
        DOC_BLOQUEADO: "🔴 BLOQUEADO POR DATOS CRÍTICOS"
    }
    
    md = [
        f"### Estado de Integridad: {status_map.get(report['status'], report['status'])}\n",
        "#### 1. Datos confirmados",
        f"- Total: {len(report['summary'][STATUS_CONFIRMADO]) + len(report['summary'][STATUS_SENSIBLE]) + len(report['summary'][STATUS_RESUMIDO])} campos.",
        "\n#### 2. Vacíos e Impactos por Fase"
    ]
    
    if not report["impacts"]:
        md.append("- No se detectaron vacíos de impacto relevante.")
    else:
        for imp in report["impacts"]:
            estado_txt = "Faltante" if imp["estado"] == STATUS_NO_INFORMADO else "Supuesto"
            md.append(f"- **{imp['campo']}** ({imp['fase']}): {estado_txt} - Severidad: {imp['severidad']}")
            
    md.append("\n#### 3. Supuestos Aplicados")
    supuestos = report["summary"][STATUS_SUPUESTO]
    if not supuestos:
        md.append("- Ninguno.")
    else:
        for s in supuestos:
            md.append(f"- **{s}**: Pendiente de confirmar (Hipótesis operativa).")
            
    md.append("\n#### 4. Privacidad e Información Sensible")
    sensibles = report["summary"][STATUS_SENSIBLE]
    if sensibles:
        md.append(f"- Se detectaron {len(sensibles)} campos de uso interno (no expuestos crudos).")
    else:
        md.append("- No se detectaron campos de alta sensibilidad.")
        
    return "\n".join(md)

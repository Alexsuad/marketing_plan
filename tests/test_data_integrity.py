# File: tests/test_data_integrity.py
# ──────────────────────────────────────────────────────────────────────
# Propósito: Pruebas unitarias para el motor de integridad de datos.
# ──────────────────────────────────────────────────────────────────────

import pytest
from src.core.data_integrity import (
    evaluate_integrity, normalize_value, is_placeholder,
    STATUS_CONFIRMADO, STATUS_NO_INFORMADO, STATUS_NO_APLICABLE,
    STATUS_SUPUESTO, STATUS_SENSIBLE, DOC_BLOQUEADO, DOC_CONDICIONADO,
    DOC_APROBADO, DOC_OBSERVACIONES
)

def test_normalize_value():
    assert normalize_value("[Completar]") == ""
    assert normalize_value("[Recomendado]") == ""
    assert normalize_value("Mi Negocio") == "Mi Negocio"
    assert normalize_value(None) == ""
    assert normalize_value("N/A") == ""

def test_ecommerce_exclusions():
    """eCommerce sin radio_influencia no debe marcarlo como faltante."""
    data = {
        "nombre_negocio": "Tienda Online",
        "tipo_negocio": "ecommerce_transaccional",
        "oferta_principal": "Ropa",
        "cliente_objetivo": "Jóvenes",
        "problema_que_resuelve": "Falta de estilo",
        "objetivo_principal": "Ventas",
        "zona_geografica": "España",
        "radio_influencia": "[Condicional]" # Vacío
    }
    report = evaluate_integrity(data, "ecommerce_transaccional")
    # radio_influencia no aplica a ecommerce puro
    assert report["fields"]["radio_influencia"] == STATUS_NO_APLICABLE

def test_local_retail_inclusions():
    """Local/Retail sin radio_influencia sí debe marcar vacío relevante."""
    data = {
        "nombre_negocio": "Barbería",
        "tipo_negocio": "retail_fisico",
        "oferta_principal": "Corte",
        "cliente_objetivo": "Hombres",
        "problema_que_resuelve": "Pelo largo",
        "objetivo_principal": "Citas",
        "zona_geografica": "Madrid",
        "radio_influencia": "" # Vacío
    }
    report = evaluate_integrity(data, "retail_fisico")
    assert report["fields"]["radio_influencia"] == STATUS_NO_INFORMADO

def test_industrial_homologacion():
    """Industrial sin homologacion debe marcar vacío relevante."""
    data = {"tipo_negocio": "b2b_producto_industrial"}
    report = evaluate_integrity(data, "b2b_producto_industrial")
    assert report["fields"]["homologacion"] == STATUS_NO_INFORMADO
    
    # No industrial
    report_ecom = evaluate_integrity(data, "ecommerce_transaccional")
    assert report_ecom["fields"]["homologacion"] == STATUS_NO_APLICABLE

def test_sensitive_data():
    """margen_bruto informado debe aparecer como sensible."""
    data = {
        "tipo_negocio": "ecommerce_transaccional",
        "margen_bruto": "30%"
    }
    report = evaluate_integrity(data, "ecommerce_transaccional")
    assert report["fields"]["margen_bruto"] == STATUS_SENSIBLE
    
    # Si falta, no debe generar supuesto (can_hyp=False en matriz)
    data_missing = {"tipo_negocio": "ecommerce_transaccional", "margen_bruto": ""}
    report_missing = evaluate_integrity(data_missing, "ecommerce_transaccional")
    assert report_missing["fields"]["margen_bruto"] == STATUS_NO_INFORMADO

def test_budget_assumption():
    """presupuesto_marketing faltante puede generar supuesto."""
    data = {"tipo_negocio": "b2b_consultivo", "presupuesto_marketing": ""}
    report = evaluate_integrity(data, "b2b_consultivo")
    assert report["fields"]["presupuesto_marketing"] == STATUS_SUPUESTO

def test_mixed_model_blocking():
    """Negocio mixto sin prioridad_90_dias debe marcar vacío relevante para F08."""
    data = {
        "nombre_negocio": "Híbrido",
        "tipo_negocio": "hibrido_producto_servicio",
        "modelo_principal": "Ecommerce",
        "modelo_secundario": "Servicio",
        "prioridad_90_dias": "" # Vacío crítico para mixtos
    }
    report = evaluate_integrity(data, "hibrido_producto_servicio")
    assert report["is_mixed"] is True
    assert report["fields"]["prioridad_90_dias"] == STATUS_NO_INFORMADO
    # Debe estar bloqueado porque prioridad_90_dias tiene block=True en matriz
    assert report["status"] == DOC_BLOQUEADO

def test_document_status_levels():
    # 1. Bloqueado (Falta Core)
    data_bad = {"nombre_negocio": ""}
    assert evaluate_integrity(data_bad, "ecommerce")["status"] == DOC_BLOQUEADO
    
    # 2. Condicionado (Falta Operativo severidad Alta como recursos_internos)
    data_cond = {
        "nombre_negocio": "OK", "tipo_negocio": "OK", "oferta_principal": "OK",
        "cliente_objetivo": "OK", "problema_que_resuelve": "OK", "objetivo_principal": "OK",
        "zona_geografica": "OK",
        "recursos_internos": "" # Vacío Alta
    }
    assert evaluate_integrity(data_cond, "ecommerce")["status"] == DOC_CONDICIONADO
    
    # 3. Observaciones (Solo supuestos como presupuesto, con resto de Operativos OK)
    data_obs = {
        "nombre_negocio": "OK", "tipo_negocio": "OK", "oferta_principal": "OK",
        "cliente_objetivo": "OK", "problema_que_resuelve": "OK", "objetivo_principal": "OK",
        "zona_geografica": "OK",
        "recursos_internos": "Equipo propio", 
        "tiempo_disponible": "20h/semana",
        "restricciones": "Ninguna técnica",
        "presupuesto_marketing": "" # Genera Supuesto -> DOC_OBSERVACIONES
    }
    report_obs = evaluate_integrity(data_obs, "ecommerce")
    assert report_obs["status"] == DOC_OBSERVACIONES
    
    # 4. Condicionado (Falta Operativo de severidad Alta sin hipótesis)
    data_cond = data_obs.copy()
    data_cond["recursos_internos"] = "" # Falta dato Alta sev
    assert evaluate_integrity(data_cond, "ecommerce")["status"] == DOC_CONDICIONADO
    
    # 5. Aprobado (Todo completo)
    data_ok = data_obs.copy()
    data_ok["presupuesto_marketing"] = "1000"
    data_ok["ticket_promedio"] = "50"
    assert evaluate_integrity(data_ok, "ecommerce")["status"] == DOC_APROBADO

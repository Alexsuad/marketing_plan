# File: tests/test_marketing_profile_resolver.py
# ──────────────────────────────────────────────────────────────────────
# Propósito: Pruebas unitarias para el resolver de perfiles de marketing.
# Rol: Validación determinista de la lógica de clasificación (Fase 06-12).
# ──────────────────────────────────────────────────────────────────────

import pytest
from src.core.marketing_profile_resolver import resolve_marketing_profile

def test_resolve_b2b_consultivo():
    """Caso 1: Brief B2B consultivo"""
    brief_data = {
        "tipo_negocio": "Consultoría IT",
        "oferta_principal": "Migración a Cloud",
        "cliente_objetivo": "Pymes"
    }
    result = resolve_marketing_profile(brief_data)
    assert result["marketing_profile"] == "b2b_consultivo"

def test_resolve_b2c_local_servicios():
    """Caso 2: Brief B2C local servicios"""
    brief_data = {
        "tipo_negocio": "Centro de estética local",
        "oferta_principal": "Tratamientos faciales y corporales",
        "cliente_objetivo": "Mujeres de 25 a 55 años en zona urbana cercana"
    }
    result = resolve_marketing_profile(brief_data)
    assert result["marketing_profile"] == "b2c_local_servicios"

def test_resolve_educativo_formativo():
    """Caso 3: Brief educativo/formativo"""
    brief_data = {
        "tipo_negocio": "Academia de idiomas para niños",
        "oferta_principal": "Clases de inglés para niños de 6 a 12 años",
        "cliente_objetivo": "Padres y madres de niños en edad escolar"
    }
    result = resolve_marketing_profile(brief_data)
    assert result["marketing_profile"] == "educativo_formativo"

def test_resolve_b2c_producto_ecommerce():
    """Caso 4: Brief B2C Producto Ecommerce"""
    brief_data = {
        "tipo_negocio": "Tienda online de moda",
        "oferta_principal": "Zapatillas deportivas de marca propia",
        "cliente_objetivo": "Jóvenes interesados en streetwear y compras online"
    }
    # Ahora con la especialización, este caso matchea con ecommerce_transaccional (prioridad)
    result = resolve_marketing_profile(brief_data)
    assert result["marketing_profile"] == "ecommerce_transaccional"

def test_resolve_b2b_producto_industrial():
    """Caso 5: Brief B2B Producto Industrial"""
    brief_data = {
        "tipo_negocio": "Mayorista de repuestos industriales",
        "oferta_principal": "Suministro de componentes para maquinaria pesada",
        "cliente_objetivo": "Empresas de construcción y minería"
    }
    result = resolve_marketing_profile(brief_data)
    assert result["marketing_profile"] == "b2b_producto_industrial"

def test_resolve_retail_fisico():
    """Caso 6: Brief Retail Físico"""
    brief_data = {
        "tipo_negocio": "Ferretería de barrio",
        "oferta_principal": "Venta de herramientas y suministros de hogar en local físico",
        "cliente_objetivo": "Vecinos y profesionales de la zona urbana"
    }
    result = resolve_marketing_profile(brief_data)
    assert result["marketing_profile"] == "retail_fisico"

def test_resolve_estrategia_general_prudente():
    """Caso 7: Brief con información ambigua (Fallback)"""
    brief_data = {
        "tipo_negocio": "Negocio de gestión documental",
        "oferta_principal": "Organización y digitalización para autónomos",
        "cliente_objetivo": "Personas con desorden administrativo"
    }
    # No llega a los 2 matches requeridos para perfiles específicos.
    result = resolve_marketing_profile(brief_data)
    assert result["marketing_profile"] == "estrategia_general_prudente"

def test_resolve_empate_usa_fallback():
    """Caso 8: Empate entre perfiles (usa fallback para evitar error)"""
    brief_data = {
        "tipo_negocio": "Tecnología para estética local",
        "oferta_principal": "Software y tratamientos",
        "cliente_objetivo": "Clínicas de belleza y Pymes"
    }
    # Ahora, con la lógica de prioridad por orden, debería ganar el primero
    # que coincida con el score máximo (en este caso b2b_consultivo).
    result = resolve_marketing_profile(brief_data)
    assert result["marketing_profile"] == "b2b_consultivo"

def test_contract_integrity():
    """
    Fase 1: Verificar que todos los canales de todos los perfiles
    cumplan con el contrato de datos extendido (effort, risk, cost).
    """
    from src.core.marketing_profile_resolver import PROFILES
    
    required_keys = ["name", "objective", "effort", "risk", "cost"]
    required_secondary_keys = ["name", "utility", "effort", "risk", "cost"]
    
    for profile_id, data in PROFILES.items():
        # Validar recomendados
        for channel in data.get("recommended_channel_families", []):
            for key in required_keys:
                assert key in channel, f"Falta llave '{key}' en canal recomendado de {profile_id}: {channel.get('name')}"
        
        # Validar secundarios
        for channel in data.get("secondary_channel_families", []):
            for key in required_secondary_keys:
                assert key in channel, f"Falta llave '{key}' en canal secundario de {profile_id}: {channel.get('name')}"

def test_ecommerce_classification():
    """Validar que un brief de Ecommerce se clasifica correctamente."""
    from src.core.marketing_profile_resolver import resolve_marketing_profile
    brief_data = {
        "tipo_negocio": "Tienda online de calzado",
        "oferta_principal": "Zapatillas deportivas con envío a domicilio",
        "cliente_objetivo": "Corredores y deportistas",
        "problema_que_resuelve": "Falta de stock en tiendas físicas y comodidad de compra web"
    }
    result = resolve_marketing_profile(brief_data)
    assert result["marketing_profile"] == "ecommerce_transaccional"
    assert "comprar ahora" in result["terminology"]["accion_principal"]

def test_hibrido_classification():
    """Validar que un brief Híbrido se clasifica correctamente."""
    from src.core.marketing_profile_resolver import resolve_marketing_profile
    brief_data = {
        "tipo_negocio": "Venta de impresoras 3D industriales",
        "oferta_principal": "Maquinaria con contrato de mantenimiento anual",
        "cliente_objetivo": "Fábricas y talleres",
        "problema_que_resuelve": "Paradas de producción por falta de servicio técnico"
    }
    result = resolve_marketing_profile(brief_data)
    assert result["marketing_profile"] == "hibrido_producto_servicio"
    assert "adquirir con soporte" in result["terminology"]["accion_principal"]

def test_resolve_artesania_sonica_ecommerce():
    """
    Fase 4: Caso real de Ecommerce D2C de artesanía premium.
    Debe clasificar como ecommerce_transaccional.
    """
    brief_data = {
        "tipo_negocio": "Ecommerce D2C (Direct to Consumer)",
        "oferta_principal": "Auriculares premium de madera hechos a mano con tecnología de alta fidelidad.",
        "cliente_objetivo": "Audiófilos, amantes del diseño natural y profesionales del sonido que buscan exclusividad y calidez sonora.",
        "problema_que_resuelve": "La frialdad estética y falta de personalidad de los dispositivos electrónicos producidos en masa."
    }
    result = resolve_marketing_profile(brief_data)
    # Se espera ecommerce_transaccional por ser venta directa de producto físico D2C
    assert result["marketing_profile"] == "ecommerce_transaccional"

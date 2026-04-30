# File: tests/test_brief_service.py
# ──────────────────────────────────────────────────────────────────────
# Propósito: Pruebas unitarias para el servicio de brief (estándar v1.2).
# ──────────────────────────────────────────────────────────────────────

import os
import pytest
from src.services.brief_service import generate_validated_brief
from src.utils.text_utils import slugify

@pytest.fixture
def mock_projects_dir(tmp_path, monkeypatch):
    """Redirige PROJECTS_DIR a un directorio temporal en todos los módulos necesarios."""
    projects_dir = tmp_path / "projects"
    projects_dir.mkdir()
    
    # Redirigir en todos los puntos donde se importe PROJECTS_DIR
    monkeypatch.setattr("src.utils.project_io.PROJECTS_DIR", str(projects_dir))
    monkeypatch.setattr("src.validators.brief_validator.PROJECTS_DIR", str(projects_dir))
    
    return projects_dir

def create_mock_brief_structure(projects_dir, project_name, content):
    """Crea estructura completa para el servicio de brief."""
    slug = slugify(project_name)
    project_path = projects_dir / slug
    context_dir = project_path / "context"
    outputs_dir = project_path / "outputs" / "plan_actual"
    
    context_dir.mkdir(parents=True)
    outputs_dir.mkdir(parents=True)
    
    brief_path = context_dir / "brief_negocio.md"
    brief_path.write_text(content, encoding="utf-8")
    return project_path

def test_generate_validated_brief_content(mock_projects_dir):
    """Verifica que el documento formal contiene las secciones y valores correctos."""
    content = (
        "- **nombre_negocio:** Dog Spa\n"
        "- **tipo_negocio:** b2c_local_servicios (servicio local)\n"
        "- **oferta_principal:** Lavado y peluquería (servicio)\n"
        "- **cliente_objetivo:** Perros de vecinos\n"
        "- **problema_que_resuelve:** Suciedad y enredos\n"
        "- **objetivo_principal:** Higiene animal\n"
        "- **zona_geografica:** Barcelona (zona geográfica local)\n"
        "- **presupuesto_marketing:** [Recomendado]\n"
        "- **radio_influencia:** 5km\n"
        "- **competidores_conocidos:** [Opcional]"
    )
    create_mock_brief_structure(mock_projects_dir, "Dog Spa", content)
    
    output_path = generate_validated_brief("Dog Spa")
    assert os.path.exists(output_path)
    
    with open(output_path, "r", encoding="utf-8") as f:
        rendered = f.read()
    
    # Validaciones v1.6
    assert "### Estado de Integridad:" in rendered
    assert "#### 1. Datos confirmados" in rendered
    assert "#### 2. Vacíos e Impactos por Fase" in rendered
    
    # Validaciones de normalización e integridad
    assert "- **presupuesto_marketing:** No informado" in rendered
    assert "- **competidores_conocidos:** No informado" in rendered
    assert "- **radio_influencia:** 5km" in rendered
    assert "- **homologacion:** No aplica a este modelo" in rendered
    
    # No deben quedar placeholders ni frases genéricas
    assert "[Recomendado]" not in rendered
    assert "Aquellos marcados en las secciones superiores" not in rendered
    assert "Se utilizarán rangos prudentes" not in rendered
    
def test_generate_validated_brief_privacy(mock_projects_dir):
    """Verifica que los datos sensibles se oculten en el output."""
    content = (
        "- **nombre_negocio:** Ecom Shop\n"
        "- **tipo_negocio:** ecommerce_transaccional\n"
        "- **oferta_principal:** Venta de Camisetas (tienda online)\n"
        "- **cliente_objetivo:** Jóvenes (D2C)\n"
        "- **problema_que_resuelve:** Falta de estilo\n"
        "- **objetivo_principal:** Ventas web\n"
        "- **zona_geografica:** Global\n"
        "- **margen_bruto:** 40%"
    )
    create_mock_brief_structure(mock_projects_dir, "Ecom Shop", content)
    output_path = generate_validated_brief("Ecom Shop")
    
    with open(output_path, "r", encoding="utf-8") as f:
        rendered = f.read()
        
    assert "40%" not in rendered
    assert "[Dato Protegido - Uso Interno]" in rendered

def test_generate_validated_brief_status_changes(mock_projects_dir):
    """Verifica que el estado del documento cambie según la integridad."""
    content_obs = (
        "- **nombre_negocio:** Obs Retail\n"
        "- **tipo_negocio:** retail_fisico (tienda de barrio)\n"
        "- **oferta_principal:** Productos locales (tráfico peatonal)\n"
        "- **cliente_objetivo:** Vecinos\n"
        "- **problema_que_resuelve:** Cercanía\n"
        "- **objetivo_principal:** Visibilidad local\n"
        "- **zona_geografica:** Madrid\n"
        "- **recursos_internos:** Equipo\n"
        "- **tiempo_disponible:** 10h\n"
        "- **restricciones:** Ninguna\n"
        "- **canales_actuales:** Ninguno\n"
        "- **capacidad_operativa:** 100 clientes/día\n"
        "- **ticket_promedio:** 20€\n"
        "- **radio_influencia:** 2km\n"
        "- **presupuesto_marketing:** [Completar]" # Genera Supuesto
    )
    create_mock_brief_structure(mock_projects_dir, "Obs Retail", content_obs)
    output_path = generate_validated_brief("Obs Retail")
    with open(output_path, "r", encoding="utf-8") as f:
        rendered = f.read()
    assert "aprobado_con_observaciones" in rendered

# File: tests/test_resumen_empresa_service.py
# ──────────────────────────────────────────────────────────────────────
# Propósito: Pruebas unitarias para el resumen de empresa (v1.6).
# ──────────────────────────────────────────────────────────────────────

import os
import pytest
from src.services.resumen_empresa_service import generate_resumen_empresa_output
from src.utils.text_utils import slugify

@pytest.fixture
def mock_projects_dir(tmp_path, monkeypatch):
    """Redirige PROJECTS_DIR a un directorio temporal."""
    projects_dir = tmp_path / "projects"
    projects_dir.mkdir()
    monkeypatch.setattr("src.utils.project_io.PROJECTS_DIR", str(projects_dir))
    return projects_dir

def create_mock_project_structure(projects_dir, project_name, brief_content):
    """Crea la estructura necesaria para el test de Fase 11."""
    slug = slugify(project_name)
    project_path = projects_dir / slug
    context_dir = project_path / "context"
    outputs_dir = project_path / "outputs" / "plan_actual"
    
    context_dir.mkdir(parents=True)
    outputs_dir.mkdir(parents=True)
    
    # Escribir brief
    brief_path = context_dir / "brief_negocio.md"
    brief_path.write_text(brief_content, encoding="utf-8")
    
    # Escribir Fase 10 dummy (requerido por el servicio)
    phase_10_path = outputs_dir / "10_kpis_y_medicion.md"
    phase_10_path.write_text("# Fase 10 Dummy", encoding="utf-8")
    
    return project_path

def test_resumen_empresa_integrity_integration(mock_projects_dir):
    """
    Valida la integración del motor de integridad en el resumen de empresa.
    Cubre puntos: 1, 2, 3, 5, 6, 7.
    """
    project_name = "Test Business"
    # Brief informado (incluyendo zona_geografica y presupuesto)
    brief_content = (
        "- **nombre_negocio:** Test Business\n"
        "- **tipo_negocio:** ecommerce de calzado\n"
        "- **oferta_principal:** Zapatillas\n"
        "- **cliente_objetivo:** Corredores\n"
        "- **problema_que_resuelve:** Dolor de pies\n"
        "- **objetivo_principal:** Vender 100 pares\n"
        "- **zona_geografica:** España\n"
        "- **presupuesto_marketing:** 5000€\n"
        "- **margen_bruto:** 40%\n"
    )
    
    create_mock_project_structure(mock_projects_dir, project_name, brief_content)
    
    output_file = generate_resumen_empresa_output(project_name)
    with open(output_file, "r", encoding="utf-8") as f:
        content = f.read()
    
    # 1. El resumen contiene “Integridad de Datos”
    assert "## Integridad de Datos" in content
    
    # 2. zona_geografica informada -> no aparece como faltante en la lista de integridad
    # (Buscamos en la sección de vacíos)
    integrity_part = content.split("## Integridad de Datos")[1]
    assert "zona_geografica" not in integrity_part
    
    # 3. presupuesto_marketing informado -> no aparece como supuesto pendiente
    assert "presupuesto_marketing" not in integrity_part
    
    # 5. margen_bruto informado no se muestra crudo
    assert "40%" not in content
    assert "[Dato Protegido - Uso Interno]" in content
    
    # 6. No aparece la frase fija “Zona geográfica (validar consistencia)”
    assert "Zona geográfica (validar consistencia)" not in content
    
    # 7. No aparece “presupuesto X considerado como rango operativo”
    assert "considerado como rango operativo" not in content

def test_resumen_empresa_presupuesto_faltante(mock_projects_dir):
    """
    Valida que si falta presupuesto, aparece como supuesto pendiente.
    Cubre punto 4.
    """
    project_name = "Missing Budget"
    brief_content = (
        "- **nombre_negocio:** Missing Budget\n"
        "- **tipo_negocio:** retail local\n"
        "- **oferta_principal:** Pan\n"
        "- **cliente_objetivo:** Vecinos\n"
        "- **problema_que_resuelve:** Hambre\n"
        "- **objetivo_principal:** Alimentar al barrio\n"
        "- **zona_geografica:** Madrid\n"
    )
    
    create_mock_project_structure(mock_projects_dir, project_name, brief_content)
    
    output_file = generate_resumen_empresa_output(project_name)
    with open(output_file, "r", encoding="utf-8") as f:
        content = f.read()
        
    # 4. Si presupuesto_marketing falta, aparece como supuesto pendiente de confirmar
    integrity_part = content.split("## Integridad de Datos")[1]
    assert "presupuesto_marketing" in integrity_part
    assert "#### 3. Supuestos Aplicados" in integrity_part
    assert "Pendiente de confirmar" in integrity_part

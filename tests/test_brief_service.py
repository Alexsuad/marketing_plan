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
        "- **tipo_negocio:** b2c_local_servicios\n"
        "- **oferta_principal:** Lavado\n"
        "- **cliente_objetivo:** Perros\n"
        "- **problema_que_resuelve:** Suciedad\n"
        "- **objetivo_principal:** Limpieza\n"
        "- **zona_geografica:** Barcelona\n"
        "- **presupuesto_marketing:** [Recomendado]\n"
        "- **radio_influencia:** 5km\n"
        "- **competidores_conocidos:** [Opcional]"
    )
    create_mock_brief_structure(mock_projects_dir, "Dog Spa", content)
    
    output_path = generate_validated_brief("Dog Spa")
    assert os.path.exists(output_path)
    
    with open(output_path, "r", encoding="utf-8") as f:
        rendered = f.read()
    
    # Validaciones v1.2
    assert "## Datos principales" in rendered
    assert "- **zona_geografica:** Barcelona" in rendered
    assert "## Datos operativos recomendados" in rendered
    assert "## Datos opcionales de contexto" in rendered
    assert "## Datos condicionales por modelo" in rendered
    assert "## Integridad de Datos" in rendered
    
    # Validaciones de normalización
    assert "- **presupuesto_marketing:** No informado" in rendered
    assert "- **competidores_conocidos:** No informado" in rendered
    assert "- **radio_influencia:** 5km" in rendered
    
    # No deben quedar placeholders
    assert "[Recomendado]" not in rendered
    assert "[Opcional]" not in rendered
    assert "[Condicional]" not in rendered
    assert "[Completar]" not in rendered

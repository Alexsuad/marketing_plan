# File: tests/test_brief_validator.py
# ──────────────────────────────────────────────────────────────────────
# Propósito: Pruebas unitarias para el validador de brief (estándar v1.2).
# ──────────────────────────────────────────────────────────────────────

import os
import pytest
from src.validators.brief_validator import validate_brief
from src.utils.text_utils import slugify

@pytest.fixture
def mock_projects_dir(tmp_path, monkeypatch):
    """Redirige PROJECTS_DIR a un directorio temporal."""
    projects_dir = tmp_path / "projects"
    projects_dir.mkdir()
    monkeypatch.setattr("src.validators.brief_validator.PROJECTS_DIR", str(projects_dir))
    return projects_dir

def create_mock_brief(projects_dir, project_name, content):
    """Crea un archivo de brief de prueba."""
    slug = slugify(project_name)
    brief_dir = projects_dir / slug / "context"
    brief_dir.mkdir(parents=True)
    brief_path = brief_dir / "brief_negocio.md"
    brief_path.write_text(content, encoding="utf-8")
    return brief_path

def test_validate_brief_complete(mock_projects_dir):
    """Debe pasar si todos los campos obligatorios existen (incluida geografía)."""
    content = (
        "- **nombre_negocio:** Test\n"
        "- **tipo_negocio:** ecommerce\n"
        "- **oferta_principal:** Algo\n"
        "- **cliente_objetivo:** Alguien\n"
        "- **problema_que_resuelve:** Dolor\n"
        "- **objetivo_principal:** Vender\n"
        "- **zona_geografica:** España"
    )
    create_mock_brief(mock_projects_dir, "Test Project", content)
    errors = validate_brief("Test Project")
    assert len(errors) == 0, f"Errores inesperados: {errors}"

def test_validate_brief_missing_geography(mock_projects_dir):
    """Debe fallar si falta zona_geografica."""
    content = (
        "- **nombre_negocio:** Test\n"
        "- **tipo_negocio:** ecommerce\n"
        "- **oferta_principal:** Algo\n"
        "- **cliente_objetivo:** Alguien\n"
        "- **problema_que_resuelve:** Dolor\n"
        "- **objetivo_principal:** Vender"
    )
    create_mock_brief(mock_projects_dir, "Test Project", content)
    errors = validate_brief("Test Project")
    assert any("zona_geografica" in e for e in errors)

def test_validate_brief_with_placeholders(mock_projects_dir):
    """Debe pasar si los obligatorios están, aunque falten recomendados o tengan placeholders."""
    content = (
        "- **nombre_negocio:** Test\n"
        "- **tipo_negocio:** b2b_consultivo\n"
        "- **oferta_principal:** Algo\n"
        "- **cliente_objetivo:** Alguien\n"
        "- **problema_que_resuelve:** Dolor\n"
        "- **objetivo_principal:** Vender\n"
        "- **zona_geografica:** Madrid\n"
        "- **presupuesto_marketing:** [Recomendado]\n"
        "- **ticket_promedio:** [Condicional]\n"
        "- **competidores_conocidos:** [Opcional]"
    )
    create_mock_brief(mock_projects_dir, "Test Project", content)
    errors = validate_brief("Test Project")
    assert len(errors) == 0, f"Errores inesperados: {errors}"

# File: tests/test_auditoria_service.py
# ──────────────────────────────────────────────────────────────────────
# Propósito: Validar la integración del motor de integridad en la auditoría.
# ──────────────────────────────────────────────────────────────────────

import os
import pytest
from src.services.auditoria_service import generate_auditoria_output
from src.utils.markdown_utils import write_markdown_file

@pytest.fixture
def temp_project(tmp_path, monkeypatch):
    """Crea una estructura de proyecto temporal para pruebas."""
    project_name = "TestAuditProject"
    project_dir = tmp_path / "projects" / project_name
    context_dir = project_dir / "context"
    # La ruta real según project_io es projects/name/outputs/plan_actual
    plan_dir = project_dir / "outputs" / "plan_actual"
    
    context_dir.mkdir(parents=True)
    plan_dir.mkdir(parents=True)
    
    # Mock de brief_negocio.md completo para aprobación total
    brief_content = """# Brief de Negocio
- **nombre_negocio:** Audit Store
- **tipo_negocio:** ecommerce_transaccional
- **oferta_principal:** Zapatillas Pro
- **cliente_objetivo:** Corredores
- **problema_que_resuelve:** Falta de amortiguación
- **objetivo_principal:** Vender 100 pares
- **zona_geografica:** Nacional
- **presupuesto_marketing:** 1000 USD
- **recursos_internos:** 1 persona part-time
- **tiempo_disponible:** 10 horas/semana
- **restricciones:** Ninguna
- **ticket_promedio:** 50 USD
"""
    write_markdown_file(str(context_dir / "brief_negocio.md"), brief_content)
    
    # Mock de Fase 11 (requerida por auditoria)
    write_markdown_file(str(plan_dir / "11_resumen_para_plan_empresa.md"), "# Fase 11")
    
    # Monkeypatch de get_project_path
    from src.utils import project_io
    monkeypatch.setattr(project_io, "get_project_path", lambda name: str(project_dir))
    
    return project_name

def test_generate_auditoria_aprobada(temp_project):
    """Valida auditoría exitosa con brief completo."""
    output_path = generate_auditoria_output(temp_project)
    assert os.path.exists(output_path)
    
    with open(output_path, "r", encoding="utf-8") as f:
        content = f.read()
        assert "plan_marketing_inicial_aprobado_estructuralmente" in content
        assert "**Oferta/Modelo y Cliente**: Existe una conexión documental entre la oferta declarada (Zapatillas Pro)" in content
        assert "### Estado de Integridad" in content
        assert "🟢 APROBADO ESTRUCTURALMENTE" in content

def test_generate_auditoria_bloqueada(tmp_path, monkeypatch):
    """Valida auditoría bloqueada con brief incompleto."""
    project_name = "BloqueadoProject"
    project_dir = tmp_path / "projects" / project_name
    context_dir = project_dir / "context"
    plan_dir = project_dir / "outputs" / "plan_actual"
    context_dir.mkdir(parents=True)
    plan_dir.mkdir(parents=True)
    
    # Brief sin campos críticos y con formato correcto de negritas
    brief_content = """# Brief Incompleto
- **nombre_negocio:** Incompleto
- **tipo_negocio:** b2b_consultivo
"""
    write_markdown_file(str(context_dir / "brief_negocio.md"), brief_content)
    write_markdown_file(str(plan_dir / "11_resumen_para_plan_empresa.md"), "# Fase 11")
    
    from src.utils import project_io
    monkeypatch.setattr(project_io, "get_project_path", lambda name: str(project_dir))
    
    output_path = generate_auditoria_output(project_name)
    
    with open(output_path, "r", encoding="utf-8") as f:
        content = f.read()
        assert "plan_marketing_inicial_bloqueado_por_vacios_criticos" in content
        assert "⚠️ SE HAN DETECTADO BLOQUEOS CRÍTICOS" in content
        assert "🔴 BLOQUEADO POR DATOS CRÍTICOS" in content

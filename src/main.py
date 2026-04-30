# File: src/main.py
# ──────────────────────────────────────────────────────────────────────
# Propósito: Punto de entrada principal (CLI) del sistema.
# Rol: Interfaz de usuario (Consola)
# ──────────────────────────────────────────────────────────────────────

import argparse
import sys
from src.core.project_manager import create_project
from src.validators.structure_validator import validate_base_structure
from src.validators.project_validator import validate_project
from src.validators.brief_validator import validate_brief
from src.services.brief_service import generate_validated_brief
from src.services.diagnostico_service import generate_diagnostico_output
from src.services.cliente_service import generate_cliente_output
from src.services.propuesta_valor_service import generate_propuesta_valor_output
from src.services.competencia_service import generate_competencia_output
from src.services.canales_service import generate_canales_output
from src.services.comunicacion_service import generate_comunicacion_output
from src.services.plan_accion_service import generate_plan_accion_output
from src.services.presupuesto_service import generate_presupuesto_output
from src.services.kpis_service import generate_kpis_output
from src.services.resumen_empresa_service import generate_resumen_empresa_output
from src.services.auditoria_service import generate_auditoria_output

def main():
    parser = argparse.ArgumentParser(description="Motor del Sistema Agéntico de Plan de Marketing")
    subparsers = parser.add_subparsers(dest="command", help="Comandos disponibles")
    
    # Comando: create-project
    parser_create = subparsers.add_parser("create-project", help="Crea un nuevo proyecto desde la plantilla")
    parser_create.add_argument("--name", required=True, help="Nombre del nuevo proyecto")
    
    # Comando: validate-base-structure
    subparsers.add_parser("validate-base-structure", help="Validación de la estructura de la plantilla base")
    
    # Comando: validate-project
    parser_validate = subparsers.add_parser("validate-project", help="Valida la estructura de un proyecto instanciado")
    parser_validate.add_argument("--name", required=True, help="Nombre del proyecto a validar")

    # Comando: validate-brief
    parser_brief = subparsers.add_parser("validate-brief", help="Valida que el brief del proyecto esté completo")
    parser_brief.add_argument("--name", required=True, help="Nombre del proyecto cuyo brief se va a validar")

    # Comando: generate-brief-output
    parser_gen_brief = subparsers.add_parser("generate-brief-output", help="Genera el documento formal de brief validado")
    parser_gen_brief.add_argument("--name", required=True, help="Nombre del proyecto para generar el output")

    # Comando: generate-diagnostico-output
    parser_gen_diag = subparsers.add_parser("generate-diagnostico-output", help="Genera el documento de diagnóstico inicial")
    parser_gen_diag.add_argument("--name", required=True, help="Nombre del proyecto para generar el diagnóstico")

    # Comando: generate-cliente-output
    parser_gen_cli = subparsers.add_parser("generate-cliente-output", help="Genera el documento de cliente y segmentos")
    parser_gen_cli.add_argument("--name", required=True, help="Nombre del proyecto para generar el análisis de cliente")

    # Comando: generate-propuesta-valor-output
    parser_gen_prop = subparsers.add_parser("generate-propuesta-valor-output", help="Genera el documento de propuesta de valor")
    parser_gen_prop.add_argument("--name", required=True, help="Nombre del proyecto para generar la propuesta")

    # Comando: generate-competencia-output
    parser_gen_comp = subparsers.add_parser("generate-competencia-output", help="Genera el documento de análisis de competencia")
    parser_gen_comp.add_argument("--name", required=True, help="Nombre del proyecto para generar the competencia")

    # Comando: generate-canales-output
    parser_gen_can = subparsers.add_parser("generate-canales-output", help="Genera el documento de matriz de canales")
    parser_gen_can.add_argument("--name", required=True, help="Nombre del proyecto para generar los canales")

    # Comando: generate-comunicacion-output
    parser_gen_com = subparsers.add_parser("generate-comunicacion-output", help="Genera el documento de estrategia de comunicación")
    parser_gen_com.add_argument("--name", required=True, help="Nombre del proyecto para generar la comunicación")

    # Comando: generate-plan-accion-output
    parser_gen_plan = subparsers.add_parser("generate-plan-accion-output", help="Genera el documento del plan de acción 90 días")
    parser_gen_plan.add_argument("--name", required=True, help="Nombre del proyecto para generar el plan")

    # Comando: generate-presupuesto-output
    parser_gen_pres = subparsers.add_parser("generate-presupuesto-output", help="Genera el documento de presupuesto de marketing")
    parser_gen_pres.add_argument("--name", required=True, help="Nombre del proyecto para generar el presupuesto")

    # Comando: generate-kpis-output
    parser_gen_kpi = subparsers.add_parser("generate-kpis-output", help="Genera el documento de KPIs y medición inicial")
    parser_gen_kpi.add_argument("--name", required=True, help="Nombre del proyecto para generar los KPIs")

    # Comando: generate-resumen-empresa-output
    parser_gen_res = subparsers.add_parser("generate-resumen-empresa-output", help="Genera el resumen ejecutivo para plan de empresa")
    parser_gen_res.add_argument("--name", required=True, help="Nombre del proyecto para generar el resumen")

    # Comando: generate-auditoria-output
    parser_gen_audit = subparsers.add_parser("generate-auditoria-output", help="Genera la auditoría final del plan de marketing")
    parser_gen_audit.add_argument("--name", required=True, help="Nombre del proyecto para generar la auditoría")
    
    args = parser.parse_args()
    
    if args.command == "create-project":
        print(f"Iniciando creación del proyecto: {args.name}")
        try:
            path = create_project(args.name)
            print(f"✅ Proyecto creado exitosamente en: {path}")
        except Exception as e:
            print(f"❌ Error al crear el proyecto: {e}")
            sys.exit(1)
            
    elif args.command == "validate-base-structure":
        print("Validando estructura base...")
        errors = validate_base_structure()
        if errors:
            print("❌ Errores encontrados en la estructura base:")
            for e in errors:
                print(f"  - {e}")
            sys.exit(1)
        else:
            print("✅ La estructura base (project_template) es correcta.")
            
    elif args.command == "validate-project":
        print(f"Validando proyecto: {args.name}...")
        errors = validate_project(args.name)
        if errors:
            print(f"❌ Errores encontrados en el proyecto '{args.name}':")
            for e in errors:
                print(f"  - {e}")
            sys.exit(1)
        else:
            print(f"✅ La estructura del proyecto '{args.name}' es correcta.")
            
    elif args.command == "validate-brief":
        print(f"Validando brief del proyecto: {args.name}...")
        errors = validate_brief(args.name)
        if errors:
            print(f"❌ Errores encontrados en el brief de '{args.name}':")
            for e in errors:
                print(f"  - {e}")
            sys.exit(1)
        else:
            print(f"✅ El brief del proyecto '{args.name}' está completo y es válido.")

    elif args.command == "generate-brief-output":
        print(f"Generando output de brief validado para: {args.name}...")
        try:
            path = generate_validated_brief(args.name)
            print(f"✅ Documento formal generado en: {path}")
        except Exception as e:
            print(f"❌ Error al generar el output: {e}")
            sys.exit(1)

    elif args.command == "generate-diagnostico-output":
        print(f"Generando diagnóstico de marketing para: {args.name}...")
        try:
            path = generate_diagnostico_output(args.name)
            print(f"✅ Diagnóstico formal generado en: {path}")
        except Exception as e:
            print(f"❌ Error al generar el diagnóstico: {e}")
            sys.exit(1)

    elif args.command == "generate-cliente-output":
        print(f"Generando análisis de cliente para: {args.name}...")
        try:
            path = generate_cliente_output(args.name)
            print(f"✅ Análisis de cliente generado en: {path}")
        except Exception as e:
            print(f"❌ Error al generar el análisis de cliente: {e}")
            sys.exit(1)

    elif args.command == "generate-propuesta-valor-output":
        print(f"Generando propuesta de valor para: {args.name}...")
        try:
            path = generate_propuesta_valor_output(args.name)
            print(f"✅ Propuesta de valor generada en: {path}")
        except Exception as e:
            print(f"❌ Error al generar la propuesta de valor: {e}")
            sys.exit(1)

    elif args.command == "generate-competencia-output":
        print(f"Generando análisis de competencia para: {args.name}...")
        try:
            path = generate_competencia_output(args.name)
            print(f"✅ Análisis de competencia generado en: {path}")
        except Exception as e:
            print(f"❌ Error al generar el análisis de competencia: {e}")
            sys.exit(1)

    elif args.command == "generate-canales-output":
        print(f"Generando matriz de canales para: {args.name}...")
        try:
            path = generate_canales_output(args.name)
            print(f"✅ Matriz de canales generada en: {path}")
        except Exception as e:
            print(f"❌ Error al generar la matriz de canales: {e}")
            sys.exit(1)

    elif args.command == "generate-comunicacion-output":
        print(f"Generando estrategia de comunicación para: {args.name}...")
        try:
            path = generate_comunicacion_output(args.name)
            print(f"✅ Estrategia de comunicación generada en: {path}")
        except Exception as e:
            print(f"❌ Error al generar la estrategia de comunicación: {e}")
            sys.exit(1)

    elif args.command == "generate-plan-accion-output":
        print(f"Generando plan de acción 90 días para: {args.name}...")
        try:
            path = generate_plan_accion_output(args.name)
            print(f"✅ Plan de acción generado en: {path}")
        except Exception as e:
            print(f"❌ Error al generar el plan de acción: {e}")
            sys.exit(1)

    elif args.command == "generate-presupuesto-output":
        print(f"Generando presupuesto de marketing para: {args.name}...")
        try:
            path = generate_presupuesto_output(args.name)
            print(f"✅ Presupuesto generado en: {path}")
        except Exception as e:
            print(f"❌ Error al generar el presupuesto: {e}")
            sys.exit(1)

    elif args.command == "generate-kpis-output":
        print(f"Generando KPIs y medición inicial para: {args.name}...")
        try:
            path = generate_kpis_output(args.name)
            print(f"✅ KPIs generados en: {path}")
        except Exception as e:
            print(f"❌ Error al generar los KPIs: {e}")
            sys.exit(1)

    elif args.command == "generate-resumen-empresa-output":
        print(f"Generando resumen para plan de empresa para: {args.name}...")
        try:
            path = generate_resumen_empresa_output(args.name)
            print(f"✅ Resumen generado en: {path}")
        except Exception as e:
            print(f"❌ Error al generar the resumen: {e}")
            sys.exit(1)

    elif args.command == "generate-auditoria-output":
        print(f"Generando auditoría final para: {args.name}...")
        try:
            path = generate_auditoria_output(args.name)
            print(f"✅ Auditoría final generada en: {path}")
        except Exception as e:
            print(f"❌ Error al generar la auditoría: {e}")
            sys.exit(1)
            
    else:
        parser.print_help()
# ──────────────────────────────────────────────────────────────────────
# Note: This is a CLI entry point.
# ──────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    main()

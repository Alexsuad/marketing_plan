# File: scripts/create_system_copy.py
# ──────────────────────────────────────────────────────────────────────
# Propósito: Crear una copia limpia y estéril del sistema base v1.1.
# Rol: Herramienta de despliegue y reutilización del núcleo.
# ──────────────────────────────────────────────────────────────────────

import os
import shutil
import argparse
import subprocess
from pathlib import Path
from datetime import datetime

# CONFIGURACIÓN DE LISTAS (WHITELIST)
WHITELIST = [
    "src",
    "tests",
    ".claude/skills",
    "system",
    "agents",
    "project_template",
    "docs",
    "README.md",
    "AGENTS.md",
    "pyproject.toml",
    "uv.lock",
    ".gitignore",
    ".python-version"
]

# EXCLUSIONES EXPLÍCITAS (BLACKLIST PARA LIMPIEZA ADICIONAL)
BLACKLIST_INTERNAL = [
    "docs/audits",
    "docs/archive",
    "docs/hitos",
    "docs/plans"
]

def get_args():
    parser = argparse.ArgumentParser(description="Crea una copia limpia del sistema base v1.1.")
    parser.add_argument("--name", type=str, help="Nombre del nuevo proyecto/sistema.")
    parser.add_argument("--dest", type=str, help="Ruta de destino para la copia.")
    parser.add_argument("--dry-run", action="store_true", help="Simula la operación sin realizar cambios.")
    parser.add_argument("--init-git", action="store_true", help="Inicializa un nuevo repositorio Git en el destino.")
    parser.add_argument("--create-workspace", action="store_true", help="Crea una estructura de workspace vacía en el destino.")
    return parser.parse_args()

def interactive_mode(args):
    print("\n=== INSTALADOR DE COPIA LIMPIA DEL SISTEMA BASE v1.1 ===")
    
    if not args.name:
        args.name = input("Nombre del nuevo sistema/proyecto: ").strip()
    
    if not args.dest:
        args.dest = input("Ruta de destino: ").strip()
    
    if not args.dry_run and not args.init_git:
        resp = input("¿Deseas inicializar Git en la copia nueva? (s/n): ").lower()
        args.init_git = resp == 's'
        
    if not args.dry_run and not args.create_workspace:
        resp = input("¿Deseas crear una estructura de workspace vacía? (s/n): ").lower()
        args.create_workspace = resp == 's'

    return args

def validate_destination(dest_path):
    dest = Path(dest_path)
    if dest.exists() and any(dest.iterdir()):
        print(f"\n❌ ERROR: La ruta de destino '{dest_path}' ya existe y no está vacía.")
        print("Por seguridad, el script no borrará contenido existente. Por favor, elige una ruta nueva.")
        return False
    return True

def create_manifest(dest_path, source_path, args):
    manifest_path = Path(dest_path) / "SYSTEM_COPY_MANIFEST.md"
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    content = f"""# SYSTEM_COPY_MANIFEST
    
**Generado por:** `create_system_copy.py`
**Fecha:** {now}
**Nombre del Proyecto:** {args.name}
**Repositorio Origen:** {source_path}

## Configuración de la Copia
- **Git Inicializado:** {'Sí' if args.init_git else 'No'}
- **Workspace Creado:** {'Sí' if args.create_workspace else 'No'}

## Contenido Copiado (Whitelist)
{chr(10).join([f"- {item}" for item in WHITELIST])}

---
*Este archivo certifica que la copia se realizó siguiendo el estándar de limpieza Lean 5S v1.1.*
"""
    with open(manifest_path, "w", encoding="utf-8") as f:
        f.write(content)

def main():
    args = get_args()
    
    # Entrar en modo interactivo si faltan argumentos básicos
    if not args.name or not args.dest:
        args = interactive_mode(args)

    source_root = Path(os.getcwd())
    dest_root = Path(args.dest)

    print(f"\n--- INICIANDO PROCESO {'(SIMULACIÓN)' if args.dry_run else ''} ---")
    print(f"Origen: {source_root}")
    print(f"Destino: {dest_root}")

    if not args.dry_run:
        if not validate_destination(args.dest):
            return

    # 1. Fase de Copiado
    items_to_copy = []
    for item in WHITELIST:
        src_item = source_root / item
        if src_item.exists():
            items_to_copy.append(item)
        else:
            print(f"⚠️ Aviso: '{item}' no encontrado en el origen, se omitirá.")

    if args.dry_run:
        print("\n[SIMULACIÓN] Se copiarían los siguientes elementos:")
        for item in items_to_copy:
            print(f"  + {item}")
        print("\n[SIMULACIÓN] Se crearían las siguientes estructuras:")
        print("  + projects/ (vacío e ignorado)")
        if args.create_workspace:
            print("  + workspace/ (vacío con subcarpetas)")
        if args.init_git:
            print("  + .git/ (inicialización)")
        print("  + SYSTEM_COPY_MANIFEST.md")
        print("\n--- SIMULACIÓN FINALIZADA SIN CAMBIOS ---")
        return

    # Ejecución Real
    dest_root.mkdir(parents=True, exist_ok=True)
    
    for item in items_to_copy:
        src = source_root / item
        dst = dest_root / item
        
        if src.is_dir():
            shutil.copytree(src, dst, dirs_exist_ok=True)
        else:
            dst.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(src, dst)

    # 2. Limpieza de exclusiones internas (docs obsoletos)
    for black_item in BLACKLIST_INTERNAL:
        target = dest_root / black_item
        if target.exists():
            if target.is_dir():
                shutil.rmtree(target)
            else:
                target.unlink()

    # 3. Creación de estructuras vacías
    (dest_root / "projects").mkdir(exist_ok=True)
    
    if args.create_workspace:
        ws_folders = ["inputs", "projects", "outputs", "reports", "exports", "sandbox"]
        for folder in ws_folders:
            (dest_root / "workspace" / folder).mkdir(parents=True, exist_ok=True)

    # 4. Manifiesto
    create_manifest(dest_root, source_root, args)

    # 5. Git Init
    if args.init_git:
        try:
            subprocess.run(["git", "init"], cwd=dest_root, check=True, capture_output=True)
            print("✅ Git inicializado correctamente.")
        except Exception as e:
            print(f"⚠️ Error al inicializar Git: {e}")

    print(f"\n✅ ¡Copia de sistema '{args.name}' creada con éxito en '{args.dest}'!")
    print("\nPróximos pasos recomendados en la nueva carpeta:")
    print(f"  cd '{args.dest}'")
    print("  uv sync")
    print("  uv run pytest")
    print("  uv run python -m src.main validate-base-structure")

if __name__ == "__main__":
    main()

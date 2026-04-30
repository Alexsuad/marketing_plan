# Registro de Materialización: Lote 4 — Workflows

**Estado:** `lote_4_workflows_materializado_pendiente_auditoria`
**Fecha:** 2026-04-30

## 1. Archivos Creados (`system/workflows/`)

1.  **`crear_proyecto.md`**: Flujo inicial para instanciar proyectos con validación de estructura base.
2.  **`validar_brief.md`**: Asegura que el brief de negocio es completo antes de avanzar.
3.  **`generar_fase.md`**: Proceso de creación de outputs con protección contra sobrescritura manual.
4.  **`revisar_fase.md`**: Auditoría experta con uso de gates específicos por fase (Canales, Presupuesto, KPIs, etc.).
5.  **`ajustar_fase_con_control_de_cambio.md`**: Gestión de iteraciones con evaluación de impacto estratégico.
6.  **`cerrar_hito.md`**: Protocolo de consolidación y versionado de etapas cumplidas.
7.  **`crear_zip_limpio.md`**: Generación de paquetes de entrega sin archivos técnicos redundantes.
8.  **`validar_zip_limpio.md`**: Control de calidad final sobre la integridad del ZIP.

## 2. Cumplimiento de Requisitos

- **Componentes:** Se ha aplicado la flexibilidad de "si aplica" para skills y gates.
- **Protección Manual:** `gate_no_regeneracion_fases_manuales` incluido en generación y ajuste.
- **Estados:** Estandarizados bajo la familia `workflow_*`.
- **Comandos:** Se han citado los comandos CLI de `src/main.py` donde existen.

## 3. Confirmación de Alcance

Confirmo que durante esta tarea **NO** se han modificado ni accedido para escritura los siguientes directorios/archivos:
- `src/` (Código fuente)
- `projects/` (Datos de clientes/pruebas)
- `.env` (Secretos)
- `ZIPs` (Copias de seguridad)
- `.claude/skills/` (Lógica de skills)
- `agents/` (Definición de agentes)
- `system/gates/` (Puntos de control)
- `system/rules/` (Reglas globales)

---
**Veredicto:** Materialización completada según el plan aprobado.

<!--
# File: system/rules/no_crear_skills_sin_entrada_salida_gate.md
# ──────────────────────────────────────────────────────────────────────
# Propósito: Mantener la calidad y estructura del sistema agéntico.
# Rol: Regla operativa documental (no validador Python ejecutable).
# ──────────────────────────────────────────────────────────────────────
-->

# Rule: no_crear_skills_sin_entrada_salida_gate

## 1. Propósito
Garantizar que toda nueva capacidad añadida al sistema sea modular, verificable y cumpla con el estándar arquitectónico definido.

## 2. Cuándo aplica
Aplica durante el diseño e implementación de nuevas habilidades (skills) en `.claude/skills/` o descritas en `docs/04_skills_y_uso.md`.

## 3. Comportamiento Obligatorio
- Definir claramente el **Input** (qué datos necesita para no improvisar).
- Definir claramente el **Output** (qué archivo o estado produce).
- Vincular la skill a un **Gate** de validación (cómo sabemos si lo hizo bien).
- Seguir la estructura de `docs/04_skills_y_uso.md`.

## 4. Comportamiento Prohibido
- Crear "scripts sueltos" que realicen tareas estratégicas sin estar documentados como skills oficiales.

## 5. Ejemplos de aplicación
- **Correcto:** "Propongo la `skill_analisis_precio`. Entrada: lista de servicios. Salida: `05_precios.md`. Gate: `gate_coherencia_precios`."
- **Incorrecto:** "Voy a escribir un script rápido para calcular precios."

## 6. Evidencia esperada
- Actualización de `docs/04_skills_y_uso.md` al añadir una skill.

## 7. Estado de incumplimiento
`error_skill_no_estandarizada`

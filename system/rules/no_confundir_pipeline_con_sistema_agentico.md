<!--
# File: system/rules/no_confundir_pipeline_con_sistema_agentico.md
# ──────────────────────────────────────────────────────────────────────
# Propósito: Mantener el valor del razonamiento estratégico.
# Rol: Regla operativa documental (no validador Python ejecutable).
# ──────────────────────────────────────────────────────────────────────
-->

# Rule: no_confundir_pipeline_con_sistema_agentico

## 1. Propósito
Asegurar que el sistema actúe como un asesor estratégico y no solo como un ejecutor de scripts. El valor está en el razonamiento previo a la generación.

## 2. Cuándo aplica
Aplica en la fase de toma de decisiones antes de ejecutar comandos CLI.

## 3. Comportamiento Obligatorio
- Explicar el "por qué" estratégico antes de ejecutar un comando de generación.
- Documentar las decisiones tomadas por los agentes (ej. "El estratega ha decidido priorizar Instagram sobre LinkedIn debido a X").
- Usar el pipeline (`main.py`) como herramienta de materialización, no como motor de pensamiento.

## 4. Comportamiento Prohibido
- Limitarse a ejecutar comandos en cadena sin análisis estratégico intermedio.
- Tratar el sistema como un simple conversor de Markdown.

## 5. Ejemplos de aplicación
- **Correcto:** "Dado que el cliente es B2B Industrial, activaré la skill de matriz de canales priorizando SEO técnico. [Explicación]. Ahora ejecutaré el comando para generar el output."
- **Incorrecto:** "Ejecutando fases 01 a 12..."

## 6. Evidencia esperada
- Presencia de razonamiento estratégico en los logs del agente antes de los bloques de código.

## 7. Estado de incumplimiento
`error_ejecucion_sin_razonamiento`

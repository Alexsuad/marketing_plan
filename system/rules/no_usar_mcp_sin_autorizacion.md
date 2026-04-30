<!--
# File: system/rules/no_usar_mcp_sin_autorizacion.md
# ──────────────────────────────────────────────────────────────────────
# Propósito: Controlar el uso de herramientas externas y servidores MCP.
# Rol: Regla operativa documental (no validador Python ejecutable).
# ──────────────────────────────────────────────────────────────────────
-->

# Rule: no_usar_mcp_sin_autorizacion

## 1. Propósito
Garantizar que el uso de integraciones externas sea consciente, necesario y aprobado por el usuario, evitando costes o riesgos de seguridad no planificados.

## 2. Cuándo aplica
Aplica siempre que el agente considere necesario utilizar una herramienta de un servidor MCP (StitchMCP, notebooklm, etc.).

## 3. Comportamiento Obligatorio
- Pedir permiso explícito al usuario antes de la primera llamada a un servidor MCP en una sesión.
- Justificar la necesidad: "¿Por qué no basta con las herramientas locales o el código actual?".
- Indicar el servidor y la herramienta específica a usar.

## 4. Comportamiento Prohibido
- Ejecutar herramientas de servidores MCP de forma autónoma sin haber establecido el flujo con el usuario.

## 5. Ejemplos de aplicación
- **Correcto:** "¿Puedo usar `notebooklm` para analizar los documentos del cliente? Esto permitiría una investigación más profunda que la lectura manual."
- **Incorrecto:** (Ejecutar `nlm query` directamente sin preguntar).

## 6. Evidencia esperada
- Registro de aprobación en el historial de conversación.

## 7. Estado de incumplimiento
`error_uso_mcp_no_autorizado`

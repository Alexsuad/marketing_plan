<!--
# File: system/rules/contrato_datos_entre_resolver_y_servicios.md
# ──────────────────────────────────────────────────────────────────────
# Propósito: Garantizar la integridad de los datos multimodelo.
# Rol: Regla operativa documental (no validador Python ejecutable).
# ──────────────────────────────────────────────────────────────────────
-->

# Rule: contrato_datos_entre_resolver_y_servicios

## 1. Propósito
Evitar errores de ejecución (KeyError) y fallos en el pipeline asegurando que el flujo de información entre componentes respete un contrato de datos estricto.

## 2. Cuándo aplica
Aplica al modificar o añadir lógica en resolvers, parsers, servicios o generadores de datos.

## 3. Comportamiento Obligatorio
- Asegurar que cualquier estructura de datos producida por un resolver, parser o generador incluya **todas las llaves requeridas** por los servicios que consumen esa información.
- En el caso actual de canales de marketing, todo diccionario de canal debe incluir: `name`, `objective`, `effort`, `risk` y `cost`.
- Al añadir un nuevo campo en un servicio, este debe ser añadido primero en el origen (resolver/parser) con un valor por defecto si es necesario.

## 4. Comportamiento Prohibido
- Pasar diccionarios incompletos asumiendo que el servicio consumidor manejará la ausencia de llaves con fallbacks no documentados.

## 5. Ejemplos de aplicación
- **Correcto:** El `marketing_profile_resolver` inyecta `effort: "Medio"` en el canal Email Marketing para que el `plan_accion_service` no falle al leerlo.
- **Incorrecto:** El resolver solo envía `name` y el servicio rompe al intentar acceder a `effort`.

## 6. Evidencia esperada
- Tests de integridad de contrato aprobados (`tests/test_marketing_profile_resolver.py`).

## 7. Estado de incumplimiento
`error_rotura_de_contrato_de_datos`

<!--
# File: system/rules/no_inventar_datos.md
# ──────────────────────────────────────────────────────────────────────
# Propósito: Evitar alucinaciones o datos ficticios en el Plan de Marketing.
# Rol: Regla operativa documental (no validador Python ejecutable).
# ──────────────────────────────────────────────────────────────────────
-->

# Rule: no_inventar_datos

## 1. Propósito
Garantizar que toda la información contenida en los documentos estratégicos tenga una base real en el brief del cliente, la investigación confirmada o los datos históricos del negocio.

## 2. Cuándo aplica
Aplica durante todas las fases de generación de contenido (Fases 01 a 12), especialmente en Diagnóstico, Cliente Objetivo y Análisis de Competencia.

## 3. Comportamiento Obligatorio
- Usar únicamente nombres de empresas, servicios y personas proporcionados por el usuario.
- Declarar explícitamente cuando un dato es una **hipótesis** basada en el sector mediante la etiqueta `[Hipótesis]`.
- Listar la información faltante necesaria para completar una sección.

## 4. Comportamiento Prohibido
- Inventar competidores específicos si el usuario no los ha nombrado.
- Crear cifras de presupuesto, facturación o ROAS sin base documental.
- Asumir problemas del cliente que no han sido detectados en el intake.

## 5. Ejemplos de aplicación
- **Correcto:** "El negocio declara no tener competidores identificados. Se asumen como competidores indirectos las agencias locales de marketing [Hipótesis]."
- **Incorrecto:** "Los principales competidores son Agencia X y Consultoría Y [Inventado]."

## 6. Evidencia esperada
- Presencia de la sección "Información Faltante" en los outputs.
- Uso consistente de etiquetas de nivel de certeza.

## 7. Estado de incumplimiento
`error_dato_inventado_detectado`

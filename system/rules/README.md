# Reglas del Sistema (Rules) - Lote 5

Este directorio contiene las restricciones y normas de comportamiento transversales del sistema agéntico. Estas reglas aseguran la integridad de los datos, la calidad estratégica y la estabilidad operativa del pipeline.

> [!NOTE]
> **Nota Documental:** Estas rules son reglas operativas documentales que sirven de guía para el comportamiento de los agentes. No son todavía validadores Python ejecutables.

## Índice de Reglas Actuales

1.  **[no_inventar_datos.md](no_inventar_datos.md)**: Prohíbe alucinaciones o datos ficticios; exige el uso de etiquetas `[Hipótesis]` cuando sea necesario.
2.  **[no_prometer_validacion_sin_evidencia.md](no_prometer_validacion_sin_evidencia.md)**: Exige citar archivos reales, comandos o logs antes de declarar el éxito de una tarea.
3.  **[no_usar_mcp_sin_autorizacion.md](no_usar_mcp_sin_autorizacion.md)**: Controla el uso de herramientas externas (MCP) mediante solicitud de permiso previa.
4.  **[no_regenerar_fases_manuales.md](no_regenerar_fases_manuales.md)**: Protege documentos marcados como `[CONGELADO]` o `[MANUAL]` de sobrescrituras accidentales.
5.  **[no_confundir_pipeline_con_sistema_agentico.md](no_confundir_pipeline_con_sistema_agentico.md)**: Prioriza el análisis estratégico y la explicación del "por qué" sobre la ejecución técnica pura.
6.  **[no_crear_skills_sin_entrada_salida_gate.md](no_crear_skills_sin_entrada_salida_gate.md)**: Garantiza que toda nueva capacidad cumpla con el estándar modular definido.
7.  **[cierre_con_evidencia.md](cierre_con_evidencia.md)**: Estandariza el resumen final de intervenciones (archivos, cambios, verificación y próximos pasos).
8.  **[mantener_alcance_por_lote.md](mantener_alcance_por_lote.md)**: Bloquea el inicio de nuevos lotes de desarrollo hasta que el actual haya sido auditado y aprobado.
9.  **[contrato_datos_entre_resolver_y_servicios.md](contrato_datos_entre_resolver_y_servicios.md)**: Asegura que el flujo de datos entre componentes respete las llaves requeridas (evita KeyError).
10. **[no_declarar_incidencia_resuelta_sin_validacion_completa.md](no_declarar_incidencia_resuelta_sin_validacion_completa.md)**: Exige validación multimodelo y de regresión ante cambios críticos en el core.

---
**Versión del Lote:** 5.0  
**Estado:** Materializado y Auditado

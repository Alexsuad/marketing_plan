# Gate: No Invención

> [!NOTE]
> Estos gates son especificaciones operativas documentales. No son todavía validadores ejecutables en Python. Su automatización queda pendiente para una fase posterior.

- **Nombre:** gate_no_invencion
- **Propósito:** Prevenir que el sistema cubra huecos de información con "alucinaciones".
- **Cuándo se activa:** Después de `skill_diagnostico_marketing` y `skill_analisis_competencia`.
- **Entradas:** Output de las skills implicadas.
- **Criterios de Aprobación:** Toda afirmación clave tiene base en el brief original, o bien se etiqueta explícitamente como "Hipótesis a validar" / "Arquetipo".
- **Criterios de Bloqueo:** Detección de marcas inventadas, datos estadísticos falsos, o asunciones sobre el negocio presentadas como hechos absolutos sin fuente.
- **Salida:** `estado_revision_ficticia_pasada` o `estado_bloqueo_por_invencion`.
- **Agente Responsable:** `auditor_plan_marketing`.
- **Evidencia requerida:** Mapeo de hechos clave contra su fuente original en el brief.
- **Estado final posible:** `Aprobado`, `Bloqueado_Correccion_Requerida`.

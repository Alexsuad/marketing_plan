# Gate: Auditoría Final

> [!NOTE]
> Estos gates son especificaciones operativas documentales. No son todavía validadores ejecutables en Python. Su automatización queda pendiente para una fase posterior.

- **Nombre:** gate_auditoria_final
- **Propósito:** La última barrera antes de dar por completado un hito de entrega del plan.
- **Cuándo se activa:** Después de `skill_auditoria_coherencia`.
- **Entradas:** Todo el directorio `outputs/plan_actual/`.
- **Criterios de Aprobación:** Todos los gates anteriores están aprobados. Coherencia narrativa end-to-end.
- **Criterios de Bloqueo:** Contradicciones (ej. canal es LinkedIn pero cliente objetivo no usa LinkedIn detectado en auditoría).
- **Salida:** `estado_plan_marketing_validado_para_entrega` o `estado_plan_marketing_con_fallas`.
- **Agente Responsable:** `auditor_plan_marketing`.
- **Evidencia requerida:** Reporte final de auditoría con veredicto.
- **Estado final posible:** `Aprobado_Global`, `Falla_Estructural`.

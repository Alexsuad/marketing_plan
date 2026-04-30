# Gate: Presupuesto Prudente

> [!NOTE]
> Estos gates son especificaciones operativas documentales. No son todavía validadores ejecutables en Python. Su automatización queda pendiente para una fase posterior.

- **Nombre:** gate_presupuesto_prudente
- **Propósito:** Prevenir promesas de presupuestos exactos incalculables, priorizando rangos.
- **Cuándo se activa:** Después de `skill_presupuesto_marketing`.
- **Entradas:** `09_presupuesto_marketing.md`.
- **Criterios de Aprobación:** Todo presupuesto de proveedor, herramienta o Ads se expresa en horquillas o rangos. 
- **Criterios de Bloqueo:** Existencia de valores monetarios absolutos generados por IA (ej. "El diseño web costará 500$").
- **Salida:** `estado_presupuesto_validado` o `estado_presupuesto_rechazado`.
- **Agente Responsable:** `auditor_plan_marketing`.
- **Evidencia requerida:** Ausencia de valores fijos mediante checkeo expreso.
- **Estado final posible:** `Aprobado`, `Rechazado_Valores_Fijos`.

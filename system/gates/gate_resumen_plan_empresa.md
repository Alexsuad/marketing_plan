# Gate: Resumen Plan Empresa

> [!NOTE]
> Estos gates son especificaciones operativas documentales. No son todavía validadores ejecutables en Python. Su automatización queda pendiente para una fase posterior.

- **Nombre:** gate_resumen_plan_empresa
- **Propósito:** Garantizar que el resumen incluya lo crítico y excluya el "ruido operativo".
- **Cuándo se activa:** Después de `skill_resumen_plan_empresa`.
- **Entradas:** `11_resumen_para_plan_empresa.md`.
- **Criterios de Aprobación:** Inclusión explícita de: cliente, propuesta, 1 o 2 canales, rangos de presupuesto, KPI. No supera un límite de longitud.
- **Criterios de Bloqueo:** Omisión de presupuestos o KPIs; exceso de detalle de acciones diarias de 90 días.
- **Salida:** `estado_resumen_aprobado` o `estado_resumen_incompleto`.
- **Agente Responsable:** `auditor_plan_marketing`.
- **Evidencia requerida:** Checkbox de los 5 elementos clave.
- **Estado final posible:** `Aprobado`, `Bloqueado`.

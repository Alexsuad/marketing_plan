# Gate: KPIs Medibles

> [!NOTE]
> Estos gates son especificaciones operativas documentales. No son todavía validadores ejecutables en Python. Su automatización queda pendiente para una fase posterior.

- **Nombre:** gate_kpis_medibles
- **Propósito:** Asegurar que el plan se mida con métricas de negocio, no de vanidad.
- **Cuándo se activa:** Después de `skill_kpis`.
- **Entradas:** `10_kpis_y_medicion.md`.
- **Criterios de Aprobación:** Hay un KPI principal atado a adquisición, costo o conversión; las herramientas de medición sugeridas son acordes a la madurez de la empresa.
- **Criterios de Bloqueo:** Solo existen métricas de vanidad (likes, reproducciones) como KPI principal; se sugieren analíticas Enterprise para un negocio hiper-local de bajo recurso.
- **Salida:** `estado_kpis_aprobados` o `estado_kpis_vanidosos`.
- **Agente Responsable:** `analista_metricas`.
- **Evidencia requerida:** Listado de los KPIs principales justificando su impacto de negocio.
- **Estado final posible:** `Aprobado`, `Bloqueado`.

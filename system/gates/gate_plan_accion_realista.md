# Gate: Plan de Acción Realista

> [!NOTE]
> Estos gates son especificaciones operativas documentales. No son todavía validadores ejecutables en Python. Su automatización queda pendiente para una fase posterior.

- **Nombre:** gate_plan_accion_realista
- **Propósito:** Asegurar que la ejecución táctica en los primeros 90 días no satura la operativa.
- **Cuándo se activa:** Después de `skill_plan_accion`.
- **Entradas:** `08_plan_accion_90_dias.md`.
- **Criterios de Aprobación:** Acciones distribuidas en el tiempo y no acumuladas en la primera semana; presencia de tareas fundacionales previas a activación.
- **Criterios de Bloqueo:** Tareas irreales (ej. "lanzar campaña" en el día 1 sin activos previos), o un volumen de tareas inasumible por un equipo pequeño.
- **Salida:** `estado_plan_aprobado` o `estado_plan_saturado`.
- **Agente Responsable:** `auditor_plan_marketing`.
- **Evidencia requerida:** Línea de tiempo con conteo de tareas por fase (Mes 1, Mes 2, Mes 3).
- **Estado final posible:** `Aprobado`, `Bloqueado_por_capacidad`.

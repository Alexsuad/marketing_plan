# Gate: Cierre de Hito

> [!NOTE]
> Estos gates son especificaciones operativas documentales. No son todavía validadores ejecutables en Python. Su automatización queda pendiente para una fase posterior.

- **Nombre:** gate_cierre_hito
- **Propósito:** Asegurar la persistencia o snapshot antes de mover el estado global del sistema.
- **Cuándo se activa:** Al concluir una gran iteración de los documentos base.
- **Entradas:** Estado global (auditoría aprobada).
- **Criterios de Aprobación:** Todas las evidencias generadas, versión congelada en outputs.
- **Criterios de Bloqueo:** Auditoría fallida, outputs faltantes.
- **Salida:** `hito_cerrado`.
- **Agente Responsable:** `orquestador_plan_marketing`.
- **Evidencia requerida:** Snapshot guardado.
- **Estado final posible:** `Cerrado`, `Pendiente`.

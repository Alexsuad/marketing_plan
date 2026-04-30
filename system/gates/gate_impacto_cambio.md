# Gate: Impacto de Cambio

> [!NOTE]
> Estos gates son especificaciones operativas documentales. No son todavía validadores ejecutables en Python. Su automatización queda pendiente para una fase posterior.

- **Nombre:** gate_impacto_cambio
- **Propósito:** Evaluar y clasificar el impacto antes de sobrescribir documentos de un plan vivo.
- **Cuándo se activa:** Después de `skill_change_request`.
- **Entradas:** `outputs/changelog/change_request_vX.md`.
- **Criterios de Aprobación:** Se ha calculado el impacto (Bajo, Medio, Alto). Si es Alto, requiere aprobación explícita de usuario.
- **Criterios de Bloqueo:** Solicitud ambigua o intento de reescribir pilares estratégicos sin registro.
- **Salida:** `cambio_autorizado` o `esperando_aprobacion_usuario`.
- **Agente Responsable:** `orquestador_plan_marketing`.
- **Evidencia requerida:** Registro de impacto y lista de documentos en cascada a modificar.
- **Estado final posible:** `Aprobado`, `Aprobacion_Manual_Requerida`.

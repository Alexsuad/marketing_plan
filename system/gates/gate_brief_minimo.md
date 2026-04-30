# Gate: Brief Mínimo

> [!NOTE]
> Estos gates son especificaciones operativas documentales. No son todavía validadores ejecutables en Python. Su automatización queda pendiente para una fase posterior.

- **Nombre:** gate_brief_minimo
- **Propósito:** Asegurar que existe la información base obligatoria antes de iniciar la estrategia.
- **Cuándo se activa:** Después de ejecutar `skill_intake_brief`.
- **Entradas:** `01_brief_negocio_validado.md`.
- **Criterios de Aprobación:** Están presentes todos los campos obligatorios: nombre, tipo, servicio, cliente objetivo, problema y objetivo. Ninguno tiene valores vacíos o suposiciones no verificadas.
- **Criterios de Bloqueo:** Falta alguno de los campos obligatorios o se detecta texto como "por definir".
- **Salida:** `estado_brief_aprobado` o `estado_brief_bloqueado_faltan_datos`.
- **Agente Responsable:** `orquestador_plan_marketing`.
- **Evidencia requerida:** Lista explícita de los campos encontrados y su estado de validación.
- **Estado final posible:** `Aprobado`, `Bloqueado`.

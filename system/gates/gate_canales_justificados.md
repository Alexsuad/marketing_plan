# Gate: Canales Justificados

> [!NOTE]
> Estos gates son especificaciones operativas documentales. No son todavía validadores ejecutables en Python. Su automatización queda pendiente para una fase posterior.

- **Nombre:** gate_canales_justificados
- **Propósito:** Evitar "estar en todas partes". Asegurar que los canales elegidos tienen sentido para los recursos y el cliente.
- **Cuándo se activa:** Después de `skill_matriz_canales`.
- **Entradas:** `06_matriz_canales_marketing.md` y capacidades internas del cliente.
- **Criterios de Aprobación:** Solo 1 canal principal y 1 secundario recomendados. Existe un párrafo justificando recursos (tiempo/equipo) compatibles.
- **Criterios de Bloqueo:** Se recomiendan múltiples redes masivas injustificadas o canales que superan las capacidades técnicas declaradas.
- **Salida:** `estado_canales_aprobados` o `estado_canales_rechazados`.
- **Agente Responsable:** `estratega_marketing` (revisión).
- **Evidencia requerida:** Razón de elección y mapeo con recursos disponibles (o declarados nulos).
- **Estado final posible:** `Aprobado`, `Bloqueado`.

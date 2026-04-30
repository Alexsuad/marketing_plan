# Gate: Coherencia Cliente -> Propuesta

> [!NOTE]
> Estos gates son especificaciones operativas documentales. No son todavía validadores ejecutables en Python. Su automatización queda pendiente para una fase posterior.

- **Nombre:** gate_coherencia_cliente_propuesta
- **Propósito:** Validar que lo que se ofrece soluciona directamente el dolor del cliente elegido y no está adornado con jerga vacía.
- **Cuándo se activa:** Después de `skill_propuesta_valor` y `skill_estrategia_comunicacion`.
- **Entradas:** `03_cliente_objetivo_y_segmentos.md`, `04_propuesta_valor_y_posicionamiento.md`, `07_estrategia_comunicacion.md`.
- **Criterios de Aprobación:** La propuesta aborda un dolor/objeción del cliente sin usar superlativos ("líder", "el mejor"). Los pilares de comunicación mapean 1 a 1 con dolores u objeciones.
- **Criterios de Bloqueo:** Uso de superlativos vacíos detectados, o pilares de contenido genéricos sin relación con el cliente (ej. "frases motivacionales" para un B2B industrial).
- **Salida:** `estado_coherencia_aprobada` o `estado_incoherencia_detectada`.
- **Agente Responsable:** `auditor_plan_marketing`.
- **Evidencia requerida:** Tabla o lista emparejando `Pilar de contenido` -> `Dolor del cliente`.
- **Estado final posible:** `Aprobado`, `Observaciones`.

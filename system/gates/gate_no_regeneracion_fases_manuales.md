# Gate: No Regeneración de Fases Manuales

> [!NOTE]
> Estos gates son especificaciones operativas documentales. No son todavía validadores ejecutables en Python. Su automatización queda pendiente para una fase posterior.

- **Nombre:** gate_no_regeneracion_fases_manuales
- **Propósito:** Prevenir que la IA reescriba archivos que el usuario ha marcado como "manuales" o "congelados".
- **Cuándo se activa:** Al iniciar cualquier update a `outputs/plan_actual/`.
- **Entradas:** Metadata de archivos, tags de congelamiento o logs de edición manual.
- **Criterios de Aprobación:** El archivo destino no tiene tag de "manual" o "freeze".
- **Criterios de Bloqueo:** El archivo tiene un tag que impide su sobrescritura automática.
- **Salida:** `escritura_permitida` o `escritura_bloqueada_por_fase_manual`.
- **Agente Responsable:** `orquestador_plan_marketing`.
- **Evidencia requerida:** Check de permisos/tags en el archivo objetivo.
- **Estado final posible:** `Permitido`, `Bloqueado`.

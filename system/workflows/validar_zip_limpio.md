# Workflow: validar_zip_limpio

**Propósito:** Asegurar que el paquete ZIP generado está completo, íntegro y cumple con los estándares de entrega.
**Cuándo se usa:** Inmediatamente después de `crear_zip_limpio.md`.
**Agente responsable:** `auditor_plan_marketing`

---

## Componentes
- **Skills implicadas:** n/a.
- **Gates obligatorios:** n/a.
- **Comandos deterministas:** n/a (verificación de contenido).

---

## Pasos Operativos

1. **Verificación de Estructura Interna:**
   - Abrir el ZIP (o listar contenido).
   - Comprobar que existe el Brief Validado y el `project_config.json`.
   - Comprobar que el número de archivos en `outputs/` coincide con las fases completadas.

2. **Control de Limpieza:**
   - Verificar que no hay archivos `.env`, claves API, o carpetas `__pycache__` dentro del paquete.

3. **Veredicto Final:**
   - Si todo es correcto: marcar el ZIP como "Validado para entrega".
   - Si falta algo: invalidar el ZIP y pedir re-generación.

---

## Control y Salida
- **Archivos que puede tocar:** Metadata del ZIP (comentarios).
- **Archivos que no debe tocar:** Contenido del ZIP (solo lectura).
- **Evidencia requerida:** Checklist de validación completado.
- **Salida esperada:** ZIP validado.
- **Estados finales posibles:**
  - `workflow_completado`
  - `workflow_error_operativo`
  - `workflow_pendiente_validacion`

---

> [!CAUTION]
> No entregar nunca un ZIP que no haya pasado por este workflow de validación.

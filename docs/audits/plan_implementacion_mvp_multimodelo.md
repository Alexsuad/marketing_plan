# Plan de Implementación: MVP Multimodelo (Productos y Servicios)

## 1. Objetivo
Transformar el sistema de Planes de Marketing para que sea agnóstico al tipo de negocio, permitiendo modelar tanto empresas de servicios como de productos (B2B, B2C, Ecommerce, Retail, Híbridos).

## 2. Cambios Estructurales (Campos del Brief)
Se migrarán los campos sesgados a nombres neutros:
- `tipo_empresa_servicios` → `tipo_negocio`
- `servicio_principal` → `oferta_principal`

## 3. Fases de Ejecución

### Fase 1: Actualización de Documentación Rectora
- **README.md**: Cambiar "empresa de servicios" por "negocios/empresas". Actualizar tabla de brief y descripción de perfiles.
- **AGENTS.md**: Actualizar alcance y campos obligatorios.
- **docs/00_planificacion_...**: Eliminar restricciones semánticas a servicios.

### Fase 2: Ajuste de Plantillas (project_template)
- Renombrar `project_template/context/servicios.md` a `project_template/context/oferta.md`.
- Actualizar contenido de `empresa.md` y `oferta.md` para usar terminología neutra.

### Fase 3: Refactorización de Lógica (src/)
- **src/validators/brief_validator.py**: Cambiar claves de validación.
- **src/core/marketing_profile_resolver.py**:
    - Actualizar `PROFILE_KEYWORDS` con términos de productos/ecommerce.
    - Añadir perfiles: `b2c_producto_ecommerce`, `b2b_producto_industrial`, `retail_fisico`.
    - Ajustar el fallback de `servicios_generales` a `estrategia_general_prudente`.
- **src/services/**: Actualizar `resumen_empresa`, `propuesta_valor` y `diagnostico` para que busquen los nuevos nombres de campos.

### Fase 4: Pruebas y Validación
- Actualizar `tests/test_marketing_profile_resolver.py`.
- Añadir nuevos casos de prueba para:
    - Ecommerce (Zapatillas).
    - Retail Local (Ferretería).
    - Producto Industrial (Válvulas).
    - Híbrido (Software + Soporte).

### Fase 5: Informe Final
- Crear `docs/audits/auditoria_alcance_multimodelo_mvp.md`.

## 4. Riesgos Identificados
- **Inconsistencia en prompts**: Si existen prompts en archivos `.md` de skills que no se actualizan, la IA podría seguir pidiendo "servicios".
- **Falsos positivos en perfiles**: Al añadir muchas palabras clave, el resolver podría clasificar erróneamente. Se requiere ajuste fino de umbrales.
- **Compatibilidad con proyectos anteriores**: Los proyectos existentes podrían romperse al validar el brief (no es crítico ya que estamos en fase MVP y no se deben tocar proyectos reales).

## 5. Verificación de Éxito
- `uv run pytest` pasa al 100%.
- El comando `validate-brief` funciona con los nuevos campos.
- El informe de auditoría refleja el nuevo estado: `sesgo_servicios_corregido_y_mvp_multimodelo_validado`.

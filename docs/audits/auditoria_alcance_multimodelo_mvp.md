# Auditoría: Transición a Sistema Multimodelo y Neutralidad de Alcance

**Fecha**: 2026-04-30
**Estado**: FINALIZADO - SESGOS ELIMINADOS
**Responsable**: Antigravity (Experto en Marketing)

## 1. Objetivo de la Intervención
Eliminar el sesgo de "Empresa de Servicios" del MVP del sistema de Planes de Marketing, permitiendo la gestión agnóstica de cualquier modelo de negocio (Servicios, Producto Industrial, Ecommerce, Retail, Educación).

## 2. Acciones Realizadas

### A. Capa de Datos y Plantillas (Infraestructura)
- **Neutralización de Terminología**: Migración global de `tipo_empresa_servicios` -> `tipo_negocio` y `servicio_principal` -> `oferta_principal`.
- **Refactorización de Contexto**: Renombrado de archivos en `project_template/` (`servicios.md` -> `oferta.md`) para reflejar un alcance multimodelo.
- **Configuración agnóstica**: Actualización de `project_config.json` para incluir los nuevos campos neutros.

### B. Capa de Lógica (Core)
- **Implementación Multimodelo**: El `marketing_profile_resolver` ahora cuenta con 6 perfiles diferenciados:
  - `b2b_consultivo`
  - `b2c_local_servicios`
  - `educativo_formativo`
  - `b2c_producto_ecommerce`
  - `b2b_producto_industrial`
  - `retail_fisico`
- **Algoritmo de Scoring Optimizado**: Se implementó una lógica de `set(keywords)` para evitar el conteo doble y se depuraron colisiones (ej. el término 'bar' colisionaba con 'barrio').
- **Mecanismo de Fallback**: Inclusión de `estrategia_general_prudente` para casos de empate o información insuficiente.

### C. Capa de Servicios (Generación)
- **Actualización de Servicios Críticos**: Refactorización de:
  - `resumen_empresa_service.py`
  - `propuesta_valor_service.py`
  - `diagnostico_service.py`
  - `cliente_service.py`
  - `canales_service.py`
  - `comunicacion_service.py`
- **Validación Automática**: Ajuste de `brief_validator.py` para requerir los nuevos campos neutros.

## 3. Resultados de Verificación
- **Tests Unitarios**: 8/8 tests aprobados en `tests/test_marketing_profile_resolver.py`, cubriendo todos los perfiles y casos de empate.
- **Validación Estructural**: `uv run python -m src.main validate-base-structure` confirma la integridad del sistema.

## 4. Conclusión
El sistema ha dejado de ser una herramienta exclusiva para servicios. La estructura actual permite escalar a nuevos modelos de negocio simplemente añadiendo palabras clave al `resolver`, sin necesidad de modificar el código de los servicios de generación, los cuales ahora operan bajo una lógica de "oferta" neutral.

## 5. Próximos Pasos Recomendados
1. **Auditoría de Skills Lote 3**: Iniciar la revisión de las skills de presupuesto y KPIs con el nuevo enfoque multimodelo.
2. **Documentación de Usuario**: Actualizar el manual de uso para explicar cómo completar el brief en casos de Ecommerce o Retail.
3. **Casos de Éxito**: Generar un proyecto de prueba real para un modelo `b2c_producto_ecommerce` para validar la narrativa final.

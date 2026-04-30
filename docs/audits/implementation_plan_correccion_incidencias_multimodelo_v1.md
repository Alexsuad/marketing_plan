# Plan de Implementación: Corrección de Incidencias Multimodelo v1.0

## 1. Objetivo Técnico
Estabilizar el pipeline de generación de marketing eliminando el bloqueo en las fases 08-12 y mejorando la precisión de la clasificación de perfiles para modelos de negocio Ecommerce e Híbridos (Venta + Servicio).

## 2. Alcance Exacto
- **Corrección Estructural**: Estandarización del contrato de datos en `marketing_profile_resolver.py`.
- **Expansión de Conocimiento**: Creación de 2 nuevos perfiles estratégicos.
- **Adaptación Semántica**: Implementación de una capa de terminología dinámica para evitar lenguaje de servicios en productos.
- **Validación**: Batería de tests que aseguren el flujo completo de 12 fases.

## 3. Archivos Propuestos para Modificación
- `src/core/marketing_profile_resolver.py`: (Principal) Añadir llaves de canal, nuevos perfiles y terminología.
- `tests/test_marketing_profile_resolver.py`: Añadir validaciones de contrato y nuevos perfiles.

## 4. Archivos que NO se deben tocar
- `src/services/plan_accion_service.py` (Solo lectura)
- `src/services/presupuesto_service.py` (Solo lectura)
- `src/main.py`: (Solo lectura para consulta de comandos)
- `src/utils/markdown_utils.py`: Las funciones de I/O son estables.
- `system/gates/*`: Los gates documentales son válidos.

## 5. Estrategia por Incidencia

### INC-001: Bloqueo de Pipeline (Fases 08-12)
- **Acción**: Actualizar todos los diccionarios de canales en `PROFILES` dentro de `marketing_profile_resolver.py`.
- **Cambio**: 
  ```python
  # De:
  {"name": "Email Marketing", "objective": "Fidelización"}
  # A:
  {"name": "Email Marketing", "objective": "Fidelización", "effort": "Medio", "risk": "Bajo", "cost": "Bajo"}
  ```
- **Justificación**: Esto elimina los `KeyError` en los servicios consumidores de forma inmediata en el origen de los datos.

### INC-002: Ecommerce Transaccional
- **Acción**: Añadir el perfil `ecommerce_transaccional`.
- **Señales**: "carrito de compra", "checkout", "shopify", "envíos", "tienda online", "ROAS", "ticket medio".
- **Canales**: Publicidad en buscadores (Shopping), Retargeting, Email de recuperación, Redes sociales transaccionales.
- **Terminología**: Verbos como "Comprar", "Añadir", "Recibir".

### INC-004: Modelo Híbrido (Producto + Servicio)
- **Acción**: Añadir el perfil `hibrido_producto_servicio`.
- **Señales**: "instalación", "mantenimiento preventivo", "soporte técnico", "venta de equipo", "licenciamiento".
- **Lógica**: Combinar la venta directa del activo (foco producto) con la recurrencia del soporte (foco servicio).
- **Terminología**: "Adquirir", "Solución", "Soporte", "Garantía".

### INC-003: Terminología Residual
- **Acción**: Añadir una llave `terminology` al diccionario de cada perfil.
- **Uso**: Los servicios usarán esta terminología para inyectar verbos y sustantivos adecuados en los outputs de markdown.
- **Ejemplo**: `b2c_ecommerce` -> `"acción_principal": "comprar"`, mientras que `b2b_servicios` -> `"acción_principal": "contratar"`.

## 6. Tests Mínimos y Verificación
1. **Test de Integridad de Contrato**: Verificar que CUALQUIER canal devuelto por el resolver contenga `name`, `objective`, `effort`, `risk` y `cost`.
2. **Test de Clasificación Ecommerce**: Validar que el brief de "Auriculares Premium" active el perfil `ecommerce_transaccional`.
3. **Test de Clasificación Híbrido**: Validar que el brief de "Impresoras 3D + Mantenimiento" active el perfil `hibrido_producto_servicio`.
4. **Test de Flujo Completo**: Ejecutar las 12 fases mediante un mock de proyecto y verificar que no hay excepciones hasta el final.

## 7. Comandos de Verificación
```bash
# 1. Ejecutar tests unitarios y de contrato
uv run pytest tests/test_marketing_profile_resolver.py

# 2. Validar generación fase a fase (Comandos reales)
uv run python -m src.main generate-plan-accion-output --name "audit_b2c_ecommerce"
uv run python -m src.main generate-presupuesto-output --name "audit_b2c_ecommerce"
```

## 8. Riesgos Técnicos
- **Sesgo de puntuación**: Que el nuevo perfil híbrido "robe" puntos a perfiles industriales puros.
- **Sobreajuste**: Que la terminología se vuelva demasiado rígida y no encaje en frases gramaticales complejas.

## 9. Plan de Rollback
En caso de fallo masivo en la clasificación:
1. `git checkout src/core/marketing_profile_resolver.py` (Revertir al estado estable previo).
2. Restaurar versión anterior de perfiles.

## 10. Estado Final Esperado
`diagnostico_multimodelo_corregido_y_pipeline_estable`.

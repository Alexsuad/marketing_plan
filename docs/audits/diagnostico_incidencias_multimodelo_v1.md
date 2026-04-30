# Informe de Diagnóstico Técnico — Incidencias Multimodelo v1.0

## 1. Identificación de la Causa Raíz (INC-001 — Crítica)

La rotura del pipeline en las fases 08 a 12 se debe a una **rotura de contrato de datos** entre el componente `marketing_profile_resolver.py` y los servicios consumidores.

- **Archivo/Función responsable:** `src/core/marketing_profile_resolver.py` (falta de llaves en diccionarios) y `src/services/plan_accion_service.py` / `src/services/presupuesto_service.py` (acceso a llaves inexistentes).
- **Detalle técnico:** Los servicios de las fases finales intentan acceder a atributos de los canales que no están definidos en el perfil devuelto por el resolver.
  - En **Fase 08**: Se intenta acceder a `channel['effort']` y `channel['risk']`.
  - En **Fase 09**: Se intenta acceder a `channel['cost']`.
- **Dato producido por el resolver:** Un diccionario de canal con solo `{ "name": "...", "objective": "..." }`.
- **Dato esperado por los servicios:** Un diccionario extendido con `{ "name": "...", "objective": "...", "effort": "...", "risk": "...", "cost": "..." }`.

## 2. Diagnóstico de Clasificación (INC-002 e INC-004)

### INC-002 — Ecommerce no detectado
- **Causa:** La lógica de desempate en `resolve_marketing_profile` envía cualquier conflicto de puntuación al fallback `estrategia_general_prudente`. Un negocio ecommerce que menciona "tienda" o "productos" compite con el perfil `retail_fisico`, provocando un empate y activando el fallback genérico.
- **Debilidad:** El umbral `MIN_MATCHES = 2` es muy bajo para diferenciar modelos complejos, y la lista de keywords para ecommerce es limitada.

### INC-004 — Modelo Híbrido
- **Causa:** El perfil `hibrido_producto_servicio` no existe en la definición de `PROFILES`. Los negocios híbridos puntúan alto en "servicios" y "productos" simultáneamente, lo que garantiza un empate y, por tanto, una caída al fallback prudente.

## 3. Terminología Residual (INC-003)
- **Causa:** Los textos en `PROFILES` son estáticos y fueron redactados con un sesgo inicial hacia servicios profesionales. No existe una capa de "traducción" o "adaptación semántica" que cambie verbos como "contratar" por "comprar" según el perfil detectado.

## 4. Propuesta de Corrección Mínima (Sin romper Fases 01-07)

1. **Estandarizar Contrato:** Actualizar `PROFILES` en `src/core/marketing_profile_resolver.py` para que todos los diccionarios de canales incluyan llaves `effort`, `risk` y `cost` (aunque sea con valores "Pendiente de definir").
2. **Nuevos Perfiles:** 
   - Crear `ecommerce_transaccional`: Foco en ROAS, conversión directa y logística.
   - Crear `hibrido_producto_servicio`: Combinación de venta de activo y recurrencia.
3. **Refuerzo de Keywords:** Ampliar `PROFILE_KEYWORDS` con términos técnicos específicos (D2C, B2B2C, SaaS, suscripción, ticket medio, etc.).
4. **Mapeo de Terminología:** Añadir una llave `terminology` a cada perfil con verbos de acción recomendados:
   - `b2c_local`: ["reservar", "visitar", "llamar"]
   - `ecommerce`: ["comprar", "añadir al carrito", "recibir"]
   - `b2b_industrial`: ["solicitar cotización", "homologar", "pedir catálogo"]

## 5. Plan de Pruebas y Riesgos

- **Tests mínimos:** 
  - Test de regresión para asegurar que los perfiles actuales siguen funcionando.
  - Test de "Contrato Completo" para validar que cualquier perfil devuelto tiene todas las llaves requeridas por los servicios 08-12.
  - Test de "Detección Específica" para los 5 casos de la auditoría multimodelo.
- **Riesgos:** Modificar el resolver afecta a TODO el sistema. Un error en la lógica de puntuación podría cambiar planes que ya estaban funcionando correctamente en las fases 01-07.

## 6. Clasificación de Archivos

| Acción | Archivos |
|---|---|
| **Modificar** | `src/core/marketing_profile_resolver.py`, `src/services/plan_accion_service.py`, `src/services/presupuesto_service.py` |
| **Añadir/Actualizar** | `tests/test_marketing_resolver.py` |
| **NO Tocar** | `src/main.py` (la estructura CLI es correcta), `src/utils/project_io.py`, `system/gates/*` |

---

**Estado final recomendado:** `diagnostico_incidencias_multimodelo_creado`

# Plan de Implementación: Validación Multimodelo del Sistema de Planes de Marketing

Este plan describe la estrategia para validar que el sistema genera planes coherentes y libres de sesgos para diversos modelos de negocio, asegurando que la refactorización técnica se traduzca en una narrativa estratégica correcta en las 12 fases.

## 1. Escenarios de Prueba (Briefs)

Se proponen 5 casos de prueba extremos para estresar el `marketing_profile_resolver` y los servicios de generación:

| ID | Modelo de Negocio | Descripción | Clave de Validación |
| :--- | :--- | :--- | :--- |
| **B2B-S** | Servicio B2B | Consultoría en Ciberseguridad para Bancos. | Enfoque en confianza, ciclo largo y LinkedIn. |
| **B2C-E** | Ecommerce B2C | Marca de auriculares premium de madera (D2C). | Enfoque en producto, logística, Instagram/TikTok. |
| **RET-L** | Retail Físico | Panadería Artesanal de masa madre en barrio. | Enfoque en cercanía, tráfico local y Google Maps. |
| **B2B-P** | Industrial B2B | Fabricante de válvulas para plantas petroquímicas. | Enfoque en ficha técnica, ferias y catálogo industrial. |
| **HYB-M** | Híbrido | Venta de Impresoras 3D + Servicio de mantenimiento. | Equilibrio entre venta de activo y recurrencia. |

## 2. Matriz de Validación de Fases

Para cada fase, se evaluarán los siguientes criterios de "Neutralidad y Coherencia":

| Fase | Criterio de Éxito | Riesgo Detectado (Sesgo de Servicio) |
| :--- | :--- | :--- |
| **01-02** | Usa `tipo_negocio` y `oferta_principal`. | Que hable de "atención al cliente" cuando es "calidad de producto". |
| **03-04** | Segmentos y Propuesta adaptados (ej. "Durabilidad" vs "Soporte"). | Que asuma que el valor es "el tiempo del consultor". |
| **05** | Compara con competidores del mismo modelo. | Que busque "agencias" en lugar de "marcas" o "fábricas". |
| **06-07** | Canales físicos (Retail) o de catálogo (Industrial). | Que recomiende LinkedIn/Contenidos a una panadería de barrio. |
| **08-09** | Acciones de stock/envío vs acciones de agenda/reunión. | Que pida "reuniones de diagnóstico" para vender unos auriculares. |
| **10-11** | KPIs de ventas/unitarios vs KPIs de leads/horas. | Que el resumen hable de "nosotros te ayudamos" en lugar de "ofrecemos X". |
| **12** | Auditoría detecta si el tono es incorrecto. | Que la auditoría no detecte que un plan industrial parece de coaching. |

## 3. Protocolo de Ejecución (Comandos)

Para cada proyecto (`B2B-S`, `B2C-E`, etc.):

1.  **Creación**: `uv run python -m src.main create-project --name "TEST_MODELO"`
2.  **Poblar Brief**: Modificar `projects/TEST_MODELO/context/brief_negocio.md`.
3.  **Validación**: `uv run python -m src.main validate-brief --name "TEST_MODELO"`
4.  **Generación Total**: 
    ```powershell
    uv run python -m src.main generate-resumen-empresa --name "TEST_MODELO"
    uv run python -m src.main generate-diagnostico --name "TEST_MODELO"
    uv run python -m src.main generate-cliente --name "TEST_MODELO"
    uv run python -m src.main generate-propuesta --name "TEST_MODELO"
    uv run python -m src.main generate-competencia --name "TEST_MODELO"
    uv run python -m src.main generate-canales --name "TEST_MODELO"
    uv run python -m src.main generate-comunicacion --name "TEST_MODELO"
    uv run python -m src.main generate-plan-accion --name "TEST_MODELO"
    uv run python -m src.main generate-presupuesto --name "TEST_MODELO"
    uv run python -m src.main generate-kpis --name "TEST_MODELO"
    uv run python -m src.main generate-resumen-final --name "TEST_MODELO"
    uv run python -m src.main generate-auditoria --name "TEST_MODELO"
    ```

## 4. Riesgos Identificados y Archivos Sensibles

Identificamos los servicios que podrían requerir ajustes quirúrgicos si los tests fallan:

*   **Riesgo 1**: `src/services/competencia_service.py` -> Podría comparar erróneamente empresas de productos con agencias de servicios.
*   **Riesgo 2**: `src/services/plan_accion_service.py` -> Podría sugerir "llamadas de descubrimiento" para un producto de compra directa en ecommerce.
*   **Riesgo 3**: `src/services/presupuesto_service.py` -> Podría omitir costes de inventario/logística.
*   **Riesgo 4**: `src/services/kpis_service.py` -> Podría medir solo "leads" y no "ROAS" o "ticket medio" de producto.

---
**Estado**: `plan_validacion_multimodelo_preparado`

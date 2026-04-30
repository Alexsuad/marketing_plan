# Auditoría de Cimientos del MVP - Sesgos de Alcance

# ──────────────────────────────────────────────────────────────────────
# Propósito: Detectar y clasificar sesgos restrictivos en el núcleo del sistema.
# Rol: Auditoría: Cimientos del MVP del sistema de Plan de Marketing

**Estado**: sesgos_de_alcance_corregidos
**Fecha**: 2026-04-30
**Responsable**: Antigravity (Experto en Marketing)

> [!IMPORTANT]
> Los sesgos de alcance detectados han sido corregidos mediante la implementación del **Sistema Multimodelo (v1.1)**. 
> Ver detalles en: [auditoria_alcance_multimodelo_mvp.md](file:///c:/Mis%20Documentos/Proyectos_Wds/marketing_plan/docs/audits/auditoria_alcance_multimodelo_mvp.md)
# ──────────────────────────────────────────────────────────────────────

## 1. Resumen Ejecutivo
Se ha realizado una auditoría exhaustiva de la documentación maestra, reglas de negocio (`AGENTS.md`), definiciones de agentes, skills y lógica de código central (`marketing_profile_resolver.py`). 

El hallazgo principal es un **sesgo estructural crítico (🔴)** hacia "empresas de servicios". El sistema, aunque diseñado para ser generalista, ha cristalizado términos restrictivos en campos obligatorios del brief y en la lógica de clasificación de perfiles, dejando fuera de alcance de forma técnica (no solo semántica) a las empresas de productos (ecommerce, retail, fabricación).

## 2. Tabla de Hallazgos

| ID | Ubicación | Hallazgo Detectado | Gravedad | Recomendación |
|:---|:---|:---|:---:|:---|
| H01 | `docs/00_..._marketing.md` | Varias menciones (L14, L24, L30, L61) limitando explícitamente el sistema a "empresas de servicios". | 🔴 | Cambiar por "negocios" o "empresas" en general. |
| H02 | `AGENTS.md` (L5, L66) | Alcance restrictivo y campos obligatorios del brief fijados como `tipo_empresa_servicios`. | 🔴 | Generalizar a `tipo_negocio` y `oferta_principal`. |
| H03 | `README.md` (L3, L27, L326) | Declaración de alcance limitada y omisión de perfiles de productos en la clasificación. | 🔴 | Incluir perfiles `b2c_producto` / `ecommerce` / `retail`. |
| H04 | `project_template/project_config.json` (L8) | Valor por defecto `"business_type": "empresa_de_servicios"`. | 🔴 | Cambiar a valor dinámico o neutro (`negocio`). |
| H05 | `src/core/marketing_profile_resolver.py` | La lógica de clasificación (L11-49) no contempla ninguna palabra clave de productos. | 🔴 | Añadir categorías para modelos basados en productos. |
| H06 | `.claude/skills/skill_intake_brief/SKILL.md` | El proceso de extracción busca campos sesgados a servicios como obligatorios. | 🔴 | Adaptar la extracción a un modelo dual Producto/Servicio. |
| H07 | `agents/estratega_marketing.md` | El flujo de trabajo asume ciclos de venta consultivos (B2B/B2C local) sin contemplar venta transaccional. | 🟡 | Incluir directrices para venta masiva o automatizada. |
| H08 | `docs/00_..._marketing.md` (L61-65) | Arrastre del caso de "logística" y "producto digital" como únicos modelos de referencia. | 🟡 | Diversificar ejemplos (ej. tienda de ropa, fábrica de muebles). |

## 3. Clasificación de Impacto

### 🟢 Aspectos Neutrales
- La **estructura de carpetas** (`context/`, `outputs/`, `system/`) es perfectamente válida para cualquier tipo de empresa.
- El **sistema de agentes** (Orquestador, Estratega, etc.) no requiere cambios de nombre, solo de directrices internas.
- Los **comandos CLI** (`create-project`, `validate-brief`) son agnósticos a nivel de ejecución.

### 🟡 Sesgos Léxicos y de Ejemplo
- Se detecta una tendencia a usar la palabra "servicio" como sinónimo de "oferta".
- Las skills de diagnóstico y canales suelen poner ejemplos B2B/Consultivos, lo que podría confundir a la IA al trabajar con un B2C de bajo ticket.

### 🔴 Sesgos Estructurales y de Bloqueo (Críticos)
- **El validador de Brief**: Si un usuario intenta modelar una "Fábrica de calzado", el sistema le pedirá un `tipo_empresa_servicios`, generando una fricción cognitiva y técnica.
- **El Perfilador (Resolver)**: Un negocio de productos caerá inevitablemente en `servicios_generales` (fallback), perdiendo la potencia de las recomendaciones específicas de canales (ej. no recomendaría Amazon o Shopify porque no existen en la lógica).

## 4. Recomendaciones de Corrección (Fase Posterior)

1.  **Generalización del Brief**:
    - Sustituir `tipo_empresa_servicios` por `tipo_negocio`.
    - Sustituir `servicio_principal` por `oferta_principal`.
    - Añadir campo opcional: `modelo_entrega` (Producto físico, Servicio, Digital).

2.  **Evolución del Resolver (`marketing_profile_resolver.py`)**:
    - Añadir perfil `b2c_producto_ecommerce`.
    - Añadir perfil `b2b_producto_industrial`.
    - Refactorizar el matching de palabras clave para evitar falsos positivos (como "bar" en "barrera").

3.  **Actualización de Documentos Rectores**:
    - Ejecutar un reemplazo masivo (con supervisión) de "empresas de servicios" por "negocios" o "empresas" en `README.md`, `AGENTS.md` y `docs/`.

4.  **Ajuste de Skills**:
    - Modificar `skill_intake_brief` para que sea capaz de detectar si el usuario habla de productos o servicios y mapear al nuevo esquema.

## 5. Lista de Archivos a Ajustar

- [ ] `README.md`
- [ ] `AGENTS.md`
- [ ] `docs/00_planificacion_mvp_sistema_plan_marketing.md`
- [ ] `docs/01_alcance_funcional_mvp.md`
- [ ] `project_template/project_config.json`
- [ ] `project_template/context/servicios.md` (Renombrar a `oferta.md`)
- [ ] `src/core/marketing_profile_resolver.py`
- [ ] `src/validators/brief_validator.py`
- [ ] `src/services/resumen_empresa_service.py`
- [ ] `.claude/skills/skill_intake_brief/SKILL.md`

## 6. Conclusión de la Auditoría
El sistema tiene unos cimientos sólidos en cuanto a **proceso y arquitectura**, pero unos cimientos **frágiles y sesgados** en cuanto a **dominio de negocio**. 

Si no se corrigen estos puntos antes de escalar, el sistema se convertirá en una herramienta de "nicho" para consultoría y servicios locales, perdiendo el potencial de ser un generador universal de planes de marketing.

**Estado Final:** `sesgos_de_alcance_mvp_identificados`

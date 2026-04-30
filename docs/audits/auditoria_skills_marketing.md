# AUDITORÍA DE SKILLS DE MARKETING — MVP v1.1
# ──────────────────────────────────────────────────────────────────────
# Propósito: Evaluar la calidad, especificidad y capacidad de auditoría de las skills actuales.
# Rol: Auditor de Marketing y Producto.
# ──────────────────────────────────────────────────────────────────────

## 1. RESUMEN EJECUTIVO
Se ha realizado una auditoría exhaustiva de las 13 skills que componen el pipeline de 12 fases del sistema agéntico. Si bien el sistema es funcional a nivel de flujo, existe un **déficit de especialización estratégica** y una **auditoría interna demasiado genérica**. El sistema corre el riesgo de generar planes coherentes gramaticalmente pero estratégicamente "tibios" o poco accionables para modelos que no sean de servicios.

---

## 2. HALLAZGOS POR CATEGORÍA

### 2.1 Sesgo Terminológico y de Alcance
- **Observación**: En skills críticas como `skill_matriz_canales` y `skill_cliente_objetivo`, se sigue utilizando el término "Servicio" como sinónimo de "Oferta" o "Modelo de Negocio".
- **Impacto**: Esto confunde a la IA cuando trata con un producto físico (Retail) o un modelo de suscripción digital (SaaS/Ecommerce), forzándola a pensar en términos de "prestación de servicios" en lugar de "venta de productos" o "logística de entrega".
- **Prioridad**: MEDIA.

### 2.2 Falta de Procedimientos Especializados (Multimodelo)
- **Observación**: El "Proceso" dentro de las skills es idéntico para todos los modelos. 
  - Ejemplo: `skill_diagnostico_marketing` no pide buscar "tasa de conversión web" para Ecommerce, ni "proceso de decisión de compra (DMU)" para B2B Industrial.
- **Impacto**: El output resultante tiende a ser genérico (FODA genérico, cliente objetivo demográfico).
- **Prioridad**: ALTA.

### 2.3 Insuficiencia en Skills de Auditoría
- **Observación**: La `skill_auditoria_coherencia` es un "catch-all" (cajón de sastre). No existen skills de auditoría especializadas en:
  - **Coherencia Financiera**: ¿El Plan de Acción (F08) es financiable con el Presupuesto (F09)?
  - **Realismo Operativo**: ¿El cliente tiene equipo para ejecutar los canales propuestos?
  - **Alineación de Canales**: ¿El canal elegido (F06) realmente sirve para llegar al segmento semilla (F03)?
- **Impacto**: El auditor actual puede aprobar planes que son técnicamente correctos pero operativamente imposibles.
- **Prioridad**: ALTA.

### 2.4 "Gaps" Funcionales (Skills Faltantes)
- **Observación**: No existe una skill de **Validación de Modelo de Negocio** al inicio que "fuerce" al sistema a adoptar el vocabulario y las métricas del perfil detectado por el resolver.
- **Impacto**: El resolver detecta que es "Ecommerce", pero las fases posteriores siguen hablando de "clientes y servicios" en lugar de "usuarios y productos".
- **Prioridad**: MEDIA.

---

## 3. AUDITORÍA DETALLADA POR SKILL CRÍTICA

| Skill | Hallazgo Crítico | Riesgo de Marketing |
| :--- | :--- | :--- |
| **skill_diagnostico** | No diferencia entre diagnóstico de marca (B2C) vs diagnóstico de capacidad técnica (B2B). | Diagnósticos superficiales. |
| **skill_cliente_objetivo** | Centrada en "problemas operativos". No contempla "deseos/aspiraciones" (B2C/Ecommerce). | Mala segmentación en consumo. |
| **skill_matriz_canales** | Proceso de selección muy simplificado (1 principal, 1 secundario). | Estrategia de canales incompleta para modelos híbridos. |
| **skill_presupuesto** | No tiene una skill de validación de "Unit Economics" (especialmente para Ecommerce). | Presupuestos desconectados de la rentabilidad real. |

---

## 4. PROPUESTA DE MEJORA (NUEVAS SKILLS Y GATES)

### A. Refuerzo de la Capa de Auditoría (Skills Especializadas)
1. **skill_auditoria_estrategica**: (NUEVA) Valida F02-F05 contra el Brief. Foco: ¿La propuesta de valor soluciona el problema inicial?
2. **skill_auditoria_operativa**: (NUEVA) Valida F06-F08. Foco: ¿Es realista ejecutar esto con los recursos declarados?
3. **skill_auditoria_financiera**: (NUEVA) Valida F09-F10. Foco: ¿Los KPIs justifican la inversión?

### B. Inyección de Inteligencia Multimodelo
- Modificar el proceso de las skills para incluir **"Bifurcaciones de Criterio"**:
  - *Si es B2B*: Investigar comité de compra (DMU).
  - *Si es Ecommerce*: Investigar funnel de conversión y recurrencia.
  - *Si es Local*: Investigar radio de influencia y visibilidad física.

---

## 5. CONCLUSIÓN DEL AUDITOR
El sistema tiene una base sólida pero necesita **"madurar estratégicamente"**. Las skills actuales actúan como generadores de texto por fase, pero no como consultores expertos. Para alcanzar un nivel profesional, las skills deben dejar de ser pasivas y empezar a **tensionar los datos** mediante procesos diferenciados por modelo de negocio.

**Estado de la Auditoría**: `skills_detectadas_como_genericas`
**Siguiente Paso Recomendado**: Refactorizar la `skill_auditoria_coherencia` en 3 skills especializadas y añadir las bifurcaciones multimodelo en los prompts de las fases 02, 03 y 06.

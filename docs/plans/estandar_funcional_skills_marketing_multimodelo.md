# File: docs/plans/estandar_funcional_skills_marketing_multimodelo.md
# ──────────────────────────────────────────────────────────────────────
# Propósito: Definir el estándar funcional para las skills de marketing
# en un entorno multimodelo para asegurar coherencia y calidad.
# Rol: Documento de arquitectura funcional y guía de implementación.
# ──────────────────────────────────────────────────────────────────────

# Estándar Funcional: Skills de Marketing Multimodelo

## 1. Propósito del estándar
Establecer las bases técnicas y estratégicas que deben cumplir todas las habilidades (skills) del sistema para garantizar que los planes de marketing generados sean coherentes, accionables y adaptados específicamente al modelo de negocio detectado.

## 2. Modelos de negocio soportados

| Modelo | Qué representa | Oferta principal | Cliente habitual | Acción principal esperada | Riesgo si se clasifica mal |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **b2b_consultivo** | Servicios especializados a empresas con ciclo de venta largo. | Consultoría, software enterprise, auditorías. | Directivos (C-Level), Gerentes de área. | Agendar reunión o demostración. | Tono demasiado informal o enfoque en venta impulsiva. |
| **b2b_producto_industrial** | Suministro de bienes tangibles para procesos productivos. | Maquinaria, componentes, materias primas. | Compradores técnicos, Jefes de planta. | Solicitud de presupuesto o cotización (RFQ). | Ignorar la importancia de la ficha técnica y la logística. |
| **ecommerce_transaccional** | Venta directa al consumidor final a través de plataforma digital. | Productos físicos (D2C), gadgets, moda. | Usuario final (B2C) digitalizado. | Compra, conversión, recompra y aumento del ticket medio. | Ignorar conversión web, ROAS, abandono de carrito, reseñas, ticket medio y recompra. |
| **retail_fisico** | Negocios con presencia física que requieren tráfico peatonal. | Ropa, hogar, alimentación en tienda. | Público de cercanía o transeúntes. | Visita física al punto de venta. | No considerar la visibilidad local y el "drive-to-store". |
| **educativo_formativo** | Venta de conocimiento y programas de capacitación. | Cursos, masters, talleres, e-learning. | Estudiantes, profesionales en activo. | Matriculación o registro en sesión informativa. | No establecer autoridad o descuidar la prueba social. |
| **hibrido_producto_servicio** | Venta de un bien físico vinculada a una recurrencia de servicio. | Equipos médicos con mantenimiento, alarmas. | Empresas o particulares con necesidades continuas. | Adquirir una solución integral con soporte, mantenimiento o SLA. | Separar artificialmente producto y soporte, perdiendo la lógica de recurrencia y confianza. |
| **b2c_local_servicios** | Servicios profesionales prestados en una zona geográfica delimitada. | Clínicas, estética, reparaciones, legal. | Usuario final local. | Reserva de cita o consulta inicial. | Usar canales de alcance nacional sin segmentación geográfica. |

## 3. Criterios mínimos para toda skill de marketing
Para garantizar la calidad técnica y estratégica, toda skill debe cumplir los siguientes criterios obligatorios:

1. **Entrada de perfil**: Exige el tipo de negocio o `marketing_profile` de forma explícita. **Evita**: Recomendaciones genéricas o desenfocadas que no aplican a la realidad operativa del cliente.
2. **Entrada de contexto**: Exige acceso a la fase anterior o al brief base validado. **Evita**: Alucinaciones sobre el modelo de negocio o falta de continuidad en la estrategia documental.
3. **Salida estandarizada**: Exige un formato de salida definido, estructurado y verificable. **Evita**: Bloques de texto amorfos que dificultan la auditoría automática y el procesamiento posterior.
4. **Trazabilidad analítica**: Exige separar claramente los hechos (datos del brief), las hipótesis (supuestos del agente) y las recomendaciones (acciones sugeridas). **Evita**: Confundir la realidad actual del negocio con las propuestas estratégicas.
5. **Adaptación multimodelo**: Exige que la lógica de recomendación cambie según el modelo detectado (ej. no recomendar SEO local a un eCommerce puramente transaccional). **Evita**: Sesgos de un modelo de negocio aplicados erróneamente a otro.
6. **Declaración de insuficiencia**: Exige la capacidad técnica de informar que no puede generar un resultado de calidad si faltan datos críticos. **Evita**: Generar planes de marketing "completos" pero basados en información insuficiente.
7. **Neutralidad terminológica**: Prohíbe el uso de lenguaje genérico ("one-size-fits-all") o excesivamente sesgado a servicios de agencia. **Evita**: Percepción de falta de expertise sectorial y propuestas que no encajan con productos físicos o industriales.
8. **Vinculación con Gates**: Exige que la salida esté conectada a un punto de control (gate) si el resultado es crítico para el avance del plan. **Evita**: El paso de información incoherente o fallida a fases estratégicas superiores.
9. **Integridad de datos**: Prohíbe inventar nombres de competidores, cifras de presupuesto, porcentajes de conversión o comportamientos de usuario no documentados. **Evita**: Pérdida total de confianza del usuario en la veracidad del plan.
10. **Coherencia histórica**: Exige alineación estricta con las restricciones y objetivos definidos en las fases previas del proyecto. **Evita**: Contradicciones internas que invaliden el plan de marketing global.

## 4. Adaptación por modelo de negocio

| Modelo | Enfoque Estratégico Principal | Canales Recomendados | KPIs Adecuados | Tono Recomendado | Qué debe evitar la skill |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **b2b_consultivo** | Autoridad, confianza y demostración de expertise. | LinkedIn, SEO de nicho, Eventos, Cold Outreach. | MQLs, SQLs, Coste por Lead, Autoridad. | Profesional, experto, analítico. | Enfoque en precio bajo o venta masiva rápida. |
| **b2b_producto_industrial** | Fiabilidad técnica, durabilidad y logística operativa. | SEO Técnico, Catálogos, Ferias, Venta Directa. | RFQs, Coste por Cotización, Homologaciones. | Técnico, preciso, institucional. | Lenguaje emocional o promesas de "viralidad". |
| **ecommerce_transaccional** | Fricción mínima, urgencia y prueba social. | Meta Ads, Google Shopping, Email Marketing. | ROAS, CR, AOV, LTV, Abandono de carrito. | Directo, persuasivo, dinámico. | Pedir "reuniones" o usar ciclos de decisión largos. |
| **retail_fisico** | Proximidad, experiencia en tienda y visibilidad local. | Google Business Profile, Local SEO, WhatsApp. | Visitas al local, Ventas POS, Tráfico local. | Cercano, amable, promocional. | Fomentar el envío nacional como eje principal. |
| **educativo_formativo** | Transformación, resultados y comunidad. | Instagram, YouTube, Webinars, Contenido. | Matrículas, CAC, Tasa de retención. | Inspirador, empático, educativo. | Marcas impersonales o falta de prueba social. |
| **hibrido_producto_servicio** | Solución integral y recurrencia de valor. | LinkedIn, Referidos, SEO de Solución. | Churn rate, LTV, Renovaciones de contrato. | Consultivo, relacional, robusto. | Tratar el soporte como un gasto y no como valor. |
| **b2c_local_servicios** | Conveniencia, reputación y disponibilidad. | Local Ads, Reseñas, WhatsApp Business. | Citas agendadas, Coste por cita, Reseñas. | De confianza, resolutivo, local. | Usar bots genéricos o ignorar la zona geográfica. |

## 5. Lenguaje permitido y lenguaje prohibido por modelo

| Modelo | Lenguaje Permitido | Lenguaje Prohibido | Ejemplo de sustitución correcta |
| :--- | :--- | :--- | :--- |
| **ecommerce_transaccional** | "Comprar producto", "Checkout", "Añadir al carrito". | "Contratar oferta", "Pedir presupuesto". | "Finalizar la compra" en lugar de "Solicitar propuesta". |
| **retail_fisico** | "Visítanos", "Ubicación", "Stock en tienda". | "Embudo de leads", "Lead Magnet". | "Aumentar visitas al local" en lugar de "Captar leads". |
| **b2b_producto_industrial** | "Cotización", "Ficha técnica", "Suministro". | "Compra impulsiva", "Oferta relámpago". | "Descargar manual técnico" en lugar de "Compra ya". |
| **educativo_formativo** | "Alumno", "Matrícula", "Programa formativo". | "Cliente" (si es ambiguo), "Usuario". | "Entrevistar al alumno" en lugar de "Vender al cliente". |

## 6. Criterios de insuficiencia
Una skill debe marcar `ESTADO_INSUFICIENTE` y detener el pipeline si:

### Criterios Generales
- Faltan campos obligatorios en el brief (ej. `nombre_negocio` o `oferta_principal`).
- El `marketing_profile` detectado no coincide con el contenido del brief.

### Criterios Específicos
- **Propuesta de valor:** No se identifica una ventaja competitiva real frente al sector.
- **Matriz de canales:** Se recomiendan canales que requieren un presupuesto >50% del disponible sin justificación.
- **Presupuesto:** No se aporta una cifra total o un rango orientativo por parte del usuario.
- **KPIs:** Las métricas sugeridas no son medibles con las herramientas declaradas en el proyecto.
- **Auditoría final:** Se detectan contradicciones entre la oferta declarada y el cliente objetivo.

## 7. Errores bloqueantes
Los siguientes errores impiden el avance automático y requieren intervención humana:
1. **Error de Clasificación:** Perfil evidente (ej. una peluquería) clasificado como `estrategia_general_prudente`.
2. **Disonancia de Lenguaje:** Uso de lenguaje de "agencia de servicios" para negocios de venta de productos físicos.
3. **Incompatibilidad de KPIs:** Sugerir "tráfico web" como KPI principal para un negocio que solo vende físicamente y no tiene web.
4. **Alucinación de Datos:** Inventar presupuestos exactos, nombres de competidores o cifras de mercado no provistas.
5. **Canales Desalineados:** Recomendar canales de alto coste (TV, Radio) para presupuestos micro o sin relación con el cliente objetivo.

## 8. Skills de auditoría recomendadas

| Skill Sugerida | Propósito | Fases que revisa | Qué puede bloquear | Gate Recomendado |
| :--- | :--- | :--- | :--- | :--- |
| **skill_auditoria_estrategica** | Validar la coherencia lógica del plan. | Diagnóstico, Propuesta. | Paso a canales. | `gate_estrategia_validada` |
| **skill_auditoria_operativa** | Asegurar que las tareas son realizables. | Plan de acción. | Finalización del plan. | `gate_accion_operativa` |
| **skill_auditoria_financiera** | Validar coherencia Presupuesto vs KPIs. | Presupuesto, KPIs. | Resumen ejecutivo. | `gate_finanzas_coherentes` |
| **skill_auditoria_multimodelo** | Verificar cumplimiento del estándar. | Todas las fases. | Cualquier fase. | `gate_estandar_cumplido` |
| **skill_auditoria_entregable** | Revisar tono, ortografía y formato final. | Documento final. | Entrega al usuario. | `gate_dossier_listo` |

## 9. Relación con gates y workflows

| Tipo de Validación | Skill Sugerida | Gate Sugerido | Workflow donde se aplica |
| :--- | :--- | :--- | :--- |
| Estructura base | `skill_intake_brief` | `gate_brief_validado` | `wf_inicio_proyecto` |
| Coherencia de perfil | `skill_auditoria_multimodelo` | `gate_perfil_correcto` | `wf_diagnostico_estrategico` |
| Viabilidad financiera | `skill_auditoria_financiera` | `gate_presupuesto_ok` | `wf_plan_financiero_kpis` |
| Calidad documental | `skill_auditoria_entregable` | `gate_calidad_final` | `wf_cierre_entregables` |

> [!NOTE]
> Los gates sugeridos en esta sección son propuestas funcionales para fases posteriores. No deben considerarse materializados hasta que exista un archivo correspondiente en `system/gates/` y un workflow que los invoque.

## 10. Estado final
Este estándar funcional queda establecido como la **fuente de verdad única** para la refactorización de las skills de marketing. Ninguna skill será considerada "Production Ready" si no supera las validaciones aquí descritas.

---
**Estado:** `fase_3_estandar_funcional_aprobado_para_cierre`
**Versión:** 1.1
**Fecha:** 2026-04-30

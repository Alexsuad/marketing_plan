# Estándar de Preguntas y Trazabilidad Multimodelo

**Versión:** 1.2 (Revisión Marketing y Privacidad)  
**Estado:** Fase 11A.2 - Aprobado con observaciones  
**Propósito:** Definir el cuestionario estratégico exhaustivo, la gestión de datos sensibles y el mapa de flujo de datos para planes de marketing realistas.

---

## 1. Preguntas Comunes y Clasificación de Datos

Los datos se clasifican según su impacto en la viabilidad técnica y estratégica del plan.

### 1.1 Niveles de Obligatoriedad
*   **Bloquea inicio**: El sistema no puede crear el proyecto ni el brief base sin estos datos.
*   **Bloquea fase**: Se puede iniciar el plan, pero el pipeline se detiene en la fase que requiere el dato.
*   **Condicional por modelo**: Obligatorio solo si se activa un perfil de negocio específico.
*   **Recomendado fuerte**: No bloquea, pero genera una alerta de "Vacío estratégico" en el output.
*   **Opcional**: Datos de refinamiento que no afectan la estructura core.

### 1.2 Preguntas Comunes
| Pregunta / Dato | Nivel | Propósito |
| :--- | :--- | :--- |
| **Nombre del Negocio** | Bloquea inicio | Identidad y branding. |
| **Tipo de Negocio** | Bloquea inicio | Clasificación para `marketing_profile`. |
| **Oferta Principal** | Bloquea inicio | Definir la propuesta de valor core. |
| **Cliente Objetivo** | Bloquea inicio | Determinar lenguaje y canales. |
| **Problema que resuelve** | Bloquea inicio | Base de la comunicación estratégica. |
| **Objetivo Principal** | Bloquea inicio | Definir el éxito (KPIs). |
| **Zona Geográfica** | Bloquea inicio | Definir alcance y segmentación. |
| **Presupuesto Mensual** | Recomendado fuerte | Viabilidad económica de las tácticas. |
| **Recursos Internos** | Recomendado fuerte | Identificar quién ejecuta las tareas. |
| **Tiempo Disponible** | Recomendado fuerte | Ajustar la carga de trabajo semanal. |
| **Capacidad Operativa** | Recomendado fuerte | Evitar el colapso por exceso de leads. |

---

## 2. Preguntas Condicionales por Modelo (Deep Intake)

### A. ecommerce_transaccional
*   **Ticket Promedio** (Bloquea fase 09): Valor medio del carrito para calcular ROAS.
*   **Plataforma** (Recomendado): (Shopify, WooCommerce, etc.).
*   **Logística** (Bloquea fase 04): Gestión de envíos como ventaja competitiva.
*   **Margen Bruto** (Condicional): Datos para límite de puja en ADS.

### B. retail_fisico
*   **Radio de Influencia** (Bloquea fase 06): Alcance de captación local.
*   **Tráfico Peatonal** (Recomendado): Dependencia de la ubicación física.
*   **Google Business Profile** (Recomendado fuerte): Visibilidad en mapas.

### C. b2b_consultivo / b2b_producto_industrial
*   **Ciclo de Venta** (Bloquea fase 08): Tiempo de maduración del lead.
*   **Decisores** (Bloquea fase 07): Mapa de roles en la compra.
*   **Homologación** (Condicional): Barreras de entrada técnicas.

---

## 3. Negocios Mixtos y Pesos (Hybrid Layer)

1.  **Peso Modelo Principal**: % de importancia en la facturación hoy.
2.  **Peso Modelo Secundario**: % de foco en el crecimiento futuro.
3.  **Compartición de Recursos**: ¿El mismo equipo/presupuesto lleva ambas líneas?
4.  **Prioridad 90 días**: Decisión obligatoria sobre qué línea se empuja primero.

---

## 4. Matriz de Trazabilidad Expandida (MTM)

| Pregunta/Dato | Modelo Aplicable | Obligatoriedad | Fase Alimenta | Decisión que permite |
| :--- | :--- | :--- | :--- | :--- |
| **Ticket Promedio** | Ecommerce (Sí) / Retail (Rec.) | Bloquea fase 09 | Fase 09 | Calcular CPA y ROAS. |
| **Ciclo de Venta** | B2B / Educativo | Bloquea fase 08 | Fase 08 | Definir hitos de seguimiento. |
| **Recursos Internos**| Todos | Recomendado fuerte | Fase 08 | Asignar responsables reales. |
| **Habilidades** | Todos | Recomendado fuerte | Fase 06 | Elegir canales autogestionables.|
| **Radio Influencia**| Retail / Local | Bloquea fase 06 | Fase 06 | Filtrar segmentación ADS. |
| **Capacidad Oper.** | B2C local / híbrido / etc. | Recomendado fuerte | Fase 10 | Definir meta de captación. |
| **Margen Bruto** | Ecommerce | Condicional | Fase 09 | Limitar inversión por venta. |

---

## 5. Reglas de Insuficiencia y Gestión de Vacíos

### 5.1 Regla de Bloqueo Automático
Se detiene el proceso si faltan campos de nivel **Bloquea inicio** o **Bloquea fase** (al llegar a dicha fase).

### 5.2 Regla de Rango Prudente (Hipótesis Operativa)
Los rangos prudentes (ej. presupuesto, ticket) son **hipótesis operativas** y no datos validados.
- Deben marcarse siempre como: **"Supuesto pendiente de confirmar"**.
- No se deben usar rangos sectoriales si no hay una fuente, dato interno o referencia explícita proporcionada por el cliente.

### 5.3 Gestión de Vacíos Estratégicos
Si falta un dato **Recomendado fuerte**, el sistema genera el documento pero añade una sección de:
> **Vacíos estratégicos pendientes de confirmar**: Lista de datos faltantes y su impacto en la precisión del plan.

---

## 6. Regla de Datos Sensibles y Privacidad

Para proteger la información estratégica del cliente, se aplican los siguientes niveles de visibilidad:

| Dato | Clasificación | Manejo en Entregable |
| :--- | :--- | :--- |
| **Margen Bruto** | Uso Interno | No mostrar porcentaje exacto; usar solo para cálculos de viabilidad. |
| **LTV / Ingresos** | Uso Interno | Mostrar solo en resúmenes de rentabilidad si es autorizado. |
| **Desempeño Pasado**| Resumido | No mostrar datos crudos de facturación; resumir como "Logros/Aprendizajes". |
| **Restricciones** | Condicional | Mostrar solo si no exponen vulnerabilidades críticas del negocio. |

---

## 7. Cómo se reflejan datos faltantes en el documento final

Todo documento generado por el sistema debe incluir una sección de **"Integridad de Datos"** al final, detallando:
1.  **Datos Confirmados usados**: Lista de información real proporcionada.
2.  **Supuestos Aplicados**: Hipótesis operativas usadas para el cálculo.
3.  **Datos Faltantes**: Qué información no se ha podido integrar.
4.  **Impacto del Vacío**: Cómo afecta la falta de ese dato a la fiabilidad del plan.
5.  **Recomendación de Validación**: Qué debe hacer el usuario para cerrar ese vacío.

---

---

## 8. Estado Final y Observaciones
`fase_11a2_estandar_preguntas_trazabilidad_aprobado_para_commit_con_observaciones`

**Nota:** Pendiente para versión posterior ampliar bancos extendidos para `educativo_formativo`, `b2c_local_servicios` y modelos híbridos complejos.

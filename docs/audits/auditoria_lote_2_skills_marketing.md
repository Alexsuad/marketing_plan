# Auditoría Lote 2 - Skills Marketing

## Estado auditado
lote_2_skills_agentica_aprobada_pendiente_auditoria_marketing

## Fuentes revisadas
- `docs/04_skills_y_uso.md`
- `docs/documento_maestro_lecciones_aprendidas_y_manual_anti_errores_final.md`
- Archivos `SKILL.md` individuales de las 13 skills en `.claude/skills/*/SKILL.md`

## Criterios de auditoría
Se ha evaluado cada skill en base a:
- calidad estratégica
- utilidad real para el plan de marketing
- claridad de entradas y salidas desde marketing
- prudencia del lenguaje
- no invención de datos
- no prometer resultados sin evidencia
- coherencia con el pipeline de 12 fases
- capacidad de producir outputs útiles
- capacidad de bloquear o marcar información insuficiente
- adaptación a diferentes perfiles de negocio
- prevención de sesgos B2B/B2C/educativo/servicios generales

---

## Revisión por skill

### 1. skill_intake_brief
- **Calidad estratégica:** Media (su función es organizativa/estructural)
- **Utilidad para el pipeline:** Alta
- **Riesgo de output genérico:** Bajo
- **Riesgo de inventar datos:** Medio (el LLM puede rellenar datos, aunque la skill lo prohíbe explícitamente)
- **Prudencia del lenguaje:** Adecuada
- **Coherencia con fase correspondiente:** Completa
- **Adaptabilidad a distintos tipos de negocio:** Alta
- **Observaciones:** Está muy bien definida la orden de bloquear/marcar si faltan campos obligatorios en lugar de inventarlos.
- **Corrección recomendada:** Ninguna.

### 2. skill_diagnostico_marketing
- **Calidad estratégica:** Alta
- **Utilidad para el pipeline:** Alta
- **Riesgo de output genérico:** Medio (riesgo de que el análisis FODA caiga en lo obvio)
- **Riesgo de inventar datos:** Bajo
- **Prudencia del lenguaje:** Adecuada
- **Coherencia con fase correspondiente:** Completa
- **Adaptabilidad a distintos tipos de negocio:** Alta
- **Observaciones:** Excelente la aclaración de "No hacer un FODA genérico sin relación con el negocio". Es vital separar hechos actuales de suposiciones.
- **Corrección recomendada:** Ninguna.

### 3. skill_cliente_objetivo
- **Calidad estratégica:** Alta
- **Utilidad para el pipeline:** Alta
- **Riesgo de output genérico:** Medio
- **Riesgo de inventar datos:** Bajo
- **Prudencia del lenguaje:** Adecuada
- **Coherencia con fase correspondiente:** Completa
- **Adaptabilidad a distintos tipos de negocio:** Alta
- **Observaciones:** Destaca positivamente la instrucción de "Definir Segmento Semilla", clave para planes realistas (MVPs).
- **Corrección recomendada:** Ninguna. 

### 4. skill_propuesta_valor
- **Calidad estratégica:** Alta
- **Utilidad para el pipeline:** Alta
- **Riesgo de output genérico:** Alto (Los LLM suelen caer en adjetivos vacíos)
- **Riesgo de inventar datos:** Bajo
- **Prudencia del lenguaje:** Adecuada
- **Coherencia con fase correspondiente:** Completa
- **Adaptabilidad a distintos tipos de negocio:** Alta
- **Observaciones:** La restricción "No redactar eslóganes publicitarios" es un gran acierto, porque enfoca la propuesta de valor en resolver el problema del cliente.
- **Corrección recomendada:** Añadir la prohibición explícita de usar superlativos o términos genéricos vacíos (ej. "somos líderes", "innovadores", "el mejor").

### 5. skill_analisis_competencia
- **Calidad estratégica:** Alta
- **Utilidad para el pipeline:** Alta
- **Riesgo de output genérico:** Medio
- **Riesgo de inventar datos:** Alto (Si el sistema no conoce competidores reales, podría "alucinar" marcas falsas)
- **Prudencia del lenguaje:** Adecuada
- **Coherencia con fase correspondiente:** Completa
- **Adaptabilidad a distintos tipos de negocio:** Alta
- **Observaciones:** Es un acierto enorme distinguir "status quo" y competidores indirectos, ya que la mayoría de pymes compite contra el "no hacer nada".
- **Corrección recomendada:** Añadir instrucción de que, ante falta de datos reales fiables, el LLM defina "arquetipos" de competidores en lugar de inventar empresas o marcas concretas.

### 6. skill_matriz_canales
- **Calidad estratégica:** Alta
- **Utilidad para el pipeline:** Alta
- **Riesgo de output genérico:** Medio
- **Riesgo de inventar datos:** Bajo
- **Prudencia del lenguaje:** Adecuada
- **Coherencia con fase correspondiente:** Completa
- **Adaptabilidad a distintos tipos de negocio:** Alta
- **Observaciones:** Muy buena prevención contra recomendar "estar en todas las redes". Priorizar 1 principal y 1 secundario es realista para empresas de servicios.
- **Corrección recomendada:** Sería útil evaluar no solo recursos financieros/tiempo, sino "habilidades/recursos internos del cliente" (ej. no sugerir YouTube si el cliente no sabe o no quiere grabar vídeos).

### 7. skill_estrategia_comunicacion
- **Calidad estratégica:** Alta
- **Utilidad para el pipeline:** Alta
- **Riesgo de output genérico:** Alto (Riesgo de proponer "pilares de contenido" desconectados de la venta)
- **Riesgo de inventar datos:** Bajo
- **Prudencia del lenguaje:** Adecuada
- **Coherencia con fase correspondiente:** Completa
- **Adaptabilidad a distintos tipos de negocio:** Alta
- **Observaciones:** Advierte bien contra la creación de contenidos desconectados de las ventas.
- **Corrección recomendada:** Obligar a que los "ejes/pilares de contenido" estén mapeados 1 a 1 contra "dolores u objeciones" documentados en la fase de cliente objetivo.

### 8. skill_plan_accion
- **Calidad estratégica:** Alta
- **Utilidad para el pipeline:** Alta
- **Riesgo de output genérico:** Medio
- **Riesgo de inventar datos:** Bajo
- **Prudencia del lenguaje:** Adecuada
- **Coherencia con fase correspondiente:** Completa
- **Adaptabilidad a distintos tipos de negocio:** Alta
- **Observaciones:** La división táctica en trimestres es perfecta y realista.
- **Corrección recomendada:** Ninguna.

### 9. skill_presupuesto_marketing
- **Calidad estratégica:** Media
- **Utilidad para el pipeline:** Alta
- **Riesgo de output genérico:** Bajo
- **Riesgo de inventar datos:** Alto (Dar costes exactos de proveedores de servicios o CPC en ads es inviable sin conocer el país)
- **Prudencia del lenguaje:** Mejorable en cuanto a la determinación de costos.
- **Coherencia con fase correspondiente:** Completa
- **Adaptabilidad a distintos tipos de negocio:** Alta
- **Observaciones:** Establece bien la priorización de dónde invertir.
- **Corrección recomendada:** Forzar que todos los costos estimados se presenten estrictamente en formato de "horquillas o rangos amplios" en lugar de valores cerrados o exactos, para evitar comprometer expectativas del negocio.

### 10. skill_kpis
- **Calidad estratégica:** Alta
- **Utilidad para el pipeline:** Alta
- **Riesgo de output genérico:** Medio
- **Riesgo de inventar datos:** Bajo
- **Prudencia del lenguaje:** Adecuada
- **Coherencia con fase correspondiente:** Completa
- **Adaptabilidad a distintos tipos de negocio:** Alta
- **Observaciones:** Excelente prevención de métricas de vanidad.
- **Corrección recomendada:** Ninguna.

### 11. skill_resumen_plan_empresa
- **Calidad estratégica:** Media (su función es ejecutiva y de compresión)
- **Utilidad para el pipeline:** Alta
- **Riesgo de output genérico:** Bajo
- **Riesgo de inventar datos:** Bajo
- **Prudencia del lenguaje:** Adecuada
- **Coherencia con fase correspondiente:** Completa
- **Adaptabilidad a distintos tipos de negocio:** Alta
- **Observaciones:** Un producto derivado muy útil para inversores o directivos.
- **Corrección recomendada:** Ninguna.

### 12. skill_auditoria_coherencia
- **Calidad estratégica:** Alta
- **Utilidad para el pipeline:** Crítica
- **Riesgo de output genérico:** Bajo
- **Riesgo de inventar datos:** Bajo
- **Prudencia del lenguaje:** Adecuada
- **Coherencia con fase correspondiente:** Completa
- **Adaptabilidad a distintos tipos de negocio:** Alta
- **Observaciones:** Componente fundamental contra el "efecto teléfono roto".
- **Corrección recomendada:** Ninguna.

### 13. skill_change_request
- **Calidad estratégica:** Alta
- **Utilidad para el pipeline:** Alta
- **Riesgo de output genérico:** Bajo
- **Riesgo de inventar datos:** Bajo
- **Prudencia del lenguaje:** Adecuada
- **Coherencia con fase correspondiente:** Completa
- **Adaptabilidad a distintos tipos de negocio:** Alta
- **Observaciones:** Soluciona un problema recurrente de consistencia documental cuando los planes cambian.
- **Corrección recomendada:** Ninguna.

---

## Revisión transversal

- **¿Cubren bien el ciclo de marketing?** Sí, cubren desde la adquisición de contexto básico hasta la verificación final, pasando por cliente, valor, distribución (canales), acción, coste y medición.
- **¿Falta alguna skill crítica?** No en el contexto del MVP. La estrategia de retención y lealtad se considera un nivel posterior de madurez; las skills actuales abordan de forma más urgente captación y establecimiento de marca, lo cual es razonable.
- **¿Invasiones de responsabilidades?** No se observan traslapos graves; el flujo es escalonado y secuencial. Las entradas y salidas de las skills están bien acopladas.
- **¿Prudencia y prevención de falsas promesas?** Existe en varias de las reglas y advertencias de las skills (ej. prohibición de eslóganes, advertencia sobre métricas de vanidad y presupuestos).
- **Adaptabilidad a sectores:** Excelente, gracias a que el sistema pre-filtra y no presupone canales ni tácticas (como se ve en la skill de canales, que evita la receta rápida de "estar en todas las redes").

---

## Hallazgos

### Críticos
Ninguno detectado. El modelo conceptual de las skills es sólido y adecuado para marketing estratégico y planificación.

### Medios
1. Riesgo de uso de jerga vacía o superlativos no probados en la `skill_propuesta_valor`.
2. Riesgo de "alucinación" de marcas inventadas en la `skill_analisis_competencia` ante falta de contexto previo.
3. Riesgo de proporcionar valores monetarios poco realistas o irresponsables en la `skill_presupuesto_marketing`.
4. Riesgo de derivar en consejos genéricos y despegados de la realidad comercial en la `skill_estrategia_comunicacion`.

### Menores
1. Falta de ponderación sobre la capacidad técnica interna del equipo/cliente antes de recomendar un canal complejo (en `skill_matriz_canales`).

---

## Correcciones recomendadas (Para fase posterior)

- **[Corregido] `skill_propuesta_valor`**: Se instruyó la prohibición de usar superlativos y jerga vacía.
- **[Corregido] `skill_analisis_competencia`**: Se añadió la instrucción de describir arquetipos de competidores si faltan datos reales.
- **[Corregido] `skill_estrategia_comunicacion`**: Se forzó el mapeo entre pilares de comunicación y dolores/objeciones.
- **[Corregido] `skill_presupuesto_marketing`**: Se exigió el uso de rangos u horquillas y no montos fijos cerrados.
- **[Corregido] `skill_matriz_canales`**: Se incluyó la evaluación de recursos y habilidades internas del cliente.

---

## Veredicto
**lote_2_skills_marketing_observaciones_corregidas**

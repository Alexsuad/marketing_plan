# DOCUMENTO MAESTRO: LECCIONES APRENDIDAS Y MANUAL ANTI-ERRORES

**Versión:** v1.0  
**Fecha:** 2026-03-13  
**Estado:** Activo  
**Última actualización:** Consolidación final del documento maestro con lecciones sobre agentes, skills, reglas, gates, prompts oficiales, memoria externa, gestión de cambios del usuario y especialidades funcionales no técnicas.

\---

## Propósito

Este documento reúne, organiza y consolida las lecciones aprendidas, los errores reales detectados y los criterios operativos que deben guiar cualquier proyecto que utilice agentes, skills, reglas, gates, workflows y, cuando aplique, memoria externa como NotebookLM.

Su función no es solo servir como memoria histórica, sino actuar como documento maestro para:

* evitar repetir errores,
* diseñar mejor futuros sistemas,
* auditar arquitecturas agentic,
* proteger trazabilidad y control,
* convertir experiencia real en reglas útiles,
* y mantener coherencia entre lo que el sistema promete y lo que realmente puede ejecutar.

La lógica general de este documento es simple:
**si el sistema ya se rompió una vez por una causa concreta, esa causa debe quedar transformada en una lección, una regla, un gate, una skill, un workflow o una verificación operativa.**

\---

## Alcance

Este documento cubre:

* diseño de agentes,
* diseño de skills,
* diseño y uso de prompts oficiales,
* reglas globales y reglas de proyecto,
* gates y control de calidad,
* desarrollo híbrido entre IA y lógica determinista,
* memoria externa y NotebookLM,
* identidad de proyecto y redacción,
* gestión de cambios del usuario,
* especialidades funcionales no técnicas,
* y errores recurrentes con su prevención.

Aplica a cualquier proyecto que utilice uno o varios de estos componentes, incluso si el dominio del proyecto cambia.

\---

## Ámbito de aplicabilidad

Este documento nace de experiencia práctica en entornos agentic como Antigravity, pero sus principios no dependen exclusivamente de esa plataforma.

Puede reutilizarse en cualquier sistema que combine:

* agentes o roles especializados,
* skills o funciones reutilizables,
* reglas y gates,
* workflows,
* memoria externa,
* prompts oficiales o maestros,
* y lógica híbrida entre IA y componentes deterministas.

Cuando el sistema se implemente como software propio, estas lecciones deben complementarse con arquitectura técnica de código, seguridad, persistencia, despliegue, observabilidad y mantenimiento.

### Distinción importante

* Si Antigravity o un entorno similar se usa como motor interno, el valor comercial suele estar en el **servicio, la implementación o el resultado**.
* Si se desea vender software propio, estas lecciones siguen siendo válidas, pero deben aterrizarse en arquitectura ejecutable y código real.

\---

# 1\. Contexto: qué se estaba construyendo y por qué falló al inicio

El objetivo general era construir un sistema capaz de llevar un proyecto desde la información inicial del usuario hasta entregables claros, verificables y útiles, usando un flujo por fases del tipo:

**Entender → Definir → Acotar → Decidir → Documentar → Validar**

En la práctica, el mayor problema inicial no fue técnico, sino estructural: el sistema deformaba la intención original del usuario a medida que avanzaba de una fase a otra.

La información entraba bien en el primer punto, pero al pasar por reinterpretaciones, resúmenes, redacciones intermedias o automatizaciones sin control, se producía un efecto de “teléfono roto”. Ese error nacía temprano y contaminaba lo que venía después.

### Lección

Si el primer documento, brief o input base nace incompleto, sesgado o ambiguo, toda la cadena posterior puede parecer coherente mientras en realidad se aleja de lo que el usuario quiso construir.

\---

# 2\. Cómo se deben crear los agentes

En un sistema con agentes, no basta con “crear roles”. Lo importante es que cada agente exista por una razón arquitectónica real.

La experiencia demostró que un sistema no mejora por tener más agentes, pero tampoco mejora por tener demasiado pocos si eso obliga a una sola entidad a absorber funciones incompatibles.

Cuando un único agente investiga, interpreta, redacta, audita y controla memoria al mismo tiempo, el sistema pierde claridad, trazabilidad y capacidad de corrección.

## 2.1 Patrón que sí funciona

La arquitectura más estable fue aquella en la que quedaron separadas, cuando el proyecto lo exigía, estas funciones:

### A. Orquestación

Coordina el flujo general. Decide qué fase sigue, qué skill se ejecuta, qué artefacto debe existir y cuándo el sistema debe detenerse.

### B. Producción o generación

Convierte contexto, payloads, datos o hallazgos en documentos, propuestas, resúmenes o entregables.

### C. Auditoría o QA

Revisa coherencia, cumplimiento de reglas, seguridad, trazabilidad y alineación. Debe poder bloquear o rechazar, no solo comentar.

### D. Especialización por capa o dominio

Entra cuando el proyecto lo requiere realmente. Por ejemplo:

* backend,
* frontend,
* datos,
* seguridad,
* negocio,
* redacción,
* memoria externa.

### Lección

Un buen sistema no mezcla capas distintas dentro del mismo rol sin necesidad.

## 2.2 Regla de diseño de agentes

No conviene ni inflar el sistema con agentes innecesarios, ni comprimir demasiadas responsabilidades en uno solo.

La decisión correcta no depende de “usar pocos agentes”, sino de **separar bien responsabilidades que generan conflicto cuando viven juntas**.

Si una función necesita criterio propio, límites claros, capacidad de veto o responsabilidad diferenciada, probablemente merece un agente o un rol separado.

Si una función es reutilizable, acotada, repetible y no requiere autonomía estratégica, normalmente debe vivir como skill y no como agente.

Cuando un mismo agente empieza a mezclar investigación, análisis estratégico, redacción, auditoría y control de memoria, el sistema pierde claridad, auditabilidad y capacidad de corrección.

### Lección

La meta no es tener pocos agentes. La meta es tener **los agentes necesarios y no menos**, apoyados por skills pequeñas, trazables y bien delimitadas.

## 2.3 Cómo decidir entre agente, skill, regla y gate

No todo problema se resuelve creando un agente nuevo.

### Un agente

Debe existir cuando hace falta un rol con responsabilidad diferenciada, criterio propio y capacidad de intervenir el flujo.

### Una skill

Debe existir cuando hay una tarea reutilizable, acotada, repetible y con entradas/salidas claras.

### Una regla

Debe existir cuando una restricción debe aplicarse de forma transversal al sistema y no depender del juicio puntual de una sola entidad.

### Un gate

Debe existir cuando hay que aprobar, bloquear o rechazar antes de permitir el avance de una fase.

### Lección

Muchos errores de arquitectura no vienen de “poca IA”, sino de asignar a una figura equivocada una responsabilidad que pertenecía a otra capa.

## 2.4 Especialidades funcionales no técnicas también pueden ser arquitectura

Una arquitectura incompleta no siempre falla por ausencia de backend, datos, seguridad o interfaz. También puede fallar porque olvidó modelar una especialidad funcional que condiciona el valor final del proyecto.

En sistemas complejos, algunas especialidades no técnicas deben tratarse como parte del diseño estructural si impactan directamente la calidad de la salida.

Por ejemplo, según el proyecto, puede ser necesario modelar desde el inicio capas como:

* marketing,
* validación comercial,
* Arquitectos de sofware
* narrativa,
* psicología,
* edición,
* auditoría editorial,
* experiencia de usuario,
* estrategia de posicionamiento,
* análisis sectorial.
* Diseñadores
* 

### Lección

La arquitectura no debe definirse solo por componentes técnicos, sino por todas las funciones que condicionan el resultado final del sistema.

### Regla práctica

Si una especialidad:

* cambia el criterio de producción,
* altera la calidad del resultado,
* obliga a revisar outputs,
* o define si el proyecto sirve o no para su objetivo real,

tonces debe representarse de forma explícita en la arquitectura.

No hace falta que siempre se convierta en un agente separado. Puede representarse como:

* agente,
* skill,
* regla,
* gate,
* workflow,
* o fase obligatoria.

Lo importante no es el nombre de la pieza, sino que esa responsabilidad no quede invisible.

## 2.5 Los prompts oficiales también forman parte de la arquitectura

En sistemas con múltiples agentes, no basta con definir “qué agente existe”. También hay que fijar **cómo piensa, qué puede hacer, qué no puede hacer, qué entradas recibe y qué salida debe producir**.

Si un agente no tiene prompt oficial o trabaja con instrucciones improvisadas:

* interpreta su rol libremente,
* invade responsabilidades ajenas,
* repite tareas,
* contradice otras piezas del sistema,
* y vuelve el proyecto mucho menos auditable.

### Lección

En proyectos con varios agentes, los prompts no son accesorios conversacionales. Son parte de la arquitectura de control del sistema.

### Regla práctica

Todo agente que tenga un rol estable dentro del sistema debe contar, como mínimo, con un prompt oficial que defina:

* rol,
* objetivo,
* límites,
* entradas,
* salidas,
* formato esperado,
* y relación con otros agentes.

### Cuándo sí hace falta crear prompts oficiales

Conviene crear prompts oficiales cuando:

* el agente se usará más de una vez,
* el agente forma parte de un workflow,
* el agente interactúa con otros agentes,
* el agente influye en decisiones, documentación o salidas sensibles,
* o el sistema necesita trazabilidad y repetibilidad.

### Cuándo no hace falta sobrediseñarlos

No hace falta crear prompts complejos para tareas puntuales, exploratorias o efímeras que no formen parte del sistema estable.

\---


## 2.6 AGENTS.md como capa de instrucción del entorno

En algunos entornos agentic puede existir un archivo como `AGENTS.md` que funcione como capa de instrucción general del repositorio o del entorno de trabajo.

Su función no es reemplazar la arquitectura del sistema, sino fijar de forma visible y centralizada el marco general de comportamiento que debe respetar la IA al operar sobre ese proyecto.

En entornos que leen `AGENTS.md` de forma nativa, este archivo no solo cumple una función documental, sino también una función operativa real. Por eso debe tratarse como una capa global del entorno, pero sin convertirlo en sustituto ni contenedor total de la arquitectura formal.

### Lección

`AGENTS.md` puede funcionar como capa operativa global del entorno cuando el sistema la soporte, pero no debe confundirse con:

* el diseño de agentes,
* los prompts oficiales de cada agente,
* las skills,
* los workflows,
* las reglas,
* ni los gates.

### Regla práctica

Si un proyecto utiliza `AGENTS.md`, debe tratarse como una capa de instrucción global que puede ayudar a definir, por ejemplo:

* prioridades generales,
* límites de comportamiento,
* reglas madre del proyecto,
* criterios de lectura inicial,
* restricciones transversales,
* o forma correcta de operar sobre el repositorio.

Pero no debe usarse como sustituto de las demás piezas arquitectónicas cuando estas siguen siendo necesarias.

### Qué sí conviene poner en `AGENTS.md`

* prioridades generales del proyecto,
* límites operativos,
* reglas madre,
* forma esperada de trabajar sobre el repositorio,
* criterio inicial de lectura,
* restricciones globales del entorno.

### Qué no conviene poner en `AGENTS.md`

* lógica detallada de una skill,
* pasos extensos de un workflow,
* auditorías específicas,
* decisiones demasiado finas por agente,
* validaciones que deban vivir en gates,
* ni instrucciones tan amplias o acumuladas que conviertan el archivo en un megaprompt desordenado.

### Jerarquía recomendada

* `AGENTS.md` = marco general del entorno o del repositorio.
* Prompt oficial de agente = definición estable de cómo piensa y opera un rol concreto.
* Skill = procedimiento reutilizable, acotado y verificable.
* Workflow = secuencia de pasos y orquestación.
* Regla = restricción transversal.
* Gate = punto de validación, bloqueo o aprobación.

### Criterio de diseño

Si una responsabilidad requiere rol, criterio, entradas, salidas y relación con otras piezas, eso sigue perteneciendo al diseño de agentes o a sus prompts oficiales.

Si una responsabilidad requiere una tarea concreta y repetible, sigue perteneciendo a una skill.

Si una restricción debe aplicarse a todo el sistema, debe vivir como regla, y no depender solo de `AGENTS.md`.

### Conclusión

`AGENTS.md` puede reforzar la coherencia operativa del sistema y, en ciertos entornos, actuar también como capa operativa real.

Pero no reemplaza la arquitectura formal.

Sirve para ordenar el marco general del entorno, no para borrar la necesidad de agentes, skills, workflows, reglas, prompts oficiales o gates cuando el sistema los necesita.

\---

# 3\. Cómo deben ser las skills y por qué

Una skill es una pieza reutilizable de comportamiento con propósito claro, fronteras definidas y resultado verificable.

No debe limitarse a “hacer algo”; debe indicar:

* qué recibe,
* qué transforma,
* qué devuelve,
* y cuándo debe detenerse o declarar insuficiencia de datos.

## 3.1 Checklist de una skill bien hecha

Una buena skill:

* hace una sola cosa, o un bloque coherente de una misma naturaleza,
* define entradas y salidas,
* aclara rutas, archivos, formatos y dependencias cuando corresponde,
* no inventa si falta información,
* declara insuficiencia cuando no hay base suficiente,
* deja trazabilidad de qué hizo,
* y, si toca una parte sensible, debe producir evidencia o estado claro.

## 3.2 Tipos de skills que conviene distinguir

### A. Skills técnicas

Se encargan de tareas concretas y repetibles:

* conectores,
* parsing,
* extracción,
* lectura,
* escritura,
* carga en memoria,
* generación de artefactos auxiliares.

### B. Skills estratégicas o cognitivas

No solo mueven datos. Interpretan, digieren, tensionan y convierten investigación o contexto en lógica útil.

Estas skills son esenciales cuando el sistema necesita separar:

* investigación,
* pensamiento,
* redacción.

### C. Skills de auditoría

Revisan salidas y detectan:

* deriva narrativa,
* faltas de evidencia,
* incoherencias,
* errores de identidad,
* contradicciones con reglas o memoria.

### D. Skills de integración o memoria

Gestionan sistemas externos como NotebookLM u otras memorias documentales. Deben tratar la memoria como una capa viva del sistema y no como repositorio pasivo.

## 3.3 Lección clave sobre skills

En proyectos de validación de negocio, estrategia o documentación compleja, las skills estratégicas no son opcionales ni decorativas.

Si no existe una capa que transforme investigación en criterio, la redacción tiende a rellenar vacíos con supuestos genéricos del LLM.

### Lección

En estos sistemas conviene separar, como mínimo:

1. investigación,
2. digestión estratégica,
3. redacción,
4. auditoría.


### 3.4 Estructura mínima recomendable de una skill

Una skill no debe tratarse como un bloque aislado de instrucciones sueltas.

Conviene entenderla como una unidad autocontenida, normalmente organizada como una carpeta cuyo núcleo obligatorio es `SKILL.md`.

Ese archivo define al menos la identidad básica de la skill y sus instrucciones de uso.

Según la necesidad, la skill puede incluir también recursos auxiliares como scripts, referencias, documentación de apoyo, plantillas o assets.

### Lección

La skill debe diseñarse como una capacidad reutilizable, auditable y portable, no como un prompt disperso sin estructura.

### Regla práctica

`SKILL.md` es el núcleo obligatorio.

Los demás recursos deben añadirse solo si ayudan realmente a ejecutar, documentar o verificar la capacidad de la skill.


## 3.5 Para más sobre skills:
https://agentskills.io/what-are-skills

\---

# 4\. Tipos de reglas: globales, del proyecto y de memoria/contexto

Una lección importante fue entender que no existe un solo tipo de regla.

## 4.1 Reglas globales

Aplican a todos los proyectos.

Ejemplos:

* idioma,
* tono general,
* política de seguridad,
* aprobación literal para impactos,
* prohibición de inventar,
* gates por fase,
* desarrollo híbrido,
* evidencia mínima,
* cierre con verificación.

Estas reglas deben ser estables y no cambiar por cada caso.

## 4.2 Reglas del proyecto

Aplican a un proyecto concreto.

Ejemplos:

* rutas reales,
* formatos,
* nombres,
* alcance,
* decisiones del usuario,
* restricciones del negocio,
* nomenclatura del repositorio o flujo específico.

Estas reglas deben vivir cerca del input del usuario o del contexto del proyecto.

## 4.3 Reglas de memoria externa y contexto vivo

Aplican cuando el sistema utiliza NotebookLM o cualquier memoria activa externa.

Estas reglas son necesarias porque la memoria externa también condiciona:

* investigación,
* inferencias,
* identidad narrativa,
* contexto sectorial,
* y outputs finales.

Aquí deben existir reglas para:

* separar memoria permanente, sectorial, rival e histórica,
* prohibir mezclas entre identidad y táctica,
* revisar validez de la memoria cuando cambia el proyecto,
* usar nomenclatura limpia,
* congelar memoria obsoleta,
* y no reutilizar cuadernos contaminados como si fueran neutros.

### Lección

Las reglas más peligrosamente ausentes no suelen ser las de estilo, sino las de identidad, contexto y memoria.

\---

# 5\. Desarrollo híbrido: IA + lógica determinista

Uno de los aprendizajes más firmes fue que no todo debe resolverse con IA.

## 5.1 Qué debe ir en lógica determinista

Todo lo que requiere exactitud, repetibilidad, control o evidencia.

Ejemplos:

* escaneo de archivos,
* parsing,
* splitting,
* rutas,
* nombres,
* filtros,
* conteos,
* hashes,
* índices,
* logs,
* mapeos,
* persistencia,
* staging,
* CRUD,
* reportes,
* automatismos de filesystem.

## 5.2 Qué puede ir en IA

Todo lo que requiere flexibilidad, formulación o ayuda interpretativa.

Ejemplos:

* explicar,
* sugerir,
* resumir,
* clasificar provisionalmente,
* proponer categorías,
* redactar borradores,
* ayudar a documentar,
* marcar dudas.

### Lección

La IA asiste, pero lo crítico no debe quedar en manos de comportamiento estadístico si necesita ser repetible.

\---


### 5.3 Skills + CLI: cuándo convienen

Una lección importante es que no toda necesidad operativa o de automatización requiere una integración compleja.

En muchos casos, una combinación de:

* skill bien definida,
* workflow claro,
* y lógica determinista o CLI,

es suficiente para resolver la necesidad de forma más simple, controlable y portable.

Esto aplica especialmente cuando el sistema:

* trabaja sobre archivos, carpetas, rutas o artefactos locales,
* necesita parsing, extracción, filtros, conteos, conversiones o validaciones,
* puede ejecutar terminal, scripts o herramientas instaladas,
* o requiere evidencia reproducible sin depender de servicios externos vivos.

### Lección

Si una necesidad puede resolverse de forma local, verificable y determinista mediante skill + CLI o scripts, no debe escalarse por defecto a una integración más compleja.

### Regla práctica

Antes de proponer una integración externa, el sistema debe preguntarse:

1. ¿Basta con una skill?
2. ¿Basta con una skill apoyada por CLI o lógica determinista?
3. ¿Hace falta realmente conexión viva con un sistema externo?

Si las dos primeras opciones cubren la necesidad, deben preferirse por simplicidad, control y portabilidad.

### Evidencia que debe exigirse

Antes de justificar una integración más pesada, debe poder explicarse:

* qué tarea concreta debe resolverse,
* por qué no basta una skill,
* por qué no basta CLI o lógica determinista,
* y qué ganancia real aporta escalar a una conexión externa formal.

### 5.4 MCP: cuándo usarlo y cuándo no

Otra lección importante es que MCP no debe tratarse como solución por defecto ni como sinónimo de integración “más avanzada”.

MCP tiene sentido cuando el proyecto realmente necesita acceso estructurado a un sistema externo vivo.

Esto incluye casos como:

* leer o escribir en servicios externos,
* ejecutar acciones sobre herramientas conectadas,
* consultar datos dinámicos fuera del entorno local,
* interactuar con memorias externas activas,
* o mantener una integración formal entre el agente y otro sistema.

### Lección

MCP debe aparecer solo cuando la necesidad real del proyecto exige acceso, acciones o memoria externa viva que no puede resolverse de forma suficiente con skill + CLI + lógica determinista local.

### Regla práctica

Conviene usar MCP cuando se cumplan una o varias de estas condiciones:

* el sistema necesita conectarse a servicios externos de forma recurrente,
* la tarea depende de datos vivos o cambiantes fuera del entorno local,
* se requiere una interfaz estructurada entre el agente y otro sistema,
* el entorno no permite resolver la tarea solo con terminal o scripts locales,
* o la integración necesita mantenerse como parte estable de la arquitectura.

No conviene usar MCP cuando:

* la tarea puede resolverse con archivos locales, scripts o terminal,
* el problema es de transformación interna y no de conexión externa,
* o se está intentando usar MCP por moda, anticipación o sobrediseño.

### Evidencia que debe exigirse

Antes de decidir MCP, debe quedar claro:

* qué sistema externo debe conectarse,
* qué acción o acceso real se necesita,
* por qué una solución local no basta,
* y qué riesgo o limitación aparecería si no existiera esa integración.

### Mas sobre MCP

https://modelcontextprotocol.io/docs/getting-started/intro

\---


# 6\. Qué estaba rompiendo el proyecto: causas reales

## 6.1 Fallo: pérdida de requisitos en cascada

### Qué pasó

El input del usuario decía una cosa, pero al pasar por reinterpretaciones o resúmenes una parte del requisito se perdía.

### Qué lo corrigió

* auditoría cruzada,
* trazabilidad entre input y outputs,
* registro explícito de cambios.

### Lección

Si no comparas input base vs outputs de fase, los requisitos se evaporan sin ruido.

\---

## 6.2 Fallo: cierre sin prueba real

### Qué pasó

El sistema podía “dar por terminado” algo que no estaba probado.

### Qué lo corrigió

* smoke test,
* evidencia mínima,
* cierre con verificación.

### Lección

Sin prueba real, el cierre es solo literario.

\---

## 6.3 Fallo: mezcla de capas

### Qué pasó

Se mezclaban infraestructura, lógica, datos, UI o auditoría en un mismo bloque.

### Qué lo corrigió

* separación por capas,
* roles especializados cuando hacía falta,
* y mejor delimitación de skills.

### Lección

La modularización no es estética. Es una condición de supervivencia y depuración.

\---

## 6.4 Fallo: outputs contaminados con el framework

### Qué pasó

El entregable al cliente o al usuario final podía quedar mezclado con carpetas, artefactos o lógica interna del sistema.

### Qué lo corrigió

Separar framework y producto final.

### Lección

Sistema interno y entrega final nunca deben confundirse.

\---

## 6.5 Fallo: bugs sin contexto ni causa

### Qué pasó

Se reportaban fallos sin explicar capa, causa o contexto.

### Qué lo corrigió

Usar RCA:

* síntoma,
* capa,
* causa probable,
* solución sugerida.

### Lección

Un bug sin contexto suele volver a aparecer.

\---

## 6.6 Fallo: la regla correcta estaba puesta demasiado tarde

### Qué pasó

Había restricciones importantes, pero solo vivían en auditoría. El sistema generaba mal, el auditor lo rechazaba y el flujo entraba en bucles.

### Qué lo corrigió

Mover esas reglas también a:

* skills estratégicas,
* redacción,
* templates,
* workflow.

### Lección

Si una regla corrige un sesgo de generación, no debe vivir solo al final.

\---

## 6.7 Fallo: la investigación pasaba demasiado rápido a redacción

### Qué pasó

La investigación cruda se convertía en prosa sin pasar por una capa clara de interpretación estratégica.

### Qué lo corrigió

Crear una capa intermedia de pensamiento mediante skills específicas.

### Lección

Investigar y redactar no son suficientes. Entre ambas fases debe existir digestión estratégica.

\---

## 6.8 Fallo: la memoria externa contaminaba el sistema

### Qué pasó

La memoria externa mezclaba identidad permanente, sector, competencia, histórico y nombres contaminados.

### Qué lo corrigió

Separar memoria en:

* permanente,
* sectorial,
* rival,
* histórica.

### Lección

La memoria externa no es una biblioteca pasiva. Es una capa viva del sistema.

\---

## 6.9 Fallo: el sistema no distinguía entre empresa, servicio y caso de entrada

### Qué pasó

El sistema confundía:

* la empresa,
* el servicio,
* el caso inicial,
* el nicho de entrada,
* o incluso un programa/incubadora.

### Qué lo corrigió

Introducir un contrato estructurado de identidad del proyecto.

### Lección

Si la identidad no está representada de forma estructurada, el LLM rellenará el vacío con marcos genéricos.

\---

## 6.10 Fallo: el naming del sistema también contaminaba

### Qué pasó

Nombres de reglas, cuadernos, workflows o archivos empujaban al sistema a interpretar mal su identidad.

### Qué lo corrigió

Purgar nombres contaminantes y rediseñar la nomenclatura.

### Lección

El naming no es decorativo. También modela el pensamiento del sistema.

\---

## 6.11 Fallo: cambios del usuario invalidaban contexto sin disparar revisión

### Qué pasó

El usuario ajustaba documentos base o redefinía elementos del proyecto, pero el sistema seguía usando memoria o outputs antiguos como si siguieran siendo válidos.

### Qué lo corrigió

Introducir una lógica de evaluación de impacto cuando cambian de forma relevante:

* identidad,
* nicho,
* cliente,
* modelo,
* problema,
* o caso de entrada.

### Lección

El cambio no es una excepción: es parte normal del proceso. El sistema debe clasificar si el impacto es nulo, parcial o invalidante.

\---

## 6.12 Fallo: la arquitectura técnica avanzó sin modelar una especialidad funcional crítica

### Qué pasó

En algunos proyectos, la estructura lógica y técnica del sistema avanzó correctamente en términos de:

* workflows,
* reglas,
* skills,
* gates,
* trazabilidad,
* y automatización.

Sin embargo, una o varias especialidades funcionales necesarias para que el resultado final tuviera valor real quedaron fuera del diseño inicial.

Esto provocó que el sistema, aunque técnicamente sólido, quedara incompleto en su propósito. El problema no era que “faltara una mejora”, sino que faltaba una capa crítica para el objetivo final del proyecto.

En la práctica, esto obligó a corregir después la arquitectura, incorporar nuevas skills, rediseñar partes del flujo y consumir tiempo y recursos que podrían haberse ahorrado si esa especialidad se hubiera modelado desde el principio.

### Qué lo corrigió

Reconocer que no todas las capas críticas de un sistema son técnicas.

Cuando el valor final del proyecto depende de una especialidad funcional concreta, esa especialidad debe reflejarse en la arquitectura desde el inicio, y no quedar relegada a una corrección tardía.

Esto puede resolverse mediante:

* agentes,
* skills,
* reglas,
* gates,
* fases del workflow,
* o validadores específicos.

### Lección

Si una especialidad afecta directamente la calidad del resultado final, no debe tratarse como complemento, ajuste posterior o “capa opcional”.

Debe modelarse desde el principio como parte del sistema.

### Regla práctica

Si al quitar una especialidad el sistema sigue funcionando técnicamente, pero deja de cumplir el objetivo real del proyecto, entonces esa especialidad no es decorativa: **es arquitectónica**.

### Ejemplos de especialidades funcionales que pueden ser arquitectónicas según el proyecto

* marketing
* validación comercial
* posicionamiento
* narrativa
* psicología del usuario o del público
* edición
* auditoría editorial
* experiencia de usuario
* análisis sectorial
* cumplimiento
* memoria externa o documental

### Evidencia que debe exigirse

Antes de declarar madura una arquitectura, debe poder responderse con claridad:

* ¿Qué especialidades funcionales condicionan el valor real del proyecto?
* ¿Dónde están representadas en el sistema?
* ¿Qué agente, skill, regla, gate o fase cubre cada una?
* ¿Cuál sería el impacto si una de ellas faltara?

Si estas preguntas no pueden responderse, la arquitectura probablemente está incompleta aunque técnicamente parezca sólida.

\---

# 7\. Qué cambió el juego: gates, evidencia y aprobación literal

## 7.1 Gates por fase

No se avanza sin output real de la fase actual.

## 7.2 Evidencia obligatoria

Toda operación crítica debe dejar rastros verificables.

## 7.3 Aprobación literal para impactos

Acciones sensibles requieren una aprobación explícita válida.

## 7.4 Los gates no solo deben bloquear errores técnicos

También deben proteger:

* identidad,
* coherencia empresarial,
* uso correcto de memoria,
* deriva narrativa,
* y validez del contexto.

### Lección

Cuanto más complejo se vuelve el sistema, más necesario es que los gates validen pensamiento y marco, no solo sintaxis o estructura.

\---

# 8\. Lección específica sobre prompts y prompts maestros

Además de agentes, skills, reglas y memoria, la experiencia mostró que los prompts también son una pieza crítica del sistema.

## 8.1 Prompts oficiales

Cuando un agente se usa de forma estable, necesita un prompt oficial que defina:

* qué es,
* qué hace,
* qué no hace,
* cómo recibe contexto,
* qué output debe producir,
* y cómo se relaciona con el resto del sistema.

### Lección

Si un agente estable trabaja con prompts improvisados, la arquitectura se vuelve frágil aunque el organigrama parezca correcto.

## 8.2 Prompts maestros

En tareas recurrentes de investigación o razonamiento, conviene fijar prompts maestros en lugar de improvisar cada llamada.

Esto aplica especialmente cuando se investiga:

* mercado,
* competencia,
* sustitutos,
* viabilidad,
* contexto sectorial,
* o validación de negocio.

### Lección

Si la investigación depende de prompts improvisados, el sistema queda demasiado expuesto al contexto accidental y a la interpretación libre del modelo.

## 8.3 Cuándo hace falta crear prompts oficiales o maestros

Conviene hacerlo cuando:

* la tarea es recurrente,
* el agente forma parte del sistema estable,
* la salida influye en decisiones o documentación,
* la consistencia entre corridas importa,
* o la trazabilidad del razonamiento es importante.

## 8.4 Cuándo no hace falta sobrediseñarlos

No hace falta crear prompts complejos para tareas únicas, efímeras o exploratorias que no forman parte de la arquitectura estable.

\---

# 9\. Caso real de prueba: validar el pipeline antes de perfeccionarlo

Una lección muy valiosa fue distinguir entre:

* probar que el sistema funciona de punta a punta,
* y perfeccionarlo.

Cuando se trabaja con miles de archivos o múltiples fuentes, es normal que aparezcan falsos positivos, ruido o materiales ambiguos.

### Lección

Primero se valida el pipeline end-to-end. Luego se afinan filtros, inteligencia fina o precisión.

Sin esta distinción, el proyecto puede atascarse intentando perfección antes de tener una base realmente operativa.

\---

# 10\. Recomendaciones prácticas para no repetir errores

## 10.1 Para cualquier proyecto nuevo

* input base completo,
* sección operativa mínima,
* preguntas específicas cuando falte algo,
* gate por fase,
* evidencia mínima,
* smoke test,
* auditoría cruzada,
* separación de capas,
* y revisión explícita de especialidades funcionales críticas.

## 10.2 Para proyectos con archivos del usuario

* staging siempre,
* no procesar todo sin filtro,
* no borrar directamente,
* separar histórico de activo.

## 10.3 Para proyectos con memoria externa

* no mezclar identidad con sector,
* separar rivalidad de memoria permanente,
* revisar validez cuando cambie el proyecto,
* congelar histórico,
* y no reciclar memoria contaminada como si fuera neutra.

## 10.4 Para proyectos con varios agentes

* no dejar agentes estables sin prompt oficial,
* no usar prompts improvisados para tareas recurrentes,
* y no asumir que la arquitectura está bien solo porque “los nombres de los roles suenan correctos”.

\---

# 11\. Qué conviene convertir en reglas globales

Estas prácticas ya demostraron suficiente valor como para institucionalizarse:

* aprobación literal para impactos,
* no inventar rutas ni estructuras,
* gates por fase,
* auditoría cruzada,
* smoke tests,
* desarrollo híbrido,
* cierre con evidencia,
* contrato de identidad del proyecto,
* reglas de modularidad de memoria externa,
* evaluación de impacto cuando cambian los documentos base del usuario,
* y obligatoriedad de prompts oficiales o prompts maestros cuando una tarea o agente forma parte del sistema estable.

\---

# 12\. Próximos pasos sugeridos para madurar el framework

* formalizar un contrato estructurado de identidad aplicable a cualquier proyecto,
* crear una política general de reevaluación de contexto,
* tratar NotebookLM y memorias externas como capas arquitectónicas vivas,
* estandarizar nomenclatura para sistema, empresa, sector, rival e histórico,
* reforzar la separación obligatoria entre investigación, pensamiento, redacción y auditoría,
* establecer una política de prompts oficiales y prompts maestros,
* y mantener las lecciones aprendidas como documento vivo.

\---

# 13\. Manual operativo anti-errores

## 13.1 Se pierde un requisito en la cascada

### Cómo se ve

El input base dice algo que ya no aparece en requisitos, alcance o outputs.

### Gate que lo detecta

Auditoría cruzada.

### Regla que lo previene

Comparar input base vs outputs y registrar Conservado / Cambiado / Descartado.

### Evidencia

Tabla comparativa o diff.

\---

## 13.2 Se avanza de fase sin entregable

### Cómo se ve

Ya se habla de implementación, pero no existe el output de la fase actual.

### Gate que lo detecta

Gate de fase.

### Regla que lo previene

No avanzar sin output en `output/` o ubicación equivalente.

### Evidencia

Lista de archivos esperados y confirmación.

\---

## 13.3 Se declara éxito sin prueba real

### Cómo se ve

Algo figura como terminado, pero falla al ejecutarse.

### Gate que lo detecta

Smoke test.

### Regla que lo previene

Sin smoke test no hay cierre.

### Evidencia

Log, captura o respuesta válida.

\---

## 13.4 Se mezclan capas

### Cómo se ve

UI, lógica, datos y auditoría se pisan.

### Gate que lo detecta

Auditoría por capas.

### Regla que lo previene

Separación mínima entre infra, datos, lógica, UI y control.

### Evidencia

Mapa de carpetas o responsabilidades.

\---

## 13.5 Se asumen rutas o formatos

### Cómo se ve

La IA usa rutas inexistentes o formatos no confirmados.

### Gate que lo detecta

Revisión operativa.

### Regla que lo previene

Si falta una ruta o formato, preguntar o declarar pendiente.

### Evidencia

Input base con sección operativa y validación del usuario.

\---

## 13.6 Se procesan datos reales sin staging

### Cómo se ve

El sistema escribe o modifica directamente el origen.

### Gate que lo detecta

Verificación de rutas.

### Regla que lo previene

Copiar primero, procesar después.

### Evidencia

Reporte origen → staging → destino.

\---

## 13.7 Entra basura al pipeline

### Cómo se ve

Se procesan documentos irrelevantes como si fueran inputs principales.

### Gate que lo detecta

Revisión de muestra y conteo.

### Regla que lo previene

Filtrar antes de procesar todo.

### Evidencia

Reporte de carpetas y muestra de archivos.

\---

## 13.8 Hay colisiones de nombres

### Cómo se ve

Archivos se sobrescriben o pierden trazabilidad.

### Gate que lo detecta

Conteo de colisiones.

### Regla que lo previene

Nunca sobrescribir sin registrar mapping.

### Evidencia

Log de colisiones.

\---

## 13.9 Falta evidencia

### Cómo se ve

Se dice “se hizo”, pero no existe rastro verificable.

### Gate que lo detecta

Checklist de cierre.

### Regla que lo previene

Toda fase crítica deja evidencia mínima.

### Evidencia

Logs, rutas, reportes, conteos.

\---

## 13.10 Se reportan bugs inútiles

### Cómo se ve

No se sabe qué falló ni por qué.

### Gate que lo detecta

Plantilla RCA.

### Regla que lo previene

Sin RCA no se acepta bug report.

### Evidencia

Síntoma, capa, causa, solución sugerida.

\---

## 13.11 Se toman decisiones críticas sin registro

### Cómo se ve

Luego nadie recuerda por qué se cambió algo importante.

### Gate que lo detecta

Guardrail de decisiones críticas.

### Regla que lo previene

Impacto alto → ADR + aprobación explícita.

### Evidencia

ADR o equivalente.

\---

## 13.12 El entregable final queda contaminado con el framework

### Cómo se ve

El cliente recibe estructura interna o basura técnica.

### Gate que lo detecta

Auditoría de entrega.

### Regla que lo previene

Separar framework y salida final.

### Evidencia

Checklist de entrega limpia.

\---

## 13.13 La IA decide cosas que debían ser deterministas

### Cómo se ve

Resultados variables o alucinaciones en lógica crítica.

### Gate que lo detecta

Repetibilidad.

### Regla que lo previene

Core crítico en lógica determinista.

### Evidencia

Scripts, hashes, outputs repetibles.

\---

## 13.14 Se usa una aprobación ambigua

### Cómo se ve

Una frase vaga dispara una acción sensible.

### Gate que lo detecta

Verificación de frase de aprobación.

### Regla que lo previene

Solo aceptar fórmulas explícitas válidas.

### Evidencia

Texto exacto aprobado.

\---

## 13.15 Se intenta perfeccionar antes de validar el pipeline

### Cómo se ve

El proyecto se atasca afinando demasiado pronto.

### Gate que lo detecta

Objetivo de fase.

### Regla que lo previene

Primero validar end-to-end, luego mejorar.

### Evidencia

Checklist MVP + backlog.

\---

## 13.16 La IA redacta con la identidad equivocada del proyecto

### Cómo se ve

Presenta como empresa algo que es incubadora, táctica, cuaderno o caso inicial.

### Gate que lo detecta

Gate de identidad o auditoría semántica.

### Regla que lo previene

Todo flujo de redacción debe consumir un contrato explícito de identidad del proyecto.

### Evidencia

Documento rector + salida que distingue empresa, servicio y caso de entrada.

\---

## 13.17 La memoria externa está contaminada

### Cómo se ve

La investigación o redacción arrastran sectores viejos, nombres incorrectos o lógica obsoleta.

### Gate que lo detecta

Auditoría de memoria.

### Regla que lo previene

Separar memoria permanente, sectorial, rival e histórica.

### Evidencia

Inventario de cuadernos o repositorios activos.

\---

## 13.18 El usuario cambió el proyecto y el sistema siguió usando contexto viejo

### Cómo se ve

Se modifican documentos base, pero el sistema reutiliza memoria o outputs ya inválidos.

### Gate que lo detecta

Evaluación de impacto sobre memoria y entregables.

### Regla que lo previene

Clasificar el cambio como sin impacto, parcial o invalidante antes de seguir.

### Evidencia

Comparación de versiones + decisión registrada.

\---

## 13.19 Una regla cognitiva vive solo en auditoría

### Cómo se ve

El sistema genera mal, el auditor rechaza y se producen bucles.

### Gate que lo detecta

Rechazos repetidos por la misma causa semántica.

### Regla que lo previene

Toda regla que corrige un sesgo de generación debe estar también en skills, templates o workflow.

### Evidencia

La misma restricción aparece en producción y en auditoría.

\---

## 13.20 Naming contaminante

### Cómo se ve

El sistema interpreta mal su identidad por nombres de archivos, reglas, cuadernos o workflows.

### Gate que lo detecta

Auditoría de nomenclatura.

### Regla que lo previene

Separar claramente nombres de sistema, proyecto, memoria activa, histórico y contexto externo.

### Evidencia

Mapa de naming activo.

\---

## 13.21 Investigación, pensamiento y redacción están mezclados

### Cómo se ve

La investigación cruda se convierte en entregable sin interpretación intermedia.

### Gate que lo detecta

Auditoría de workflow y trazabilidad.

### Regla que lo previene

Separar investigación, digestión estratégica, redacción y auditoría.

### Evidencia

Payloads intermedios o skills cognitivas antes de la redacción.

\---

## 13.22 El sistema depende de prompts improvisados

### Cómo se ve

Agentes o herramientas externas producen outputs inconsistentes porque cada ejecución depende de instrucciones diferentes, parciales o cambiantes.

### Gate que lo detecta

Auditoría de uso de agente o de memoria externa.

### Regla que lo previene

Si una tarea es recurrente, crítica o estructural, debe tener prompt oficial o prompt maestro estable.

### Evidencia

Repositorio o carpeta con prompts oficiales versionados, o referencia explícita al prompt maestro activo.

\---

# 14\. Criterio final de uso de este documento

Este documento debe usarse como:

* memoria viva,
* referencia para diseñar agentes, skills, reglas, prompts y gates,
* base para auditorías,
* checklist de prevención,
* y guía para detectar cuándo el sistema sigue funcionando técnicamente pero ya no está pensando desde el marco correcto.

Si una nueva decisión contradice una lección ya aprendida aquí, esa decisión debe revisarse antes de avanzar.

\---

# 15\. Regla práctica de mantenimiento

Cada vez que aparezca un fallo nuevo que se repita o revele una debilidad estructural, debe añadirse aquí indicando:

* qué pasó,
* cómo se veía,
* qué lo detectó,
* qué lo corrigió,
* qué regla conviene fijar,
* y qué evidencia debe exigirse la próxima vez.

Si el fallo afectó identidad, memoria externa, redacción estratégica, prompts oficiales o validez del contexto, debe registrarse además:

* si el problema era local o sistémico,
* qué capa quedó contaminada,
* y si la corrección fue de salida o de raíz.

Así este documento deja de ser solo histórico y se convierte en una herramienta activa de control, aprendizaje y evolución del sistema.



\---


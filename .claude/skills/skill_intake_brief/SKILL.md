---
name: skill_intake_brief
description: Extraer, organizar y clasificar la información estratégica, geográfica y operativa necesaria para iniciar un Plan de Marketing multimodelo (v1.2).
---

# skill_intake_brief

## Estado
activa_documental

## Objetivo
Extraer, organizar y clasificar la información estratégica a partir de texto libre o entrevista, asegurando la captura de la zona geográfica y la capacidad operativa para evitar recomendaciones genéricas.

## Cuándo usarla
Al inicio de un nuevo proyecto, cuando el usuario proporciona la descripción inicial del negocio o briefing.

## Agente activador
`orquestador_plan_marketing`

## Entradas necesarias
- Texto libre proporcionado por el usuario, transcripción de entrevista o documento inicial del negocio.

## Proceso de Extracción Jerárquica

### 1. Campos que Bloquean Inicio (Core)
Extraer y validar que no sean vagos:
- `nombre_negocio`: Identidad comercial.
- `tipo_negocio`: Clasificar según los 7 modelos (ecommerce, b2b_consultivo, b2b_industrial, retail, educativo, local_servicios, hibrido).
- `oferta_principal`: Qué se vende (producto, formación, solución).
- `cliente_objetivo`: Quién compra.
- `problema_que_resuelve`: Por qué compran.
- `objetivo_principal`: Qué se busca lograr.
- `zona_geografica`: Alcance físico o digital de la operación.

### 2. Campos Recomendados Fuertes (Viabilidad)
Si faltan, marcar como "[Recomendado]" (el sistema usará supuestos):
- `presupuesto_marketing`, `recursos_internos`, `tiempo_disponible`, `capacidad_operativa`, `canales_actuales`, `restricciones`.

### 3. Campos Opcionales (Refinamiento)
- `competidores_conocidos`, `activos_existentes`, `herramientas_medicion`, `desempeno_pasado`.

### 4. Campos Condicionales por Modelo
Identificar datos específicos según el `tipo_negocio` detectado:
- **Ecommerce**: `ticket_promedio`, `logistica`, `margen_bruto`.
- **B2B**: `ciclo_venta`, `decisores_compra`, `homologacion`.
- **Retail/Local**: `radio_influencia`, `google_business_profile`, `sistema_reservas`.
- **Educativo**: `modalidad_formativa`, `modelo_recurrencia`.

## Reglas de Oro
- **No Inventar**: Si un dato no está en la entrada, usar el marcador correspondiente (`[Completar]`, `[Recomendado]`, `[Opcional]` o `[Condicional]`).
- **Terminología**: Usar "oferta" como término universal. Evitar "servicio" salvo que el negocio sea puramente de servicios.
- **Validación de Especificidad**: Rechazar descripciones genéricas (ej. "somos profesionales").

## Cuándo declarar insuficiencia
Debe declarar insuficiencia (Bloqueo Hard) si:
- Falta cualquier campo del grupo **1. Bloquean Inicio** (incluyendo `zona_geografica`).
- La descripción de la **oferta** o el **cliente** es tan vaga que impide clasificar el modelo de negocio.
- El usuario proporciona información contradictoria que impide la trazabilidad.

## Salida esperada
`projects/nombre_proyecto/context/brief_negocio.md` siguiendo estrictamente la estructura de la plantilla base.

## Gates relacionados
`gate_brief_minimo`

## Errores frecuentes
- Aceptar "Nacional" o "Global" en `zona_geografica` sin validar si el negocio tiene capacidad operativa para ello.
- No identificar el `tipo_negocio` correcto, lo que arrastra errores en la elección de canales.

## Límites
No debe proponer estrategias; su única función es estructurar los datos de entrada con rigor consultivo.

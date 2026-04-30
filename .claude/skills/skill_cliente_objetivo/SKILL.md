---
name: skill_cliente_objetivo
description: Pasar de un "cliente objetivo" genérico a un perfil claro, accionable y dividido en segmentos operativos.
---

# skill_cliente_objetivo

## Estado
activa_documental

## Objetivo
Pasar de un "cliente objetivo" genérico a un perfil claro, accionable y dividido en segmentos operativos basados en necesidades, comportamientos y señales de compra reales, identificando por dónde empezar la validación.

## Cuándo usarla
Usar después del diagnóstico, antes de definir canales y mensajes, o cuando el cliente objetivo definido sea demasiado amplio para realizar una prospección efectiva.

## Agente activador
`estratega_marketing` (apoyado por `investigador_marketing`)

## Entradas necesarias
- `brief_negocio.md` (campos: `cliente_objetivo`, `problema_que_resuelve`, tipo de empresa y servicio principal).
- `02_diagnostico_marketing.md`

## Proceso
1. **Identificar Necesidades**: ¿Qué mueve realmente a este cliente a buscar la solución hoy?
2. **Dividir por Perfil**: Separar el público genérico en 2-3 grupos con características operativas distintas.
3. **Evaluar Accesibilidad**: ¿Cómo de fácil es encontrar a este segmento hoy mismo?
4. **Definir Segmento Semilla (Seed)**: Elegir el grupo más pequeño y accesible para iniciar la validación (ej. de 30 días).
5. Listar los problemas operativos diarios que sufre el cliente.
6. Identificar quién toma la decisión de compra vs. quién es el usuario.

## Salida esperada
`outputs/plan_actual/03_cliente_objetivo_y_segmentos.md`

## Gates relacionados
`gate_coherencia_cliente_propuesta`

## Criterios de insuficiencia
La skill es insuficiente si el resultado es "Cualquier empresa que necesite X". Los segmentos deben derivar directamente de los datos del brief. Se deben plantear hipótesis claras. El lenguaje debe ser prudente (ej. "Segmento potencial" en lugar de "Mercado cautivo"). Debe existir conexión lógica entre el problema, el cliente, su operativa y su proceso de compra.

## Errores frecuentes
- Segmentar solo por datos demográficos irrelevantes.
- Proponer un segmento inaccesible o inabarcable sin presupuesto millonario.

## Límites
No debe proponer canales de comunicación todavía, se enfoca únicamente en entender quién es el cliente.

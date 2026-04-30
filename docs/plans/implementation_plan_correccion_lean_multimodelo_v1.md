# Plan de Implementación: Corrección Lean Multimodelo v1.1

```
Propósito : Corregir fallos estructurales y estratégicos antes de aprobar v1.1.
Rol       : Plan Maestro de Auditoría y Refactor Funcional.
Estado    : PLANIFICACIÓN — no tocar código ni archivos operativos todavía.
Fecha     : 2026-04-30
```

---

## 0. Resumen ejecutivo

El sistema está estructuralmente avanzado pero tiene cuatro categorías de fallos
confirmados que impiden aprobar v1.1:

| # | Categoría | Severidad | Evidencia |
|---|-----------|-----------|-----------|
| 1 | Repositorio sucio | Media | ZIP, `projects/`, `docs/archive/` presentes; `.claude/` ignorado por completo |
| 2 | Resolver falla con ecommerce real | Alta | Brief de Artesanía Sónica → `estrategia_general_prudente` (1 match, umbral 2) |
| 3 | Terminología no se aplica en outputs | Media | `canales_service.py` nunca usa `profile['terminology']` |
| 4 | Skills tienen sesgo de servicios | Media | `skill_propuesta_valor`, `skill_matriz_canales`, et al. dicen "servicio" siempre |

---

## 1. Estado confirmado del repositorio

### 1.1 Archivos y carpetas sucias presentes

```
marketing_plan/
├── marketing_plan_base_v1.0.zip   ← comprometido en el commit inicial; .gitignore no es retroactivo
├── projects/                       ← 10 proyectos activos; ignorado en git pero presente localmente
├── docs/archive/                   ← 2 historiales de cierre; debería no distribuirse en ZIP
└── skills/                         ← solo README.md; confunde con .claude/skills/
```

### 1.2 .gitignore — problema con .claude/skills/

Línea 17 del `.gitignore` actual:
```
.claude/
```
Consecuencia: toda la carpeta `.claude/skills/` (13 skills estructurales) queda
fuera del control de versiones. Las skills son parte del sistema, no metadata local.

Corrección necesaria:
```
.claude/
!.claude/skills/
!.claude/skills/**
```

### 1.3 skills/ raíz — ambigüedad estructural

`skills/README.md` describe un sistema de skills de marketing que "se estandarizan".
Pero las skills operativas viven en `.claude/skills/`. Esta carpeta raíz no tiene
subdirectorios, solo un README que puede confundir a cualquier colaborador o al
propio sistema agéntico.

Decisión a tomar (ver Fase 2): eliminar `skills/` o convertirla en documentación
explícita de las skills de `.claude/skills/`.

### 1.4 Sesgo de servicios en skills — evidencia concreta

`skill_propuesta_valor/SKILL.md`, líneas 2 y 12:
```
description: Construir el mensaje central que explique por qué el cliente
             debería elegir este **servicio**.
Objetivo: Construir el mensaje central que explique por qué el cliente
          debería elegir este **servicio**.
```
Y el proceso (línea 26):
```
1. Relacionar el **servicio principal** con el problema prioritario del cliente.
```

Para un ecommerce, la oferta es un producto, no un servicio. El sesgo
es léxico y condiciona todos los outputs generados con esa skill.

---

## 2. Diagnóstico técnico del resolver (Fase 4 — evidencia)

### 2.1 Brief real de audit_b2c_ecommerce

```
tipo_negocio    : Ecommerce D2C (Direct to Consumer)
oferta_principal: Auriculares premium de madera hechos a mano con tecnología
                  de alta fidelidad.
cliente_objetivo: Audiófilos, amantes del diseño natural y profesionales del
                  sonido que buscan exclusividad y calidez sonora.
problema_que_resuelve: La frialdad estética y falta de personalidad de los
                        dispositivos electrónicos producidos en masa.
```

### 2.2 Análisis de scoring contra PROFILE_KEYWORDS

Texto analizado (concatenado, lower):
`"ecommerce d2c (direct to consumer) auriculares premium de madera hechos a mano con tecnología de alta fidelidad. audiófilos, amantes del diseño natural y profesionales del sonido que buscan exclusividad y calidez sonora. la frialdad estética y falta de personalidad de los dispositivos electrónicos producidos en masa."`

| Perfil | Matches confirmados | Score |
|--------|--------------------|----|
| `ecommerce_transaccional` | "ecommerce" | 1 |
| `b2b_consultivo` | "tecnología" | 1 |
| `b2c_local_servicios` | "estética" (en "frialdad estética") | 1 |
| Todos los demás | 0 | 0 |

Umbral mínimo `MIN_MATCHES = 2`. Ningún perfil supera el umbral.

**Resultado real**: `estrategia_general_prudente` (fallback).

### 2.3 Causa raíz

`PROFILE_KEYWORDS["ecommerce_transaccional"]` cubre términos transaccionales
("carrito", "checkout", "ticket medio", "roas") pero no cubre el campo semántico
de negocios D2C premium que describirse desde la **exclusividad del producto**
y no desde la mecánica de la tienda.

Palabras ausentes en la lista:
- `"d2c"`, `"direct to consumer"`, `"direct-to-consumer"`
- `"venta online"`, `"compra online"` (esta última sí está en `b2c_producto_ecommerce`)
- `"dispositivo"`, `"auriculares"` no son categorías de keywords
- La descripción "ecommerce D2C" debería ser clasificable con score 1 si reducimos
  el umbral contextualmente, o añadimos keywords semánticas.

### 2.4 Tests sintéticos actuales vs. caso real

El test `test_resolve_b2c_producto_ecommerce` usa "Zapatillas deportivas" que SÍ
están en el listado de keywords (línea 16 del resolver: `"zapatillas"`). Pasa.

El test `test_ecommerce_classification` usa "Zapatillas deportivas con envío a
domicilio" + "compra web" en `problema_que_resuelve`. Pasa por 3 matches:
"calzado" (implícito tipo negocio "calzado"), "zapatillas", "envíos".

Ningún test cubre el brief real de Artesanía Sónica. El sistema parece funcionar
pero falla con casos reales no sintéticos.

---

## 3. Diagnóstico de terminología no aplicada (INC-003)

`src/services/canales_service.py` extrae `profile['terminology']` del resolver
(**no lo hace**). El perfil sí tiene el diccionario:

```python
# marketing_profile_resolver.py — PROFILES["ecommerce_transaccional"]
"terminology": {
    "accion_principal": "comprar ahora",
    "cliente": "usuario",
    "oferta": "producto ecommerce"
}
```

Pero en `canales_service.py` ninguna línea usa `profile['terminology']`. El output
generado incluye frases como:

- Línea 75: `"Nivel de confianza: Requerido para **contratar** la oferta."` — lenguaje de servicios
- Línea 79: `"Basado en la naturaleza del **servicio**..."` — siempre "servicio"
- Línea 131: `"Dada la naturaleza de la oferta..."` — neutro, pero no usa terminología de perfil

Para un ecommerce, debería decir "comprar ahora", "usuario", "producto", no "contratar".

---

## 4. Fases del plan

### Fase 1 — Auditoría Lean del repositorio

**Alcance**: solo leer, documentar, registrar. No modificar nada.

**Acciones**:
1. Confirmar qué archivos/carpetas están siendo rastreados por git:
   ```bash
   git ls-files --cached | head -60
   ```
2. Confirmar si `marketing_plan_base_v1.0.zip` está en el índice git:
   ```bash
   git ls-files --cached | grep ".zip"
   ```
3. Listar contenido de `docs/archive/` y `projects/` para evaluar su riesgo de
   distribución.
4. Revisar si `.claude/skills/` tiene algún archivo rastreado:
   ```bash
   git ls-files --cached | grep ".claude"
   ```
5. Leer README.md y AGENTS.md para detectar lenguaje desactualizado.
6. Documentar todos los hallazgos en `docs/audits/auditoria_lote_5_rules.md`
   (archivo ya existe — actualizar sección o añadir apéndice).

**Entregable**: informe de hallazgos confirmados (en traza o apéndice de auditoría).

**Gate**: ninguno — es auditoría pura.

---

### Fase 2 — Limpieza Lean

**Alcance**: solo `.gitignore`, `skills/` raíz, `README.md`, `AGENTS.md`.
No tocar `src/`, `tests/`, `.claude/skills/`.

**Acciones**:

2.1 **Corregir `.gitignore`** — problema crítico (`.claude/skills/` invisible al git):
```diff
- .claude/
+ .claude/
+ !.claude/skills/
+ !.claude/skills/**
```
Adicionalmente, verificar si `marketing_plan_base_v1.0.zip` está siendo rastreado.
Si está rastreado (committed), eliminarlo del índice:
```bash
git rm --cached marketing_plan_base_v1.0.zip
```
Si NO está rastreado, ya lo cubre la regla `*.zip`.

2.2 **Decidir destino de `skills/` raíz** — dos opciones:
- **Opción A (recomendada)**: eliminar `skills/` y añadir nota en `README.md`
  apuntando a `.claude/skills/` como ubicación real de las skills.
- **Opción B**: convertir `skills/README.md` en un índice explícito de las 13 skills
  de `.claude/skills/` con descripción breve de cada una.
La decisión debe confirmarse antes de ejecutar.

2.3 **Actualizar `README.md`** — reflejar:
- Soporte multimodelo real (no solo "servicios")
- Que `.claude/skills/` es la ubicación operativa de las skills
- Que `projects/` no se distribuye (solo `project_template/`)
- Eliminar cualquier referencia a "v1.0" como versión estable

2.4 **Actualizar `AGENTS.md`** — reflejar:
- Los 7 modelos de negocio soportados (`b2b_consultivo`, `b2b_producto_industrial`,
  `ecommerce_transaccional`, `retail_fisico`, `educativo_formativo`,
  `hibrido_producto_servicio`, `b2c_local_servicios`)
- Regla explícita: las skills en `.claude/skills/` son parte del sistema base
- Eliminar o aclarar si `skills/` raíz sigue existiendo

2.5 **Registrar limpieza** en hito nuevo o apéndice de `docs/hitos/`.

**Gate**: `git status` limpio + `git ls-files .claude/skills/` muestra los 13 SKILL.md.

---

### Fase 3 — Estándar funcional de skills marketing multimodelo

**Alcance**: crear un documento normativo nuevo. No modificar skills todavía.

**Entregable**: `docs/plans/estandar_funcional_skills_marketing_multimodelo.md`

**Contenido del estándar**:

3.1 **Bifurcación por modelo de negocio** — para cada uno de los 7 modelos:

| Modelo | `tipo_empresa` correcto | `accion_principal` | `oferta` correcta | `cliente` correcto |
|--------|------------------------|--------------------|-------------------|--------------------|
| `b2b_consultivo` | empresa consultora | contratar | servicio consultivo | empresa/decisor |
| `b2b_producto_industrial` | fabricante/distribuidor | homologar | suministro industrial | depto. compras |
| `ecommerce_transaccional` | tienda online D2C | comprar ahora | producto ecommerce | usuario/comprador |
| `retail_fisico` | comercio local | visitar | producto de tienda | cliente local |
| `educativo_formativo` | academia/formación | inscribirse | formación/curso | alumno/padre |
| `hibrido_producto_servicio` | fabricante con soporte | adquirir con soporte | solución integral | socio/cliente |
| `b2c_local_servicios` | servicio de proximidad | reservar | servicio | vecino/cliente |

3.2 **Lenguaje prohibido por modelo**:
- `ecommerce_transaccional`: prohibido usar "contratar", "servicio principal", "sesión"
- `b2b_consultivo`: prohibido usar "comprar ahora", "ticket", "carrito"
- `educativo_formativo`: prohibido usar "cliente" sin especificar (alumno/padre/empresa)

3.3 **Criterios de insuficiencia per skill**:
- `skill_propuesta_valor`: insuficiente si usa "servicio" para un modelo de producto
- `skill_matriz_canales`: insuficiente si recomienda LinkedIn para retail local o ecommerce B2C
- `skill_kpis`: insuficiente si propone CPL para ecommerce en vez de ROAS/CPA

3.4 **Errores bloqueantes** (que invalidan el output):
- Perfil resuelto como `estrategia_general_prudente` para un brief con modelo evidente
- Uso de terminología de servicios en outputs de ecommerce o retail
- KPIs sin unidad o sin benchmark de referencia sectorial

3.5 **Propuesta de nuevas skills de auditoría** (para aprobación posterior):
- `skill_auditoria_terminologia`: verificar que los outputs usan el léxico correcto por modelo
- `skill_auditoria_perfil_resolver`: verificar que el perfil resuelto es coherente con el brief
- `skill_validacion_kpis_modelo`: verificar que los KPIs propuestos son propios del modelo

---

### Fase 4 — Corrección ecommerce real

**Alcance**: `src/core/marketing_profile_resolver.py`, `tests/test_marketing_profile_resolver.py`.

**Acciones**:

4.1 **Añadir test con brief real de Artesanía Sónica** en `tests/`:

```python
def test_resolve_artesania_sonica_ecommerce():
    """Brief real de audit_b2c_ecommerce — debe clasificar como ecommerce_transaccional."""
    brief_data = {
        "tipo_negocio": "Ecommerce D2C (Direct to Consumer)",
        "oferta_principal": "Auriculares premium de madera hechos a mano con tecnología de alta fidelidad.",
        "cliente_objetivo": "Audiófilos, amantes del diseño natural y profesionales del sonido.",
        "problema_que_resuelve": "La frialdad estética y falta de personalidad de los dispositivos electrónicos producidos en masa."
    }
    result = resolve_marketing_profile(brief_data)
    assert result["marketing_profile"] == "ecommerce_transaccional", (
        f"Esperado ecommerce_transaccional, obtenido: {result['marketing_profile']}"
    )
```

Ejecutar primero para confirmar que falla (estado actual).

4.2 **Ampliar `PROFILE_KEYWORDS["ecommerce_transaccional"]`** con términos D2C:
```python
"d2c", "direct to consumer", "direct-to-consumer",
"venta online", "compra online", "tienda propia",
"exclusividad", "producto artesanal", "hecho a mano",
"envío", "envio",  # variantes sin tilde
```

Opción alternativa o complementaria: **ajustar lógica del resolver** para que un
score de 1 en un keyword de alta señal (como "ecommerce") sea suficiente
sin requerir el umbral de 2 — gestionado con una lista de "super-keywords":

```python
SUPER_KEYWORDS = {
    "ecommerce_transaccional": ["ecommerce", "tienda online", "d2c"],
    "b2b_consultivo": ["erp", "crm", "saas"],
    ...
}
# Si alguna super-keyword del perfil aparece, forzar ese perfil sin umbral mínimo
```

4.3 **Regenerar fases 06-12 de `audit_b2c_ecommerce`** — solo después de que el test
del paso 4.1 pase correctamente.

4.4 **Verificar ausencia de `estrategia_general_prudente`** en todos los outputs
de `audit_b2c_ecommerce/outputs/plan_actual/`.

**Gate**: `uv run pytest tests/ -v` — todos los tests pasan, incluyendo el nuevo.

---

### Fase 5 — Terminología comercial aplicada

**Alcance mínimo**: `src/services/canales_service.py`. Extender solo con evidencia de contaminación.

**Acciones**:

5.1 **Extraer `terminology` del perfil en `canales_service.py`**:

```python
# Después de: profile = resolve_marketing_profile(brief_data)
terminology = profile.get("terminology", {})
accion_principal = terminology.get("accion_principal", "contratar")
tipo_cliente = terminology.get("cliente", "cliente")
tipo_oferta = terminology.get("oferta", "oferta")
```

5.2 **Sustituir strings hardcodeados** con variables de terminología:

| Línea actual | Texto actual | Texto corregido |
|-------------|-------------|----------------|
| 75 | `"Requerido para contratar la oferta."` | `f"Requerido para {accion_principal}."` |
| 79 | `"naturaleza del servicio"` | `f"naturaleza de la oferta ({tipo_oferta})"` |
| 131 | `"la naturaleza de la oferta '{oferta_principal}' y el perfil del cliente '{cliente_objetivo}'"` | conservar, pero añadir perfil semántico |

5.3 **Auditar servicios restantes** — revisar si hay contaminación en:
- `propuesta_valor_service.py` — probablemente "servicio" hardcodeado
- `comunicacion_service.py` — verificar
- `plan_accion_service.py` — verificar
Solo corregir si se confirma contaminación real con texto hardcodeado.

**Gate**: regenerar salida de Fase 06 para Artesanía Sónica y verificar que aparece
"comprar ahora" / "usuario" / "producto ecommerce" en lugar de "contratar" / "servicio".

---

### Fase 6 — Refactor funcional de skills

**Alcance**: `.claude/skills/` (13 SKILL.md). No crear nuevas skills hasta aprobación.

**Acciones**:

6.1 **Eliminar sesgo de servicios** — skills a revisar prioritariamente:

| Skill | Texto sesgado actual | Corrección propuesta |
|-------|---------------------|---------------------|
| `skill_propuesta_valor` | "elegir este **servicio**" (x2) | "elegir esta **oferta**" |
| `skill_propuesta_valor` | "Relacionar el **servicio principal**" | "Relacionar la **oferta principal**" |
| `skill_matriz_canales` | (pendiente de leer) | verificar en auditoría |
| `skill_cliente_objetivo` | (pendiente de leer) | verificar en auditoría |
| `skill_plan_accion` | (pendiente de leer) | verificar en auditoría |

6.2 **Añadir bifurcación por modelo** en las skills que producen texto adaptativo:
Para cada SKILL.md donde aplique, añadir sección:

```markdown
## Adaptación por modelo de negocio
- **ecommerce_transaccional**: hablar de producto, compra, conversión, ROAS.
- **b2b_consultivo**: hablar de propuesta consultiva, ciclo de venta, autoridad.
- **educativo_formativo**: hablar de formación, alumno, metodología, resultados.
- **retail_fisico**: hablar de tráfico a tienda, producto local, visita.
- **hibrido_producto_servicio**: hablar de solución integral, mantenimiento, SLA.
```

6.3 **Reforzar entradas/salidas en cada SKILL.md**:
- Campo `tipo_negocio` debe ser entrada explícita en todas las skills
- Si el tipo_negocio no está disponible, la skill debe declarar insuficiencia

6.4 **Definir cuándo declarar insuficiencia** — añadir a cada skill:

```markdown
## Cuándo declarar insuficiencia
Declarar insuficiencia si:
- El tipo de modelo de negocio es desconocido o ambiguo.
- Los datos del brief no permiten diferenciación real del competidor.
- [criterio específico por skill]
```

6.5 **Propuesta de nuevas skills de auditoría** (sujeta a aprobación en Fase 3):
- `skill_auditoria_terminologia`
- `skill_auditoria_perfil_resolver`
- `skill_validacion_kpis_modelo`

**Gate**: leer output de una skill refactorizada con brief de ecommerce y confirmar
ausencia de "servicio" donde debería decir "producto".

---

### Fase 7 — Gates y workflows asociados

**Alcance**: solo gates/workflows que tengan conexión directa con skills modificadas.
No crear gates sueltos sin skill ni workflow que los active.

**Acciones**:

7.1 **Revisar `gate_coherencia_cliente_propuesta.md`** — único gate directamente
ligado a `skill_propuesta_valor`. Verificar si el gate asume lenguaje de servicios.

7.2 **Revisar `gate_canales_justificados.md`** — asociado a `skill_matriz_canales`.
Verificar si los criterios de validación son modelo-agnósticos o asumen servicios.

7.3 **Revisar `gate_kpis_medibles.md`** — verificar si acepta tanto ROAS/CPA
(ecommerce) como CPL/MQL (B2B consultivo) como métricas válidas.

7.4 **Proponer actualización solo si** se detecta incompatibilidad concreta.
No hacer refactor preventivo de gates que no presenten problema evidente.

7.5 **No tocar**:
- `gate_brief_minimo.md` — modelo-agnóstico por diseño
- `gate_no_invencion.md` — transversal, no ligado a modelo
- `gate_plan_accion_realista.md` — sin sesgo de modelo detectado
- Workflows: sin cambios salvo que se detecte problema concreto

**Gate**: ningún gate nuevo debe crearse sin una skill o workflow que lo invoque.

---

### Fase 8 — Validación end-to-end multimodelo

**Alcance**: 6 modelos mínimos. Usar proyectos existentes en `projects/`.

**Modelos a validar y proyectos asociados**:

| Modelo | Proyecto en `projects/` | Fases a generar |
|--------|------------------------|-----------------|
| B2B Consultivo | `audit_b2b_service` | 01-12 |
| B2B Industrial | `audit_b2b_industrial` | 01-12 |
| Ecommerce transaccional | `audit_b2c_ecommerce` (Artesanía Sónica) | 01-12 |
| Retail local | `audit_retail_local` | 01-12 |
| Educativo | `academia_idiomas_infantil` | 01-12 |
| Híbrido | `audit_hybrid_model` | 01-12 |

**Criterios de aprobación por modelo**:

| Criterio | Ecommerce | B2B Consultivo | Educativo |
|----------|-----------|----------------|-----------|
| Perfil resuelto correcto | `ecommerce_transaccional` | `b2b_consultivo` | `educativo_formativo` |
| Sin `estrategia_general_prudente` | ✓ | ✓ | ✓ |
| Terminología correcta en Fase 06 | "comprar ahora" | "contratar" | "inscribirse" |
| KPIs correctos en Fase 08 | ROAS, CPA, tasa conversión | CPL, MQL, ciclo venta | Matrícula, retención |
| Propuesta sin "servicio" genérico | "producto artesanal" | admite "servicio consultivo" | "formación" |
| Auditoría final coherente | ✓ | ✓ | ✓ |

**Gate**: todos los modelos pasan la validación antes de generar ZIP.

---

### Fase 9 — ZIP limpio v1.1

**Alcance**: generar el ZIP de distribución siguiendo el workflow `crear_zip_limpio.md`.

**Exclusiones confirmadas** (basadas en Fases 1-2):
```
projects/          ← datos de clientes
docs/archive/      ← historial interno
.venv/             ← entorno local
__pycache__/       ← generado automáticamente
.git/              ← repositorio interno
*.zip              ← ZIPs previos (incluido marketing_plan_base_v1.0.zip)
.claude/           ← metadata local (excepto .claude/skills/ — ver nota)
.pytest_cache/     ← generado automáticamente
*.log              ← logs de ejecución
```

**Nota sobre `.claude/skills/`**: si el `.gitignore` ha sido corregido en Fase 2
para incluir `.claude/skills/`, el ZIP debe incluirlo también. Actualizar el workflow
`crear_zip_limpio.md` para reflejar esta excepción explícitamente.

**Validación**:
1. Descomprimir en carpeta limpia
2. Ejecutar `uv run pytest tests/ -v` — debe pasar sin instalar nada extra
3. Ejecutar pipeline completo con un brief de prueba
4. Verificar que ningún output menciona `estrategia_general_prudente` para briefs con modelo evidente
5. Verificar tamaño del ZIP — no debe superar ~500KB sin `projects/`

**Gate**: `validar_zip_limpio.md` completado con evidencia adjunta.

---

## 5. Archivos propuestos para modificar en fases posteriores

### Archivos de código (`src/`)

| Archivo | Fase | Tipo de cambio |
|---------|------|----------------|
| `src/core/marketing_profile_resolver.py` | 4 | Ampliar keywords + opcional super-keywords |
| `src/services/canales_service.py` | 5 | Aplicar `terminology` del perfil en texto generado |
| `src/services/propuesta_valor_service.py` | 5 | Verificar y corregir si tiene "servicio" hardcodeado |
| `src/services/comunicacion_service.py` | 5 | Verificar y corregir si aplica |
| `src/services/plan_accion_service.py` | 5 | Verificar y corregir si aplica |
| `tests/test_marketing_profile_resolver.py` | 4 | Añadir test con brief real de Artesanía Sónica |

### Archivos de skills (`.claude/skills/`)

| Archivo | Fase | Tipo de cambio |
|---------|------|----------------|
| `skill_propuesta_valor/SKILL.md` | 6 | Eliminar sesgo servicios, añadir bifurcación |
| `skill_matriz_canales/SKILL.md` | 6 | Auditar y corregir |
| `skill_cliente_objetivo/SKILL.md` | 6 | Auditar y corregir |
| `skill_plan_accion/SKILL.md` | 6 | Auditar y corregir |
| `skill_kpis/SKILL.md` | 6 | Verificar KPIs por modelo |
| `skill_comunicacion/SKILL.md` | 6 | Auditar y corregir |
| Todas las demás skills | 6 | Auditar y corregir si aplica |

### Archivos de configuración y documentación

| Archivo | Fase | Tipo de cambio |
|---------|------|----------------|
| `.gitignore` | 2 | Añadir excepción `!.claude/skills/` |
| `README.md` | 2 | Actualizar para multimodelo real |
| `AGENTS.md` | 2 | Añadir 7 modelos, actualizar reglas de skills |
| `system/gates/gate_coherencia_cliente_propuesta.md` | 7 | Verificar y corregir si aplica |
| `system/gates/gate_canales_justificados.md` | 7 | Verificar y corregir si aplica |
| `system/gates/gate_kpis_medibles.md` | 7 | Verificar si acepta métricas multimodelo |
| `system/workflows/crear_zip_limpio.md` | 9 | Añadir excepción `.claude/skills/` |

### Archivos nuevos a crear

| Archivo | Fase | Descripción |
|---------|------|-------------|
| `docs/plans/estandar_funcional_skills_marketing_multimodelo.md` | 3 | Estándar normativo por modelo |
| `tests/test_resolver_casos_reales.py` (o en archivo existente) | 4 | Test con brief de Artesanía Sónica |

---

## 6. Archivos que NO se tocan

```
src/                        ← hasta Fase 4 mínimo
tests/                      ← hasta Fase 4 mínimo
projects/                   ← nunca en este plan (solo validación manual)
project_template/           ← sin cambios
.claude/skills/             ← hasta Fase 6
agents/                     ← sin cambios detectados
system/rules/               ← sin cambios detectados
README.md                   ← hasta Fase 2
AGENTS.md                   ← hasta Fase 2
.gitignore                  ← hasta Fase 2
docs/archive/               ← no tocar (solo excluir de ZIP)
marketing_plan_base_v1.0.zip ← eliminar del índice git (git rm --cached) en Fase 2
```

---

## 7. Riesgos identificados

| Riesgo | Probabilidad | Impacto | Mitigación |
|--------|-------------|---------|-----------|
| Al ampliar keywords del resolver, algún brief que antes clasificaba correctamente puede reclasificarse mal | Media | Alto | Ejecutar todos los tests existentes antes y después de cada cambio |
| Reducir `MIN_MATCHES` puede hacer el resolver demasiado permisivo en casos ambiguos | Media | Medio | Usar super-keywords como alternativa sin bajar el umbral global |
| Corregir terminología en `canales_service.py` puede romper el formato de outputs si hay dependencias implícitas | Baja | Medio | Leer todos los servicios que usan `profile` antes de cambiar |
| Eliminar `skills/` raíz puede romper referencias en `README.md` o documentación externa | Baja | Bajo | Verificar todas las referencias antes de eliminar |
| La corrección del `.gitignore` para `.claude/skills/` puede añadir archivos al índice inesperadamente si hay archivos de sesión en `.claude/` | Baja | Medio | Hacer `git status` después del cambio y antes de `git add` |
| Tests de validación end-to-end dependen de que los proyectos en `projects/` tengan briefs correctos | Media | Medio | Verificar que cada brief tenga los campos mínimos antes de generar |

---

## 8. Verificaciones esperadas por fase

| Fase | Verificación | Comando / Criterio |
|------|-------------|-------------------|
| 1 | ZIP rastreado por git | `git ls-files --cached \| grep .zip` → debe aparecer |
| 1 | `.claude/skills/` no rastreado | `git ls-files --cached \| grep .claude` → vacío |
| 2 | `.claude/skills/` rastreado tras corrección | `git ls-files --cached \| grep .claude/skills` → 13 SKILL.md |
| 2 | ZIP eliminado del índice | `git ls-files --cached \| grep .zip` → vacío |
| 4 | Test Artesanía Sónica falla antes del fix | `uv run pytest tests/ -k artesania -v` → FAILED |
| 4 | Test Artesanía Sónica pasa tras fix | `uv run pytest tests/ -k artesania -v` → PASSED |
| 4 | Todos los tests siguen pasando | `uv run pytest tests/ -v` → 10+ PASSED |
| 5 | Terminología en output de Fase 06 ecommerce | grep "comprar ahora" en 06_matriz_canales_marketing.md |
| 6 | Skill propuesta_valor sin "servicio" genérico | leer SKILL.md — ausencia de "elegir este servicio" |
| 8 | Ningún modelo resuelve como estrategia_general | revisar perfil en outputs de las 6 validaciones |
| 9 | ZIP válido en entorno limpio | descomprimir + `uv run pytest` → PASSED |

---

## 9. Estado final esperado

```
implementation_plan_correccion_lean_multimodelo_creado
```

Condiciones de cierre de v1.1 (todas deben cumplirse):

- [ ] `.gitignore` corregido — `.claude/skills/` visible en git
- [ ] `marketing_plan_base_v1.0.zip` eliminado del índice git
- [ ] `skills/` raíz eliminada o reconvertida
- [ ] `README.md` y `AGENTS.md` actualizados para multimodelo
- [ ] `docs/plans/estandar_funcional_skills_marketing_multimodelo.md` creado
- [ ] Test con brief de Artesanía Sónica añadido y pasando
- [ ] Resolver clasifica correctamente los 6+ modelos con briefs reales
- [ ] `canales_service.py` aplica terminología del perfil
- [ ] Skills sin sesgo de servicios
- [ ] Validación end-to-end de los 6 modelos mínimos completa
- [ ] ZIP limpio v1.1 generado y validado en entorno limpio
- [ ] Sin `estrategia_general_prudente` en outputs de modelos con brief evidente

---

## 10. Restricciones de este plan

Este documento es solo planificación. No se ha modificado ningún archivo
operativo durante su redacción. La ejecución comienza solo tras aprobación
explícita por el usuario, fase a fase.

Archivos que este plan SÍ ha modificado:
- `docs/plans/implementation_plan_correccion_lean_multimodelo_v1.md` (este archivo)
- `task_list_correccion_lean_multimodelo_v1.md` (actualización de task list)

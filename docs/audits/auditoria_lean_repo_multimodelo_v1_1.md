# Auditoría Lean Repositorio Multimodelo v1.1

```
Fase     : 1 — Auditoría Lean del repositorio
Fecha    : 2026-04-30
Estado   : fase_1_auditoria_lean_repo_completada
Método   : solo lectura — ningún archivo operativo modificado
Plan ref : docs/plans/implementation_plan_correccion_lean_multimodelo_v1.md

Fase 2   : 2 — Limpieza Lean (workflows de ZIP)
Fecha 2  : 2026-04-30
Estado 2 : fase_2_limpieza_lean_repo_aplicada_pendiente_revision_final
```

---

## Resumen ejecutivo

| Hallazgo | Severidad | Estado en git | Acción en Fase 2 |
|----------|-----------|---------------|-----------------|
| `.claude/skills/` excluida del índice git | Alta | No rastreado | Corregir `.gitignore` |
| `docs/archive/project_history/` rastreada en git | Media | Rastreado (2 archivos) | Excluir de ZIP; evaluar si hacer `git rm --cached` |
| `marketing_plan_base_v1.0.zip` | Baja | **No rastreado** ✓ | Sin acción git necesaria |
| `projects/` | Ninguna | **No rastreado** ✓ | Sin acción git necesaria |
| `skills/` raíz — 15+ referencias cruzadas | Media | Rastreado (README.md) | Decidir destino; no eliminar hasta mapear refs |
| `system/rules/README.md` modificado sin commit | Baja | Modificado, sin stage | Registrar; no bloquea v1.1 |
| 4 nuevos archivos sin commitear | Info | Untracked | Commitear cuando corresponda |

**Actualización Fase 2 (2026-04-30):**
- Workflows de ZIP actualizados para separar explícitamente dos modos: **Modo A (ZIP cliente/proyecto)** y **Modo B (ZIP base sistema v1.1)**.
- Estado de Fase 2: `fase_2_limpieza_lean_repo_aplicada_pendiente_revision_final`.

---

## 1. Estado del índice git — evidencia directa

### 1.1 `git status --short` (estado actual)

```
 M system/rules/README.md
?? docs/audits/auditoria_lote_5_rules.md
?? docs/audits/auditoria_skills_marketing.md
?? docs/plans/implementation_plan_correccion_lean_multimodelo_v1.md
?? task_list_correccion_lean_multimodelo_v1.md
```

**Interpretación**:
- `M` (modificado, sin stage): `system/rules/README.md` — cambio local pendiente de commit.
  No bloquea ninguna fase. No es parte del alcance actual.
- `??` (untracked): 4 archivos nuevos generados en la sesión de planificación de hoy.
  Deben commitearse cuando la Fase 2 esté aprobada y ejecutada.

### 1.2 `git ls-files --cached | grep ".zip"`

```
docs/hitos/2026-04-30_validacion_zip_base_v1.md
system/workflows/crear_zip_limpio.md
system/workflows/validar_zip_limpio.md
```

**Interpretación**: Ninguno de estos es un archivo `.zip`. Son documentos Markdown que
contienen "zip" en el nombre (hitos y workflows). El archivo `marketing_plan_base_v1.0.zip`
**NO está en el índice git**.

✅ **Conclusión**: La regla `*.zip` en `.gitignore` funcionó correctamente desde el
inicio. **No se necesita `git rm --cached`** para el ZIP. El ZIP vive únicamente en el
sistema de archivos local.

### 1.3 `git ls-files --cached | grep ".claude"`

```
(sin resultados)
```

**Interpretación**: `.claude/` está completamente excluida del índice git, incluyendo
`.claude/skills/` (las 13 skills operativas del sistema).

⚠️ **Conclusión**: Las skills son invisibles al control de versiones. Si el repositorio
se clona en otra máquina, las 13 skills no estarán presentes. Esto es un fallo
estructural que debe corregirse en Fase 2.

### 1.4 `git ls-files --cached | grep "projects/"`

```
(sin resultados)
```

✅ **Conclusión**: `projects/` está correctamente excluido de git. Los 10 proyectos
locales (banco de validación multimodelo) no entrarán al ZIP ni al repositorio remoto.

### 1.5 `git ls-files --cached | grep "docs/archive"`

```
docs/archive/project_history/2026-04-29_cierre_pipeline_real_controlado.md
docs/archive/project_history/2026-04-29_cierre_preparacion_30_dias.md
```

⚠️ **Conclusión**: `docs/archive/` está rastreado en git (2 archivos). Son historiales
de cierre de sesiones internas. No son parte del sistema distribuible. No deben
incluirse en el ZIP v1.1.

**Opciones para Fase 2**:
- Opción A: `git rm --cached` de ambos archivos + añadir `docs/archive/` al `.gitignore`.
- Opción B: Mantenerlos en git como registro histórico, pero excluirlos explícitamente
  al generar el ZIP (workflow `crear_zip_limpio.md`).

La decisión queda pendiente de aprobación. Se recomienda la **Opción B** por ser
menos destructiva (preserva el historial sin reescribir el índice git).

---

## 2. Contenido local no rastreado por git

### 2.1 `projects/` — 10 proyectos presentes localmente

```
academia_idiomas_infantil/     (educativo)
audit_b2b_industrial/          (b2b_producto_industrial)
audit_b2b_service/             (b2b_consultivo)
audit_b2c_ecommerce/           (ecommerce_transaccional — Artesanía Sónica)
audit_hybrid_model/            (hibrido_producto_servicio)
audit_retail_local/            (retail_fisico)
centro_estetica_local/         (b2c_local_servicios)
proyecto_prueba/               (prueba genérica)
proyecto_real_controlado/      (producción real)
servicio_gestion_documental/   (b2b_consultivo / fallback)
```

Estado: locales, no en git, no distribuibles. Correctamente configurados.

**Nota Fase 8**: `projects/` actúa como banco de validación end-to-end local.
Nunca debe entrar al ZIP v1.1. Esta restricción debe mantenerse aunque la
validación use esos proyectos como fixtures de prueba.

### 2.2 `docs/archive/project_history/` — 2 archivos presentes

```
2026-04-29_cierre_pipeline_real_controlado.md   (3151 bytes, 29-abr-2026)
2026-04-29_cierre_preparacion_30_dias.md        (2032 bytes, 30-abr-2026)
```

Contenido: registros de cierre de sesiones de desarrollo anteriores.
No son funcionales para el sistema, solo son historial interno.

---

## 3. Análisis de la carpeta `skills/` raíz

### 3.1 Estado actual

```
skills/
└── README.md    (único archivo — rastreado en git)
```

La carpeta `skills/` raíz fue creada en una sesión anterior como estructura inicial.
Posteriormente, todas las skills operativas fueron migradas al formato estándar
`.claude/skills/<skill_name>/SKILL.md`.

Evidencia de la migración en `docs/audits/auditoria_lote_2_skills_agentica.md`:
> "que no quedan skills MVP como archivos sueltos en `skills/`: **Cumplido**"

`skills/README.md` describe el propósito de las skills como concepto pero no
referencia las 13 skills actuales de `.claude/skills/`.

### 3.2 Referencias activas a `skills/` — mapa completo

**AGENTS.md** — 1 referencia:
```
AGENTS.md:41 → src/, project_template/, docs/, tests/, system/, agents/, skills/.
```
Lista `skills/` como carpeta estructural del sistema base.

**README.md** — 3 referencias:
```
README.md:183  → ├── skills/             # Estructura inicial creada: habilidades
README.md:229  → ### 7.4 `skills/`
README.md:238  → skills/skill_intake_brief/SKILL.md   ← apunta a FORMATO ANTIGUO
README.md:768  → - Migrar `system/`, `agents/` y `skills/` a implementación real (En proceso).
```
La referencia en línea 238 apunta a `skills/skill_intake_brief/SKILL.md`, que es el
**formato anterior** a la migración a `.claude/skills/`. Esta ruta ya no existe.

**docs/ (documentos de especificación)** — referencias históricas:
```
docs/00_planificacion_mvp_sistema_plan_marketing.md:249  → ├── skills/
docs/04_skills_y_uso.md:1150                             → skills/skill_nombre/ (formato antiguo)
docs/07_estructura_repositorio.md:64, 336, 343, 857, 860 → múltiples (5 referencias)
docs/08_arquitectura_tecnica_inicial.md:504, 897         → 2 referencias
docs/09_criterios_de_hecho.md:577                        → referencia de exclusión
```

**docs/audits/** — referencias mixtas (antiguas + nuevas):
```
auditoria_gap_agentico.md       → explica la migración de skills/ a .claude/skills/
auditoria_lote_2_skills_agentica.md → confirma migración completada
auditoria_lote_3_materializacion.md → referencia conceptual
```

**Total de referencias**: 15+ en 10+ archivos distintos.

### 3.3 Evaluación de riesgo

| Acción | Riesgo | Impacto |
|--------|--------|---------|
| Eliminar `skills/` sin actualizar referencias | Alto | README y AGENTS quedarían con rutas rotas |
| Eliminar `skills/` después de actualizar refs | Bajo | Correcto, pero requiere tocar README y AGENTS (Fase 2) |
| Mantener `skills/` y reconvertirla | Muy bajo | La más segura para Fase 2 |

**Recomendación confirmada**: no eliminar `skills/` en esta fase. La decisión
queda para Fase 2, después de actualizar README.md y AGENTS.md.

---

## 4. Estado de README.md y AGENTS.md — hallazgos de lenguaje

### 4.1 README.md — lenguaje desactualizado detectado

Evidencia sin leer el archivo completo (basada en referencias del grep):

| Línea | Problema detectado |
|-------|--------------------|
| 183 | `skills/` referenciada como ubicación de habilidades (rol ahora de `.claude/skills/`) |
| 238 | `skills/skill_intake_brief/SKILL.md` — ruta del formato antiguo, ya no existe |
| 768 | "En proceso" — migración de skills ya completada, texto desactualizado |

Para Fase 2: verificar también si README habla del sistema como orientado solo a
"servicios" (sesgo no multimodelo).

### 4.2 AGENTS.md — hallazgo puntual

| Línea | Problema detectado |
|-------|--------------------|
| 41 | Lista `skills/` como carpeta estructural del sistema base junto a `src/`, `docs/`, etc. |

La referencia mezcla `skills/` (carpeta raíz, casi vacía) con la estructura real
que es `.claude/skills/`. Debe aclararse en Fase 2.

---

## 5. Archivos del repositorio no commiteados — pendientes

Los siguientes 4 archivos fueron creados en la sesión de planificación (hoy)
y están sin commitear:

| Archivo | Estado git | Fase en que se commitea |
|---------|-----------|------------------------|
| `docs/audits/auditoria_lote_5_rules.md` | `??` untracked | Pendiente de aprobación |
| `docs/audits/auditoria_skills_marketing.md` | `??` untracked | Pendiente de aprobación |
| `docs/plans/implementation_plan_correccion_lean_multimodelo_v1.md` | `??` untracked | Al cerrar Fase 1 |
| `task_list_correccion_lean_multimodelo_v1.md` | `??` untracked | Al cerrar Fase 1 |
| `docs/audits/auditoria_lean_repo_multimodelo_v1_1.md` | `??` untracked (este archivo) | Al cerrar Fase 1 |

Además: `system/rules/README.md` tiene una modificación sin stage. No es parte del
alcance actual — debe registrarse para commit posterior.

---

## 6. Conclusiones consolidadas por ítem del plan

| Ítem del plan (Fase 1) | Resultado confirmado |
|------------------------|---------------------|
| Confirmar si ZIP está en índice git | ✅ NO está — `*.zip` funciona correctamente |
| Confirmar si `.claude/skills/` está fuera del índice | ✅ Confirmado — 0 archivos rastreados |
| Verificar que `projects/` no está rastreado | ✅ Confirmado — 0 archivos rastreados |
| Confirmar `docs/archive/` en índice git | ⚠️ Confirmado — 2 archivos rastreados |
| Listar proyectos locales para Fase 8 | ✅ 10 proyectos listos como banco de validación |
| Buscar referencias a `skills/` antes de decidir su destino | ✅ 15+ referencias en 10+ archivos |
| Detectar lenguaje desactualizado en README y AGENTS | ⚠️ Detectado — rutas antiguas y referencias obsoletas |

---

## 7. Acciones propuestas para Fase 2 (sin ejecutar todavía)

Ordenadas por prioridad:

1. **Corregir `.gitignore`**: añadir excepción `!.claude/skills/` — crítico
2. **Actualizar `README.md`**: corregir ruta de skills (línea 238), lenguaje multimodelo
3. **Actualizar `AGENTS.md`**: aclarar `skills/` vs `.claude/skills/`
4. **Decidir destino de `skills/` raíz**: después de actualizar README y AGENTS
5. **Evaluar `docs/archive/`**: Opción A (git rm --cached) o Opción B (excluir de ZIP)
6. **Registrar hito de Fase 2**

**No se propone `git rm --cached` del ZIP** — no está en el índice, no es necesario.

---

## 8. Estado de cierre

```
fase_1_auditoria_lean_repo_completada
```

Fecha de cierre: 2026-04-30
Archivos modificados en esta fase: ninguno operativo.
Archivo creado: `docs/audits/auditoria_lean_repo_multimodelo_v1_1.md` (este documento).

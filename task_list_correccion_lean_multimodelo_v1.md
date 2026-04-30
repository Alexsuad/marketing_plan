# Task List: Corrección Lean Multimodelo v1.1

```
Estado : PLANIFICACIÓN COMPLETA — pendiente aprobación para ejecutar
Fecha  : 2026-04-30
Plan   : docs/plans/implementation_plan_correccion_lean_multimodelo_v1.md
```

---

## Fase 1 — Auditoría Lean del repositorio [ ]

- [ ] Ejecutar `git ls-files --cached | grep .zip` — confirmar si ZIP está en índice git
- [ ] Ejecutar `git ls-files --cached | grep .claude` — confirmar que `.claude/skills/` está fuera del índice
- [ ] Listar contenido de `docs/archive/` para evaluar riesgo de distribución
- [ ] Verificar que `projects/` tiene 10 proyectos presentes pero no rastreados
- [ ] Revisar `README.md` y `AGENTS.md` — detectar lenguaje desactualizado
- [ ] Documentar hallazgos en auditoría (apéndice de `docs/audits/`)

## Fase 2 — Limpieza Lean [ ]

- [ ] Corregir `.gitignore`: añadir `!.claude/skills/` y `!.claude/skills/**`
- [ ] Si ZIP está en índice: ejecutar `git rm --cached marketing_plan_base_v1.0.zip`
- [ ] Decidir destino de `skills/` raíz (Opción A: eliminar / Opción B: indexar)
- [ ] Ejecutar decisión sobre `skills/` raíz
- [ ] Actualizar `README.md` — multimodelo real, ubicación de skills, sin "v1.0 estable"
- [ ] Actualizar `AGENTS.md` — 7 modelos soportados, reglas de `.claude/skills/`
- [ ] Registrar limpieza en hito de `docs/hitos/`
- [ ] Verificar: `git ls-files --cached | grep .claude/skills` → 13 SKILL.md

## Fase 3 — Estándar funcional multimodelo [ ]

- [ ] Crear `docs/plans/estandar_funcional_skills_marketing_multimodelo.md`
- [ ] Documentar bifurcación por los 7 modelos (tabla: accion_principal, cliente, oferta)
- [ ] Definir lenguaje prohibido por modelo
- [ ] Definir criterios de insuficiencia por skill
- [ ] Definir errores bloqueantes
- [ ] Proponer (sin crear aún) 3 nuevas skills de auditoría

## Fase 4 — Corrección ecommerce real [ ]

- [ ] Añadir test `test_resolve_artesania_sonica_ecommerce` en `tests/`
- [ ] Ejecutar test — confirmar que FALLA en estado actual
- [ ] Ampliar `PROFILE_KEYWORDS["ecommerce_transaccional"]` con términos D2C
- [ ] Evaluar si añadir lógica de super-keywords (alta señal con score=1)
- [ ] Ejecutar test — confirmar que PASA tras corrección
- [ ] Ejecutar suite completa — confirmar 0 regresiones
- [ ] Regenerar fases 06-12 de `audit_b2c_ecommerce`
- [ ] Verificar ausencia de `estrategia_general_prudente` en outputs de ese proyecto

## Fase 5 — Terminología comercial aplicada [ ]

- [ ] Extraer `profile['terminology']` en `canales_service.py`
- [ ] Sustituir strings hardcodeados "contratar", "servicio" por variables de terminología
- [ ] Auditar `propuesta_valor_service.py` — verificar si tiene sesgo
- [ ] Auditar `comunicacion_service.py` — verificar si tiene sesgo
- [ ] Auditar `plan_accion_service.py` — verificar si tiene sesgo
- [ ] Corregir solo donde haya contaminación confirmada
- [ ] Verificar: output Fase 06 para Artesanía Sónica contiene "comprar ahora"

## Fase 6 — Refactor funcional de skills [ ]

- [ ] Auditar las 13 skills de `.claude/skills/` — detectar sesgo de servicios
- [ ] Corregir `skill_propuesta_valor`: "elegir este servicio" → "elegir esta oferta"
- [ ] Corregir `skill_propuesta_valor`: "servicio principal" → "oferta principal"
- [ ] Corregir resto de skills con sesgo detectado
- [ ] Añadir sección "Adaptación por modelo de negocio" en skills que producen texto
- [ ] Añadir campo `tipo_negocio` como entrada explícita en todas las skills
- [ ] Añadir sección "Cuándo declarar insuficiencia" en cada skill
- [ ] Propuesta de nuevas skills de auditoría — pendiente aprobación

## Fase 7 — Gates y workflows asociados [ ]

- [ ] Revisar `gate_coherencia_cliente_propuesta.md` — verificar sesgo
- [ ] Revisar `gate_canales_justificados.md` — verificar sesgo
- [ ] Revisar `gate_kpis_medibles.md` — verificar si acepta ROAS/CPA + CPL/MQL
- [ ] Actualizar solo los gates con incompatibilidad confirmada
- [ ] No crear gates nuevos sin skill o workflow que los invoque

## Fase 8 — Validación end-to-end multimodelo [ ]

- [ ] Validar B2B Consultivo (`audit_b2b_service`) — fases 01-12
- [ ] Validar B2B Industrial (`audit_b2b_industrial`) — fases 01-12
- [ ] Validar Ecommerce (`audit_b2c_ecommerce`) — fases 01-12
- [ ] Validar Retail Local (`audit_retail_local`) — fases 01-12
- [ ] Validar Educativo (`academia_idiomas_infantil`) — fases 01-12
- [ ] Validar Híbrido (`audit_hybrid_model`) — fases 01-12
- [ ] Confirmar: perfil correcto en cada modelo
- [ ] Confirmar: terminología correcta en Fase 06 de cada modelo
- [ ] Confirmar: KPIs correctos en Fase 08 de cada modelo
- [ ] Confirmar: auditoría final coherente en Fase 12 de cada modelo

## Fase 9 — ZIP limpio v1.1 [ ]

- [ ] Generar ZIP siguiendo workflow `crear_zip_limpio.md`
- [ ] Verificar exclusiones: `projects/`, `docs/archive/`, `.venv/`, `__pycache__/`, `*.zip`, `.git/`
- [ ] Verificar inclusión de `.claude/skills/` en ZIP
- [ ] Descomprimir en carpeta limpia y ejecutar `uv run pytest tests/ -v`
- [ ] Ejecutar pipeline completo con brief de prueba
- [ ] Verificar tamaño del ZIP ≤ ~500KB
- [ ] Registrar hito de cierre con evidencia

---

**Estado actual**: `implementation_plan_correccion_lean_multimodelo_creado`

**Próximo paso**: aprobación del plan por el usuario → inicio de Fase 1.

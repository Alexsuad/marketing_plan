# skills/ — Carpeta documental / legada

> **Las skills operativas del sistema NO están aquí.**
>
> Las 13 skills del MVP viven en **`.claude/skills/`** (raíz del repositorio).
> Esa ubicación está bajo control de versiones y es parte estructural del sistema.

---

## Por qué existe esta carpeta

Esta carpeta fue creada en una etapa inicial del proyecto como estructura provisional.
Posteriormente, todas las skills fueron migradas al formato estándar:

```
.claude/skills/<nombre>/SKILL.md
```

La migración está completada. Esta carpeta se conserva como referencia documental
y para no romper referencias históricas en documentos de auditoría anteriores.

## Reglas

- **No crear nuevas skills aquí.**
- **No modificar skills desde aquí** — los cambios no tendrán efecto operativo.
- Toda skill nueva debe ir a `.claude/skills/<nombre>/SKILL.md`.

## Skills operativas actuales (en `.claude/skills/`)

| Skill | Fase | Agente activador |
|-------|------|-----------------|
| `skill_intake_brief` | 01 | orquestador |
| `skill_diagnostico_marketing` | 02 | estratega |
| `skill_cliente_objetivo` | 03 | estratega |
| `skill_propuesta_valor` | 04 | estratega |
| `skill_analisis_competencia` | 05 | investigador |
| `skill_matriz_canales` | 06 | estratega |
| `skill_estrategia_comunicacion` | 07 | redactor |
| `skill_plan_accion` | 08 | estratega |
| `skill_presupuesto_marketing` | 09 | analista |
| `skill_kpis` | 10 | analista |
| `skill_resumen_plan_empresa` | 11 | redactor |
| `skill_auditoria_coherencia` | 12 | auditor |
| `skill_change_request` | transversal | orquestador |

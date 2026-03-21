# PARA EL WORKSHOP (2h)
---
## Prerequisitos
- Tener configurado Claude Code en Wallbox.
- 


## PAblos
- Modelo: cuando usar cada uno
- Cómo reducir el uso de tokens
- 


## 1 hora con repo demo

- ¿qué modelo elijo?

- configuración y básicos
- rewind
- add-dir
- ojo compact
- lsp
- permisos

- memoria
- claude.md, rules
- automemory
- skills/agents




- Permisos:
    - Ejemplos de allow y Deny en el settings.json (se puede hacer a nivel global, de usuario o de proyecto)
    - Pidele que lea este fichero con cat. Te pregunta. 
    - Añade el allow (No te pregunta)
    - Deny en el settings no te deja leerlo.
- CLAUDE.md and RULES.md
    - no /init o solo como base
    -
- LSP para determinismo
    - https://claude.com/plugins/ -> LSP
    - Instalar plugins
    
- Ejemplos de Skills 
    - Skills creator: https://claude.com/plugins/skill-creator 
- Agents: 
    - sample Stepwise-dev deep-research o  research-codebase
- Hooks: 
    - Ejempo Toni-Agent API: "command": "make lint-fix"


## 1 hora libre con sus repos y nosotros ayudamos:

- Apuntado que os va bien y qué os va mal para compartir luego.


- Cada persona trae un ticket pequeño/mediano de su equipo.

## 20 min de retro para ver que va bien, que va mal, siguientes pasos.










---




# Lo que sí poner en CLAUDE.md

**Título:** CLAUDE.md: el briefing, no la enciclopedia
**Contenido (dos columnas):**

**❌ No hagas:**
- Markdowns enormes con todo lo imaginable
- Duplicar README o configs
- Explicar principios que la IA ya conoce
- Meter todos los comandos "por si acaso"

**✅ Haz esto:**
- Escríbelo como para un compañero nuevo que no meta la pata
- 40–300 líneas máximo
- Solo lo que no se puede deducir del código
- Convenciones que difieran del estándar del lenguaje
- **Cómo verificar sus cambios** (lo más importante)

```markdown
## Verification Requirements
- Run `npm test` after code changes
- Run `npm run typecheck` before marking complete
- For API changes, test with curl
- For UI changes, verify in browser
```

**🎤 Notas de orador:**
"CLAUDE.md sigue siendo importante, pero para lo esencial. Lo que no se puede deducir del código, las convenciones propias, y sobre todo: cómo verificar. Si le das una forma de comprobar su trabajo, se autocorrige. Sin eso, eres tú quien revisa cada línea."

"Todo lo demás — las prácticas especializadas, los workflows complejos, la experiencia acumulada — eso va en skills, no en CLAUDE.md."


# De CLAUDE.md a Skills: experiencia codificada

**Título:** No repitas instrucciones. Codifica tu experiencia.
**Contenido:**

**El problema de CLAUDE.md:**
- Todo se carga siempre, sea relevante o no
- Claude inyecta: *"Este contexto puede o no ser relevante. No respondas a él salvo que sea altamente relevante."*
- Cuanta más basura, más probable que ignore lo importante

**La solución: Skills**
Conocimiento empaquetado que se activa solo cuando es relevante. Progressive disclosure para el contexto de la IA.

**Ejemplo — pipeline de delivery (Eduardo Ferro / skill-factory):**
```
/story-splitting     → ¿Es esta historia realmente tres historias con un trench coat?
/hamburger-method    → Corta la feature en capas, genera opciones, compón el slice más fino
/small-safe-steps    → Incrementos de 1-3h, cada uno desplegable de forma independiente
/complexity-review   → 30 dimensiones de complejidad. "¿Por qué Kafka y no una cola?"
/code-simplifier     → Reduce complejidad sin cambiar comportamiento
```

**🎤 Notas de orador:**
"Todos los que usáis Claude Code conocéis CLAUDE.md. Funciona. Pero tiene un problema: todo se carga siempre. Tus guías de TDD, tus prácticas de Docker, tu workflow de refactoring... todo compitiendo por la ventana de contexto, sea relevante o no."

"Eduardo Ferro encontró algo mejor: las Skills. Conocimiento empaquetado que se activa solo cuando lo necesitas. Escribes `/mutation-testing` y la IA gana experiencia profunda en encontrar tests débiles. Escribes `/complexity-review` y se convierte en un revisor técnico que desafía tu propuesta contra 30 dimensiones de complejidad. El resto del tiempo, ese conocimiento está fuera del camino."

"Pensadlo así: es progressive disclosure para el contexto de la IA. Le das lo que necesita, cuando lo necesita."

"Pero lo más potente es que las skills se encadenan como un pipeline. Un ejemplo real: tienes una historia de usuario grande. Invocas `/story-splitting` y detecta que en realidad son tres historias disfrazadas. Coges la primera, invocas `/hamburger-method` para cortarla en capas y generar el slice más fino. Luego `/small-safe-steps` para planificar incrementos de 1-3 horas, cada uno desplegable de forma independiente."

"No es una skill que lo hace todo. Son skills que componen. Eso es lo que las hace poderosas."

**Transición:**
"Y esto es open source. El skill-factory de Lada Kesseler tiene 315 commits de skills bien construidas. Eduardo añadió 11 más. Podéis forkearlo hoy y empezar a codificar vuestra experiencia."

---

8. Rewind

Si Claude se desvía, puedo hacer rewind instantáneamente con `Esc+Esc` o el comando `/rewind`.

Tres modos de restauración:
- **Conversation only**: Mantener cambios en código, revertir chat
- **Code only**: Mantener conversación, revertir código
- **Both**: Restauración completa al estado anterior

**Tip del taller**: enseña que rewind no revierte cambios hechos por bash (por ejemplo `rm`, `mv`, `cp`).

### Para refactors grandes

1. Los checkpoints no rastrean comandos bash. Claude ejecutó un script de migración de base de datos que quería revertir. Los checkpoints solo rastrean ediciones de archivos, no operaciones bash.
   - **Workaround**: Ahora hago que Claude escriba los comandos bash en scripts temporales en vez de ejecutarlos directamente. Luego puedo revisarlos antes de ejecutar.



---

### Verification Requirements en CLAUDE.md

The fix — add verification requirements to CLAUDE.md:

```markdown
## Verification Requirements
- Run `npm test` after code changes
- Run `npm run typecheck` before marking complete
- For API changes, test with `curl` or Postman
- For UI changes, verify in browser before committing
```

Then Claude will actually run these checks. Not because you told it to in the prompt — because it's baked into project context.

Dale a Claude una forma de verificar su trabajo.

---



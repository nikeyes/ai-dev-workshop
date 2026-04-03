# Workshop: Desarrollo guiado por IA (2h)

**Objetivo:** Aprender las bases para desarrollar con IA de forma efectiva.

---

## Prerequisitos

- Claude Code instalado y configurado con Bedrock.
- Haber ejecutado al menos una vez `claude` en terminal
- Tener descargado el proyecto: ....
- Haber ejecutado:
    - cd workshop-project
    - docker compose build
    - docker compose run --rm app uv run pytest
- Traer un ticket pequeño/mediano del equipo

---

## Bloque 1: Guiado (1h)

### 1. **Verificar el entorno** — Todos tienen Claude Code funcionando antes de empezar.

Antes de empezar, todos ejecutan:

```bash
cd workshop-project
claude --version
claude "hola, di solo 'listo'"
```

No seguimos hasta que todos tengan Claude Code funcionando.

Para ver el estado completo del entorno en cualquier momento:

```
/doctor
/status
``` 

### Tips 
**¿Tuviste que parar en mitad de una tarea?
- `claude --continue` para reanudar la última sesión.
- `claude --resume` para elegir una sesión anterior.
- Las sesiones son por carpeta.

- Si no puedes explicar en una frase qué tiene que hacer el agente, el agente tampoco lo va a saber.


### 2. **Modelos y coste** — Cuándo usar Haiku / Sonnet / Opus.

| Modelo | Cuándo usarlo                                                |
| ------ | ------------------------------------------------------------ |
| Haiku  | Tareas simples: renombrar, formatear, buscar                 |
| Sonnet | El 80% del trabajo cotidiano                                 |
| Opus   | Arquitectura, debugging difícil, decisiones críticas, planes |

Por defecto yo empiezo con Sonnet.  
Escribe `/cost` para ver el gasto. Sube a Opus solo si Sonnet no llega.

How to choose a model?  ( La guia para no tech que hice en KA)
- Haiku: Your reliable assistant. Ideal for simple, repetitive work: updating Jira tickets, formatting content, summarising notes, or other structured tasks where speed and cost matter more than depth.

- Sonnet: Your experienced all-rounder. Handles the vast majority of day-to-day work well. The gap with Opus has narrowed significantly. This should be your default choice.

- Opus: Your most senior expert. Reserve it for genuinely complex tasks: nuanced analysis, multi-layered reasoning, or problems where a cheaper model didn't deliver.

Si os preocupa mucho el consumo de tokens: https://github.com/rtk-ai/rtk
Pero es una herramienta de terceros con decisiones opinionadas y con telemetría por defecto...


### 3. **Memoria de los agentes** — CLAUDE.md, RULES.md,

Sin CLAUDE.md, el agente empieza cada sesión desde cero. Es como contratar a alguien nuevo cada día.

**¿CREAR SLIDE - BUENAS PRACTICAS CLAUDE.md?**

**Demo en el repo:**

**PROMPT**
```
Ejecuta los tests del proyecto
```

- Renombrar el ___CLAUDE.md a CLAUDE.md

**PROMPT**
```
Ejecuta los tests del proyecto
```

**PROMPT**
```
Comprueba si el proyecto esta ready 
```

- Renombrar el workshop-project/.claude/____rules a rules

**PROMPT**
```
Comprueba si el proyecto esta ready 
```


**Nota sobre la jerarquía de CLAUDE.md y Rules:**

- `~/.claude/CLAUDE.md` — aplica a todos tus proyectos (convenciones personales)
- `<raíz-del-proyecto>/CLAUDE.md` — aplica al proyecto completo
- `<subdirectorio>/CLAUDE.md` — aplica solo a ese módulo (útil en monorepos)
- doc: https://code.claude.com/docs/en/memory#organize-rules-with-claude/rules/


### 4. Contexto

- /context
- /compact Cuidado
    - ⚠️ Ojo con los compacts automáticos: Claude los hace solo cuando no queda espacio. Pueden perder contexto crítico que no has guardado. Si ves que el agente "olvida" algo, puede ser esto.
- Puedes mostrarlo en la status bar
- si necesitas contexto de otro módulo sin abrir una sesión nueva:
```
/add-dir ../otro-servicio
```


### 4. **Permisos** — Configurar `allow`/`deny` en `settings.json` antes de empezar a trabajar o durante la sesión

**Dónde van los settings:**

- Global: `~/.claude/settings.json` (todos los proyectos)
- Proyecto: `.claude/settings.json` (proyecto)
- local: `.claude/settings.local.json` (solo tú)

```
Ejecuta los tests del proyecto -> Añadirlo con el yes
Ejecuta los tests del proyecto
```

Allow and Deny

Enseñar mi ejemplo de settings para ToniAgent

### 5. **Rewind** — Deshacer cuando el agente se desvía. Enseñar limitaciones con comandos bash.

**PROMPT**
```
Crea un fichero de texto con una haiku en japonés
```

**PROMPT**
```
Borra el fichero del Haiku
```

Rewind


⚠️ **Aviso importante**: En las últimas versiones también deshace comandos de bash, pero no os fiéis...


### 6. **Hooks** — Guardarraíles automáticos (linter, tests) que se ejecutan sin pedirlo.

Los hooks ejecutan comandos automáticamente en respuesta a acciones del agente. Son el "diseña para supervisar" de la charla hecho realidad.

Hay dos eventos clave con usos distintos:

- **`PostToolUse` + matcher `Edit`** — se dispara después de cada edición. Ideal para el linter: corriges el fichero mientras aún está en foco.
- **`Stop`** — se dispara cuando el agente termina su turno, sea cual sea el número de ediciones que haya hecho. Ideal para la build: esperas a que todos los cambios estén hechos antes de compilar.

Crear hooks para el linter y el formatter.
**PROMPT**
```
Using the claude-code-guide agent, configure a hook in the settings.json of the project to run the format tool after every file edit.   
```

A partir de ahora, el linter corre en cada fichero editado y la build corre una sola vez al terminar. Sin que tengas que pedirlo.

Por si acaso he creado un ___settings.json con un Hook de format


# 7. **Agents and Skills** - Gestionar el conocimiento compartido
- Anthropic Skill Creator: https://github.com/anthropics/skills/tree/main/skills/skill-creator

**PROMPT**
```
Haz el code review del main.py 
```

Renombra la ___skills a skills

**PROMPT**
```
Haz el code review del main.py 
```


- Podemos enseñar los agentes y comandos del plugin para hacer desarrollo incremental de mi plugin:
    - Stepwise-dev: Flujo de desarrollo
    - /story-splitting: ¿Es una historia o 3 disfrazdas?
    - /hamburger-method: Corta en capas, genera opciones, elige uno que de feedback rápido
    - /small-safe-steps: Incrementos pequeñños, cada uno desplegable de forma independiente



## Bloque 2: Tu ticket, tu repo (1h)

- Cada persona trabaja su propio ticket.
- El objectivo no es terminar el ticket entero.
- El objetivo es aprender a usar y configurar Claude Code con código real vuestro.
- Al principio ireis inseguros y lentos, cuando tengáis el repo configurado, iréis volando.

- De forma iterativa id configurando los permisos que os hacen falta para el ticket.
- Si CC no se comporta como esperáis añadid el comportamiento correcto al CLAUDE.md o a las Rules
- Si escribis el mismo prompt más de 2 veces: Sacadlo a una Skill...
- Mirad como se va llenando el contexto.
- Añadid hooks por ejemplo para el linter...

---

## Bloque 3: Retro (20 min)

- ¿Qué ha funcionado mejor de lo esperado?
- ¿Qué os ha costado más?
- Patrones comunes
- Siguientes pasos como equipo (CLAUDE.md, hooks, forma de compartir aprendizajes)

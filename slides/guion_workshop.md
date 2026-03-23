# WORKSHOP: Desarrollo guiado por IA (2h)

## Objetivo del workshop

Aprender las bases para desarrollar con IA y no morir en el intento.
---

## Prerequisitos

- Claude Code instalado y configurado con Bedrock.
- Haber ejecutado al menos una vez `claude` en terminal
- Traer un ticket pequeño/mediano del equipo

### Verificación de entorno (primeros 5 min)

Antes de empezar, todos ejecutan:

```bash
claude --version
claude "hola, di solo 'listo'"
```
No seguimos hasta que todos tengan Claude Code funcionando.

Para ver el estado completo del entorno en cualquier momento:
```
/doctor
/status
```

---

## Bloque 1: El journey guiado (1h)

### Puente con la charla (5 min)

En la charla vimos 4 problemas concretos. Ahora cada uno tiene una herramienta:

| Problema (charla) | Herramienta (workshop) |
|---|---|
| No tiene contexto → alucinaciones | Memoria (Contexto, CLAUDE.md, Rules.md...) |
| Contexto contaminado → indeterminismo | Separar fases con `/clear` |
| Difícil de verificar | Hooks + Verification Requirements |
| Difícil de revisar | Rewind + checklist pre-merge |

---

### Paso 1: CLAUDE.md — el onboarding del agente (10 min)

Sin CLAUDE.md, el agente empieza cada sesión desde cero. Es como contratar a alguien nuevo cada día.

**Demo en el repo:**
1. Crea un CLAUDE.md mínimo con `/init` como base
2. Borra lo que no sirve — `/init` genera demasiado por defecto. Objetivo: menos de 100 líneas
   - Fuera: duplicar README, listar principios que la IA ya conoce, comandos "por si acaso"
   - Dentro: convenciones propias del proyecto, comandos de verificación
3. La sección más importante es **Verification Requirements**:

```markdown
## Verification Requirements
- Run `npm test` after code changes
- Run `npm run typecheck` before marking complete
- For API changes, test with curl
```

Dale a Claude una forma de verificar su propio trabajo. Sin esto, eres tú quien revisa cada línea.

**Nota sobre la jerarquía de CLAUDE.md:**
- `~/.claude/CLAUDE.md` — aplica a todos tus proyectos (convenciones personales)
- `<raíz-del-proyecto>/CLAUDE.md` — aplica al proyecto completo
- `<subdirectorio>/CLAUDE.md` — aplica solo a ese módulo (útil en monorepos)

---

### Paso 2: Permisos — configura antes de empezar (5 min)

**Demo rápida antes de tocar nada:**
1. Pídele que lea un fichero sensitivo sin permisos → te pregunta
2. Añade el `allow` en `.claude/settings.json` → ya puede sin preguntar
3. Añade un `deny` → bloqueado aunque el usuario lo pida

```json
// .claude/settings.json (nivel proyecto)
{
  "permissions": {
    "allow": ["Read(.env.example)"],
    "deny": ["Read(.env)"]
  }
}
```

**Dónde van los settings:**
- Global: `~/.claude/settings.json` (todos los proyectos)
- Proyecto: `.claude/settings.json` (solo aquí)

Empieza restrictivo. Ve abriendo permisos a medida que ganas confianza.

---

### Paso 3: Hooks — el guardarraíl que se configura una vez (5 min)

Los hooks ejecutan comandos automáticamente en respuesta a acciones del agente. Son el "diseña para supervisar" de la charla hecho realidad.

**Demo: linter automático después de cada edición:**

```json
// .claude/settings.json
{
  "hooks": {
    "PostToolUse": [
      {
        "matcher": "Edit",
        "hooks": [{ "type": "command", "command": "npm run lint --fix" }]
      }
    ]
  }
}
```

A partir de ahora, cada vez que el agente edite un fichero, el linter corre solo. Sin que tengas que pedirlo.

Otros usos útiles: ejecutar tests después de cambios, formatear código, validar que no se rompa el build.

---

### Paso 4: Modelos y tokens — el coste importa (3 min)

Referencia rápida — el detalle está en la hoja impresa al final:

| Modelo | Cuándo usarlo |
|--------|---------------|
| Haiku | Tareas simples: renombrar, formatear, buscar |
| Sonnet | El 80% del trabajo cotidiano |
| Opus | Arquitectura, debugging difícil, decisiones críticas |

**Regla**: empieza con Sonnet. Escribe `/cost` para ver el gasto. Sube a Opus solo si Sonnet no llega.

---

### Paso 5: Las 3 fases en acción (15 min)

Cogemos una tarea del repo demo. El objetivo es ver en vivo por qué separar fases importa.

**Antes de empezar las fases: prompt malo vs bueno (3 min)**

La diferencia entre un prompt vago y uno preciso es la diferencia entre el estudio METR y el resultado que queremos.

```
❌ "Arregla el bug del login"

✅ "En el fichero src/auth/login.ts, la función validateToken()
   devuelve true para tokens expirados cuando el campo exp es null.
   Repara solo esa función. No toques nada más. Los tests están en
   src/auth/__tests__/login.test.ts."
```

La regla: si no puedes explicar en una frase el scope, el fichero y el criterio de éxito, el agente va a adivinar. Y cuando adivina, alucina.

**Fase 1 — Investigar** (sesión limpia):
```
"Analiza el código de [feature X]. Solo quiero entender el estado actual.
No hagas ningún cambio."
```
El agente investiga. Tú lees. Cuando terminas, limpias el contexto con:
```
/clear
```
`/clear` resetea la conversación sin cerrar el proceso — CLAUDE.md y los settings siguen activos.

**Fase 2 — Planificar** (contexto limpio tras `/clear`):
```
"Basándote en lo que encontré [resumen], crea un plan detallado para [tarea].
No implementes nada todavía."
```
Revisas el plan. Corriges lo que no tiene sentido. Si el problema es complejo, prueba:
```
"think harder: ¿qué podría salir mal con este plan?"
```
`think harder` o `think deeply about` fuerzan razonamiento más profundo — útil para decisiones de arquitectura o cuando la respuesta por defecto parece demasiado fácil.

**Fase 3 — Implementar** (nuevo `/clear`):
```
"Implementa exactamente este plan: [plan aprobado]"
```

Cada `/clear` = ventana de contexto limpia = menos alucinaciones.

> **¿Tuviste que parar a mitad?** Retoma con `claude --continue` para reanudar la última sesión, o `claude --resume` para elegir una sesión anterior.

---

### Paso 6: Ver y gestionar el contexto (5 min)

El indicador de tokens aparece en la barra de estado. Aprende a leerlo antes de que sea tarde.

- El porcentaje sube con cada mensaje, fichero añadido y resultado de herramienta
- Cuando supera el 50-60%, la calidad empieza a bajar

**`/compact`** — comprime el historial manteniendo el contexto esencial:
```
/compact
```
Úsalo antes de que el contexto llegue al límite, no después.

⚠️ Ojo con los compacts automáticos: Claude los hace solo cuando no queda espacio. Pueden perder contexto crítico que no has guardado. Si ves que el agente "olvida" algo, puede ser esto.

**Para monorepos** — si necesitas contexto de otro módulo sin abrir una sesión nueva:
```
/add-dir ../otro-servicio
```

---

### Paso 7: Rewind — el seguro de vida (5 min)

Claude se ha desviado. ¿Ahora qué?

**Demo en vivo:**
- Escribe un prompt intencionalmente ambiguo
- Deja que el agente vaya en la dirección equivocada
- `Esc+Esc` o `/rewind` → elige modo:
  - **Conversation only**: mantén cambios en código, revierte el chat
  - **Code only**: mantén conversación, revierte código
  - **Both**: restauración completa

⚠️ **Aviso importante**: rewind NO revierte comandos bash (`rm`, `mv`, scripts). Si quieres reversibilidad total, haz que Claude escriba los scripts en ficheros temporales antes de ejecutarlos — luego los revisas y ejecutas tú.

---

## Bloque 2: Tu ticket, tu repo (1h)

### Briefing (5 min)

Cada persona trabaja con su propio ticket/repo.

**Objetivo**: llevar el ticket de inicio a fin aplicando lo que acabamos de ver.

Checklist antes de empezar (solo dos cosas):
- [ ] ¿Tengo CLAUDE.md con al menos una sección de Verification Requirements?
- [ ] ¿Voy a separar las fases con `/clear` entre ellas?

Lo demás (permisos, hooks) es bonus si el repo lo permite. No te atranques ahí.

> **Para los facilitadores**: organizad las mesas en grupos de 4-5 con al menos una persona por mesa que ya haya usado Claude Code antes. Esa persona es el "mini-facilitador" de la mesa — con 100 personas no llega el soporte centralizado.

Anota qué te funciona y qué no — lo compartiremos en la retro.

> **Expectativa realista**: no intentéis terminar el ticket entero. El objetivo es practicar las fases correctamente, no entregar. Si llegáis al final de la Fase 2 con un plan sólido, habéis ganado.

### Ejercicios de backup (para quien no trae ticket)

Si no tienes ticket propio, elige uno de estos:

**Ejercicio A — Feature simple:**
En el repo demo, añade validación de email a un formulario. Usa las 3 fases (investigar → planificar → implementar) y asegúrate de que los tests pasen antes de dar la tarea por terminada.

**Ejercicio B — Refactoring:**
En el repo demo hay una función que hace demasiadas cosas. Refactorízala en funciones pequeñas con nombres claros. El comportamiento no puede cambiar — tienes los tests como red de seguridad.

**Ejercicio C — Debugging:**
En el repo demo hay un test roto (comentado). Descubre por qué falla, arréglalo con Claude, y documenta en el CLAUDE.md qué aprendiste para que no vuelva a pasar.

---

## Bloque 3: Retro (20 min)

### ¿Qué ha funcionado mejor de lo esperado? (5 min)
2 minutos por mesa para consensuar una respuesta. Luego 3-4 mesas comparten en voz alta. No ronda completa — con 100 personas son 100 minutos.

### ¿Qué ha costado más de lo esperado? (5 min)
Mismo formato: 2 min por mesa, 3-4 mesas comparten. Fricciones reales, no teóricas.

### Patrones comunes (5 min)
El facilitador recoge y sintetiza. ¿Coinciden con los 4 problemas de la charla?

### Siguientes pasos como equipo (5 min)
- ¿Qué CLAUDE.md necesitáis en vuestro repo principal?
- ¿Qué hooks tiene sentido activar ya?
- ¿Cómo compartís lo que vais aprendiendo? (canal de Slack, wiki, reunión quincenal)
- **El siguiente nivel**: una vez domináis CLAUDE.md y las fases, el siguiente paso son las **Skills** (conocimiento empaquetado que se activa bajo demanda con `/nombre`) y los **subagentes** para tareas especializadas. No para hoy — pero ya sabéis por dónde crecer.

---

## Material de referencia rápida

> 💡 **Imprimir esta sección en A4 y repartirla físicamente** reduce la fricción de "¿cuál era el comando?" cuando todo el mundo tiene la pantalla ocupada con Claude Code.

### Comandos de sesión
| Comando | Para qué |
|---------|----------|
| `/clear` | Resetear conversación manteniendo CLAUDE.md y settings |
| `/compact` | Comprimir contexto sin perder el hilo |
| `/rewind` | Deshacer cambios del agente |
| `Esc+Esc` | Rewind rápido |
| `/cost` | Ver gasto acumulado en la sesión |
| `/status` | Modelo activo, tokens usados, permisos |
| `/doctor` | Verificar instalación y entorno |
| `/add-dir <ruta>` | Añadir directorio al contexto (monorepos) |

### Flags de arranque
| Flag | Para qué |
|------|----------|
| `--model <modelo>` | Elegir modelo al iniciar |
| `--continue` | Reanudar la última sesión |
| `--resume` | Elegir sesión anterior para reanudar |

### Señales de que algo va mal
- El agente lleva más de 5 pasos sin preguntar → interrumpe
- El contexto supera el 60% → `/compact` o sesión nueva con `/clear`
- El código "suena bien" pero no entiendes qué hace → para y revisa
- El agente modifica cosas fuera del scope → rewind inmediato
- El agente "olvidó" algo que dijiste antes → compact automático, recupera el contexto
- El agente ejecutó un bash destructivo (`rm`, `mv`, migración) que no puedes revertir → la próxima vez, pídele que escriba el script en un fichero temporal antes de ejecutarlo

### La regla de oro
Si no puedes explicar en una frase qué tiene que hacer el agente, el agente tampoco lo va a saber.

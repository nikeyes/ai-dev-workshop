


# Descubriendo mejores formas de desarrollar

- Charla para 100 desarrolladores. 
- 20-30 minutos

---

Hacer in menti con preguntas para ver tipo: (PENSAR PREGUNTAS)
- ¿ Cada cuánto usáis la IA para desarrollar?
- ¿Qué herramientas de IA usáis para desarrollar?
- ¿Cuántas Skills o Agentes tenéis configurados en vuestra IA favorita?


---

### SLIDE 1 - Portada 

**Título:** Descubriendo mejores formas de desarrollar
**Subtítulo:** ¿otra vez?

**Notas **
Presentación rápida. No vengo a hablar de si "la IA es increíble" o si es basura "la IA es basura". Vengo a hablar sobre lo que sí funciona y lo que no. Pero sobre todo lo que necesitáis cambiar como desarrolladores para que funcione de verdad.

---

### SLIDE 2 - El Manifiesto Ágil como punto de partida

**Título:** "We are uncovering better ways of developing software"
**Subtítulo:** — Manifiesto Ágil, 2001

**Contenido:** 
- Imagen de la web del Manifiesto ágil: https://agilemanifesto.org/
- La frase no dice "we have uncovered". Dice "we ARE uncovering". Presente continuo. Un proceso que no termina.


**Notas**
¿Conocéis esta web horrible y este manifiesto?. 
Es el Manifiesto Ágil. 
Y fijaros que no dice 'hemos descubierto'. Dice 'estamos descubriendo'. 
Es un proceso que nunca se acaba.

"Llevamos décadas descubriendo mejores formas de hacer software. De waterfall a iterativo, Agile, Lean, XP.. Continuous Delivery, DevOps... Cada salto nos obligó a mejorar y cambiar nuestra forma de trabajar.

"La IA es la siguiente iteración. No es una revolución que reemplaza todo lo anterior. Es una capa nueva sobre fundamentos que ya sabemos que funcionan.
Y como siempre, lo que marca la diferencia no es la herramienta. Es entender lo que cambia y lo que permanece."

---

### SLIDE 3 - El estudio METR: la ducha fría 

**Título:** 19% más lentos (sí, más LENTOS)
**Contenido:**
- Estudio controlado: 16 desarrolladores experimentados, 246 tareas reales
- Herramientas de vanguardia: Cursor Pro + Claude Sonnet
- Resultado: con IA, tardaron un 19% MÁS
- Lo más inquietante: ellos creían haber ido un 20% más rápido

**Fuente:** METR, julio 2025 — actualización febrero 2026 muestra indicios de mejora
- **Estudio original (julio 2025):** [https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/](https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/
- **Actualización (febrero 2026):** [https://metr.org/blog/2026-02-24-uplift-update/](https://metr.org/blog/2026-02-24-uplift-update/)
- El paper completo en ArXiv: [https://arxiv.org/abs/2507.09089](https://arxiv.org/abs/2507.09089)

**Notas **
Principio de 2025: "16 seniors con una media de 5 años trabajando en sus repos. Tareas reales. Las mejores herramientas del momento. Y fueron un 19% más lentos."

"Pero lo fascinante es que ellos mismos creían haber ido un 20% más rápido. 
La IA genera el código muy rápido y nos da la sensación de velocidad. 
Pero en el estudio se pasaban el tiempo revisando output, limpiando alucinaciones, cambiando entre 'modo programar' y 'modo promptear'."

"Ojo: esto es de principios de 2025. Las herramientas han evolucionado muy rápido y METR ya observa mejoras en 2026. 
La clave no es si la IA ayuda o no. Es que cómo la usas y la configuras para que te ayude.

En mi experiencia hay un patrón hacia el fracaso: usar prompts vagos, no trabajar el contexto del proyecto o la tarea, no usar un flujo iterativo de desarrollo, no tener revisiones humanas para arquitectura o partes core del sistema. 
Si sigues esos malos hábitos, desarrollas a la velocidad de la luz velocidad. Pero en la novena o décima iteración te darás cuenta de que también has obtenido  deuda a la velocidad de la luz.


---

### SLIDE 4 - Los 4 problemas de programar con IA 

**Título:** Lo que la IA hace mal
**Contenido (4 bloques):**

1. **Falta de contexto** — Al empezar cada sesión, la IA no sabe nada de tu base de código. Cero.
2. **Alucinaciones** — Inventa APIs, métodos, dependencias que no existen. Y te lo dice convencida.
3. **Indeterminismo** — El mismo prompt puede dar resultados diferentes cada vez.
4. **Dificultad para verificar** — Generamos código más rápido de lo que nuestra carga cognitiva permite revisar.

**Notas**
Está en vuestra mano crear los mecanismos para minimizar estos problemas.

Tened en cuenta que generáis código mucho más rápido de lo que vuestro cerebro puede procesar. Si no implementáis los mecanismo para que ese código se comporten como queréis, tendréis muchos problemas

Porque ojo, la IA no está bajando la calidad de vuestro código. Está amplificando vuestra falta de rigor y vuestra malas prácticas.
Si antes no testeabais todos los posibles caminos de error, ahora generáis diez veces más caminos de error sin testear...


---

### SLIDE 5 - Sin IA, ya seguíamos un flujo de desarrollo 

**Título:** Investigar → Planificar → Implementar → Validar
**Contenido visual:** 
- Pipeline con cuatro fases. Una X roja sobre un atajo que las colapsa todas.
- Compactación automática: cuidado, no controlas qué se queda y qué se va
- La precisión de llamar a tools se degrada exponencialmente en una sesión

**Notas**
"Si dejas que la IA junte la investigación, la planificación y la implementación en una sola sesión de 'vibe coding', sacrificas la coherencia por la velocidad."

"La ventana de contexto no es infinita. Un solo MCP de GitHub mete 50.000 tokens de JSON en la memoria del modelo antes de que hagas nada. Si encadenas cinco herramientas al 90% de acierto cada una, tu probabilidad total es del 59%."

"Gestiona el contexto de forma agresiva. Menos ruido, más relevancia. El modelo es más inteligente cuando le das menos información pero más precisa."


### SLIDE 6 - Ya conocemos las practicas que funcionan 
**Título:** 
**Contenido visual:** 

**El cuello de botella real:**
El cuello de botella nunca ha sido el número de líneas por minuto. Siempre ha sido el ciclo de feedback: verificar que lo que hacemos es correcto y es lo que teníamos que hacer.
Para eso ya sabemos algunas prácticas que funcionan:

- Story Splitting
- Hamburger methid
- Small Safe Steps
- Testing avanzazo: Mutant testing, Acceptance Testings, Architectural Testing

** Notas:**
Esto con IA es aún más importante. La tentación es generar un PR gigante de una sentada. Resistidla. Que el agente genere mucho código no significa que debáis desplegarlo todo junto.

Recordad: el cuello de botella nunca ha sido las líneas por minuto. Siempre ha sido el ciclo de feedback.


### SLIDE 7 - Diseña para supervisión

**Título:** No puedes revisar cada línea. Diseña sistemas que capturen errores.
**Contenido:**

**Guardarraíles técnicos además de los habituales**
- Hooks: linter automático en cada tool use
- Tests de arquitectura: verifican estructura, no solo funcionalidad
- Aceptance Testing.
- CI/CD maduro: si no es fiable con humanos, será un desastre con agentes
- Permisos configurados: qué puede hacer la IA sin aprobación y qué no

**Checklist de verificación cuando hay IA:**
- ¿Respeta el dominio o es código plausible?
- ¿Los tests validan invariantes reales?
- ¿Hay observabilidad y límites operativos?
- ¿Puedo borrarlo sin romper el sistema?

**Evaluación de riesgo por cambio (Birgitta Böckeler / Thoughtworks):**

| Probabilidad de error | Impacto del error | Detectabilidad | → Nivel de revisión |
|---|---|---|---|
| Baja | Bajo | Alta (tests, CI) | "Vibe coding" sin miedo |
| Alta | Alto | Baja (sin tests) | Revisión exhaustiva |

**Notas**
"Tu rol pasa de programador a supervisor de sistemas de producción. No podéis revisar cada línea. Necesitáis sistemas que capturen errores."

"Un hook que ejecuta el linter en cada modificación le da feedback inmediato al modelo. Tests de arquitectura que verifican que la estructura se respeta. Permisos que impidan que la IA haga un `push` a main sin aprobación. Permisos que impidan borrar la Infra....

"Y cuando hay IA generando código, añadid estas preguntas a vuestra revisión: 
¿esto respeta mi dominio o solo suena bien? 
¿Los tests prueban algo real?
¿Hay observabilidad?
¿Podría borrar este código sin romper nada?




### SLIDE 8 - Ajusta el rigor a la fase del producto

**Título:** No todo necesita el mismo rigor. Pero con IA, siempre verifica.
**Contenido:**

**Framework Explore / Expand / Extract:**

| Fase | Prioriza | Tolera | Nivel de rigor |
|---|---|---|---|
| **Explore** | Velocidad y aprendizaje | Deuda consciente | Tests funcionales básicos, validar hipótesis rápido |
| **Expand** | Escala y observabilidad | Estética irrelevante | Tests de integración, monitoring, contratos API |
| **Extract** | Sostenibilidad y seguridad | Cero hacks sin plan | Mutation testing, tests de arquitectura, security scans |

** Notas**
"No todo necesita el mismo nivel de rigor. Y eso está bien. Pero necesitáis un criterio para decidir cuánto."

"En fase de exploración, priorizáis velocidad. Estáis aprendiendo, validando hipótesis. Podéis tolerar deuda consciente . La palabra clave es 'consciente'. Tests funcionales básicos y adelante."

"En fase de expansión, ya tenéis usuarios. Ahora importa la escala y la observabilidad. Tests de integración, monitoring, contratos de API."

"En fase de extracción, estáis protegiendo el core del negocio. Aquí es mutation testing, tests de arquitectura, security scans. Cero hacks sin plan."


### SLIDE 9 y 10— Lo que cambia y Lo que permanece

**Título:** ¿Qué cambia y qué permanece?

**Cambia tu rol:**
- ❌ Ya no te pagan por escribir código
- ❌ Tampoco por usar IA
- ✅ Te pagan por decidir qué NO debe entrar en producción
- ✅ Te pagan por proteger el sistema

**Cambia:**
- La herramienta de escritura de código
- La velocidad de generación
- La barrera económica del testing riguroso
- El formato de la documentación (CLAUDE.md, skills)
- Quién escribe el código (humano vs. agente)

**Permanece y cobra más relevancia:**
- El problema siempre ha sido integrarla y mantenerla a lo largo del tiempo
- Desarrollo iterativo en pasos pequeños y seguros
- Definir comportamiento esperado antes de implementar
- Ciclo de feedback como cuello de botella real
- Arquitectura y diseño simple
- Ajustar el rigor al contexto, no buscar perfección.
- Trabajo en equipo y comunicación clara
- "We are uncovering better ways of developing software"

**🎤 Notas de orador:**
"Cambian las herramientas. Cambia la velocidad. Cambia quién escribe el código. Pero lo que permanece es lo mismo de siempre: desarrollo iterativo, definir qué esperas antes de construir, el ciclo de feedback como cuello de botella real, y pensar la arquitectura antes de acelerar."

"El Manifiesto Ágil sigue vigente. No porque sea sagrado, sino porque captura algo atemporal: estamos siempre descubriendo mejores formas. La IA es la forma nueva. Los principios son los de siempre."




# PARA EL WORKSHOP
---

- Cada persona trae un ticket pequeño/mediano de su equipo.
- Configurar Claude Code (en Wallbox, tendremos un script o similar, lo estoy hablando con ellos)
- Claude.md
- skills.
- agents 




### SLIDE 13 — Lo que sí poner en CLAUDE.md

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


### SLIDE 12 — De CLAUDE.md a Skills: experiencia codificada

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


---



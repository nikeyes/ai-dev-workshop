


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

**Título:** No puedes revisar cada línea de código. Diseña sistemas que capturen errores.
**Contenido:**

**Guardarraíles técnicos además de los habituales**
- Hooks: linter automático en cada tool use
- Testing avanzado: 
    - Tests de arquitectura: verifican estructura, no solo funcionalidad
    - Aceptance Testing: 
- CI/CD maduros y estables: si no es fiable con humanos, será un desastre con agentes
- Configuración de permisos del agente: ¿Qué puede hacer la IA sin aprobación y qué no?

**Checklist de verificación cuando hay IA:**
- ¿Esto respeta mi dominio o solo suena bien? 
- ¿Los tests prueban algo real?
- ¿Hay observabilidad de ese caso de uso?
- ¿Podría borrar este código sin romper nada?

**Notas**
"Tu rol pasa de programador a supervisor de sistemas de producción. No podéis revisar cada línea. Necesitáis sistemas que capturen errores."

"Un hook que ejecuta el linter en cada modificación le da feedback inmediato al modelo. Tests de arquitectura que verifican que la estructura se respeta. Permisos que impidan que la IA haga un `push` a main sin aprobación. Permisos que impidan borrar la Infra....


### SLIDE 8 - Diseña para supervisión

**Título:** ¿Qué nivel de autonomía tiene que tener la IA?
**Contenido:**

| ¿Qué estás tocando? | ¿Qué pasa si falla? | Autonomía humano/IA | Antes de mergear... |
|---|---|---|---|
| **Un prototipo interno** | Perdemos tiempo | 🟢 **Tu diseñas, la AI implementa, no te preocupas del código** | Tests unitários y de integración. A Main directo. |
| **Un producto con usuarios** | Un usuario tiene un problema | 🟡 **Tu diseñas, la AI implementa, tú supervisas la arquitectura** | Tests de arquitectura, Tests de aceptación, Observabilidad, PR con review como mínimo de IA |
| **El core del negocio** | Perdemos dinero o confianza | 🟠 **Tu diseñas, la AI implementa, tú supervisas la arquitecura y el código de los módulos críticos** | Mutation testing, security scan, PR con review humano |
| **Algo que toca el mundo físico** | Alguien puede sufrir un daño real | 🔴 **Tú decides y supervisas a bajo nivel, la IA solo asiste** | Tests con el hardware real, revisión de seguridad obligatoria |

**Ejemplo:** ¿Auth, pagos, datos personales, energía o comunicación con el cargador? Trátalo siempre como core del negocio.Si afecta al mundo físico, sube al último nivel.


**Notas**
"Y cuando hay IA generando código, ¿qué nivel de autonomía le damos? La tabla


### SLIDE 9 y 10— Lo que cambia y Lo que permanece

**Título:** ¿Qué cambia y qué permanece?

**Cambia tu rol:**
- ❌ Ya no te pagan por escribir código
- ❌ Tampoco por usar IA
- ✅ Te pagan por decidir qué NO debe entrar en producción
- ✅ Te pagan por proteger el sistema

**Cambia el entorno:**
- La herramienta de escritura de código
- La velocidad de generación
- La barrera económica del testing riguroso
- El formato de la documentación (CLAUDE.md, skills)
- Quién escribe el código (humano vs. agente)

**Permanece y cobra más relevancia:**
- El problema siempre ha sido integrar y mantener a lo largo del tiempo
- Desarrollo iterativo en pasos pequeños y seguros
- Definir comportamiento esperado antes de implementar
- Ciclo de feedback como cuello de botella real
- Arquitectura y diseño simple
- Ajustar el nivel de autonomía al contexto, no buscar perfección.
- Trabajo en equipo y comunicación clara
- "We are uncovering better ways of developing software"

**🎤 Notas de orador:**
"Cambian las herramientas. Cambia la velocidad. Cambia quién escribe el código. Pero lo que permanece es lo mismo de siempre: desarrollo iterativo, definir qué esperas antes de construir, el ciclo de feedback como cuello de botella real, y pensar la arquitectura antes de acelerar."

"El Manifiesto Ágil sigue vigente. No porque sea sagrado, sino porque captura algo atemporal: estamos siempre descubriendo mejores formas. La IA es la forma nueva. Los principios son los de siempre."





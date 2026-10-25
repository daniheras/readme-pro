<div align="center">
  <img src="assets/banner.svg" width="600" alt="readme-pro">

  <p><strong>Skills de OpenCode para montar READMEs de puta madre.</strong><br>
  Tres niveles de intensidad, un router que sabe qué le toca a cada proyecto,
  y cero plantillas maximalistas pegadas con escupe.</p>

  <p>
    <a href="LICENSE"><img alt="license MIT" src="https://img.shields.io/badge/license-MIT-3F3F3F?style=flat-square"></a>
    <img alt="4 skills" src="https://img.shields.io/badge/skills-4-3F3F3F?style=flat-square">
    <img alt="made for OpenCode" src="https://img.shields.io/badge/made_for-OpenCode-D71921?style=flat-square">
    <img alt="evals: 60/60 con skill" src="https://img.shields.io/badge/evals-60%2F60_con_skill-D71921?style=flat-square">
  </p>

  <img src="assets/levels.svg" width="640" alt="Los tres niveles de intensidad: LOW, MEDIUM, HIGH">
</div>

<p align="center">
  <a href="#por-qu%C3%A9">Por qué</a> &#183; <a href="#las-cuatro-skills">Skills</a> &#183; <a href="#tres-filosof%C3%ADas-una-regla">Filosofías</a> &#183; <a href="#instalar">Instalar</a> &#183; <a href="#uso">Uso</a> &#183; <a href="#evals">Evals</a> &#183; <a href="#fuentes">Fuentes</a>
</p>

## Por qué

Porque no: no todos los proyectos necesitan un GIF hero ni una fila de
quince badges. Un parser de JSON con banner parece un creador de contenido,
y un tema de terminal sin GIF demo es casi un delito. La gracia no es
decorar todo — es saber leer cada repo y darle la intensidad que merece.

## Las cuatro skills

| ID | Cuándo se carga | Qué te deja |
|---|---|---|
| `readme-pro` | Cualquier tarea de README, por defecto | Evalúa el proyecto, elige nivel y enruta a la receta que toca |
| `readme-pro-low` | Algo simple/limpio/sobrio; librerías, CLIs, herramientas internas | README documentación-primero: sin badges, sin imágenes, sin marketing |
| `readme-pro-medium` | README profesional/estándar; apps y tools con público | Puerta de entrada: pitch, badges que informan, screenshot si hay UI, install, usage, config |
| `readme-pro-high` | Cuando el look ES el producto: UIs, TUIs, temas, dotfiles — o *«que la portada luzca»* | Escaparate: banner, badge row, hero, nav, galería, extras de comunidad |

## Tres filosofías, una regla

- **LOW (escuela Yegor)** — el README se lee, no se mira. Cada línea informa o sobra.
- **MEDIUM (makeareadme / thoughtbot)** — la puerta de entrada. Qué y por qué en una pantalla, install funcionando en dos.
- **HIGH (doomemacs / sniffnet)** — el README es parte de la experiencia del producto. Identidad primero: la paleta sale del propio proyecto, no de un shield azul genérico.

La regla que comparten los tres niveles: **no fabricar nada**. Ni badge de
CI que no existe, ni badge de licencia sin fichero LICENSE, ni screenshots
de features que no corren — y ni un mock de HTML colado como screenshot. Un
README que miente lo pillas en el primer clone.

## El tono

¿Y que este README vaya con tacos mientras las skills escriben READMEs
sobrios? No es hipocresía, es exactamente el principio de la skill: el tono
lo pone el proyecto, no la plantilla.

**Cero dependencias:** funciona en cualquier SO sin instalar nada previo —
escritura, SVG hechos a mano y servicios web. ImageMagick o vhs son mejoras
opcionales: la skill los detecta y solo los usa si ya están.

## Instalar

En un proyecto — copia las skills que quieras:

```sh
cp -r readme-pro/.opencode/skills/readme-pro* tu-repo/.opencode/skills/
```

Global: lo mismo pero a `~/.config/opencode/skills/`. O apunta tu
`opencode.jsonc` a este repo:

```jsonc
{
  "$schema": "https://opencode.ai/config.json",
  "skills": ["~/Work/readme-pro/.opencode/skills"]
}
```

## Uso

- *«escríbeme un readme para este proyecto»* → `readme-pro` evalúa y enruta.
- *«déjalo mínimo, sin badges»* → `readme-pro-low` directo.
- *«quiero que la portada luzca»* → `readme-pro-high`.

El router dice en una línea qué nivel ha elegido y por qué, y la receta pasa
su checklist antes de darte el README por bueno.

## Evals

Tests con fixtures reales en [`evals/`](evals/), metodología skill-creator:
mismos prompts con skill y sin ella, grading programático + revisión humana,
dos iteraciones.

| | con skill | baseline (media, 4 runs) |
|---|---|---|
| assertions | **60/60** | 73% |

El caso que lo dice todo: un baseline, con el mismo prompt, renderizó mocks
de HTML y los presentó como screenshots reales. Con skill, el agente generó
capturas de verdad, encontró un bug, borró los assets a medio hacer y lo
flaggeó — y con la máquina bloqueada (sin poder instalar nada) entregó el
showcase completo con SVGs escritos a mano.

Lo que produce `readme-pro-high`, en vivo:
[`examples/graphite-theme/`](examples/graphite-theme/) — un README showcase
completo generado en la eval, con banner, paleta y extras de comunidad.

## Fuentes

Toda la skill es una destilación de una lista de estudio curada:
[Make a README](https://www.makeareadme.com/),
[The Art of README](https://github.com/hacktivistto/The-Art-of-README),
[la guía de thoughtbot](https://thoughtbot.com/blog/how-to-write-a-great-readme),
[README-Driven Development](https://tom.preston-werner.com/2010/08/23/readme-driven-development.html),
[Elegant READMEs](https://www.yegor256.com/2019/04/23/elegant-readme.html),
[ARCHITECTURE.md](https://matklad.github.io/2021/02/06/ARCHITECTURE.md.html),
[awesome-readme](https://github.com/matiassingers/awesome-readme) — y para el
escaparate, [vhs](https://github.com/charmbracelet/vhs) y
[shields.io](https://shields.io/). La lista anotada completa:
[`.opencode/skills/readme-pro-high/references/examples.md`](.opencode/skills/readme-pro-high/references/examples.md).

## Licencia

[MIT](LICENSE)

---

<div align="center">
  <sub><strong>readme-pro</strong> — este README lo construyó
  <code>readme-pro-high</code> sobre sí mismo. Si te gusta la portada, esto
  es la demo.</sub>
</div>

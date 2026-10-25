# readme-pro

Skills de OpenCode para montar READMEs de puta madre. Tres niveles de
intensidad, un router que sabe qué le toca a cada proyecto, y cero plantillas
maximalistas pegadas con escupe.

Porque no: no todos los proyectos necesitan un GIF hero ni una fila de
quince badges. Un parser de JSON con banner parece un creador de contenido,
y un tema de terminal sin GIF demo es casi un delito. La gracia no es
decorar todo — es saber leer cada repo y darle la intensidad que merece.

## Las cuatro skills

| ID | Cuándo se carga | Qué te deja |
|---|---|---|
| `readme-pro` | Cualquier tarea de README, por defecto | Evalúa el proyecto, elige nivel y enruta a la receta que toca |
| `readme-pro-low` | Quieres algo simple/limpio/sobrio; librerías, CLIs, herramientas internas | README documentación-primero: sin badges, sin imágenes, sin marketing |
| `readme-pro-medium` | Quieres un README profesional/estándar; apps y tools con público | README puerta de entrada: pitch, badges que informan, screenshot si hay UI, install, usage, configuración |
| `readme-pro-high` | Cuando el look ES el producto: UIs, TUIs, temas, dotfiles — o peticiones "que quede chulo" | README escaparate: banner, fila de badges, GIF hero, TOC, galería, extras de comunidad |

Las tres filosofías que codifican:

- **LOW (escuela Yegor)** — el README se lee, no se mira. Cada línea informa o sobra.
- **MEDIUM (makeareadme / thoughtbot)** — el README es la puerta de entrada. Qué y por qué en una pantalla, install funcionando en dos.
- **HIGH (doomemacs / sniffnet)** — el README es parte de la experiencia del producto. Identidad primero: la paleta sale del propio proyecto, no de un shield azul genérico.

Regla compartida de los tres niveles: **no fabricar nada**. Ni badge de CI
que no existe, ni badge de licencia sin fichero LICENSE, ni screenshots de
features que no corren. Un README que miente lo pillas en el primer clone.

¿Y que este README vaya con tacos mientras las skills escriben READMEs
sobrios? No es hipocresía, es exactamente el principio de la skill: el tono
lo pone el proyecto, no la plantilla.

## Instalar

**En un proyecto** — copia las carpetas de skills que quieras:

```sh
cp -r readme-pro/.opencode/skills/readme-pro* tu-repo/.opencode/skills/
```

**Global** — lo mismo pero a `~/.config/opencode/skills/`.

**Como fuente** — apunta tu `opencode.jsonc` a este repo:

```jsonc
{
  "$schema": "https://opencode.ai/config.json",
  "skills": ["~/Work/readme-pro/.opencode/skills"]
}
```

## Uso

En cualquier sesión de OpenCode:

- *«escríbeme un readme para este proyecto»* → `readme-pro` evalúa y enruta.
- *«déjalo mínimo, sin badges»* → carga `readme-pro-low` directamente.
- *«quiero que la portada pegue fuerte»* → `readme-pro-high`.

El router dice en una línea qué nivel ha elegido y por qué, y la receta pasa
su checklist antes de darte el README por bueno.

## Evals

Los tests viven en `evals/evals.json` con fixtures pequeños pero reales en
`evals/fixtures/` (un CLI, un tema de Hyprland, una app con un README
vergonzoso que reconstruir). Cubren el routing, la estructura y la regla de
no-fabricar. Los outputs de cada ronda caen en `evals/workspace/`
(gitignoreado).

## Fuentes

Toda la skill es una destilación de una lista de estudio curada:
[Make a README](https://www.makeareadme.com/),
[The Art of README](https://github.com/hacktivistto/The-Art-of-README),
[la guía de thoughtbot](https://thoughtbot.com/blog/how-to-write-a-great-readme),
[README-Driven Development](https://tom.preston-werner.com/2010/08/23/readme-driven-development.html),
[Elegant READMEs](https://www.yegor256.com/2019/04/23/elegant-readme.html),
[ARCHITECTURE.md](https://matklad.github.io/2021/02/06/ARCHITECTURE.md.html),
[awesome-readme](https://github.com/matiassingers/awesome-readme), y para el
escaparate [vhs](https://github.com/charmbracelet/vhs) y
[shields.io](https://shields.io/). La lista anotada completa está en
`.opencode/skills/readme-pro-high/references/examples.md`.

## Licencia

[MIT](LICENSE)

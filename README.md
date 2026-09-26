# Simuladores de reacciones químicas

Cuatro simuladores educativos para el aula de Química de secundaria (CABA / Argentina). Pensados para docentes que quieren trabajar el **nivel submicroscópico** y el **simbólico** sin depender de un laboratorio ni de una conexión permanente a internet.

Autores del material: **Federico Garberi** ([kekule91](https://github.com/kekule91)).  
Contacto: fgarberi91@gmail.com · federico.garberi@bue.edu.ar · Fgarberi91@uba.ar

> **Origen del código.** Exportado desde [Google AI Studio](https://aistudio.google.com/). El balanceador es un **build de producción** (bundle Vite/React minificado + CSS). Los otros tres son HTML+CSS+JS en un solo archivo, listos para abrir en el navegador.

---

## ¿Para quién?

- Docentes de Química / Físico-Química de secundaria (NES–CABA y afines).
- Estudiantes que quieran practicar en casa o en el aula de informática.
- Quien necesite material **offline**: se abre el `index.html` y listo.

No hace falta instalar Node ni compilar nada.

---

## Los cuatro simuladores

| Simulador | Qué enseña | Demo (AI Studio) | Path local |
|---|---|---|---|
| **Balanceador de ecuaciones** | Ajustar coeficientes estequiométricos; ver la conservación de átomos | [balanceador-de-ecuaciones-químicas.ai.studio](https://balanceador-de-ecuaciones-qu-micas.ai.studio/) | `balanceador/` |
| **Velocidad de reacción** | Factores que afectan la cinética (concentración, temperatura, catalizador) con visualización de partículas | [simulador-de-velocidad-de-reacción.ai.studio](https://simulador-de-velocidad-de-reacci-n.ai.studio/) | `velocidad/` |
| **Equilibrio químico** | Dinámica del equilibrio y principio de Le Chatelier (concentración / temperatura) | [simulador-de-equilibrio-químico.ai.studio](https://simulador-de-equilibrio-qu-mico.ai.studio/) | `equilibrio/` |
| **Clasificador de reacciones** | Reconocer tipos de reacción (síntesis, descomposición, desplazamiento, combustión, etc.) | [clasificador-de-reacciones-químicas.ai.studio](https://clasificador-de-reacciones-qu-micas.ai.studio/) | `clasificador/` |

Portal relacionado: [quimica-y-mas-profe-garberi.pages.dev](https://quimica-y-mas-profe-garberi.pages.dev/)

---

## Cómo abrir en local

### Opción rápida (archivo)

Abrí cualquiera de estos archivos en el navegador (doble clic o «Abrir con…»):

- `balanceador/index.html`
- `velocidad/index.html`
- `equilibrio/index.html`
- `clasificador/index.html`

> En el **balanceador**, si el navegador bloquea los módulos ES por `file://`, usá la opción con servidor local (abajo). Los otros tres suelen andar bien abiertos directo.

### Opción con servidor local

Desde la raíz del repo:

```bash
python3 -m http.server 8080
```

Después entrá a:

- http://localhost:8080/balanceador/
- http://localhost:8080/velocidad/
- http://localhost:8080/equilibrio/
- http://localhost:8080/clasificador/

---

## Pedagogía (tres niveles de Johnstone)

Alex Johnstone describió que la química se enseña y se aprende en **tres niveles** que hay que conectar, no mezclar a ciegas:

1. **Macroscópico** — lo que se ve, se toca, se mide en el laboratorio (cambio de color, gas, temperatura).
2. **Submicroscópico** — partículas, choques, reordenamiento de átomos y enlaces.
3. **Simbólico** — fórmulas, ecuaciones, diagramas, gráficos.

Estos simuladores no reemplazan el lab. Sirven para **puentear** el nivel simbólico (ecuaciones, tipos de reacción) con una representación submicroscópica simple, y para ensayar ideas (cinética, Le Chatelier) antes o después del trabajo experimental. No «ensenan solas»: hace falta la guía del docente y, cuando se pueda, la evidencia del laboratorio.

---

## Estructura del repo

```
simuladores-reacciones/
├── balanceador/
│   ├── index.html
│   └── assets/
│       ├── index-CQJLsIZd.js   # bundle de producción (AI Studio / Vite)
│       └── index-JoypX4Sf.css
├── velocidad/index.html
├── equilibrio/index.html
├── clasificador/index.html
├── LICENSE
├── README.md
└── .gitignore
```

---

## Licencia

[MIT](LICENSE) — podés usar, adaptar y compartir en el aula con atribución.

---

## Autor

**Federico Ernesto Garberi** · [@kekule91](https://github.com/kekule91)  
Profesor de Química y Físico-Química (secundaria pública, CABA).  
Mail: fgarberi91@gmail.com · Institucional: federico.garberi@bue.edu.ar

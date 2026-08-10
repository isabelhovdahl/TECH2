# TECH2: Introduction to Programming, Data, and Information Technology

[![License: CC BY-NC-SA 4.0](https://img.shields.io/badge/License-CC%20BY--NC--SA%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by-nc-sa/4.0/)

Course material for part 1 of TECH2 at NHH.

Author: Isabel Hovdahl

Part 1 assumes no previous programming experience. It covers the fundamentals of Python — data types, decisions, loops, and functions — together with the tools you need to work like a programmer: VS Code, version control with git, and reproducible project environments with conda.

## Before you start

Install VS Code, Git, and Miniforge, then confirm everything works using the verification checklist. All the instructions are in the **[installation guides](guides/README.md)**.

## Course overview

Each week has one lecture and one workshop, where the workshop puts that week's lecture into practice.

| Week | Lecture | Workshop | Solutions |
| --- | --- | --- | --- |
| Week 1 | [Course introduction](lectures/00-introduction.pdf) | [Getting started with VS Code](workshops/week01/vscode_slides.pdf) | — |
| Week 2 | [Python basics](lectures/01-python-basics.ipynb) | [Version control with git](workshops/week02/git_slides.pdf) · [Exercises](workshops/week02/exercises.md) | [week02/](workshops/week02/) |
| Week 3 | [Decisions](lectures/02-decisions.ipynb) | [Exercises](workshops/week03/exercises.md) | [week03/](workshops/week03/) |
| Week 4 | [Loops](lectures/03-loops.ipynb) | [Exercises](workshops/week04/exercises.md) | [week04/](workshops/week04/) |
| Week 5 | [Functions](lectures/04-functions.ipynb) | [Exercises](workshops/week05/exercises.md) | [week05/](workshops/week05/) |
| Week 6 | [Python packages](lectures/05-python-packages.ipynb) | [Virtual environments](workshops/week06/conda_slides.pdf) · [Exercises](workshops/week06/exercises.md) | — |

A few things worth knowing:

- **Lecture notebooks open directly in your browser here on GitHub.** Download them to run and edit the code yourself.
- **Slides are linked as PDF.** The original PowerPoint files sit next to them in the same folder if you prefer those.
- **From week 2 onwards, each workshop lives in its own folder with its own git repository.** Create the `.gitignore` for it by copying [gitignore-template.txt](workshops/week02/gitignore-template.txt).

## Assignments

Three mandatory assignments, all of which must be passed to qualify for the exam. Deadlines and submission are on Canvas.

- **[Assignment 1 — Check your installation](assignments/assignment1/test-installation.ipynb)** — run the notebook and submit the report it produces.

## Guides

The [guides/](guides/README.md) folder holds the installation instructions above, plus reference material you can come back to at any point in the course:

- **[Working with conda environments](guides/conda-environments.md)** — a general reference for creating, sharing, and managing conda environments.
- **[AI guidelines for learning to code](guides/ai-guidelines.md)** — how to use AI assistants so they help your learning rather than quietly replace it, and what counts as good practice when you do.

## Getting the material

- **Read it here.** Notebooks, exercise sheets, and guides all render in your browser
  on GitHub — no account and no download needed.
- **Download a single file.** Open the file, then use the download button at the top
  right. This is the usual way to pick up a notebook or an exercise script.
- **Download everything.** Click the green **Code** button at the top of this page,
  then **Download ZIP**.

> 📝 **TECH2 students:** each week's material is linked from Canvas under **Modules**.
> If a week is not linked yet, it may still be changing — wait for the link rather than
> working ahead from here.

The material is updated during the semester, so this repository is always the current
version. Re-download a notebook at the start of the lecture that uses it.

## What comes next

Part 2 of the course covers working with data using `pandas` and `matplotlib`, and is taught by Richard Foltyn. The material lives in a separate repository: [TECH2-H26](https://github.com/richardfoltyn/TECH2-H26).

## Additional resources

1. [SKL401: Introduction to Python](https://isabelhovdahl.github.io/skl401/) — a free, self-paced online seminar I developed at NHH: short videos, each followed by programming problems. It covers the same ground as part 1 and continues into data analysis with `pandas` and `matplotlib`.
2. [Think Python](https://allendowney.github.io/ThinkPython/index.html) by Allen B. Downey — a general introduction to Python; chapters are available as Jupyter notebooks.
3. [Python for Everybody](https://www.py4e.com/book) by Charles R. Severance — an introduction to Python with a focus on data, available as a free PDF.
4. [The Python Tutorial](https://docs.python.org/3/tutorial/) — the official documentation, useful once you want to look something up precisely.
5. [QuantEcon](https://quantecon.org/lectures/) — Python for economics and finance, for beginners through to advanced.

## Reusing this material

You are welcome to use and adapt this material for your own teaching or study, under the terms of the licence below. To take a copy you can keep up to date:

```bash
git clone https://github.com/isabelhovdahl/TECH2.git
```

Run `git pull` in that folder to pick up later changes. If you find the material useful, I would be glad to hear about it.

## Licence

This material is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License](http://creativecommons.org/licenses/by-nc-sa/4.0/). 

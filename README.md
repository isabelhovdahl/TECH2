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
| Week 1 | Course introduction | [Getting started with VS Code](workshops/week01/vscode_slides.pdf) | — |
| Week 2 | [Python basics](lectures/01-python-basics.ipynb) | [Version control with git](workshops/week02/exercises.md) · [slides](workshops/week02/git_slides.pdf) | [week02/](workshops/week02/) |
| Week 3 | [Decisions](lectures/02-decisions.ipynb) | [Exercises](workshops/week03/exercises.md) | [week03/](workshops/week03/) |
| Week 4 | [Loops](lectures/03-loops.ipynb) | [Exercises](workshops/week04/exercises.md) | [week04/](workshops/week04/) |
| Week 5 | [Functions](lectures/04-functions.ipynb) | [Exercises](workshops/week05/exercises.md) | [week05/](workshops/week05/) |
| Week 6 | [Python packages](lectures/05-python-packages.ipynb) | [Virtual environments](workshops/week06/exercises.md) · [slides](workshops/week06/conda_slides.pdf) | — |

A few things worth knowing:

- **Lecture notebooks open directly in your browser here on GitHub.** Download them to run and edit the code yourself.
- **Slides are linked as PDF.** The original PowerPoint files sit next to them in the same folder if you prefer those.
- **From week 2 onwards, each workshop lives in its own folder with its own git repository.** Create the `.gitignore` for it by copying [gitignore-template.txt](workshops/week02/gitignore-template.txt).

## Guides

The [guides/](guides/README.md) folder holds the installation instructions above, plus reference material you can come back to at any point in the course:

- **[Working with conda environments](guides/conda-environments.md)** — a general reference for creating, sharing, and managing conda environments.
- **[AI guidelines for learning to code](guides/ai-guidelines.md)** — how to use AI assistants so they help your learning rather than quietly replace it, and what counts as good practice when you do.

## Getting the material

The material is updated during the semester, so this repository is always the current version. There are three ways to get it:

1. **Read it here.** Notebooks, exercises, and guides all render directly on GitHub — no download needed.
2. **Download single files.** Open a file, then use the download button.
3. **Download everything.** Click the green **Code** button above, then **Download ZIP**.

Once you have covered git in week 2, you can also **clone** the repository, which makes it easy to pick up changes later. Either clone it from the terminal:

```bash
git clone https://github.com/isabelhovdahl/TECH2.git
```

or from inside VS Code: press `Ctrl+Shift+P` (`Cmd+Shift+P` on Mac), run **Git: Clone**, paste the same URL, and choose where to put it. To fetch later changes, run `git pull` in the terminal, or use the sync button in VS Code's Source Control panel.

> ⚠️ **Treat the cloned folder as read-only.** Copy a notebook into your own working folder before you run or edit it — simply running a notebook changes the file. If you edit files inside the clone, `git pull` will stop with a merge conflict, and conflicts inside a notebook are particularly awkward to untangle.

Whichever you choose, pick up the latest version of a notebook at the start of each lecture.

## What comes next

Part 2 of the course covers working with data using `pandas` and `matplotlib`, and is taught by Richard Foltyn. The material lives in a separate repository: [TECH2-H26](https://github.com/richardfoltyn/TECH2-H26).

## Additional resources

1. [SKL401: Introduction to Python](https://isabelhovdahl.github.io/skl401/) — a free, self-paced online seminar I developed at NHH: short videos, each followed by programming problems. It covers the same ground as part 1 and continues into data analysis with `pandas` and `matplotlib`.
2. [Think Python](https://allendowney.github.io/ThinkPython/index.html) by Allen B. Downey — a general introduction to Python; chapters are available as Jupyter notebooks.
3. [Python for Everybody](https://www.py4e.com/book) by Charles R. Severance — an introduction to Python with a focus on data, available as a free PDF.
4. [The Python Tutorial](https://docs.python.org/3/tutorial/) — the official documentation, useful once you want to look something up precisely.
5. [QuantEcon](https://quantecon.org/lectures/) — Python for economics and finance, for beginners through to advanced.

## Licence

This material is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License](http://creativecommons.org/licenses/by-nc-sa/4.0/). You are welcome to use and adapt this material for your own teaching or study, under the terms of the licence. If you find it useful, I would be glad to hear about it.

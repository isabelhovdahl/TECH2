# Working with Conda Environments

A **virtual environment** is an isolated folder containing its own copy of Python and its own set of packages. Each project gets its own environment, so the packages one project needs can never interfere with another project's.

> ⚠️ **Never install packages into the `base` environment.** `base` is the environment conda creates for itself when you install Miniforge. Keep it clean and create a new environment for each project instead.

## Quick reference

| Task | Command |
| --- | --- |
| Check conda is working | `conda --version` |
| List all your environments | `conda env list` |
| Create an environment | `conda create --name my_env python=3.14` |
| Activate an environment | `conda activate my_env` |
| Deactivate (return to `base`) | `conda deactivate` |
| Install a package (into the active environment) | `conda install numpy` |
| List packages in the active environment | `conda list` |
| Check whether one package is installed | `conda list numpy` |
| Check where conda gets packages from | `conda config --show channels` |
| Save an environment to a file | `conda env export --from-history > environment.yml` |
| Create an environment from a file | `conda env create --file environment.yml` |
| Delete an environment | `conda env remove --name my_env` |

## Opening a terminal

All conda commands are typed into a terminal:

- **Windows:** open **Miniforge Prompt** from the Start Menu.
- **Mac:** open **Terminal** from the Applications folder (or via Spotlight search).

You'll know conda is available if the prompt starts with `(base)`. To confirm, run:

```
conda --version
```

## Creating an environment

```
conda create --name my_env python=3.14 numpy
```

This creates an environment called `my_env` containing Python 3.14 and numpy. Breaking down the command:

- `--name my_env` — the name of the environment. Use something descriptive; the project name is usually a good choice.
- `python=3.14` — the Python version. Always include this, otherwise conda decides for you.
- `numpy` — any packages you want installed right away. You can list several, separated by spaces, or none at all.

Conda will show you what it plans to install and ask you to confirm with `y`.

> 📝 **Note:** You can pin a specific version of any package with `=`, e.g. `numpy=2.1`. Pinning matters when a project needs an exact version; otherwise conda installs the newest version that works.

Environments are stored centrally (inside your Miniforge folder), not in your project folder — so it doesn't matter which folder you are in when you create one.

## Activating and deactivating

Creating an environment does not start using it. To activate it:

```
conda activate my_env
```

Your prompt changes from `(base)` to `(my_env)`, telling you which environment is currently active. Any package you install now goes into `my_env`.

To leave the environment and return to `base`:

```
conda deactivate
```

## Installing packages

With the environment activated:

```
conda install pandas matplotlib
```

To check what's installed in the active environment:

```
conda list
```

Or check a single package (the output is empty if it isn't installed):

```
conda list pandas
```

## Using an environment in VS Code

Creating an environment in the terminal is only half the job — you also need to tell VS Code to use it.

**For Python scripts (`.py`):**

1. Open your project folder in VS Code.
2. Press `Ctrl+Shift+P` (Windows) or `Cmd+Shift+P` (Mac) to open the Command Palette.
3. Type **Python: Select Interpreter** and press Enter.
4. Choose your environment from the list — it appears as `Python 3.14 ('my_env')`.

The selected environment is shown in the status bar at the bottom of the window. 

**For notebooks (`.ipynb`):**

1. Open the notebook.
2. Click **Select Kernel** in the top-right corner.
3. Choose **Python Environments...**, then pick your environment.

Notebooks additionally need the `ipykernel` package in the environment. If it's missing, VS Code offers to install it for you — accept, or install it yourself with `conda install ipykernel`.

## Saving an environment to a file

To let someone else (or your future self) recreate an environment exactly, export it to an `environment.yml` file.

1. Activate the environment you want to export:

   ```
   conda activate my_env
   ```

2. Navigate to the folder where you want to save the file:

   ```
   cd <path-to-your-project-folder>
   ```

3. Export it:

   ```
   conda env export --from-history > environment.yml
   ```

The resulting file lists the environment's name, its channels, and the packages you asked for. It's a small text file — open it in VS Code and read it.

> 💡 **Tip:** Use `--from-history`. Without it, conda exports *every* package in the environment, including ones that were installed automatically as dependencies, pinned to versions that may only exist on your operating system. That makes the file long and often unusable on a different computer.

> ⚠️ **Warning:** `--from-history` only records packages installed with `conda`. If you installed anything with `pip` (see below), you'll need to add it to the file by hand.

## Creating an environment from a file

Given an `environment.yml` file, anyone can rebuild the same environment:

1. Navigate to the folder containing the file:

   ```
   cd <path-to-folder>
   ```

2. Create the environment:

   ```
   conda env create --file environment.yml
   ```

The environment's name comes from inside the file, so you don't specify it. Check that it worked with `conda env list`, then activate it as usual.

You can also create an environment directly from a file published online, without downloading it first:

```
conda env create --file https://example.com/path/to/environment.yml
```

## Deleting an environment

Environments take up disk space, so it's worth removing ones you no longer use. You can't delete an environment while it's active, so deactivate first:

```
conda deactivate
conda env remove --name my_env
```

Confirm it's gone with `conda env list`.

## conda vs. pip

`conda` is not the only way to install Python packages — Python's own package installer, `pip`, is also available inside every conda environment:

```
pip install some-package
```

Both work, but they aren't interchangeable:

- **Prefer `conda`.** It checks that all your packages are compatible with each other before installing anything, which prevents a lot of broken environments.
- **Use `pip` when conda can't help.** Some packages aren't distributed through conda channels at all, and brand-new releases usually appear on PyPI (pip's repository) before conda-forge.
- **Install conda packages first, then pip packages.** Installing with conda after pip can overwrite what pip did.

> 📝 **Note:** Miniforge already uses **[conda-forge](https://conda-forge.org)** as its default channel, so you don't need to configure channels yourself. Conda-forge is a large, community-maintained package repository. To check, run `conda config --show channels` — it should list `conda-forge` and nothing else.

## Troubleshooting

**`conda: command not found` or `'conda' is not recognized`**

**Windows:** conda is only set up in the **Miniforge Prompt** by default — use that rather than Command Prompt or PowerShell.

VS Code's integrated terminal usually works too, but only *after* you have selected a conda environment as the interpreter for that folder (see [Using an environment in VS Code](#using-an-environment-in-vs-code)) — VS Code then activates it for you in each new terminal. If conda isn't recognized there, fall back to the Miniforge Prompt.

**Mac:** you probably answered "no" (or just pressed Enter) when the installer asked whether to initialize conda. Run the following in Terminal, then close the window and open a new one:

```
~/miniforge3/bin/conda init zsh
```

Your prompt should now start with `(base)`, and `conda --version` should work.

**`conda config --show channels` lists something other than `conda-forge`**
First check that you are actually using Miniforge: run `conda info --base` and confirm that the path contains `miniforge3`. If it doesn't, conda is coming from another installation (such as Anaconda or Miniconda) — changing channels won't fix that, so ask for help instead.

If the path *does* contain `miniforge3`, make conda-forge your only channel:

```
conda config --add channels conda-forge
```

```
conda config --remove channels defaults
```

Run `conda config --show channels` again to confirm.

**Conda takes a very long time, or fails with a message about conflicts**
Conda is trying to find a combination of package versions that work together, and there may not be one. Try pinning fewer versions — for example, ask for `numpy` rather than `numpy=1.21`.

**`PackagesNotFoundError`**
The package isn't available on conda-forge under that name. Check the spelling, then try installing it with `pip` instead.

**A package is installed, but Python says `ModuleNotFoundError`**
The package is probably installed in a different environment than the one that's running your code. Check which environment is active in your terminal (the `(name)` prefix), and check which interpreter VS Code has selected in the status bar.

**I don't know which environment I'm in**
Run `conda env list` — the active one is marked with an asterisk `*`.

## Best practices

- **One environment per project.** Keeps dependencies isolated and makes each project reproducible.
- **Never install into `base`.** Keep your base installation clean.
- **Use descriptive names**, usually matching the project name.
- **Pin versions for packages that matter** to the project, so it keeps working later.
- **Export an `environment.yml`** and keep it alongside your project code, so others can rebuild it.
- **Delete environments you no longer use.**

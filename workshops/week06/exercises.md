# Week 6 — Workshop: Virtual Environments

This week's workshop is different from the previous ones: there are no Python programs to write, and no git repository to create. Almost everything happens in the terminal.

The commands you need are written out below — copy and paste them rather than typing them by hand. For the general explanation of what each command does (and the options we don't use today), see the **[conda environments guide](../../guides/conda-environments.md)**, which is a reference you can consult at any point in the course.

---

## Before you start

Open a terminal — **Miniforge Prompt** on Windows, **Terminal** on Mac. Your prompt should start with `(base)`. On a Mac, if it doesn't and `conda` isn't recognized, see the [troubleshooting section](../../guides/conda-environments.md#troubleshooting) of the guide.

Run these commands to check that everything is working:

```
conda --version
```

```
conda env list
```

```
conda list
```

The last command lists what's installed in your `base` environment. Among the packages, you should see `numpy`, `matplotlib` and `sympy` — the three packages we installed in the lecture.

Finally, check where conda gets its packages from:

```
conda config --show channels
```

You should see `conda-forge` and nothing else. [conda-forge](https://conda-forge.org) is a large, community-maintained collection of packages, and it's where every `conda install` and `conda create` downloads packages from.

> ⚠️ **Warning:** If you see anything other than `conda-forge` (for example `defaults`), don't try to change it yourself — ask for help. It usually means that conda comes from an older Anaconda or Miniconda installation rather than Miniforge, and that needs fixing properly.

---

## Exercise 1 — Create an environment and use it

Create your own environment, and prove to yourself that its packages really are isolated from the rest of your computer.

### Part A: in the terminal

Create an environment called `tech2-test` with Python 3.14 and pandas, and confirm the package is there:

```
conda create --name tech2-test python=3.14 pandas
```

```
conda activate tech2-test
```

```
conda list pandas
```

Now leave the environment and run the same check again:

```
conda deactivate
```

```
conda list pandas
```

> **Check:** `conda list pandas` shows a version inside `tech2-test`, and nothing in `base`. Two environments on one computer, two different sets of packages.

### Part B: in VS Code

Creating an environment in the terminal is only half the job — your editor needs to know about it too.

1. Make a new folder called `week06` inside your `TECH2` folder, and open it in VS Code. Don't initialize a git repository this time — we won't be writing any code this week, so there is nothing to commit.
2. Create a file called `test.py` containing:

   ```python
   import pandas as pd

   temperatures = pd.DataFrame({"day": ["Mon", "Tue"], "temp": [4.1, 5.6]})
   print(temperatures)
   ```

3. Press `Ctrl+Shift+P` (Windows) or `Cmd+Shift+P` (Mac), type **Python: Select Interpreter**, and choose `tech2-test`.
4. Run the script.
5. Now select the **`base`** interpreter instead, and run it again.

> **Check:** the script prints a small table under `tech2-test`, and fails with `ModuleNotFoundError: No module named 'pandas'` under `base`. Same code, same computer, different environment, different result — this is the single most common cause of "but it works on my machine!"

*Guide: [Creating an environment](../../guides/conda-environments.md#creating-an-environment) · [Using an environment in VS Code](../../guides/conda-environments.md#using-an-environment-in-vs-code)*

---

## Exercise 2 — Export, delete, and rebuild your environment

An environment can be written down as a small text file — that's what makes a project reproducible.

Activate the environment and navigate to your workshop folder:

```
conda activate tech2-test
```

```
cd <path-to-your-workshop-folder>
```

> 💡 **Tip:** To avoid typing a long path, copy it instead, just like in week 1. Type `cd` followed by a space, then paste the path and press Enter.
> - **Windows:** in File Explorer, right-click the folder → **Copy as path**, and paste with `Shift+Insert`.
> - **Mac:** in Finder, hold `Option`, right-click the folder → **Copy "…" as Pathname**, and paste with `Cmd+V`.

Export the environment to a file:

```
conda env export --from-history > environment.yml
```

Open `environment.yml` in VS Code and read it. You should recognize everything in it.

Now delete the environment entirely:

```
conda deactivate
```

```
conda env remove --name tech2-test
```

```
conda env list
```

And rebuild it from the file you just exported:

```
conda env create --file environment.yml
```

```
conda activate tech2-test
```

```
conda list pandas
```

> **Check:** `tech2-test` disappears from `conda env list` after removing it, then comes back with pandas intact after rebuilding. You destroyed an environment and recreated it from a text file — that file is all anyone needs to reproduce your setup.

*Guide: [Saving an environment to a file](../../guides/conda-environments.md#saving-an-environment-to-a-file) · [Creating an environment from a file](../../guides/conda-environments.md#creating-an-environment-from-a-file) · [Deleting an environment](../../guides/conda-environments.md#deleting-an-environment)*

---

## Exercise 3 — Set up your environment for Part 2

In Part 2 of the course you'll be working with data using pandas and matplotlib. That work has its own environment, and you can build it straight from a file published online — without downloading anything first.

```
conda env create --file https://raw.githubusercontent.com/richardfoltyn/TECH2-H26/refs/heads/main/environment.yml
```

```
conda env list
```

```
conda activate TECH2
```

```
conda list pandas
```

Now check for `sympy`, which we used in the lecture:

```
conda list sympy
```

Finally, check that the environment works in VS Code. In Part 2 you'll mainly work in notebooks, so this time you select the environment as the notebook's *kernel*:

1. In VS Code, open your `week06` folder and create a new file called `check-tech2.ipynb`.
2. Click **Select Kernel** in the top-right corner of the notebook.
3. Choose **Python Environments...**, then pick `TECH2`.
4. Paste the following code into the first cell and run it:

   ```python
   import platform
   import numpy as np
   import pandas as pd
   import matplotlib

   print(f"Python:     {platform.python_version()}")
   print(f"numpy:      {np.__version__}")
   print(f"pandas:     {pd.__version__}")
   print(f"matplotlib: {matplotlib.__version__}")
   print("All imports successful!")
   ```

> **Check:** the new environment appears in `conda env list` and contains pandas, but not sympy. Sympy is installed in `base`, but that doesn't make it available here — a package can only be used in an environment it has been installed into. In the notebook, the top-right corner shows `TECH2` as the kernel, and the cell prints a version number for each package followed by `All imports successful!`. Keep this environment — it's the one you'll use for the rest of the course.

*Guide: [Creating an environment from a file](../../guides/conda-environments.md#creating-an-environment-from-a-file) · [Using an environment in VS Code](../../guides/conda-environments.md#using-an-environment-in-vs-code)*

---

## Exercise 4 — Recreate someone else's project

So far you've built environments from your own file and from the course's file. Now try it with a project you've never seen before.

Download **`temp-conversion-app.zip`** and unzip it. It contains a small web app version of the temperature conversion program from week 5, built with a package called `dash`.

Open `environment.yml` from the unzipped folder and see what the project needs. Then navigate there and build the environment:

```
cd <path-to-the-unzipped-folder>
```

```
conda env create --file environment.yml
```

```
conda activate temp-conversion-app
```

Now open the folder in VS Code and open `temp-conversion-app.ipynb`. Select the environment as the notebook's kernel, just like in Exercise 3:

1. Click **Select Kernel** in the top-right corner of the notebook.
2. Choose **Python Environments...**, then pick `temp-conversion-app`.
3. Click **Run All**.

A link appears below the last cell — click it to open the app in your browser, and convert a few temperatures.

> **Check:** the app runs in your browser, and the top-right corner of the notebook shows `temp-conversion-app` as the kernel. Note what just happened: you ran a project built with a package you've never used, without installing anything by hand or reading any setup instructions. That is what an `environment.yml` buys you.

*Guide: [Creating an environment from a file](../../guides/conda-environments.md#creating-an-environment-from-a-file) · [Using an environment in VS Code](../../guides/conda-environments.md#using-an-environment-in-vs-code)*

---

## Tidying up

Environments take up disk space, so it's worth deleting ones you no longer need. `tech2-test` was only for practice:

```
conda deactivate
```

```
conda env remove --name tech2-test
```

You still have its `environment.yml` if you ever want it back — which is rather the point.

You can also remove the `temp-conversion-app` environment if you want, but keep the `TECH2` environment.

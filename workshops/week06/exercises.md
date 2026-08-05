# Week 6 — Workshop: Virtual Environments

This week's workshop is different from the previous ones: there are no Python programs to write, and no git repository to create. Almost everything happens in the terminal.

The commands you need are written out below — copy and paste them rather than typing them by hand. For the general explanation of what each command does (and the options we don't use today), see the **[conda environments guide](../../guides/conda-environments.md)**, which is a reference you can consult at any point in the course.

---

## Before you start

Open a terminal — **Miniforge Prompt** on Windows, **Terminal** on Mac. Your prompt should start with `(base)`.

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

The last command lists what's installed in your `base` environment. 

---

## Exercise 1 — Create an environment and use it

Create your own environment, and prove to yourself that its packages really are isolated from the rest of your computer.

### Part A: in the terminal

Create an environment called `tech2-test` with Python 3.13 and pandas, and confirm the package is there:

```
conda create --name tech2-test python=3.13 pandas
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

1. Make a new folder for this workshop and open it in VS Code.
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

> 💡 **Tip:** To avoid typing a long path, drag the folder from File Explorer (Windows) or Finder (Mac) onto the terminal window — the full path is pasted for you.

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

## Exercise 3 — Recreate someone else's project

So far you've rebuilt your own environment. Now try it with a project you've never seen before.

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

Now open the folder in VS Code, select `temp-conversion-app` as your interpreter (`Ctrl+Shift+P` → **Python: Select Interpreter**), and run `temp-conversion-app.py`. A URL will appear in the terminal — open it in your browser and convert a few temperatures.

> **Check:** the app runs in your browser. Note what just happened: you ran a project built with a package you've never used, without installing anything by hand or reading any setup instructions. That is what an `environment.yml` buys you.

---

## Exercise 4 — Set up your environment for Part 2

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

> **Check:** the new environment appears in `conda env list` and contains pandas. Keep this one — it's the environment you'll use for the rest of the course.

*Guide: [Creating an environment from a file](../../guides/conda-environments.md#creating-an-environment-from-a-file)*

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

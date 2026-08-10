# Verification Checklist

Once you've installed VS Code, Git, and Miniforge, go through this checklist to confirm everything is working. This should take about two minutes.

| # | Check | How | Looks right if... |
| --- | --- | --- | --- |
| 1 | VS Code | Open VS Code from the Start Menu (Windows) or Applications folder (Mac) | It opens and shows the Welcome tab |
| 2 | Git | **Windows:** open Git Bash. **Mac:** open Terminal. Run `git --version` | A version number appears, e.g. `git version 2.43.0` |
| 3 | Miniforge | **Windows:** open Miniforge Prompt. **Mac:** open Terminal. Run `conda info --base` | A path appears that contains `miniforge3`, e.g. `C:\Users\you\miniforge3` or `/Users/you/miniforge3` |

## If everything shows correctly

You're all set for the first lecture — no further action needed.

## If check 3 shows a different path

If the path doesn't contain `miniforge3`, another Python installation is answering instead of Miniforge. On Windows, check that you opened the **Miniforge Prompt** and not another terminal. If it still looks wrong, note what it said and bring it to the first lecture.

## If something doesn't work

Don't worry — we've reserved time in the first lecture to help. Before class:

1. Take a screenshot or note of any error message you saw.
2. Note which of the three checks above failed.

Bring this to class and we'll fix it together.

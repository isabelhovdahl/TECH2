# Installing Git (Windows)

Git is the version control tool we'll use to track and share code throughout the course.

## Steps

Install [VS Code](install-vscode.md) before you start, if you haven't already — step 4 below depends on it.

1. Go to [https://git-scm.com/download/win](https://git-scm.com/download/win)
2. Click the link to download the most recent version of Git for Windows.
3. Open the downloaded installer and click Next through the setup wizard. The default options are fine, with one exception — see the next step.
4. Stop at the screen titled **"Choosing the default editor used by Git"**. Open the dropdown and select **"Use Visual Studio Code as Git's default editor"**, then carry on clicking Next.
5. Finish the installation.

> ⚠️ **Warning:** VS Code only appears in that dropdown if it was installed *before* Git. If it isn't listed, close the installer, follow the [VS Code installation guide](install-vscode.md), and then start again from step 3.

Git sometimes needs to open a text editor for you — for example, to write a commit message when you haven't given one on the command line. The installer's default choice is **Vim**, an editor that is genuinely hard to use, and hard even to close, if you have never seen it before. Picking VS Code instead means those messages open in the editor you already know.

Once installed, git can be used via the command line by launching **Git Bash** from the start menu.

## Next step

Continue to the [Miniforge installation guide](install-miniforge-windows.md).

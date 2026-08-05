# Installing Miniforge (Windows)

Miniforge gives us Python — the programming language we'll be coding in — along with `conda`, a tool for managing project environments.

You may have heard of **Anaconda** or **Miniconda**, which do the same job. **Miniforge** works exactly the same way and uses the same `conda` command — the only real difference is which repository packages come from, which avoids some licensing restrictions that can affect Anaconda's own distribution. For this course, it makes no difference which of the three you use — so if you already have one, you're already set up.

## Step 1: Check whether you already have Anaconda, Miniconda, or Miniforge installed

1. Open the **Start Menu** and look for "Anaconda Prompt" or "Miniforge Prompt."
2. **If you find either:** you already have what you need — skip straight to the [verification checklist](verify-installation.md).
3. **If you find neither:** continue to Step 2 below.

## Step 2: Download Miniforge

Download the installer from here: https://conda-forge.org/download/. Click on the button for Windows. 

## Step 3: Run the installer

Open the downloaded `.exe` file and go through the setup wizard. When you reach the installation options screen, use these settings:

| Option | Setting |
| --- | --- |
| Create shortcuts | ✅ Ticked (default) |
| Add Miniforge3 to my PATH environment variable | ❌ **Leave unticked** (the installer itself recommends this) |
| Register Miniforge3 as my default Python | ✅ Tick this |
| Clear the package cache upon completion | ✅ Tick this |

Click Install and wait for it to finish.

## Next step

Continue to the [verification checklist](verify-installation.md).

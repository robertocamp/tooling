# Annaconda

set up Anaconda on your Mac M1 without disrupting your current Python environment by following these steps:

## Anaconda:  do I already have it???

 quickly check if Anaconda is already installed on your machine by following these steps:

### Step 1: Check for Anaconda Installation

1. **Open your terminal.**
2. **Check if the `conda` command is available:**


   ```bash
   which conda
   ```

   ```bash
   conda --version
   ```

   - If Anaconda is installed, you will see output similar to this:
     ```
     conda 4.11.0
     ```
   - If the command is not found, Anaconda is not installed, and you'll see a message like this:
     ```
     zsh: command not found: conda
     ```


### Step 2: Check Your PATH Environment Variable

1. **Check if Anaconda is in your PATH:**
   ```bash
   echo $PATH | grep -i anaconda
   ```
   - If Anaconda is in your PATH, the command will return a line that includes something like `/Users/yourusername/anaconda3/bin`.
   - If nothing is returned, Anaconda is likely not in your PATH.

These steps will help you determine whether Anaconda is already installed on your machine. If Anaconda is not installed, you can proceed with the installation steps


## Anaconda installation and setup


### 1. **Install Anaconda:**
   - **Download Anaconda:** Go to the [Anaconda distribution website](https://www.anaconda.com/products/individual) and download the macOS version for Apple Silicon (M1/M2). Choose the `arm64` installer.
   - **Install Anaconda:** Run the installer by following the on-screen instructions. During installation, make sure to uncheck the option that asks if you want to add Anaconda to your PATH.

   **NOTE** if you were not prompted for permission to alter your $PATH, validate what your $PATH looks like after the Anaconda installation completes:

   `echo $PATH | grep -i anaconda`

#### Anaconda directories after installation:  ~/.conda and ~/.anaconda

Yes, the Anaconda installation typically creates two hidden directories in your home directory: `~/.conda` and `~/.anaconda`. Here’s a brief description of their purposes:

### 1. **`~/.conda` Directory**
   - **Purpose:** This directory is used by Conda (the package and environment management system that comes with Anaconda) to store user-specific configuration, environment, and package-related data.
   - **Contents:** It typically contains:
     - **Environments:** A `envs` subdirectory where Conda might store environments created by the user (if they are created in this directory rather than the default `anaconda3/envs` directory).
     - **Configurations:** Some Conda configuration files may reside here.
     - **Logs and History:** It might also include logs or other files that track the history of operations performed by Conda.

### 2. **`~/.anaconda` Directory**
   - **Purpose:** This directory is associated with the Anaconda Navigator and related user preferences or settings.
   - **Contents:** It generally contains:
     - **Navigator Configurations:** User-specific configuration files for the Anaconda Navigator, which is the graphical interface for managing environments, packages, and more.
     - **Backup Files:** It may also include backup files or other user-specific data related to Anaconda's GUI tools.

### Summary
- **`~/.conda`:** Primarily for storing Conda-related data like environments and configurations.
- **`~/.anaconda`:** Used for storing preferences and settings specific to the Anaconda Navigator and potentially other GUI tools provided by Anaconda.

These directories are part of the standard setup for Anaconda and Conda and help manage the environments, packages, and configurations on a per-user basis. They don’t interfere with your existing Python setup and are generally lightweight in terms of storage.


## How has Anaconda effected my $PATH?

- `echo $PATH`

```
/opt/anaconda3/bin:/opt/anaconda3/condabin:/opt/homebrew/opt/openjdk/bin:/opt/homebrew/bin:/opt/homebrew/sbin:/usr/local/bin:/System/Cryptexes/App/usr/bin:/usr/bin:/bin:/usr/sbin:/sbin:/var/run/com.apple.security.cryptexd/codex.system/bootstrap/usr/local/bin:/var/run/com.apple.security.cryptexd/codex.system/bootstrap/usr/bin:/var/run/com.apple.security.cryptexd/codex.system/bootstrap/usr/appleinternal/bin:/opt/homebrew/opt/openjdk/bin:/opt/homebrew/bin:/opt/homebrew/sbin:/usr/local/go/bin:/Users/robertc/go/bin:/usr/local/go/bin:/Users/robertc/go/bin
```

- `python --version`
- `which python`


Your `$PATH` is set up to prioritize Anaconda, as `/opt/anaconda3/bin` and `/opt/anaconda3/condabin` are listed first. This means that by default, the Python interpreter and packages from Anaconda will be used when you open a new terminal session.

### Ensuring You Can Still Create Python Virtual Environments Independently of Anaconda

To maintain your ability to create Python virtual environments independent of Anaconda, you can follow these steps:

1. **Use the Full Path to Your Homebrew Python:**
   - When you want to create a virtual environment that is independent of Anaconda, use the full path to your Homebrew-installed Python:
     ```bash
     /opt/homebrew/bin/python3 -m venv myenv
     ```

2. **Temporarily Modify the PATH (Optional):**
   - If you want to use your Homebrew Python for a session without Anaconda, you can temporarily modify your PATH by removing the Anaconda directories:
     ```bash
     export PATH="/opt/homebrew/bin:/opt/homebrew/sbin:$PATH"
     ```
   - This will prioritize your Homebrew Python for the current session.

3. **Create a Permanent Alias (Optional):**
   - You can create an alias in your `~/.zshrc` to make it easier to use your Homebrew Python:
     ```bash
     alias hbpython='/opt/homebrew/bin/python3'
     alias hbvenv='/opt/homebrew/bin/python3 -m venv'
     ```
   - After adding this to your `~/.zshrc`, reload it:
     ```bash
     source ~/.zshrc
     ```
   - Now, you can use `hbpython` to invoke the Homebrew Python and `hbvenv` to create virtual environments with it.

### Summary

- **Anaconda:** Your setup currently defaults to using Anaconda's Python.
- **Homebrew Python:** You can still use Homebrew's Python explicitly by referencing its full path or by adjusting your `$PATH` or using aliases.

This setup allows you to seamlessly switch between using Anaconda for data science work and using your Homebrew Python for other projects.

## Managing anaconda environments


Great! This output confirms that `conda` is correctly installed and available on your system. You're now in the `(base)` Conda environment, which is the default environment that activates when you start a new terminal session.

### What You Can Do Next:

1. **Create a New Conda Environment (Optional):**
   - You can create a new Conda environment for specific projects or tasks:
     ```bash
     conda create --name myenv
     ```
   - Activate the new environment:
     ```bash
     conda activate myenv
     ```
   - To deactivate the environment and return to the base environment:
     ```bash
     conda deactivate
     ```

2. **Manage Your Environments:**
   - List all available environments:
     ```bash
     conda info --envs
     ```
   - Remove an environment (if needed):
     ```bash
     conda remove --name myenv --all
     ```

3. **Keep Using Your Existing Python Setup:**
   - For projects that don’t require Anaconda, you can deactivate the Conda environment:
     ```bash
     conda deactivate
     ```
   - You can then use your Homebrew-installed Python and virtual environments as you usually do.

4. **Launch the Anaconda Navigator (Optional):**
   - If you prefer a graphical interface, you can launch the Anaconda Navigator:
     ```bash
     anaconda-navigator
     ```

You’re all set to work with Anaconda for your data science projects while maintaining your existing Python workflow for other tasks. If you have any more questions or need further assistance, feel free to ask!

## Example Project: Conda environment


Yes, you're absolutely correct! It’s a good practice to navigate to your project directory before creating a new Conda environment, especially if you plan to keep your project files and environment-related files together or want to be in the right context when activating the environment.

### Recap of the Procedure to Create a New Conda Environment and Develop Python Code

1. **Navigate to Your Project Directory:**
   - First, navigate to the directory where your new project will reside:
     ```bash
     cd /Users/robertc/go/src/github/tooling/python/anaconda/hello
     ```

2. **Create a New Conda Environment:**
   - Once in the project directory, create a new Conda environment. This will ensure that any environment-specific files or dependencies are associated with this project:
     ```bash
     conda create --name myenv
     ```
   - You can also specify Python versions or packages during environment creation:
     ```bash
     conda create --name myenv python=3.12
     ```

3. **Activate the Conda Environment:**
   - After creating the environment, activate it:
     ```bash
     conda activate myenv
     ```
   - Your command prompt will change to indicate that you are now working within the `myenv` Conda environment.

4. **Develop Your Python Code:**
   - Now you can start developing your Python code within this environment. Create your Python files or start coding directly:
     ```bash
     touch hello_conda.py
     ```
   - Write your code, save it, and then run it using Python from the Conda environment:
     ```bash
     python hello_conda.py
     ```

**IMPORTANT:**  you may discover that the `python` command is not available in your environment:

```
python hello_conda.py                 ▦ anaconda/hello ◬ update-readmes⎪◌◦⎥ py ⌉⌊ 3.12 conda ◯ myenv aws ▲   us-east-2 21:26
zsh: command not found: python
(myenv) 
```

**RESOLUTION:**  if this is the case, have conda install python into the conda virt env:  `conda install python`


5. **Install Additional Packages (if needed):**
   - If you need to install additional Python packages, use `conda` or `pip` while your environment is activated:
     ```bash
     conda install numpy
     # or
     pip install requests
     ```

6. **Deactivate the Environment When Done:**
   - After you're finished working on your project, deactivate the Conda environment:
     ```bash
     conda deactivate
     ```
   - This returns you to your default shell environment.

By following this procedure, you'll ensure that your Conda environment is specific to your project and that all dependencies are managed within that environment. This practice helps maintain clean, isolated environments for different projects.

## Conda Virtual Environments

Yes, that's correct! When you create a Conda environment, it can include its own installation of Python, which is isolated from other environments and the system-wide Python installation. This is one of the key features of Conda, allowing you to have multiple environments with different versions of Python and different sets of packages, all without interfering with each other.

### How Conda Environments Work with Python:
1. **Isolated Python Installation:**
   - Each Conda environment can have its own version of Python installed. When you specify a Python version during the creation of a Conda environment, Conda installs that specific version of Python into the environment.

2. **Environment-Specific Packages:**
   - The packages installed in a Conda environment are also isolated to that environment. This means that you can have different versions of the same package in different environments without any conflicts.

3. **Environment Activation:**
   - When you activate a Conda environment, the `python` command (and any other installed packages) will refer to the versions installed within that environment. This ensures that your scripts run with the correct interpreter and dependencies.

4. **No Interference with System Python:**
   - The Python installation in a Conda environment does not affect your system-wide Python or other environments. This is particularly useful for working on projects that require different Python versions or dependencies.

### Example Workflow:
1. **Create a Conda Environment with a Specific Python Version:**
   ```bash
   conda create --name myenv python=3.12
   ```

2. **Activate the Environment:**
   ```bash
   conda activate myenv
   ```

3. **Install Packages and Develop:**
   ```bash
   conda install numpy
   python hello_conda.py
   ```

4. **Deactivate the Environment:**
   ```bash
   conda deactivate
   ```

This setup allows you to work on multiple projects with different requirements on the same machine without running into version conflicts.


## links

https://www.youtube.com/watch?v=V4riykgUS94
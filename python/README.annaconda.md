# Annaconda

set up Anaconda on your Mac M1 without disrupting your current Python environment by following these steps:


## Conda Virtual Environments

When you create a Conda environment, it can include its own installation of Python, which is isolated from other environments and the system-wide Python installation. This is one of the key features of Conda, allowing you to have multiple environments with different versions of Python and different sets of packages, all without interfering with each other.

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



## Anaconda:  do I already have it???

 quickly check if Anaconda is already installed on your machine by following these steps:

### Step 1: Check for Anaconda Installation

1. **Open your terminal.**
2. **Check if the `conda` command is available:**


   ```bash
   which conda
   ```


The output you are seeing from the `which conda` command indicates that `conda` is not a simple executable or a binary file on your system but rather a shell function. 

When you type `which conda`, the shell is telling you that `conda` is defined as a function in your shell environment. This function is responsible for handling the various operations of `conda` (like `activate`, `deactivate`, `install`, etc.) and likely includes logic to manage these operations properly within your shell session.

Here's a breakdown of what you're seeing:

- **conda () { ... }**: This indicates that `conda` is a shell function.
- **local cmd="${1-__missing__}"**: This line sets the `cmd` variable to the first argument passed to the `conda` function, or to `__missing__` if no argument is provided.
- **case "$cmd" in ... esac**: This `case` statement is used to decide what the function should do based on the value of `cmd`. Different cases correspond to different `conda` commands:
  - **(activate | deactivate)**: If the `cmd` is `activate` or `deactivate`, it calls `__conda_activate` with all the provided arguments.
  - **(install | update | upgrade | remove | uninstall)**: If the `cmd` is one of these package management operations, it first calls `__conda_exe`, and if that command fails, it attempts to "reactivate" the current environment by calling `__conda_reactivate`.
  - **(*)**: For any other command, it just calls `__conda_exe` with all the provided arguments.

The reason this is more complex than what you would normally see is that `conda` uses functions like this to integrate more deeply with your shell environment, allowing it to manage environment variables and paths more effectively. This is necessary for managing virtual environments, modifying the `$PATH`, and other shell-related tasks that `conda` needs to perform.

In contrast, most commands you run via `which` are simple executables or scripts located somewhere in your `$PATH`, which is why `which` typically returns just the file path to the command.


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

#### Anaconda directories after installation: 

   - there will be two directories in your $HOME:   ~/.conda and ~/.anaconda

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

   - there will an additional directory in /opt:   `/opt/anaconda3`

### Summary
- **`~/.conda`:** Primarily for storing Conda-related data like environments and configurations.
- **`~/.anaconda`:** Used for storing preferences and settings specific to the Anaconda Navigator and potentially other GUI tools provided by Anaconda.
- **`/opt/anaconda3`** is the prinicipal directory where annaconda installs its software


These directories are part of the standard setup for Anaconda and Conda and help manage the environments, packages, and configurations on a per-user basis. They don’t interfere with your existing Python setup and are generally lightweight in terms of storage.


## How has Anaconda effected my $PATH?

- `echo $PATH`

```
/opt/homebrew/opt/openjdk/bin:/opt/homebrew/bin:/opt/homebrew/sbin:/usr/local/bin:/System/Cryptexes/App/usr/bin:/usr/bin:/bin:/usr/sbin:/sbin:/var/run/com.apple.security.cryptexd/codex.system/bootstrap/usr/local/bin:/var/run/com.apple.security.cryptexd/codex.system/bootstrap/usr/bin:/var/run/com.apple.security.cryptexd/codex.system/bootstrap/usr/appleinternal/bin:/opt/anaconda3/bin:/opt/anaconda3/condabin:/opt/homebrew/opt/openjdk/bin:/opt/homebrew/bin:/opt/homebrew/sbin:/usr/local/go/bin:/Users/robertc/go/bin:/usr/local/go/bin:/Users/robertc/go/bin
```

- `python --version`
- `which python`


◉ python --version                                                                                                        /opt/anaconda3 aws ▲   us-east-2 12:39
Python 3.12.4
(base) 
◉ which python                                                                                                            /opt/anaconda3 aws ▲   us-east-2 12:39
/opt/anaconda3/bin/python
(base) 
◉                 

`$PATH` is set up to prioritize Anaconda, as `/opt/anaconda3/bin` and `/opt/anaconda3/condabin` are listed first. This means that by default, the Python interpreter and packages from Anaconda will be used when you open a new terminal session.

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

### "(base)" vs manual environment creation


Yes, the `(base)` in your terminal prompt indicates that the default Anaconda environment, called `base`, is activated automatically when you open your terminal. This behavior is typical when Anaconda is installed, as it sets up your shell environment to activate the `base` environment by default.

### Removing the `(base)` from Your Prompt

If you don't want the `base` environment to be activated automatically when you open your terminal, you can disable this behavior. To do so:

1. **Disable Auto Activation of the Base Environment:**
   You can configure Anaconda not to auto-activate the `base` environment by running the following command:
   ```bash
   conda config --set auto_activate_base false
   ```
   After running this command, the `(base)` will no longer appear in your terminal prompt when you start a new terminal session.

2. **Restart Your Terminal:**
   Close and reopen your terminal or simply source your shell configuration file (`~/.zshrc` or `~/.bashrc`, depending on your shell) to apply the changes.

### Implications of Disabling Auto-Activation

- **Manual Activation:** After disabling auto-activation, you will need to manually activate the `base` environment or any other conda environment you want to use by running:
  ```bash
  conda activate base
  ```
  Or, for another environment:
  ```bash
  conda activate <environment_name>
  ```

- **More Control:** Disabling auto-activation gives you more control over which Python environment is active, which can be especially useful if you use multiple Python versions or environments on your system.

- **Avoid Conflicts:** If you have other Python environments or versions installed (e.g., via Homebrew or system Python), not auto-activating the `base` environment can help avoid potential conflicts between Anaconda and other Python installations.

In your case, since you've already expressed a preference for controlling Anaconda activations manually, this approach aligns well with your workflow and avoids any unintended interference from the `base` environment.



**Manage Your Environments:**
   - List all available environments:
     ```bash
     conda info --envs
     ```
   - Remove an environment (if needed):
     ```bash
     conda remove --name myenv --all
     ```

**Keep Using Your Existing Python Setup:**
   - For projects that don’t require Anaconda, you can deactivate the Conda environment:
     ```bash
     conda deactivate
     ```
   - You can then use your Homebrew-installed Python and virtual environments as you usually do.

**Launch the Anaconda Navigator (Optional):**
   - If you prefer a graphical interface, you can launch the Anaconda Navigator:
     ```bash
     anaconda-navigator
     ```

You’re all set to work with Anaconda for your data science projects while maintaining your existing Python workflow for other tasks. If you have any more questions or need further assistance, feel free to ask!



## Example Project: Conda environment without Jupyter Notebookd


It’s a good practice to navigate to your project directory before creating a new Conda environment, especially if you plan to keep your project files and environment-related files together or want to be in the right context when activating the environment.

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

## Example Project: Jupyter Notebooks

To set up a smooth workflow for working with Jupyter Notebooks and Conda on your machine, especially given that you've disabled the auto-activation of the `base` environment, you can follow these steps:

### 1. **Create a Conda Environment for Your Course**
   It’s a good practice to create a separate Conda environment for your university course. This helps keep your dependencies organized and avoids conflicts.

   ```bash
   conda create --name university_course python=3.12.4
   ```

   Replace `university_course` with a meaningful name for the environment.

### 2. **Activate the Conda Environment**
   Once the environment is created, activate it:

   ```bash
   conda activate university_course
   ```

   This ensures that all packages and dependencies installed are within this environment.

### 3. **Install Jupyter Notebook in the Environment**
   With the environment activated, install Jupyter Notebook:

   ```bash
   conda install jupyter
   ```

   This installs Jupyter Notebook in your `university_course` environment.

### 4. **Add the Conda Environment to Jupyter**
   Next, you need to add this environment as a kernel in Jupyter so that you can select it when working in notebooks:

   ```bash
   python -m ipykernel install --user --name university_course --display-name "Python (university_course)"
   ```

   This command adds the environment to Jupyter’s list of available kernels, so you can select it when opening or creating a notebook.

### 5. **Launch Jupyter Notebook**
   You can now launch Jupyter Notebook from within the activated environment:

   ```bash
   jupyter notebook
   ```

   This will open the Jupyter Notebook interface in your web browser.

### 6. **Open the Downloaded Notebook**
   In the Jupyter interface, navigate to the directory where you downloaded the notebook file from your class portal and open it.

### 7. **Select the Conda Environment Kernel**
   Once the notebook is open, make sure it’s using the correct Conda environment. You can do this by going to `Kernel` > `Change kernel` and selecting "Python (university_course)" from the list.

### 8. **Work on Your Notebook**
   You can now work on your notebook with the environment fully set up. All the packages you need for your course should be installed within the `university_course` environment.

### 9. **Deactivating the Environment**
   When you’re done, you can deactivate the environment:

   ```bash
   conda deactivate
   ```

### Summary Workflow

1. **Download the notebook file from your course portal.**
2. **Activate your course-specific Conda environment.**
3. **Launch Jupyter Notebook from within the activated environment.**
4. **Open the notebook and ensure the correct kernel is selected.**

This approach keeps your work organized and ensures that the dependencies required by your course are isolated in a specific environment, reducing the risk of conflicts.

## links

https://www.youtube.com/watch?v=V4riykgUS94
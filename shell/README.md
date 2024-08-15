# shell

## echo $SHELL


To turn your default `/usr/zsh` shell into "Oh My Zsh" on your Mac M1, follow these steps:

### 1. **Install Homebrew (if not already installed)**

Homebrew is a package manager for macOS that will help you install `Oh My Zsh` dependencies. If you don't have Homebrew installed, you can install it by running:

```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

## Oh My Zsh

To verify whether "Oh My Zsh" is already installed on your Mac, you can follow these steps:

### 1. **Check the Zsh Configuration File**

Open your Terminal and check if the `~/.zshrc` file contains the line that loads "Oh My Zsh." You can do this by running:

```bash
cat ~/.zshrc | grep "oh-my-zsh.sh"
```

If "Oh My Zsh" is installed, you should see something like:

```bash
source $ZSH/oh-my-zsh.sh
```

This line indicates that the `oh-my-zsh.sh` script is being sourced when you start a new terminal session, which is a key part of "Oh My Zsh."

### 2. **Check for the Oh My Zsh Directory**

Another way to check is by seeing if the "Oh My Zsh" directory exists in your home directory:

```bash
ls -la ~/.oh-my-zsh
```

If "Oh My Zsh" is installed, this command will list the contents of the `.oh-my-zsh` directory. If the directory exists, "Oh My Zsh" is installed on your system.

### 3. **Check the Terminal Prompt**

If your terminal prompt looks more colorful or customized (for example, showing the current git branch when inside a git repository), it's likely that "Oh My Zsh" is installed. By default, "Oh My Zsh" comes with the "robbyrussell" theme, which displays a `➜` character at the prompt.

### 4. **Check the Zsh Version and Themes**

Run the following command to see if the `ZSH_THEME` variable is set, which is typically configured by "Oh My Zsh":

```bash
echo $ZSH_THEME
```

If it returns a theme name (e.g., `robbyrussell`), it indicates that "Oh My Zsh" is managing your shell environment.

If any of these checks indicate the presence of "Oh My Zsh," then it is already installed on your Mac. If not, you can follow the steps to install it as described in the previous response.

## INSTALL OH MY ZSH IF NOT INSTALLED


### 2. **Install Zsh (if not already installed)**

Zsh is pre-installed on macOS, but if you want to make sure you're using the latest version, you can install it via Homebrew:

```bash
brew install zsh
```

### 3. **Install Oh My Zsh**

Now, install "Oh My Zsh" by running the following command in your terminal:

```bash
sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"
```

This script will:

- Download and install "Oh My Zsh."
- Set Zsh as your default shell (if it's not already).
- Create a configuration file (`~/.zshrc`) in your home directory.

### 4. **Restart the Terminal**

After the installation is complete, restart your Terminal to start using "Oh My Zsh." You should see a new, more colorful prompt, which is a sign that "Oh My Zsh" is active.

### 5. **Customize Your Shell**

You can now customize "Oh My Zsh" by editing the `~/.zshrc` file. For example, you can change the theme by modifying the `ZSH_THEME` variable.

To open the file in VSCode, you can use:

```bash
code ~/.zshrc
```

After making changes, save the file and run `source ~/.zshrc` to apply them.

### 6. **Install Plugins (Optional)**

"Oh My Zsh" comes with many useful plugins. You can enable them by adding them to the `plugins` array in the `~/.zshrc` file. Popular plugins include:

- `git`: For Git integration.
- `z`: For quickly navigating your filesystem.

Example:

```bash
plugins=(git z)
```

Again, run `source ~/.zshrc` after saving your changes to activate the plugins.

With these steps, your `/usr/zsh` shell should now be fully equipped with "Oh My Zsh," offering you a more powerful and customizable shell environment.
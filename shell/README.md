# shell

## echo $SHELL


To turn your default `/usr/zsh` shell into "Oh My Zsh" on your Mac M1, follow these steps:

### 1. **Install Homebrew (if not already installed)**

Homebrew is a package manager for macOS that will help you install `Oh My Zsh` dependencies. If you don't have Homebrew installed, you can install it by running:

```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

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
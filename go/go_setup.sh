#!/bin/bash

# Display a message with the user's name
echo "Validating Go environment for $USER..."

# Change to the user's home directory
cd $HOME

# Display the home directory
echo "Home directory: $HOME"

# Create the Go workspace directory structure
echo "Creating Go workspace..."
mkdir -p $HOME/go/{bin,pkg,src}

# Detect the user's current shell
CURRENT_SHELL=$(echo $SHELL)

# Display the detected shell
echo "Detected shell: $CURRENT_SHELL"

# Check if the shell is /bin/zsh
if [ "$CURRENT_SHELL" = "/bin/zsh" ]; then
  # Update the .zshrc file
  echo "Updating .zshrc with Go environment variables..."
  echo "export GOPATH=$HOME/go" >> $HOME/.zshrc
  echo "export PATH=\$PATH:/usr/local/go/bin:\$GOPATH/bin" >> $HOME/.zshrc
  echo "Go environment setup complete. Please restart your terminal or run 'source ~/.zshrc' to apply the changes."
else
  # Display a message if the shell is not supported
  echo "Unsupported shell detected: $CURRENT_SHELL"
  echo "Please switch to the zsh shell to use this setup script."
fi

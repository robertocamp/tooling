# git


## git install / validate
To determine if Git is installed on your Mac M1, you can use the Terminal and run the following command:

```bash
git --version
```

If Git is installed, this command will return the installed version of Git, for example:

```
git version 2.40.1
```

If Git is not installed, your Mac will prompt you to install the Xcode Command Line Tools, which include Git. You can follow the on-screen instructions to install it if needed.

## Git ssh keys

### 1. **Generate a New SSH Key**

Open the Terminal and run the following command to generate a new SSH key:

```bash
ssh-keygen -t ed25519 -C "your_email@example.com"
```

Replace `"your_email@example.com"` with the email address you use for your GitHub account.

### 2. **Save the SSH Key**

When prompted to "Enter a file in which to save the key," press Enter. This will save the key in the default location (`~/.ssh/id_ed25519`).

You can also choose a different location by providing a path.

### 3. **Enter a Passphrase (Optional)**

You’ll be asked to enter a passphrase. You can either enter a secure passphrase or leave it blank for no passphrase. It's recommended to use a passphrase for added security.

### 4. **Add Your SSH Key to the SSH-Agent**

Run the following commands to start the `ssh-agent` and add your SSH key:

```bash
eval "$(ssh-agent -s)"
ssh-add ~/.ssh/id_ed25519
```

If you saved your SSH key in a different location, replace `~/.ssh/id_ed25519` with the correct path.

### 5. **Add the SSH Key to Your GitHub Account**

Now you need to add the SSH key to your GitHub account.

1. Copy the SSH key to your clipboard with the following command:

    ```bash
    pbcopy < ~/.ssh/id_ed25519.pub
    ```

2. Go to [GitHub SSH settings](https://github.com/settings/ssh/new).
3. Click on "New SSH key" or "Add SSH key."
4. In the "Title" field, add a descriptive label for the new key (e.g., "Mac M1").
5. Paste your key into the "Key" field.
6. Click "Add SSH key."

### 6. **Test the SSH Connection**

Finally, test the connection to make sure everything is working:

```bash
ssh -T git@github.com
```

You should see a message like:

```bash
Hi username! You've successfully authenticated, but GitHub does not provide shell access.
```

If you see this message, you’ve successfully added your SSH key to your Mac M1 and connected it to GitHub.


**TO CLONE A REPO**  `git clone <github clone link>`
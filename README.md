# Mad Scientist Linux - Dev Branch

This branch (`dev`) contains experimental scripts and configurations for the Mad Scientist Linux environment. Changes here are for development and testing purposes before being merged into the `main` branch.

---

## Usage Instructions

### Setting Up the `config` Alias in `.zshrc`

To use this bare repository efficiently, set up the `config` alias as follows:

1. **Add the Alias to `.zshrc`:**
   Open your `.zshrc` file in an editor:
   ```bash
   vim ~/.zshrc
   ```
   Add the following line to create the config alias:
   ```bash
   alias config='/usr/bin/git --git-dir=$HOME/.cfg/ --work-tree=$HOME'
   ```

2. **Source Your .zshrc File:** Apply the changes to your shell:
   ```bash
   source ~/.zshrc
   ```

3. **Verify the Alias:** Test the alias by running:
   ```bash
   config status
   ```

## Managing the Bare Repository

### First-Time Setup

1. Initialize the Bare Repository (if not already set up):
   ```bash
   git init --bare $HOME/.cfg
   ```

2. Add the Remote Repository:
   ```bash
   config remote add origin https://github.com/iTrauco/mad-scientist-linux.git
   ```

3. Check Out the dev Branch:
   ```bash
   config fetch origin dev
   config checkout dev
   ```

4. Configure Git to Ignore Untracked Files:
   ```bash
   config config --local status.showUntrackedFiles no
   ```

### Development Workflow

#### Adding Files to the Repository

1. Stage a File or Directory:
   ```bash
   config add path/to/file_or_directory
   ```

2. Commit the Changes:
   ```bash
   config commit -m "feat: Add file_or_directory to dev branch"
   ```

3. Push Changes to the Remote Repository:
   ```bash
   config push origin dev
   ```

#### Pulling Updates

To pull the latest changes from the dev branch:
```bash
config pull origin dev
```

#### Checking Repository Status

To see the current status of the repository:
```bash
config status
```

#### Resolving Conflicts

If there are conflicts when pulling changes:

1. Check the conflicting files:
   ```bash
   config status
   ```

2. Open and resolve conflicts manually in a text editor.

3. Add the resolved files:
   ```bash
   config add path/to/resolved_file
   ```

4. Commit the resolved changes:
   ```bash
   config commit -m "fix: Resolve merge conflict"
   ```

#### Removing Files or Directories

To remove a file or directory from tracking:
```bash
config rm -r --cached path/to/file_or_directory
config commit -m "chore: Remove file_or_directory"
```

## Structure of the Repository

- `scripts/`: Shell scripts and automation tools for various system tasks
- `.zshrc`: Zsh configuration file with customizations for this environment
- Other Config Files: Additional configuration files for the system

## Notes

- Use this branch for testing and development purposes only
- Merge validated changes into the main branch for stability
- Always back up critical files before making changes to the repository

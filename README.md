# Mad Scientist Linux - XPS 13 9520

Configuration files and system setup for Dell XPS 13 9520 Linux development environment.

## System Specifications

### Hardware
- **Model**: Dell XPS 9320
- **Processor**: 12th Gen Intel® Core™ i7-1260P (12-core)
  - 4 Performance cores, 8 Efficiency cores
  - Cache: L1: 1.1 MiB, L2: 9 MiB, L3: 18 MiB
- **Memory**: 15.23 GiB
- **Storage**: Western Digital PC SN810 NVMe 512GB
- **Display**: 3840x2160 (4K)
- **Graphics**: Intel Alder Lake-P Integrated Graphics

### Software
- **OS**: Ubuntu 22.04.5 LTS (Jammy Jellyfish)
- **Kernel**: 6.8.0-49-generic x86_64
- **Desktop Environment**: XFCE 4.18.4
- **Shell**: Zsh 5.8.1
- **Display Server**: X.Org 1.21.1.4
- **Graphics Driver**: Mesa Intel Graphics (ADL GT2)

### Network
- **WiFi**: Intel Alder Lake-P PCH CNVi
- **Ethernet**: Realtek RTL8153 Gigabit Adapter

## Repository Setup

### First Time Setup
1. Create the bare repository:
```bash
git init --bare $HOME/mad-scientist-linux
```

2. Add the alias to .zshrc:
```bash
echo "alias config='git --git-dir=$HOME/mad-scientist-linux --work-tree=$HOME'" >> ~/.zshrc
```

3. Source your shell config:
```bash
source ~/.zshrc
```

4. Configure git to ignore untracked files:
```bash
config config --global status.showUntrackedFiles no
```

### System Information Command
To gather complete system information, run:
```bash
echo -e "=== System Info ===" && lsb_release -a && echo -e "\n=== CPU Info ===" && lscpu | grep "Model name" && echo -e "\n=== Desktop Environment ===" && xfce4-about -V && echo -e "\n=== Full System Details ===" && inxi -Fxz
```

### Using the Configuration

#### Adding Files
```bash
config add /path/to/file
config commit -m "feat: add new configuration"
```

#### Checking Status
```bash
config status
```

#### Creating New Machine Branches
```bash
config checkout -b mad-scientist-[machine-name]
```

## Directory Structure
- `/scripts`: Shell scripts and automation tools
- `/README.md`: This documentation

## Branch Information
This branch (`mad-scientist-xps-13-9520`) contains configurations specific to the Dell XPS 13 9520 laptop. Each system should maintain its own branch with system-specific configurations.

## Author
Chris Trauco (chris@trau.co)

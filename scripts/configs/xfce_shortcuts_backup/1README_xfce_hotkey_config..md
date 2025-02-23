# XFCE Keyboard Shortcuts Backup Guide

## Simple Backup Command

To back up only your XFCE keyboard shortcuts:

```bash
# Create a backup directory for keyboard shortcuts
mkdir -p ~/scripts/xfce_shortcuts_backup

# Copy only the keyboard shortcuts configuration
cp ~/.config/xfce4/xfconf/xfce-perchannel-xml/xfce4-keyboard-shortcuts.xml ~/scripts/xfce_shortcuts_backup/

# Add a timestamp
echo "Keyboard shortcuts backup created on $(date)" > ~/scripts/xfce_shortcuts_backup/backup_info.txt
```

## Automated Backup Script

For regular backups with date-stamped filenames, create a script with this content:

```bash
#!/bin/bash
BACKUP_DATE=$(date +%Y-%m-%d)
BACKUP_DIR=~/scripts/xfce_shortcuts_backup
mkdir -p $BACKUP_DIR
cp ~/.config/xfce4/xfconf/xfce-perchannel-xml/xfce4-keyboard-shortcuts.xml "$BACKUP_DIR/shortcuts_$BACKUP_DATE.xml"
```

Save as `~/scripts/backup_shortcuts.sh` and make executable:

```bash
chmod +x ~/scripts/backup_shortcuts.sh
```

## Adding to Crontab (Optional)

To run the backup automatically, you can add it to your crontab:

```bash
# Open crontab editor
crontab -e

# Add this line to run weekly (Sunday at midnight)
0 0 * * 0 ~/scripts/backup_shortcuts.sh
```

## Restoring XFCE Shortcuts

To restore shortcuts from a backup:

```bash
cp ~/scripts/xfce_shortcuts_backup/shortcuts_YYYY-MM-DD.xml ~/.config/xfce4/xfconf/xfce-perchannel-xml/xfce4-keyboard-shortcuts.xml
```

Replace `YYYY-MM-DD` with the date of the backup you want to restore.

After restoring, you may need to restart XFCE for the changes to take effect:

```bash
xfce4-panel -r
```

Or log out and log back in to ensure all shortcuts are properly loaded.

## Viewing Your Current Shortcuts

To view your current keyboard shortcuts configuration:

```bash
cat ~/.config/xfce4/xfconf/xfce-perchannel-xml/xfce4-keyboard-shortcuts.xml
```

You can also use a GUI tool to view and edit shortcuts:

```bash
xfce4-keyboard-settings
```

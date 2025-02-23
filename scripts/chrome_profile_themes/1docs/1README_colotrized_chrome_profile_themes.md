# Chrome Profile Color Themes Guide

## Creating Color Theme Directories
This command creates 16 color themes in your scripts directory:

```bash
mkdir -p ~/scripts/chrome_profile_themes && cd ~/scripts/chrome_profile_themes && \
for color in "Hot_Pink:#FF3366:255,51,102" "Neon_Green:#33FF66:51,255,102" "Electric_Blue:#3366FF:51,102,255" "Bright_Orange:#FF6633:255,102,51" "Purple:#9933FF:153,51,255" "Cyan:#33FFFF:51,255,255" "Yellow:#FFFF33:255,255,51" "Magenta:#FF33FF:255,51,255" "Turquoise:#00CC99:0,204,153" "Red_Orange:#FF4400:255,68,0" "Indigo:#6633FF:102,51,255" "Light_Orange:#FF9933:255,153,51" "Aqua:#00FFCC:0,255,204" "Bright_Purple:#CC33FF:204,51,255" "Sky_Blue:#3399FF:51,153,255" "Deep_Pink:#FF3399:255,51,153"; do \
  name=$(echo $color | cut -d':' -f1) && \
  hex=$(echo $color | cut -d':' -f2) && \
  rgb=$(echo $color | cut -d':' -f3) && \
  mkdir -p "$name" && \
  echo '{
  "name": "'"$name"' Theme",
  "version": "1.0",
  "description": "'"$name"' theme for Chrome",
  "manifest_version": 3,
  "theme": {
    "colors": {
      "frame": ['"$rgb"'],
      "toolbar": ['"$rgb"'],
      "tab_text": [255, 255, 255],
      "tab_background_text": [200, 200, 200],
      "bookmark_text": [255, 255, 255],
      "ntp_background": [240, 240, 240],
      "ntp_text": [50, 50, 50]
    }
  }
}' > "$name/manifest.json" && \
  echo "Created $name theme with color $hex"; \
done
```

## Installing Themes in Chrome Profiles

For each Chrome profile:

1. Open Chrome with the specific profile:
   ```bash
   google-chrome --profile-directory="Profile X"
   ```
   Replace X with your profile number (e.g., 14)

2. Navigate to `chrome://extensions/`

3. Enable "Developer mode" (toggle in top-right corner)

4. Click "Load unpacked" button

5. Navigate to `~/scripts/chrome_profile_themes/COLOR_NAME/` and select the folder
   (where COLOR_NAME is the theme you want, e.g., Hot_Pink)

## Color Reference

Here's a reference of all the colors included:

| Color Name | Hex Code | RGB Value |
|------------|----------|-----------|
| Hot Pink | #FF3366 | 255,51,102 |
| Neon Green | #33FF66 | 51,255,102 |
| Electric Blue | #3366FF | 51,102,255 |
| Bright Orange | #FF6633 | 255,102,51 |
| Purple | #9933FF | 153,51,255 |
| Cyan | #33FFFF | 51,255,255 |
| Yellow | #FFFF33 | 255,255,51 |
| Magenta | #FF33FF | 255,51,255 |
| Turquoise | #00CC99 | 0,204,153 |
| Red Orange | #FF4400 | 255,68,0 |
| Indigo | #6633FF | 102,51,255 |
| Light Orange | #FF9933 | 255,153,51 |
| Aqua | #00FFCC | 0,255,204 |
| Bright Purple | #CC33FF | 204,51,255 |
| Sky Blue | #3399FF | 51,153,255 |
| Deep Pink | #FF3399 | 255,51,153 |

## Chrome Profile Scripts

Example script for launching Chrome with a specific profile (after installing the appropriate theme):

```bash
#!/bin/bash

# Launch Chrome with Profile 14 (which should have the Hot Pink theme installed)
/usr/bin/google-chrome --profile-directory="Profile 14" --new-window "https://claude.ai"
```

Save this as `~/scripts/claude.1.sh` and make it executable:

```bash
chmod +x ~/scripts/claude.1.sh
```

You can create similar scripts for each profile, using different URLs as needed.

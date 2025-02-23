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
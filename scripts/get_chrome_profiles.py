#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import json
from pathlib import Path
from rich.console import Console

console = Console()

def get_chrome_profiles():
    profiles = []
    chrome_path = Path.home() / ".config" / "google-chrome"
    if chrome_path.exists():
        for profile in chrome_path.iterdir():
            if profile.is_dir() and (profile.name.startswith("Profile ") or profile.name == "Default"):
                profiles.append(profile.name)
    return profiles

def get_profile_users():
    profile_users = {}
    chrome_path = Path.home() / ".config" / "google-chrome"
    for profile in get_chrome_profiles():
        preferences_path = chrome_path / profile / "Preferences"
        if preferences_path.exists():
            user_info = extract_user_info(preferences_path)
            if user_info:
                profile_users[profile] = user_info
    return profile_users

def extract_user_info(preferences_path):
    try:
        with open(preferences_path, "r") as file:
            data = json.load(file)
            # First try to get email for signed-in accounts
            email = data.get("account_info", [{}])[0].get("email", None)
            if email:
                return email
            
            # If no email, get the custom profile name from the profile info
            profile_name = data.get("profile", {}).get("name", None)
            if profile_name:
                return profile_name
            
            # Fall back to "Unnamed Profile" if neither is found
            return "Unnamed Profile"
    except (json.JSONDecodeError, KeyError) as e:
        console.print(f"Error reading JSON from Preferences file: {e}", style="bold red")
        return "Unknown"

def display_chrome_profiles():
    profile_users = get_profile_users()
    if not profile_users:
        console.print("No Chrome profiles found.")
        return

    console.print("\nChrome profiles:")
    for profile, info in profile_users.items():
        console.print(f"{profile}: {info}")

if __name__ == "__main__":
    display_chrome_profiles()

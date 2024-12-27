# # # #!/usr/bin/env python3
# # # # -*- coding: utf-8 -*-

# # # import os
# # # import json
# # # from pathlib import Path
# # # from rich.console import Console

# # # console = Console()

# # # def get_chrome_profiles():
# # #     profiles = []
# # #     chrome_path = Path.home() / ".config" / "google-chrome"
# # #     if chrome_path.exists():
# # #         for profile in chrome_path.iterdir():
# # #             if profile.is_dir() and (profile.name.startswith("Profile ") or profile.name == "Default"):
# # #                 profiles.append(profile.name)
# # #     return profiles

# # # def get_profile_users():
# # #     profile_users = {}
# # #     chrome_path = Path.home() / ".config" / "google-chrome"
# # #     for profile in get_chrome_profiles():
# # #         preferences_path = chrome_path / profile / "Preferences"
# # #         if preferences_path.exists():
# # #             user_info = extract_user_info(preferences_path)
# # #             if user_info:
# # #                 profile_users[profile] = user_info
# # #     return profile_users


# # # def extract_user_info(preferences_path):
# # #     try:
# # #         with open(preferences_path, "r", encoding='utf-8') as file:
# # #             data = json.load(file)
            
# # #             # Check for profile name first
# # #             profile_name = data.get("profile", {}).get("name")
            
# # #             # Then check for signed in account
# # #             account_info = data.get("account_info", [])
# # #             if account_info and len(account_info) > 0:
# # #                 email = account_info[0].get("email")
# # #                 if email:
# # #                     # If we have both, use email
# # #                     return email
            
# # #             # If we have a profile name but no email, use the profile name
# # #             if profile_name:
# # #                 return profile_name
            
# # #             # Fall back to "Unnamed Profile" if neither exists
# # #             return "Unnamed Profile"
            
# # #     except (json.JSONDecodeError, KeyError) as e:
# # #         console.print(f"Error reading JSON from Preferences file: {e}", style="bold red")
# # #         return "Unknown"

# # # def display_chrome_profiles():
# # #     profile_users = get_profile_users()
# # #     if not profile_users:
# # #         console.print("No Chrome profiles found.")
# # #         return

# # #     console.print("\nChrome profiles:")
# # #     for profile, info in profile_users.items():
# # #         console.print(f"{profile}: {info}")

# # # if __name__ == "__main__":
# # #     display_chrome_profiles()


# # #!/usr/bin/env python3
# # # -*- coding: utf-8 -*-
# # import os
# # import json
# # from pathlib import Path
# # from rich.console import Console

# # console = Console()

# # def get_chrome_profiles():
# #     profiles = []
# #     chrome_path = Path.home() / ".config" / "google-chrome"
# #     if chrome_path.exists():
# #         for profile in chrome_path.iterdir():
# #             if profile.is_dir() and (profile.name.startswith("Profile ") or profile.name == "Default"):
# #                 profiles.append(profile.name)
# #     return profiles

# # def get_profile_users():
# #     profile_users = {}
# #     chrome_path = Path.home() / ".config" / "google-chrome"
# #     for profile in get_chrome_profiles():
# #         preferences_path = chrome_path / profile / "Preferences"
# #         if preferences_path.exists():
# #             user_info = extract_user_info_multiple(preferences_path)
# #             if user_info:
# #                 profile_users[profile] = user_info
# #     return profile_users

# # def extract_user_info_multiple(preferences_path):
# #     results = {}
    
# #     try:
# #         with open(preferences_path, "r") as file:
# #             data = json.load(file)
            
# #             # Version 1: Original working version
# #             try:
# #                 results["v1"] = {
# #                     "method": "Original",
# #                     "value": data.get("account_info", [{}])[0].get("email") or 
# #                             data.get("profile", {}).get("name") or 
# #                             "Unnamed Profile"
# #                 }
# #             except IndexError:
# #                 results["v1"] = {"method": "Original", "value": "Error"}

# #             # Version 2: Email priority
# #             try:
# #                 account_info = data.get("account_info", [])
# #                 if account_info and account_info[0].get("email"):
# #                     results["v2"] = {"method": "Email Priority", "value": account_info[0]["email"]}
# #                 else:
# #                     profile_name = data.get("profile", {}).get("name")
# #                     results["v2"] = {"method": "Email Priority", "value": profile_name or "Unnamed Profile"}
# #             except IndexError:
# #                 results["v2"] = {"method": "Email Priority", "value": "Error"}

# #             # Version 3: Profile name priority
# #             try:
# #                 profile_name = data.get("profile", {}).get("name")
# #                 if profile_name:
# #                     results["v3"] = {"method": "Profile Priority", "value": profile_name}
# #                 else:
# #                     account_info = data.get("account_info", [])
# #                     email = account_info[0].get("email") if account_info else None
# #                     results["v3"] = {"method": "Profile Priority", "value": email or "Unnamed Profile"}
# #             except IndexError:
# #                 results["v3"] = {"method": "Profile Priority", "value": "Error"}

# #             # Version 4: Combined approach
# #             try:
# #                 profile_name = data.get("profile", {}).get("name")
# #                 account_info = data.get("account_info", [])
# #                 email = account_info[0].get("email") if account_info else None
# #                 gaia_name = data.get("profile", {}).get("gaia_name")
                
# #                 value = email or profile_name or gaia_name or "Unnamed Profile"
# #                 results["v4"] = {"method": "Combined", "value": value}
# #             except IndexError:
# #                 results["v4"] = {"method": "Combined", "value": "Error"}

# #     except Exception as e:
# #         console.print(f"Error reading file: {e}", style="bold red")
# #         return None

# #     return results

# # def display_chrome_profiles():
# #     profile_users = get_profile_users()
# #     if not profile_users:
# #         console.print("No Chrome profiles found.")
# #         return

# #     console.print("\nChrome profiles with different extraction methods:")
# #     for profile, methods in profile_users.items():
# #         console.print(f"\n[bold]{profile}[/bold]:")
# #         for version, info in methods.items():
# #             console.print(f"  {info['method']}: {info['value']}")

# # if __name__ == "__main__":
# #     display_chrome_profiles()

# #!/usr/bin/env python3
# # -*- coding: utf-8 -*-
# import os
# import json
# from pathlib import Path
# from rich.console import Console

# console = Console()

# def get_chrome_profiles():
#    profiles = []
#    chrome_path = Path.home() / ".config" / "google-chrome"
#    if chrome_path.exists():
#        for profile in chrome_path.iterdir():
#            if profile.is_dir() and (profile.name.startswith("Profile ") or profile.name == "Default"):
#                profiles.append(profile.name)
#    return profiles

# # Original working version
# def extract_user_info_v1(preferences_path):
#    try:
#        with open(preferences_path, "r") as file:
#            data = json.load(file)
#            email = data.get("account_info", [{}])[0].get("email", None)
#            if email:
#                return email
#            profile_name = data.get("profile", {}).get("name", None)
#            if profile_name:
#                return profile_name
#            return "Unnamed Profile"
#    except Exception as e:
#        return "Unknown"

# # Email priority version
# def extract_user_info_v2(preferences_path):
#    try:
#        with open(preferences_path, "r") as file:
#            data = json.load(file)
#            account_info = data.get("account_info", [])
#            if account_info and len(account_info) > 0:
#                email = account_info[0].get("email")
#                if email:
#                    return email
#            profile_name = data.get("profile", {}).get("name")
#            if profile_name:
#                return profile_name
#            return "Unnamed Profile"
#    except Exception as e:
#        return "Unknown"

# # Profile name priority
# def extract_user_info_v3(preferences_path):
#    try:
#        with open(preferences_path, "r") as file:
#            data = json.load(file)
#            profile_name = data.get("profile", {}).get("name")
#            if profile_name:
#                return profile_name
#            account_info = data.get("account_info", [])
#            if account_info and len(account_info) > 0:
#                email = account_info[0].get("email")
#                if email:
#                    return email
#            return "Unnamed Profile"
#    except Exception as e:
#        return "Unknown"

# # Combined fields approach
# def extract_user_info_v4(preferences_path):
#    try:
#        with open(preferences_path, "r") as file:
#            data = json.load(file)
#            profile_name = data.get("profile", {}).get("name")
#            account_info = data.get("account_info", [])
#            email = account_info[0].get("email") if account_info else None
#            gaia_name = data.get("profile", {}).get("gaia_name")
#            return email or profile_name or gaia_name or "Unnamed Profile"
#    except Exception as e:
#        return "Unknown"

# # Deep inspection version
# def extract_user_info_v5(preferences_path):
#    try:
#        with open(preferences_path, "r") as file:
#            data = json.load(file)
#            # Try multiple possible paths for user info
#            sources = [
#                data.get("account_info", [{}])[0].get("email"),
#                data.get("profile", {}).get("name"),
#                data.get("profile", {}).get("gaia_name"),
#                data.get("signin", {}).get("email"),
#                data.get("google", {}).get("user_name")
#            ]
#            return next((s for s in sources if s), "Unnamed Profile")
#    except Exception as e:
#        return "Unknown"

# def display_chrome_profiles_v1():
#    print("\n=== Using Original Version (V1) ===")
#    for profile in get_chrome_profiles():
#        preferences_path = Path.home() / ".config" / "google-chrome" / profile / "Preferences"
#        if preferences_path.exists():
#            info = extract_user_info_v1(preferences_path)
#            console.print(f"{profile}: {info}")

# def display_chrome_profiles_v2():
#    print("\n=== Using Email Priority Version (V2) ===")
#    for profile in get_chrome_profiles():
#        preferences_path = Path.home() / ".config" / "google-chrome" / profile / "Preferences"
#        if preferences_path.exists():
#            info = extract_user_info_v2(preferences_path)
#            console.print(f"{profile}: {info}")

# def display_chrome_profiles_v3():
#    print("\n=== Using Profile Priority Version (V3) ===")
#    for profile in get_chrome_profiles():
#        preferences_path = Path.home() / ".config" / "google-chrome" / profile / "Preferences"
#        if preferences_path.exists():
#            info = extract_user_info_v3(preferences_path)
#            console.print(f"{profile}: {info}")

# def display_chrome_profiles_v4():
#    print("\n=== Using Combined Fields Version (V4) ===")
#    for profile in get_chrome_profiles():
#        preferences_path = Path.home() / ".config" / "google-chrome" / profile / "Preferences"
#        if preferences_path.exists():
#            info = extract_user_info_v4(preferences_path)
#            console.print(f"{profile}: {info}")

# def display_chrome_profiles_v5():
#    print("\n=== Using Deep Inspection Version (V5) ===")
#    for profile in get_chrome_profiles():
#        preferences_path = Path.home() / ".config" / "google-chrome" / profile / "Preferences"
#        if preferences_path.exists():
#            info = extract_user_info_v5(preferences_path)
#            console.print(f"{profile}: {info}")

# if __name__ == "__main__":
#    # Comment out the versions you don't want to see
#    display_chrome_profiles_v1()
#    display_chrome_profiles_v2()
#    display_chrome_profiles_v3()
#    display_chrome_profiles_v4()
#    display_chrome_profiles_v5()


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
        print("\nDebug - Checking directory:", chrome_path)
        for item in chrome_path.iterdir():
            print(f"Debug - Found item: {item.name} (is_dir: {item.is_dir()})")
            if item.is_dir():
                # Look for any directory that could be a profile
                if item.name == "Default" or item.name.startswith("Profile"):
                    print(f"Debug - Adding profile: {item.name}")
                    profiles.append(item.name)
    else:
        print(f"Debug - Chrome path not found: {chrome_path}")
    
    # Sort profiles naturally
    profiles.sort(key=lambda x: int(x.split()[-1]) if x != "Default" and x.split()[-1].isdigit() else 0)
    print(f"\nDebug - Total profiles found: {len(profiles)}")
    return profiles

# Original working version
def extract_user_info_v1(preferences_path):
    try:
        with open(preferences_path, "r") as file:
            data = json.load(file)
            email = data.get("account_info", [{}])[0].get("email", None)
            if email:
                return email
            profile_name = data.get("profile", {}).get("name", None)
            if profile_name:
                return profile_name
            return "Unnamed Profile"
    except Exception as e:
        return "Unknown"

# Email priority version
def extract_user_info_v2(preferences_path):
    try:
        with open(preferences_path, "r") as file:
            data = json.load(file)
            account_info = data.get("account_info", [])
            if account_info and len(account_info) > 0:
                email = account_info[0].get("email")
                if email:
                    return email
            profile_name = data.get("profile", {}).get("name")
            if profile_name:
                return profile_name
            return "Unnamed Profile"
    except Exception as e:
        return "Unknown"

# Profile name priority
def extract_user_info_v3(preferences_path):
    try:
        with open(preferences_path, "r") as file:
            data = json.load(file)
            profile_name = data.get("profile", {}).get("name")
            if profile_name:
                return profile_name
            account_info = data.get("account_info", [])
            if account_info and len(account_info) > 0:
                email = account_info[0].get("email")
                if email:
                    return email
            return "Unnamed Profile"
    except Exception as e:
        return "Unknown"

# Combined fields approach
def extract_user_info_v4(preferences_path):
    try:
        with open(preferences_path, "r") as file:
            data = json.load(file)
            profile_name = data.get("profile", {}).get("name")
            account_info = data.get("account_info", [])
            email = account_info[0].get("email") if account_info else None
            gaia_name = data.get("profile", {}).get("gaia_name")
            return email or profile_name or gaia_name or "Unnamed Profile"
    except Exception as e:
        return "Unknown"

# Deep inspection version
def extract_user_info_v5(preferences_path):
    try:
        with open(preferences_path, "r", encoding='utf-8') as file:
            data = json.load(file)
            print(f"Debug - Raw profile data for {preferences_path}:")
            print(json.dumps(data.get("profile", {}), indent=2))
            print(json.dumps(data.get("account_info", []), indent=2))
            
            # Try multiple possible paths for user info
            sources = [
                data.get("account_info", [{}])[0].get("email"),
                data.get("profile", {}).get("name"),
                data.get("profile", {}).get("gaia_name"),
                data.get("signin", {}).get("email"),
                data.get("google", {}).get("user_name")
            ]
            result = next((s for s in sources if s), "Unnamed Profile")
            print(f"Debug - Selected value: {result}")
            return result
    except Exception as e:
        print(f"Debug - Error in v5: {str(e)}")
        return "Unknown"

def display_chrome_profiles_v1():
    print("\n=== Using Original Version (V1) ===")
    profiles = get_chrome_profiles()
    for profile in profiles:
        preferences_path = Path.home() / ".config" / "google-chrome" / profile / "Preferences"
        if preferences_path.exists():
            print(f"Debug - Reading preferences from: {preferences_path}")
            info = extract_user_info_v1(preferences_path)
            console.print(f"{profile}: {info}")
        else:
            print(f"Debug - No preferences file found for: {profile}")

def display_chrome_profiles_v2():
    print("\n=== Using Email Priority Version (V2) ===")
    profiles = get_chrome_profiles()
    for profile in profiles:
        preferences_path = Path.home() / ".config" / "google-chrome" / profile / "Preferences"
        if preferences_path.exists():
            print(f"Debug - Reading preferences from: {preferences_path}")
            info = extract_user_info_v2(preferences_path)
            console.print(f"{profile}: {info}")
        else:
            print(f"Debug - No preferences file found for: {profile}")

def display_chrome_profiles_v3():
    print("\n=== Using Profile Priority Version (V3) ===")
    profiles = get_chrome_profiles()
    for profile in profiles:
        preferences_path = Path.home() / ".config" / "google-chrome" / profile / "Preferences"
        if preferences_path.exists():
            print(f"Debug - Reading preferences from: {preferences_path}")
            info = extract_user_info_v3(preferences_path)
            console.print(f"{profile}: {info}")
        else:
            print(f"Debug - No preferences file found for: {profile}")

def display_chrome_profiles_v4():
    print("\n=== Using Combined Fields Version (V4) ===")
    profiles = get_chrome_profiles()
    for profile in profiles:
        preferences_path = Path.home() / ".config" / "google-chrome" / profile / "Preferences"
        if preferences_path.exists():
            print(f"Debug - Reading preferences from: {preferences_path}")
            info = extract_user_info_v4(preferences_path)
            console.print(f"{profile}: {info}")
        else:
            print(f"Debug - No preferences file found for: {profile}")

def display_chrome_profiles_v5():
    print("\n=== Using Deep Inspection Version (V5) ===")
    profiles = get_chrome_profiles()
    for profile in profiles:
        preferences_path = Path.home() / ".config" / "google-chrome" / profile / "Preferences"
        if preferences_path.exists():
            print(f"Debug - Reading preferences from: {preferences_path}")
            info = extract_user_info_v5(preferences_path)
            console.print(f"{profile}: {info}")
        else:
            print(f"Debug - No preferences file found for: {profile}")

if __name__ == "__main__":
    print("Debug - Starting profile scan...")
    # Comment out the versions you don't want to see
    display_chrome_profiles_v1()
    display_chrome_profiles_v2()
    display_chrome_profiles_v3()
    display_chrome_profiles_v4()
    display_chrome_profiles_v5()
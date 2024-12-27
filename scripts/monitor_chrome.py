#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import json
import time
import psutil
import subprocess
from pathlib import Path
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from datetime import datetime

console = Console()
OUTPUT_FILE = Path.home() / "chrome_profile_activity.txt"

class ChromeProfileHandler(FileSystemEventHandler):
    def __init__(self):
        self.last_processed = set()
        self.activity_count = 0
        self.last_check = 0
        self.chrome_running = False
        
    def check_chrome_processes(self):
        current_time = time.time()
        # Only check every second to avoid too frequent checks
        if current_time - self.last_check < 1:
            return
            
        self.last_check = current_time
        chrome_was_running = self.chrome_running
        self.chrome_running = False
        
        for proc in psutil.process_iter(['name', 'cmdline']):
            try:
                if 'chrome' in proc.info['name'].lower():
                    self.chrome_running = True
                    # If Chrome just started, scan all profiles
                    if not chrome_was_running:
                        self.scan_all_profiles()
                    break
            except (psutil.NoSuchProcess, psutil.AccessDenied):
                pass

    def scan_all_profiles(self):
        chrome_path = Path.home() / ".config" / "google-chrome"
        if not chrome_path.exists():
            return
            
        for profile_dir in chrome_path.iterdir():
            if profile_dir.is_dir() and (profile_dir.name.startswith("Profile") or profile_dir.name == "Default"):
                preferences_path = profile_dir / "Preferences"
                if preferences_path.exists():
                    self.process_profile_change(str(preferences_path), force=True)

    def on_modified(self, event):
        if event.is_directory:
            return
        if any(x in event.src_path.lower() for x in ["preferences", "secure preferences", "login data"]):
            self.process_profile_change(event.src_path)
        
        # Check Chrome process status on any file change
        self.check_chrome_processes()
            
    def process_profile_change(self, preferences_path, force=False):
        if not force and preferences_path in self.last_processed:
            return
            
        self.last_processed.add(preferences_path)
        if len(self.last_processed) > 100:
            self.last_processed.clear()
            
        try:
            # Get both basic and detailed profile info
            basic_info = extract_user_info_v5(preferences_path)
            detailed_info = get_detailed_profile_info(preferences_path)
            profile_dir = os.path.basename(os.path.dirname(preferences_path))
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            
            # Create detailed log entry
            log_entry = (f"\n=== Profile Activity at {timestamp} ===\n"
                        f"Profile Directory: {profile_dir}\n"
                        f"Basic Info: {basic_info}\n"
                        f"Detailed Info:\n{detailed_info}\n")
            
            # Write to file
            with open(OUTPUT_FILE, "a") as f:
                f.write(log_entry)
            
            # Display in terminal
            self.activity_count += 1
            
            table = Table(title=f"Profile Activity Detected #{self.activity_count}")
            table.add_column("Field", style="cyan")
            table.add_column("Value", style="green", overflow="fold")
            
            table.add_row("Timestamp", timestamp)
            table.add_row("Profile Directory", profile_dir)
            table.add_row("Basic Info", basic_info)
            table.add_row("Details", detailed_info)
            
            console.print("\n")
            console.print(Panel(table, title="Chrome Profile Activity"))
            console.print(f"[dim]Total activities logged: {self.activity_count}[/dim]")
            
        except Exception as e:
            console.print(Panel(f"Error processing profile: {e}", style="red bold"))

def get_detailed_profile_info(preferences_path):
    try:
        with open(preferences_path, "r", encoding='utf-8') as file:
            data = json.load(file)
            details = []
            
            # Check account info
            account_info = data.get("account_info", [])
            if account_info:
                for account in account_info:
                    details.append(f"Email: {account.get('email', 'None')}")
                    details.append(f"Gaia: {account.get('gaia', 'None')}")
            
            # Check profile info
            profile = data.get("profile", {})
            if profile:
                details.append(f"Name: {profile.get('name', 'None')}")
                details.append(f"Gaia Name: {profile.get('gaia_name', 'None')}")
                
            # Check signin info
            signin = data.get("signin", {})
            if signin:
                details.append(f"Signin: {signin.get('email', 'None')}")
            
            return "\n".join(details)
    except Exception as e:
        return f"Error getting details: {str(e)}"

def extract_user_info_v5(preferences_path):
    try:
        with open(preferences_path, "r", encoding='utf-8') as file:
            data = json.load(file)
            sources = [
                data.get("account_info", [{}])[0].get("email"),
                data.get("profile", {}).get("name"),
                data.get("profile", {}).get("gaia_name"),
                data.get("signin", {}).get("email"),
                data.get("google", {}).get("user_name")
            ]
            return next((s for s in sources if s), "Unnamed Profile")
    except Exception as e:
        return f"Unknown (Error: {str(e)})"

def start_monitoring():
    chrome_path = Path.home() / ".config" / "google-chrome"
    if not chrome_path.exists():
        console.print(Panel("Chrome profile directory not found!", style="red bold"))
        return

    # Create or clear the output file
    OUTPUT_FILE.touch()
    with open(OUTPUT_FILE, "w") as f:
        f.write(f"=== Chrome Profile Activity Log ===\nStarted: {datetime.now()}\n\n")

    event_handler = ChromeProfileHandler()
    observer = Observer()
    observer.schedule(event_handler, str(chrome_path), recursive=True)
    
    startup_table = Table(title="Chrome Profile Monitor Started")
    startup_table.add_column("Setting", style="cyan")
    startup_table.add_column("Value", style="green")
    
    startup_table.add_row("Monitor Status", "Active")
    startup_table.add_row("Chrome Path", str(chrome_path))
    startup_table.add_row("Log File", str(OUTPUT_FILE))
    startup_table.add_row("Start Time", datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    
    console.print("\n")
    console.print(Panel(startup_table, border_style="green"))
    console.print("[dim]Waiting for profile activity...[/dim]")
    
    observer.start()
    try:
        while True:
            event_handler.check_chrome_processes()
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
        console.print(Panel("Monitoring stopped by user", style="yellow bold"))
    
    observer.join()

if __name__ == "__main__":
    start_monitoring()
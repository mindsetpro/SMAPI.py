#|===================================|
#|SMAPI.py | Main.py                 |
#|===================================|

from ToolKit import *     import requests
from Installer import *   import aiohttp
import bs4                import asyncio
import shutil             import harmony
import os                 import subprocess


# Mod patcher
# Patches and makes the exe with the mods
# Function to patch Stardew Valley executable with DLL mods using Harmony
def patch_stardew_valley_exe(exe_path, mod_dll_paths):
    # Check if the executable exists
    if not os.path.exists(exe_path):
        print("Error: Stardew Valley executable not found.")
        return

    # Create a backup of the original executable
    backup_exe_path = exe_path + ".bak"
    shutil.copyfile(exe_path, backup_exe_path)

    try:
        # Initialize Harmony
        harmony.patch_all(exe_path)

        # Inject DLL mods using Harmony
        for dll_path in mod_dll_paths:
            harmony.inject_dll(exe_path, dll_path)

        print("Patching successful.")
    except Exception as e:
        # Restore the original executable if an error occurs
        shutil.move(backup_exe_path, exe_path)
        print(f"Error: Failed to patch executable. {str(e)}")
        return
    finally:
        # Remove the backup executable
        os.remove(backup_exe_path)

# Example usage:
if __name__ == "__main__":
    # Path to the Stardew Valley executable
    stardew_valley_exe_path = 'Stardew Valley.exe'

    # Paths to the DLL mods
    mod_dll_paths = ['CJBItemSpawner.dll', 'CJBCheatsMenu.dll', 'TractorMod.dll']

    # Patch the Stardew Valley executable
    patch_stardew_valley_exe(stardew_valley_exe_path, mod_dll_paths)
  

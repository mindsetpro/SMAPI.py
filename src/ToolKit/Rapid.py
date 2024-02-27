# Rapid.py

import os
from harmony import Harmony
from ctypes import CDLL

class ModLoader:
    def __init__(self, mods_folder, game_exe):
        self.mods_folder = mods_folder
        self.game_exe = game_exe
        self.mods = []

    def load_mods(self):
        print("[SMAPI.py Mod Loader]: Loading mods...\n")
        for mod_file in os.listdir(self.mods_folder):
            if mod_file.endswith('.dll'):
                mod_path = os.path.join(self.mods_folder, mod_file)
                mod_name = mod_file[:-4]  # Remove .dll extension
                self.load_mod(mod_name, mod_path)
        print("\nMods loaded successfully!\n")

    def load_mod(self, mod_name, mod_path):
        mod = CDLL(mod_path)
        self.mods.append((mod_name, mod))
        print(f"[SMAPI.py]: Loaded {mod_name}")
        self.patch_mod_into_executable(mod_path)

    def patch_mod_into_executable(self, mod_path):
        with Harmony(self.game_exe) as harmony:
            harmony.apply_patch(mod_path)

    def run_mod_hooks(self, hook_name, *args, **kwargs):
        for _, mod in self.mods:
            hook = getattr(mod, hook_name, None)
            if hook:
                hook(*args, **kwargs)

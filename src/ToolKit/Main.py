# Main.py

from Toolkit.Rapid import ModLoader

def main():
    mods_folder = "Mods"  # Specify the folder where your mods are
    game_exe = "Stardew Valley.exe"  # Specify the path to Stardew Valley executable
    mod_loader = ModLoader(mods_folder, game_exe)
    mod_loader.load_mods()
    mod_loader.run_mod_hooks("on_game_start")

if __name__ == "__main__":
    main()

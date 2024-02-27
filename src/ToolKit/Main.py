# main.py

from Rapid import ModLoader
from Toolkit import ToolkitError, TerminalMenu

def main():
    try:
        mods_folder = "Mods"  # Specify the folder where your mods are
        game_exe = "Stardew Valley.exe"  # Specify the path to Stardew Valley executable
        mod_loader = ModLoader(mods_folder, game_exe)

        # Display menu
        TerminalMenu.display_menu("Stardew Valley Mod Loader Menu", [
            "Load Mods",
            "Exit"
        ])

        choice = TerminalMenu.select_option(["Load Mods", "Exit"])

        if choice == 1:
            mod_loader.load_mods()
            mod_loader.run_mod_hooks("on_game_start")
            TerminalMenu.success_message("Mods loaded successfully!")
        elif choice == 2:
            TerminalMenu.success_message("Exiting...")
            return
    except ToolkitError as e:
        TerminalMenu.error_message(str(e))

if __name__ == "__main__":
    main()

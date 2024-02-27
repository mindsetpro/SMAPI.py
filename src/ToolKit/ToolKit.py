# Toolkit.py

class ToolkitError(Exception):
    pass

class TerminalMenu:
    @staticmethod
    def display_menu(title, options):
        print(title)
        for index, option in enumerate(options, start=1):
            print(f"{index}. {option}")
        print()

    @staticmethod
    def select_option(options):
        while True:
            try:
                choice = int(input("Choose an option: "))
                if choice < 1 or choice > len(options):
                    raise ValueError
                return choice
            except ValueError:
                print("Invalid choice. Please enter a number corresponding to an option.")

    @staticmethod
    def error_message(message):
        print(f"Error: {message}\n")

    @staticmethod
    def success_message(message):
        print(f"Success: {message}\n")

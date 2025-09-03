import json
import rich
import os
from rich import print as rprint
from rich.prompt import Prompt

try:
    def loadfile(filename="logo.txt"):
        try:
            with open(filename, 'r', encoding="UTF-8") as f:
                return f.read()
        except:
            return "ERROR"

    start_actions = ["Make new character", "Edit existing characters", "Export character", "Edit settings"]

    print(f"\n{loadfile()}\n")
    rprint("Welcome to Character Manager!")
    for i, name in enumerate(start_actions, 1):
        print(f"{i}. {name}")
    print()

    start_choice = Prompt.ask("Choice: ")
    print()

    if start_choice == "1":
        pass
    elif start_choice == "2":
        pass
    elif start_choice == "3":
        pass
    elif start_choice == "4":
        settings = ["Character library path"]
        for i, name in enumerate(settings, 1):
            print(f"{i}. {name}")
        print()
        settings_choice = input("Choice: ")
        print()

        if settings_choice == "1":
            with open("settings.json", "w") as f:
                json.dump(new_path, f)
        else:
            os.system(f"python3 {__file__}")
        
except KeyboardInterrupt:
    exit("\nGoodbye!")
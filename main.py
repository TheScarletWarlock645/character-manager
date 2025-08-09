import json
import rich
from rich import print as rprint

try:
    print()
    print("Welcome to Character Manager!")
    print()
    startActions = ["Make new character", "Edit existing character","Export character sheet"]
    for i, item in enumerate(startActions, 1):
        print(f"{i}. {item}")

    print()
    startChoice = int(input("Enter an option: "))
    if startChoice == 1:
        createChoice = int(input("Guided or non guided character creation? (1, 2) "))

        if createChoice == 1:
            print("You chose: guided character creation")
        elif createChoice == 2:
            print("You chose: non-guided character creation")

    elif startChoice == 2:
        print()
    elif startChoice == 3:
        print()
    else:
        print()
        rprint("[bold red]ERROR: Please enter a valid number.[/bold red]")
        exit()

except KeyboardInterrupt:
    print("goodbye")
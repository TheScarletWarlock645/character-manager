import json
import os
import rich
from rich import print as rprint

try:
    print()
    print("Welcome to Character Manager!")
    print()
    startActions = ["Make new character", "Edit existing character","Export character sheet", "Make or change character library"]
    for i, item in enumerate(startActions, 1):
        print(f"{i}. {item}")

    print()
    startChoice = int(input("Enter an option: "))
    if startChoice == 1:
        createChoice = int(input("Guided or non guided character creation? (1, 2) "))

        statList = ["Name", "Class and level", "Race", "Background", "Alignment", "XP", "Prof bonus", "Ability scores", "Ability profs", "Skill profs",
        "Other profs and languages", "Armour class", "Initiative", "Speed", "HP", "Hit dice", "Money", "Equipment", "Features and traits", "Attacks and spellcasting"]
        statListList = len(statList) // 2

        if createChoice == 1:
            print()
            print("You chose: guided character creation")
            print()

        elif createChoice == 2:
            print()
            print("You chose: non-guided character creation")
            print("Choose a stat to edit:")
            print()
            for i in range(statListList):
                left = f"{i+1}. {statList[i]}"
                right = f"{i+1+statListList}. {statList[i+statListList]}"
                print(f"{left:<30} {right}")


    elif startChoice == 2:
        print()
    elif startChoice == 3:
        print()
    elif startChoice == 4:
        print()
        settingsChange = int(input("Would you like to change the character library path or make a new directory? (1, 2) "))
        print()
        
        if settingsChange == 1:
            chCarLib = input("Enter new path for ")
            newPath = {
                "CharLibPath": f"{chCarLib}"
            }
            with open('settings.json', 'w') as f:
                json.dump(newPath, f)

    else:
        print()
        rprint("[bold red]ERROR: Please enter a valid number.[/bold red]")
        exit()

except KeyboardInterrupt:
    print("goodbye")
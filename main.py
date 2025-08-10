import json
import os
import rich
from rich import print as rprint
from rich.prompt import Prompt

try:
    statList = ["Name", "Class and level", "Race", "Background", "Alignment", "XP", "Prof bonus", "Ability scores", "Ability profs", "Skill profs",
    "Other profs and languages", "Armour class", "Initiative", "Speed", "HP", "Hit dice", "Money", "Equipment", "Features and traits", "Attacks and spellcasting"]
    statListList = len(statList) // 2

    classList = ["Barbarian", "Bard", "Cleric", "Druid", "Fighter", "Monk", "Paladin", "Ranger", "Rogue", "Sorcerer", "Warlock", "Wizard"]
    classListList = len(classList) // 2

    raceList = ["Dragonborn", "Dwarf", "Elf", "Gnome", "Half-elf", "Half-orc", "Halfling", "Human", "Tiefling"]
    raceListList = len(raceList) // 2

    def getValue(file, value):
        with open(f'{file}', 'r') as f:
            setting = json.load(f)
        return setting[value]

    def className(number):
        try:
            return str(classList[int(number) - 1])
        except:
            rprint("[bold red]ERROR: Please enter a valid option.[/bold red]")
    print()
    print("Welcome to Character Manager!")
    print()
    startActions = ["Make new character", "Edit existing character","Export character sheet", "Make or change character library"]
    for i, item in enumerate(startActions, 1):
        print(f"{i}. {item}")
        rprint("[bold red]ERROR: Please enter a valid number.[/bold red]")
        exit()

    print()
    startChoice = int(input("Enter an option: "))
    if startChoice == 1:
        createChoice = int(input("Guided or non guided character creation? (1, 2) "))

        if createChoice == 1:
            print()
            print("You chose: guided character creation")
            print()

        elif createChoice == 2:
            print()
            print("You chose: non-guided character creation")
            print()
            for i in range(statListList):
                left = f"{i+1}. {statList[i]}"
                right = f"{i+1+statListList}. {statList[i+statListList]}"
                print(f"{left:<30} {right}")
            print("21. Save character")
            print()
            statChoice = int(input("Choose a stat to edit: "))
            print()

            if statChoice == 1:
                name  = input("Enter a first and last name for your character: ")
                os.environ['NAME'] = str(name.replace(" ", "-").lower())
            elif statChoice == 2:
                for i in range(classListList):
                    left = f"{i+1}. {classList[i]}"
                    right = f"{i+1+classListList}. {classList[i+classListList]}"
                    print(f"{left:<15} {right}")
                print()
                charClass = input("Choose a class for your character: ")
                os.environ['CLASS'] = str(className(charClass))
                
                level = int(input("Enter a level for your character: (1-20) "))
                if level > 20:
                    rprint("ERROR: Please enter a valid level.")
                elif level < 1:
                    rprint("ERROR: Please enter a valid level.")
                elif level ==str:
                    rprint("ERROR: Please enter a valid level.")
                else:
                    os.environ['LEVEL'] = str(level)

            elif statChoice == 3:
            elif statChoice == 4:
            elif statChoice == 5:
            elif statChoice == 6:
            elif statChoice == 7:
            elif statChoice == 8:
            elif statChoice == 9:
            elif statChoice == 10:
            elif statChoice == 11:
            elif statChoice == 12:
            elif statChoice == 13:
            elif statChoice == 14:
            elif statChoice == 15:
            elif statChoice == 16:
            elif statChoice == 17:
            elif statChoice == 18:
            elif statChoice == 19:
            elif statChoice == 20:
            elif statChoice == 21:
                charData = {
                    "name": f"{os.environ.get['NAME']}"
                    "classLevel": {
                        "class": f"{os.environ.get['CLASS']}"
                        "level": f"{int(os.environ.get['LEVEL'])}"
                    }
                }
                charName = name.replace(" ", "-").lower()
                libPath = getValue(char.json, CharlibPath)
                os.system(f"touch {libPath}{charname}.json")

                with open(f'{libPath}{charName}.json', 'w') as f:
                    json.dump(charData, f)
            else:
                print()
                rprint("[bold red]ERROR: Please enter a valid number.[/bold red]")
                exit()
            

    elif startChoice == 2:
        print()
    elif startChoice == 3:
        print()
    elif startChoice == 4:
        print()
        settingsChange = int(input("Would you like to change the character library path or make a new directory? (1, 2) "))
        print()
        
        if settingsChange == 1:
            chCarLib = input("Enter new path for character library: (make sure the path ends with a /)")
            newPath = {
                "CharLibPath": f"{chCarLib}"
            }
            with open('settings.json', 'w') as f:
                json.dump(newPath, f)
        elif settingsChange == 2:
            dirName = input("Choose a name for the directory: ")
            newDirName = dirName.replace(" ", "-").lower()
            os.system(f"mkdir ~/{newDirName}/")

            newPath = {
                "CharLibPath": f"~/{newDirName}"
            }
            with open('settings.json', 'w') as f:
                json.dump(newPath, f)

    else:
        print()
        rprint("[bold red]ERROR: Please enter a valid number.[/bold red]")
        exit()

except KeyboardInterrupt:
    quitWarning = Prompt.ask("[bold yellow]WARNING: Quitting now will delete any unsaved changed. Quit? (y/N)").strip()
    if quitWarning.lower() in ["", "n", "no"]:
        print()
    else:
        print()
        rprint("Goodbye [bold yellow]:))[/bold yellow]")
        exit()
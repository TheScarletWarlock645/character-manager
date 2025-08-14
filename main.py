import json
import random
import sys
import math
import os
import rich
import subprocess
from rich import print as rprint
from rich.prompt import Prompt
from rich.table import Table
from rich.console import Console

#os.environ['PRODUCTION'] = str("true")

if os.environ.get('PRODUCTION') == "true":
    sys.tracebacklimit = 0

try:
    console = Console()

    statList = ["Name", "Class and level", "Race", "Background", "Alignment", "XP", "Prof bonus", "Ability scores", "Ability profs", "Skill profs",
    "Other profs and languages", "Armour class", "Initiative", "Speed", "HP", "Hit dice", "Money", "Equipment", "Features and traits", "Attacks and spellcasting"]
    statListList = len(statList) // 2

    classList = ["Barbarian", "Bard", "Cleric", "Druid", "Fighter", "Monk", "Paladin", "Ranger", "Rogue", "Sorcerer", "Warlock", "Wizard"]
    classListList = len(classList) // 2

    raceList = ["Dragonborn", "Dwarf", "Elf", "Gnome", "Half-elf", "Half-orc", "Halfling", "Human", "Tiefling"]
    raceListList = len(raceList) // 2

    startActions = ["Make new character", "Edit existing character","Export character sheet", "Make or change character library"]

    def valueEnv(var):
        value = os.environ.get(var)
        if value and value.strip():
            return value
        else:
            return

    def loadLogo(filename="logo.txt"):
        try:
            with open(filename, 'r', encoding="UTF-8") as logo:
                return logo.read()
        except:
            return "!ERROR: Logo not found!"

    def getValue(file, key, unwrap_single_lists=True):
        try:
            with open(file, "r") as f:
                data = json.load(f)
            keys = key.split(".")
            current = data

            for k in keys:
                if isinstance(current, dict) and k in current:
                    current = current[k]
                elif isinstance(current, list) and k.isdigit():
                    idx = int(k)
                    if 0 <= idx < len(current):
                        current = current[idx]
                    else:
                        return None
                else:
                    return None
            
            if unwrap_single_lists and isinstance(current, list) and len(current) == 1:
                return current[0]

            return current
            
        except (FileNotFoundError, json.JSONDecodeError, KeyError) as e:
            return f"{e}"

    def listBaseStats(filePath):
        try:
            with open(filePath, 'r') as f:
                stats = json.load(f)
            name = data.get('name', 'N/A')
            charClass = data.get('classLevel', {}).get('class', 'N/A') if isinstance(data.get('classLevel'), dict) else 'N/A'
            level = data.get('classLevel', {}).get('level', 'N/A') if isinstance(data.get('classLevel'), dict) else 'N/A'

            return name, charClass, level

        except (json.JSONDecodeError, IOError) as e:
            return f"ERROR: {e}"


    def paramName(number, var):
        try:
            return str(var[int(number) - 1])
        except:
            rprint("[bold red]ERROR: Please enter a valid option.[/bold red]")

    def listChars():
        table = Table(title="Characters")

        table.add_column("ID", justify="right", style="green")
        table.add_column("Name", style="magenta")
        table.add_column("Level", justify="left", style="cyan")
        table.add_column("Class", justify="left",style="cyan")

        try:
            libPath = os.path.expanduser(getValue("settings.json", "CharLibPath"))
            result = subprocess.run(['ls', os.path.expanduser(libPath)], capture_output= True, text= True, check= True)
            
            files = result.stdout.strip().split('\n')
            files = [f for files in f if f]
            if not files:
                rprint(f"[bold red]ERROR: No files in directory: {libPath}[/bold red]")
                return
            for i, filename in enumerate(files, 1):
                filePath = os.path.join(libPath, filename)
                name, charClass, level = listBaseStats(filePath)
                table.add_row(f"{i}", f"{name.replace("-", " ").title()}", f"{level}", f"{charClass}")

                console.print(table)

        except subprocess.CalledProcessError as e:
            rprint(f"[bold red]ERROR: Error listing directory: {e}[/bold red]")
        except Exception as e:
            rprint(f"[bold red]ERROR: Unexpected error: {e}[/bold red]")

    def rollDice(dice, count):
        def d6():
            value = sum(random.randint(1, 6) for _ in range(int(count)))
            return value
        def d8():
            value = random.randint(1, 8)
            return value
        def d10():
            value = random.randint(0, 9)
            return value
        def d12():
            value = random.randint(1, 12)
            return value
        def d20():
            value = random.randint(1, 20)
            return value
        
        target = locals()[dice]
        result = target()
        return result
    
    def convertScores(strth, dex, intel, wis, con, char):
        def formula(stat):
            stepOne = int(stat) - 10
            stepTwo = stepOne // 2
            stepThree = math.floor(stepTwo)

            if stepThree < 0:
                return str(f"{stepThree}")
            elif stepThree >= 0:
                return str(f"+{stepThree}")

        resultStr = formula(strth)
        resultDex = formula(dex)
        resultInt = formula(intel)
        resultWis = formula(wis)
        resultCon = formula(con)
        resultChar = formula(char)

        return resultStr, resultDex, resultInt, resultWis, resultCon, resultChar

    print(f"\n{loadLogo()}\n")
    for i, item in enumerate(startActions, 1):
        print(f"{i}. {item}")
    print()
    startChoice = input("Enter an option: ")
    if startChoice == "1":
        createChoice = Prompt.ask("Guided or non guided character creation? [bold green](1, 2)[/bold green] ")

        if createChoice == "1":
            rprint("You chose: [bold green]guided character creation[/bold green]\n")
            rprint("Welcome to guided character creation! This will walk you through creating a character\nfor the first time or maybe just refresh your skills.\n[bold green]After each step, press enter to proceed.[/bold green]\n\n")
            print("The first step will be choosing a race for your character. This step will determine things lke your name and features in the future.\n")
            for i in range(raceListList):
                left = f"{raceList[i]}"
                right = f"{raceList[i+raceListList]}"
                print(f"{left:<15} {right}")
            print()
            race = Prompt.ask("Choose a race for your character: [bold green](Please ensure it is spelled correctly)[/bold green]").lower()
            while True:
                print("\nNext, choose a gender for your character. This will determine which the example names that will show up. Choosing other will\nshow male and female names.\n")
                genderInput = Prompt.ask("Choose a gender for your character: [bold green]male(m)/female(f)/other(o)[/bold green]")
                if genderInput == "m":
                    names = getValue("names.json", f"{race}.m")
                    break
                elif genderInput == "f":
                    names = getValue("names.json", f"{race}.f")
                    break
                elif genderInput == "o":
                    names = f"{getValue("names.json", f"{race}.m")} {getValue("names.json", f"{race}.m")}"
                    break
                else:
                    rprint("[bold red]ERROR: Please enter a valid gender: male(m)/female(f)/other(o)[/bold red]")
                    continue
            
            print(f"\n{names}\n")
            rprint("[bold green]Don't forget you can make up your own name too![/bold green]\n")
            firstName = Prompt.ask("Enter a first name for your character: ")
            lastName = Prompt.ask("Enter a last name for your character: ")

            name = f"{firstName.lower()}-{lastName.lower()}"
            rprint(f"\n[bold yellow]Nice to meet you {name.replace("-", " ").title()}![/bold yellow]\n")

            # Begin again here

        elif createChoice == "2":
            rprint("You chose: [bold green]non-guided character creation[/bold green]")
            while True:
                name = valueEnv('NAME')
                classLevel = valueEnv('CLASS_LEVEL')
                race = valueEnv('RACE')
                background = valueEnv('BACKGROUND')
                align = valueEnv('ALIGNMENT')
                xp = valueEnv('XP')
                profBonus = valueEnv('PROFICIENCY_BONUS')
                abilityScores = valueEnv('ABILITY_SCORES')
                abilityProfs = valueEnv('ABILITY_PROFIENCIES')
                skillProfs = valueEnv('SKILL_PROFICIENCIES')
                miscProfs = valueEnv('MISC_PROFS')
                armourClass = valueEnv('ARMOUR_CLASS')
                initiative = valueEnv('INITIATIVE')
                speed = valueEnv('SPEED')
                hp = valueEnv('HP')
                hitDice = valueEnv('HIT_DICE')
                money = valueEnv('MONEY')
                equipment = valueEnv('EQUIPMENT')
                featuresTraits = valueEnv('FEATURES_AND_TRAITS')
                atkSpells = valueEnv('ATTACK_SPELLS')

                statValue = {"Name": name, "Class and level": classLevel, "Race": race, "Background": background, "alignment": align, "XP": xp, "Prof bonus": profBonus,
                "Ability scores": abilityScores, "Ability profs": abilityProfs, "Skill profs": skillProfs, "Other profs and languages": miscProfs, "Armour class": armourClass,
                "Initiative": initiative, "Speed": speed, "HP": hp, "Hit dice": hitDice, "Money": money, "Equipment": equipment, "Features and traits": featuresTraits,
                "Attacks and spellcasting": atkSpells}

                print()
                extra = statValue.get(item, "")
                for i in range(statListList):
                    left = f"{i+1}. {statList[i]}: {extra}"
                    right = f"{i+1+statListList}. {statList[i+statListList]}: {extra}"
                    print(f"{left:<30} {right}")
                print()
                rprint("[bold green]Save character[/bold green] (s)\n")
                statChoice = input("Choose a stat to edit: ")
                print()

                if statChoice == "1":
                    name  = input("Enter a first and last name for your character: ")
                    os.environ['NAME'] = str(name.replace(" ", "-").lower())
                    continue
                elif statChoice == "2":
                    for i in range(classListList):
                        left = f"{i+1}. {classList[i]}"
                        right = f"{i+1+classListList}. {classList[i+classListList]}"
                        print(f"{left:<15} {right}")
                    print()
                    charClassOG = input("Choose a class for your character: ")
                    charClass = str(paramName(classList, charClass))
                    
                    level = int(input("Enter a level for your character: (1-20) "))
                    if level > 20:
                        rprint("ERROR: Please enter a valid level.")
                    elif level < 1:
                        rprint("ERROR: Please enter a valid level.")
                    else:
                        os.environ['CLASS_LEVEL'] = str(f"{level}, {charClass}")
                        continue

                elif statChoice == "3":
                    for i in range(raceListList):
                        left = f"{i+1}. {raceList[i]}"
                        right = f"{i+1+raceListList}. {raceList[i+raceListList]}"
                        print(f"{left:<15} {right}")
                    print()
                    race = int(input("Choose a race: "))
                    os.environ['RACE'] = str(paramName(raceList, race))
                    continue

                #elif statChoice == "4":
                #elif statChoice == "5":
                #elif statChoice == "6":
                #elif statChoice == "7":
                #elif statChoice == "8":
                #elif statChoice == "9":
                #elif statChoice == "10":
                #elif statChoice == "11":
                #elif statChoice == "12":
                #elif statChoice == "13":
                #elif statChoice == "14":
                #elif statChoice == "15":
                #elif statChoice == "16":
                #elif statChoice == "17":
                #elif statChoice == "18":
                #elif statChoice == "19":
                #elif statChoice == "20":
                elif statChoice == "s":
                    charData = {
                        "name": f"{os.environ.get('NAME')}",
                        "classLevel": {
                            "class": f"{os.environ.get('CLASS')}",
                            "level": int(os.environ.get('LEVEL'))
                        }
                    }
                    charName = name.replace(" ", "-").lower()
                    libPath = getValue("char.json", "CharLibPath")
                    os.system(f"touch {libPath}{charname}.json")

                    with open(f'{libPath}{charName}.json', 'w') as f:
                        json.dump(charData, f)
                    
                    rprint("[bold green]Character saved succesfully![/bold green]")
                else:
                    print()
                    rprint("[bold red]ERROR: Please enter a valid number.[/bold red]")
                    exit()

        else:
            print()
            rprint("[bold red]ERROR: Please enter a valid number.[/bold red]")
            exit()

    elif startChoice == "2":
        print()
    elif startChoice == "3":
        print()
    elif startChoice == "4":
        print()
        settingsChange = input("Would you like to change the character library path or make a new directory? (1, 2) ")
        print()
        
        if settingsChange == "1":
            chCarLib = input("Enter new path for character library: (make sure the path ends with a /)")
            newPath = {
                "CharLibPath": f"{os.path.expanduser(chCarLib)}"
            }
            with open('settings.json', 'w') as f:
                json.dump(newPath, f)
        elif settingsChange == "2":
            dirName = input("Choose a name for the directory: ")
            newDirName = dirName.replace(" ", "-").lower()
            os.mkdir(os.path.expanduser(f"~/{newDirName}"))

            newPath = {
                "CharLibPath": f"~/{newDirName}"
            }
            with open('settings.json', 'w') as f:
                json.dump(newPath, f)
        
        else:
            rprint("[bold red]ERROR: Please enter a valid number.[/bold red]")
            exit()

    else:
        print()
        rprint("[bold red]ERROR: Please enter a valid number.[/bold red]")
        exit()

except KeyboardInterrupt:
    print("\n")
    quitWarning = Prompt.ask("[bold yellow]WARNING: Quitting now will delete any unsaved changed. Quit? (y/N)").strip()
    if quitWarning.lower() in ["", "n", "no"]:
        os.system(f"python3 {os.path.abspath(__file__)}")
    else:
        exit("\nGoodbye!")
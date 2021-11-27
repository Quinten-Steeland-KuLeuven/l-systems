
import re

from ls_json import readJsonFile


def checkAxiom(variables, constants, axiom, rules, translations):
    for chara in axiom:
        if chara not in translations.keys():
            print(f"Error: the character '{chara}' has no translation.")
            exit(0)
    
    return axiom
    
def checkRules(variables, constants, axiom, rules, translations):
    for rule in rules.items():
        for chara in rule[0]:
            if chara not in translations.keys():
                print(f"Error: the character '{chara}' has no translation.")
                exit(0)
        
        for chara in rule[1]:
            if chara not in translations.keys():
                print(f"Error: the character '{chara}' has no translation.")
                exit(0)
    
    return rules

def checkTranslations(variables, constants, axiom, rules, translations):
    listOfValidTranslations = ["angle", "draw", "forward", "color", "move", "push", "pop"]
    listOfValidColors = getAllValidColors()
    
    for translation in translations.values():
        counter = 0
        while counter < len(translation):
            item = translation[counter]
            #for counter, item in enumerate(translation):
            if type(item) is not int and type(item) is not float and item not in listOfValidTranslations:
                print(f"Warning: '{item}' is not a valid translation, it will be ignored.")
                
            if item in ["draw", "angle", "forward", "move"]:
                try:
                    nextTranslation = translation[counter+1]
                except IndexError:
                    print(f"Error: '{item}' must be followed by an int or a float.")
                    exit(0)
                    
                if type(nextTranslation) is not float and type(nextTranslation) is not int:
                    try: 
                        translation[counter+1] = float(nextTranslation)
                        print(f"Waring: changing '{nextTranslation}' from '{type(nextTranslation).__name__}' to 'float'.")
                    except ValueError:
                        print(f"Error: '{item}' must be followed by an int or a float, not '{nextTranslation}'.")
                        exit(0)
                counter += 1
                        
            if item == "color":
                try:
                    nextTranslation = translation[counter+1]
                except IndexError:
                    print(f"Error: '{item}' must be followed by a color; name or hex-code.")
                    exit(0)    
                    
                if type(nextTranslation) is not str:
                    try: 
                        translation[counter+1] = str(nextTranslation)
                        print(f"Waring: changing '{nextTranslation}' from '{type(nextTranslation).__name__}' to 'str'.")
                    except ValueError:
                        print(f"Error: '{item}' must be followed by a str, not '{nextTranslation}'.")
                        exit(0)
                
                if nextTranslation not in listOfValidColors:
                    if checkIfHexColorIsValid(nextTranslation) is None:
                        print(f"Error: '{nextTranslation}' is not a valid color or hex code.")
                        exit(0)
                counter += 1
                    
            counter +=1
            
    return translations

def getAllValidColors():
    try:
        content = readJsonFile("valid_colors.json")
    except FileNotFoundError:
        print("Error: missing file: 'valid_colors.json'")
        exit(0)
        
    return list(content.get("colors"))

def checkIfHexColorIsValid(hexcode):
    return re.search(r"^#[0-9A-F]{6}$", hexcode) 

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
        
        if len(rule[0]) != 1:
            print(f"Error: {rule[0]} must be lenght of 1 but has a lenght of {len(rule[0])}.")
            exit(0)
        
        if type(rule[0]) is not str:
            try:
                print(f"Warning: trying to change '{rule[0]}' from '{type(rule[0]).__name__}' to 'str'.")
                rule = str(rule[0]), rule[1]
            except ValueError:
                print(f"Error: '{rule[0]}' must be a str.")
                exit(0)
                
        if type(rule[1]) is not str:
            try:
                print(f"Warning: trying to change '{rule[1]}' from '{type(rule[1]).__name__}' to 'str'.")
                rule = rule[0], str(rule[1])
            except ValueError:
                print(f"Error: '{rule[1]}' must be a str.")
                exit(0)
        
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
    listOfValidTranslations = ["angle", "draw", "forward", "color", "move", "push", "pop", "nop"]
    listOfValidColors = getAllValidColors()
    
    
    
    for key, translation in translations.items():
      
        if len(key) != 1:
            print(f"Error: {key} must be lenght of 1 but has a lenght of {len(key)}.")
            exit(0)
        
        if type(key) is not str:
            try:
                print(f"Warning: trying to change '{key}' from '{type(key).__name__}' to 'str'.")
                key = str(key)
            except ValueError:
                print(f"Error: '{key}' must be a str.")
                exit(0)
        
        if type(translation) is not list:
            try:
                print(f"Warning: trying to change '{translation}' from '{type(translation).__name__}' to 'list'.")
                translation = list(translation)
            except ValueError:
                print(f"Error: '{translation}' must be a list.")
                exit(0)
                
        try:
            translation = [item.lower() if type(item) is not int and type(item) is not float else item for item in translation ]
        except AttributeError:
            print(f"Error: bad translation for {key}: {translation}.")
            exit(0)
        
        if len(translation) == 0:
            print(f"Warning: {key} has empty translation.")
        
        translations[key] = translation
        
        counter = 0
        while counter < len(translation):
            item = translation[counter]
            
            
            
            if type(item) is not int and type(item) is not float and item not in listOfValidTranslations:
                print(f"Warning: '{item}' is not a valid translation, it will be ignored.")
                
            elif item in ["draw", "angle", "forward", "move"]:
                try:
                    nextTranslation = translation[counter+1]
                except IndexError:
                    print(f"Error: '{item}' must be followed by an int or a float.")
                    exit(0)
                    
                if type(nextTranslation) is not float and type(nextTranslation) is not int:
                    try:
                        print(f"Warning: trying to change '{nextTranslation}' from '{type(nextTranslation).__name__}' to 'float'.") 
                        translation[counter+1] = float(nextTranslation)
                    except (ValueError, TypeError):
                        print(f"Error: '{item}' must be followed by an int or a float, not '{nextTranslation}'.")
                        exit(0)
                counter += 1
                        
            elif item == "color":
                try:
                    nextTranslation = translation[counter+1]
                except IndexError:
                    print(f"Error: '{item}' must be followed by a color; name or hex-code.")
                    exit(0)    
                    
                if type(nextTranslation) is not str:
                    try:
                        print(f"Warning: trying to change '{nextTranslation}' from '{type(nextTranslation).__name__}' to 'str'.") 
                        translation[counter+1] = str(nextTranslation)
                    except ValueError:
                        print(f"Error: '{item}' must be followed by a str, not '{nextTranslation}'.")
                        exit(0)
                
                nextTranslation = translation[counter+1]
                if nextTranslation not in listOfValidColors:
                    if checkIfHexColorIsValid(nextTranslation) is None:
                        print(f"Error: '{nextTranslation}' is not a valid color or hex code.")
                        exit(0)
                counter += 1
                    
            counter +=1
        
        translations[key] = translation
            
    return translations

def getAllValidColors():
    try:
        content = readJsonFile("valid_colors.json")
    except FileNotFoundError:
        print("Error: missing file: 'valid_colors.json'")
        exit(0)
        
    return list(content.get("colors"))

def checkIfHexColorIsValid(hexcode):
    return re.search(r"^#[0-9A-Fa-f]{6}$", hexcode) 
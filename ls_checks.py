#for checking if a hex color is valid
import re

#to read a json file
from ls_json import readJsonFile

def checkAxiom(variables, constants, axiom, rules, translations):
    """
    function that checks if an axiom is valid


    Parameters
    ----------
    variables : list
        list of variables
    constants : list
        list of constants
    axiom : str
        the axiom
    rules : dict
        dict of rules
    translations : dict 
        dict of translation

    Returns
    -------
    str
        the axiom if it is valid
    """     
    axiom = checkType(axiom, str)
    for chara in axiom:
        if chara not in translations.keys():
            print(f"Error: the character '{chara}' has no translation.")
            exit(0)
    
    return axiom
    
def checkRules(variables, constants, axiom, rules, translations):
    """
    function that checks if the rules are valid

    Parameters
    ----------
    variables : list
        list of variables
    constants : list
        list of constants
    axiom : str
        the axiom
    rules : dict
        dict of rules
    translations : dict 
        dict of translation

    Returns
    -------
    dict
        dict of rules if they are valid
    """    
    for key, rule in rules.items():
        
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
                
        if type(rule) is not str:
            try:
                print(f"Warning: trying to change '{rule}' from '{type(rule).__name__}' to 'str'.")
                rule = str(rule)
            except ValueError:
                print(f"Error: '{rule}' must be a str.")
                exit(0)
        
        if key not in translations.keys():
            print(f"Error: the character '{key}' has no translation.")
            exit(0)
        
        for chara in rule:
            if chara not in translations.keys():
                print(f"Error: the character '{chara}' has no translation.")
                exit(0)
        rules[key] = rule
        
    return rules

def checkTranslations(variables, constants, axiom, rules, translations):
    """
    function that checks if the translations are valid

    Parameters
    ----------
    variables : list
        list of variables
    constants : list
        list of constants
    axiom : str
        the axiom
    rules : dict
        dict of rules
    translations : dict 
        dict of translation

    Returns
    -------
    dict
        dict of translations if they are valid
    """    
    
    listOfValidTranslations = ["angle", "draw", "forward", "color", "move", "push", "pop", "nop"]
    listOfValidColors = getAllValidColors()
    
    for key, translation in translations.items():
      
        if len(key) != 1:
            print(f"Error: {key} must be lenght of 1 but has a lenght of {len(key)}.")
            exit(0)
        
        key = checkType(key, str)
        translation = checkType(translation, list)
                
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
                   
                translation[counter+1] = checkType(nextTranslation, float, int)
                counter += 1
                        
            elif item == "color":
                try:
                    nextTranslation = translation[counter+1]
                except IndexError:
                    print(f"Error: '{item}' must be followed by a color; name or hex-code.")
                    exit(0)    
                
                translation[counter+1] = checkType(nextTranslation, str)
                
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
    """
    function that gets all valid colors stored in valid_colors.json

    Returns
    -------
    list
        list of all valid colors
    """    
    try:
        content = readJsonFile("valid_colors.json")
    except FileNotFoundError:
        print("Error: missing file: 'valid_colors.json'")
        exit(0)
        
    return list(content.get("colors"))

def checkIfHexColorIsValid(hexcode):
    """function that checks if a hexcode is a valid hex color code

    Parameters
    ----------
    hexcode : str
        hexcode of color to check

    Returns
    -------
    None
        if color is invalid
    not None
        if color is valid
    """    
    return re.search(r"^#[0-9A-Fa-f]{6}$", hexcode) 

def checkType(item, targetType, otherAllowedType=None):
    """
    function that checks if the type of an input variable is the same as one type
                         or if the type of the input is either one type or another type
    if it's not the correct type, try to change the type

    Parameters
    ----------
    item : any
        value that needs to be check for it's type
    targetType : type
        type to check for
    otherAllowedType : type, optional
        other type to check for, by default None

    Returns
    -------
    type(targetType)
        returns the item in the type of targetType
    """
    if otherAllowedType is None:
        otherAllowedType = targetType
    
    if type(item) is not targetType and type(item) is not otherAllowedType:
        try:
            print(f"Warning: trying to change '{item}' from '{type(item).__name__}' to '{targetType.__name__}'.")
            item = targetType(item)
        except ValueError:
            print(f"Error: '{item}' must be a {targetType.__name__}.")
            exit(0)
    return item

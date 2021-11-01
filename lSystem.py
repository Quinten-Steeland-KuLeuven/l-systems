#for reading config file
import json
#for drawing l-system
#import turtle
#for checking if config file exists
import os

def main():
    configFilename = getConfigFilename()
    iterations = getIterations()
    configTuple = readConfigFile(configFilename)
    generateLSystem(configTuple, iterations)
    
    
    

def getConfigFilename():
    """
    function that ask user for name of config file and checks if the file exists

    Returns
    -------
    str
        full path of config file
    """
    userInput = input("Enter config file name: ")
    
    if os.path.exists("./config_files/" + userInput):
        configFilename = os.path.abspath("./config_files/" + userInput)
        print("Using config file at", configFilename)
        
    elif os.path.exists("./config_files/" + userInput + ".json"):
        configFilename = os.path.abspath("./config_files/" + userInput + ".json")
        print("Using config file at", configFilename)
        
    elif os.path.exists(userInput):
        configFilename = os.path.abspath(userInput)
        print("Using config file at", configFilename)
        
    elif os.path.exists(userInput + ".json"):
        configFilename = os.path.abspath(userInput + ".json")
        print("Using config file at", configFilename)
        
    else:
        print("Config file not found, please check it is placed in the 'config_file' folder.")
        exit(0)
    
    return configFilename


def getIterations():
    """
    function that ask the user for the amount of iterations that will be made.
        checks that it is an int and is bigger than zero

    Returns
    -------
    int
        amount of iterations that the user wants to be made
    """
        
    while True:
        try:
            userInput = int(input("Enter the amount of iterations: "))
        except:
            print("Not an integer, iterations must be a positive integer.")
            exit(0)
        
        if (userInput > 0):
            break
        else:
            print("Iterations needs to be bigger than zero.")
        
    print(userInput, "iteration(s) will be made.")  
     
    return userInput 
    

def readConfigFile(configFilename):
    """
    function that gets all the info out of the config file

    Parameters
    ----------
    configFilename : str
        full path to the config file

    Returns
    -------
    tuple
    list, list, str, dict, dict
    
    returns a tuple of:
        variables, constants, axiom, rules, translations
    """
    with open(configFilename) as configFile:
        config = json.load(configFile)
        configFile.close()
        
    axiom = getAxiomFromConfig(config)
    
    constants, translations = getConstantsTranslationsFromConfig(config)
    
    variables = getVariablesFromConfig(config)
    
    #TODO check rules
    rules = getRulesFromConfig(config)
    
    checkVariablesConstantsAxiom(variables, constants, axiom)
    
    return variables, constants, axiom, rules, translations
    
    
def checkVariablesConstantsAxiom(variables, constants, axiom):
    """
    function that does some checks to see if variables constants & axiom are:
        Not empty & axiom does not contain undefined characters

    Parameters
    ----------
    variables : List
        List of all variables
    constants : List
        List of all constants
    axiom : str
        the given axiom
    """
    
    if len(variables)+len(constants) == 0:
        print("Config error: variables and constants can't be both empty.")
        exit(0)
    
    if len(axiom) == 0:
        print("Config error: axiom can't be empty.")
        exit(0)
        
    for chara in axiom:
        if chara not in variables and chara not in constants:
            confirm = input("A character from the axiom is not a variable or a constant, is this correct? [Y/n] ").lower()
            if confirm == "y" or confirm == "":
                break
            else:
                exit(0)
                
def getAxiomFromConfig(config):
    """
    Get axiom from config if it exists

    Parameters
    ----------
    config : dict
        config json file opened with json.load

    Returns
    -------
    str
        the axiom
    """
    try: 
        axiom = str(config["axiom"]).upper()
    except KeyError:
        print("Config error: no axiom found.")
        exit(0) 
    return axiom

def getConstantsTranslationsFromConfig(config):
    """
    gets constants and translations or nothing if there are no constants

    Parameters
    ----------
    config : dict
        config json file opened with json.load

    Returns
    -------
    tuple
        list, dict
        returns a tuple of
        constants, translations
        
    """
    constants = []
    translations = dict()
    try: 
        constants = list(config["constants"])
        try:
            translations = dict(config["translations"])
            translations = dict((k, v.lower()) for k,v in translations.items())            
        except KeyError:
            print("Config error: constants where given but no translations.")
            exit(0)
    except KeyError:
        pass
    return constants, translations

def getVariablesFromConfig(config):
    """
    Get variables from config if they exists

    Parameters
    ----------
    config : dict
        config json file opened with json.load

    Returns
    -------
    list
        list of the variables
    """
    try:
        variables = list(config["variables"])
    except KeyError:
        print("Config error: no variables found.")
        exit(0) 
    return variables

def getRulesFromConfig(config):
    """
    Get rules from config if they exists

    Parameters
    ----------
    config : dict
        config json file opened with json.load

    Returns
    -------
    dict
        dict of the rules
    """
    try:
        rules = dict(config["rules"])
    except KeyError:
        print("Config error: no rules found.")
        exit(0) 
    
    #make rules always uppercase
    rules = dict((k.upper(), v.upper()) for k,v in rules.items())
    return rules

#TODO this is/was for the checks of the translations
""" def checkAngle(angle):
    
    if angle >= -360 and angle <= 360:
        return angle
    else:
        print("problem with config file: angle", angle, "not between -360 and 360") """
    
    
def generateLSystem(configTuple, iterations):
    """
    generates a basic l system from the config for a certain amount of iterations

    Parameters
    ----------
    configTuple : Tuple
        Tuple of: list,      list,      str,   dict,  dict
                  variables, constants, axiom, rules, translations
    iterations : int
        amount of iterations that need to be made
    """
    variables, constants, axiom, rules, translations = configTuple[0], configTuple[1], configTuple[2], configTuple[3], configTuple[4], 

    currentString = axiom 

    print("0", currentString)

    for i in range(iterations):
        newList = []
        
        for item in currentString:
            if item in rules.keys():
                newList.append(rules[item])
                
            elif item in translations.keys():
                newList.append(item)
            
            else:
                newList.append(item)
            
        currentString = ''.join(newList)
        
        print(i+1, currentString)
        
    

    
    



main()
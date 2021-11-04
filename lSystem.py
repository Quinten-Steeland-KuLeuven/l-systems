#for reading config file
import json
#for drawing l-system
import turtle
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
    
    checkIfCacheExists()
    
    if userInput == "":
        configFilename = getFromCache("lastUsedConfigFile")
        print("Using config file at", configFilename)
    
    elif os.path.exists("./config_files/" + userInput):
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
        
    storeInCache("lastUsedConfigFile", configFilename)

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
        userInput = input("Enter the amount of iterations: ")
        if userInput != "":
            try:
                userInput = int(userInput)
            except:
                print("Not an integer, iterations must be a positive integer.")
                exit(0)
            
            if (userInput > 0):
                break
            else:
                print("Iterations needs to be bigger than zero.")
        else:
            userInput = getFromCache("lastUsedIterations")
            break
            
    storeInCache("lastUsedIterations", userInput)
        
    print(userInput, "iteration(s) will be made.")  
     
    return userInput 
    
def storeInCache(itemName, value):
    """
    Function that stores something in cache:

    Parameters
    ----------
    itemName : str
        name of the key of the value you want to store
    value : any
        what you want to store
    """
    with open("cache.json", "r") as cacheFile:
        cache = json.load(cacheFile)
        cacheFile.close()
    with open("cache.json", "w") as cacheFile:
        cache[itemName] = value
        json.dump(cache, cacheFile)
        cacheFile.close()
        
def getFromCache(itemName):
    """
    get some value from cache

    Parameters
    ----------
    itemName : str
        name of the key of the value you want to get

    Returns
    -------
    any
        the value with key itemName
    """
    with open("cache.json") as cacheFile:
        cache = json.load(cacheFile)
        if itemName in cache.keys():
            response = cache[itemName]
            cacheFile.close()
            
        else:
            print("This has not been cached yet.")
            exit(0)
    return response
    
def checkIfCacheExists():
    """
    function that checks of the cache file exists;
    if it does not exist, it makes one
    """
    if os.path.exists("cache.json") == False:
        cacheFile = open("cache.json", "w")
        cacheFile.write(str(dict()))
        cacheFile.close()

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
    
    constants = getConstantsFromConfig(config)
    
    translations = getTranslationsFromConfig(config)
    
    variables = getVariablesFromConfig(config)
    
    rules = getRulesFromConfig(config)
    
    checkVariablesConstantsAxiom(variables, constants, axiom)
    checkRulesTranslations(rules, translations)
    
    
    return variables, constants, axiom, rules, translations
    
def checkRulesTranslations(rules, translations):
    if len(rules) == 0:
        print("Config error: rules are empty.")
        
    if len(translations) == 0:
        print("Config error: translations are empty.")
    
def checkVariablesConstantsAxiom(variables, constants, axiom):
    """
    function that does some checks to see if variables constants & axiom are:
        Not empty 
        Axiom does not contain undefined characters

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

def getConstantsFromConfig(config):
    """
    gets constants from config if it exists
    if no constants exist it returns an empty list

    Parameters
    ----------
    config : dict
        config json file opened with json.load

    Returns
    -------
    list
        list of constans
        returns a tuple of
        constants, translations
        
    """
    
    try: 
        constants = list(config["constants"])
    except KeyError:
        constants = []
    return constants

def getTranslationsFromConfig(config):
    """
    gets constants from config if it exists

    Parameters
    ----------
    config : dict
        config json file opened with json.load

    Returns
    -------
    dict
        dict of translations        
    """
    
    try:
        translations = dict(config["translations"])
        translations = dict((k, [x if type(x) != str else x.lower() for x in v]) for k,v in translations.items())    
        
        #item.lower() for item in v if type(item) == str         
    except KeyError:
        print("Config error: no translations were found.")
        exit(0)
        
    return  translations

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
    
    #maxScreenSize = getMaxScreenSize(translations, iterations)
    maxScreenSize = 19200*2
    screen, turt = turtleInitiate(maxScreenSize)

    print("0", currentString)
    
    #turtleInstructions(screen, turt, currentString, translations)

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
        
        #TODO
    turtleInstructions(screen, turt, currentString, translations)
        
    input("Enter to continu")
        
def turtleInstructionsPrint(currentString, translations):
    print(42*"-")
    
    for chara in currentString:
        print(chara, "  ", translations[chara])
        
    print(42*"=")

def turtleInstructions(screen, turt, currentString, translations):
    print(screen, turt)
    
    print(42*"-")
    
    for chara in currentString:
        if translations[chara][0] in ["angle", "draw", "forward", "color"]:
            print(translations[chara][0], " + ", translations[chara][1])
            if translations[chara][0] == "angle":
                turtleAngle(screen, turt, translations[chara][1])
            elif translations[chara][0] == "draw":
                trutleDraw(screen, turt, translations[chara][1])
            elif translations[chara][0] == "forward":
                trutleForward(screen, turt, translations[chara][1])
            elif translations[chara][0] == "color":
                trutleColor(screen, turt, translations[chara][1])
                
        else:
            print(translations[chara][0])
            #if
            
    print(42*"=")

def turtleInitiate(maxScreenSize):
    print(maxScreenSize)
    turtle.screensize(canvwidth=maxScreenSize, canvheight=maxScreenSize)
    screen = turtle.getscreen()
    
    turt = turtle.Turtle()
    print(screen.screensize())
    return screen, turt

def turtleAngle(screen,turt,angle):
    turt.lt(angle)

def trutleDraw(screen, turt, distance):
    turt.fd(distance)

def trutleMove(screen, turt, distance):
    turt.up
    turt.fd(distance)
    turt.down

def trutleColor(screen, turt, color):
    turt.pencolor(color)

#bad attempt at getting max screen size
""" def getMaxScreenSize(translations, iterations):
    largest = 10
    for item in translations.values():
        
        if item[0] == "draw":
            largest = max(largest, (2*(item[1]**((iterations+item[1]/iterations)/item[1]))) )
    
    return largest """

main()
#for writing timestamp to filename
import datetime
#for generating random int/intervals
from random import randint, uniform
#for writing to configfile
import json

#for reading json file with settings
from ls_json import readJsonFile
#for getting all valid colors
from ls_checks import getAllValidColors
#for checking if a json file exists
from ls_user_input import returnPathIfJsonExists

def generateRandomConfig(settingsFilename=None):
    """
    function that is called by our main program, it generates a random config and returns its name

    Parameters
    ----------
    settingsFilename : str, optional
        name of custom settings file, by default None

    Returns
    -------
    str
        name of configfile
    """
    filename, config = generateConfig(settingsFilename)
    return filename

def main(settingsFilename=None):
    """
    this function is run if the program is run normally, it generates a random config and prints it and its name

    Parameters
    ----------
    settingsFilename : str, optional
        name of custom settings file, by default None
    """
    
    filename, config = generateConfig(settingsFilename)
    
    print(config)
    print("\nDone:", filename)

def generateConfig(settingsFilename):
    """
    function that generates a valid random config based on parameters in a json file

    Parameters
    ----------
    settingsFilename : str
        name of settings file

    Returns
    -------
    tuple
        filename, config
        str,      dict
        filename:
            name of file
        config:
            the config it generated
    """
    path = None
    if settingsFilename is None:
        path = "./Random_configs/Random_gen_settings/Default.json"
    else:
        path = returnPathIfJsonExists("./Random_configs/Random_gen_settings/", settingsFilename)
    
    if path is None:
        print("Error: settings file not found.")
        exit(0)
        
    settings = readJsonFile(path)
    
    if settings.get("_comment") is not None:
        settings.pop("_comment")
    
    if settings.get("variables") is None:
        availableVariables = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    else:
        availableVariables = settings.get("variables")
    
    if settings.get("constants") is None:
        availableConstants = ["+","-","|",",",".","!","@","#","$","%","^","&","*","=","_","~","<",">","/","\\","`","?","{","}","0","1","2","3","4","5","6","7","8","9",":",";","º","£","€","¿","¡","«","»","×","±","÷","²","¦","¢","¥","§"]
    else:
        availableConstants = settings.get("constants")
        
    if settings.get("instructions") is None:
        instructions = ["angle","draw","forward","color","nop"]
    else:
        instructions = settings.get("instructions")
        
    if settings.get("instructionsOdds") is None:
        instructionsOdds = [1/len(instructions)]*len(instructions)
    else:
        instructionsOdds = settings.get("instructionsOdds")
        
    if settings.get("colors") is None or settings.get("colors").lower() == "random":
        useColors = "random"
    if settings.get("colors").lower() == "list":
        useColors = getAllValidColors()
    else:
        useColors = settings.get("colors")
        
    if settings.get("usePushPop"):
        pushPopOdds = settings.get("usePushPopOdds")
        pushOdds = settings.get("pushOdds")
    else:
        pushPopOdds = -1
        pushOdds = -1
        
    variableVsConstantOdds = settings.get("variableVsConstantOdds")
    amountVariables = settings.get("amountVariables")
    amountConstants = settings.get("amountConstants")
    axiomLenght = settings.get("axiomLenght")
    ruleLenght = settings.get("ruleLenght")
    translationLenght = settings.get("translationLenght")
    amountMove = settings.get("amountMove")
    amountAngle = settings.get("amountAngle")
    
    if amountVariables.get("max") > len(availableVariables):
        amountVariables["max"] = len(availableVariables)
        
    if amountConstants.get("max") > len(availableConstants):
        amountConstants["max"] = len(availableConstants)
        
    selectedVariables = pickAmountOfItemsFromList(availableVariables, randint(amountVariables.get("min"), min(amountVariables.get("max"), len(availableVariables))))
    selectedConstants = pickAmountOfItemsFromList(availableConstants, randint(amountConstants.get("min"), min(amountConstants.get("max"), len(availableConstants))))
    
    if uniform(0, 1) <= pushPopOdds:
        for i in range(round(len(selectedConstants)*pushOdds)):
            selectedConstants.append("[")
    
    rules = dict()
    for chara in selectedVariables:
        lenght = randint(ruleLenght.get("min"), ruleLenght.get("max"))
        rules[chara] = generateRule(selectedVariables, selectedConstants, variableVsConstantOdds, lenght)
        
    if "[" in selectedConstants:
        selectedConstants = list(set(selectedConstants))
        selectedConstants.append("]")

    translations = dict()
    for chara in selectedConstants:
        lenght = randint(translationLenght.get("min"), translationLenght.get("max"))
        translations[chara] = generateTranslation(instructions, instructionsOdds, useColors, amountMove, amountAngle, variableVsConstantOdds, lenght, chara)
    
    for chara in selectedVariables:
        lenght = randint(translationLenght.get("min"), translationLenght.get("max"))
        translations[chara] = generateTranslation(instructions, instructionsOdds, useColors, amountMove, amountAngle, variableVsConstantOdds, lenght)
    
    lenght = randint(axiomLenght.get("min"), axiomLenght.get("max"))
    axiom = generateAxiom(selectedVariables, selectedConstants, lenght, variableVsConstantOdds)
    
    config = {
        "random_config_gen_settings": settings,
        "variables": selectedVariables,
        "constants": selectedConstants,
        "axiom": axiom,
        "rules": rules,
        "translations": translations
              }
    
    filename = "./Random_configs/C_" + datetime.datetime.now().isoformat(sep="T",timespec='seconds') + ".json"
    
    saveToFile(filename, config)
    
    return filename, config

def generateRandomColor():
    """
    function that generates a random hex color code

    Returns
    -------
    str
        hex color code
    """
    return "#%06x" % randint(0, 0xFFFFFF)

def pickAmountOfItemsFromList(availableItemsList, amountToPick, returnFirstStr=False):
    """
    function that picks a certain amount of items from a list

    Parameters
    ----------
    availableItemsList : list
        list of items we can choose from
    amountToPick : int
        amount of items to pick
    returnFirstStr : bool, optional
        if true returns the first picked item, by default False

    Returns
    -------
    if False:
        list
            list of selected items
    if True:
        str
            first chosen item
    """
    counter = 0
    selectedItems = []
    while counter < amountToPick:
        pick = randint(0, len(availableItemsList)-1)
        selectedItems += availableItemsList[pick]
        availableItemsList.pop(pick)
        counter += 1
        if returnFirstStr:
            return selectedItems[0]
    return selectedItems

def generateRule(selectedVariables,selectedConstants,variableVsConstantOdds,ruleLenght):
    """
    function that generates a valid rule given certain parameters

    Parameters
    ----------
    selectedVariables : list
        list of variables to pick from
    selectedConstants : list
        list of constants to pick from
    variableVsConstantOdds : float
        chances for a variable over an constant
           (e.g. 0.75 means on avarage 3 variables and 1 constant)
    ruleLenght : int
        lenght of the rule

    Returns
    -------
    str
        str of the rule
    """
    rule = []
    while rule == []:
        for i in range(ruleLenght):
            if uniform(0, 1) <= variableVsConstantOdds:
                pick = randint(0, len(selectedVariables)-1)
                rule += selectedVariables[pick]
            else:
                pick = randint(0, len(selectedConstants)-1)
                rule += selectedConstants[pick]
        
        if rule != []: 
            count = 0
            while count < len(rule):
                if rule[count] == "[":
                    pick = randint(count+1, len(rule))
                    rule.insert(pick, "]")
                count += 1
             
    strRule = "".join(rule)
    while "[]" in strRule:
        strRule = strRule.replace("[]", "")
    return strRule

def generateTranslation(instructions, instructionsOdds, useColors, amountMove, amountAngle, variableVsConstantOdds, lenght, chara=None):
    """
    generates a valid translation given input parameters

    Parameters
    ----------
    instructions : list
        list of instructions
    instructionsOdds : list
        list of odds for each instruction
    useColors : str or list
        if list:
            list of colors to pick from
        if str is "random"
            it will generate a random color
    amountMove : dict
        dict containing min and max amount of movement
    amountAngle : dict
        dict containting min and max amount of angle
    variableVsConstantOdds : float
        chances for a variable over an constant
           (e.g. 0.75 means on avarage 3 variables and 1 constant)
    lenght : int
        lenght of the translation
    chara : str, optional
        chara for which the translation is being made, only used for constants "[" and "]" so, by default None

    Returns
    -------
    list
        translations list of instructions 
            (e.g. ["draw", 10.42, "color", "#b00df1"])
    """
    translation = []
    oddsList = addUpOdds(list(instructionsOdds))
    while translation == []:
        for i in range(lenght):
            
            if chara == "[" and uniform(0, lenght) <= 1/lenght and "push" not in translation:
                translation.append("push")
                i += 1
                
            elif chara == "]" and uniform(0, lenght) <= 1/lenght and "pop" not in translation:
                translation.append("pop")
                i += 1
                
            else:
                
                tran = chooseInstruction(instructions,oddsList)
                if tran != "nop":
                    translation.append(tran)
                else:
                    if "nop" not in translation:
                        translation.append(tran)
                    else:
                        i -= 1
                        
                if tran in ["color","draw","angle","forward"]:
                    
                    if tran == "color":
                        if useColors == "random":
                            nextTran = generateRandomColor()
                        else:
                            nextTran = pickAmountOfItemsFromList(useColors, 1, True)
                            
                    elif tran == "draw":
                        nextTran = round(uniform(amountMove.get("min"), amountMove.get("max")),3)
                        
                    elif tran == "angle":
                        nextTran = round(uniform(amountAngle.get("min"), amountAngle.get("max")),3)
            
                    elif tran == "forward":
                        nextTran = round(uniform(amountMove.get("min"), amountMove.get("max")),3)
                    
                    translation.append(nextTran)     
                    i += 1
                    
    if chara == "[" and "push" not in translation:
        translation.append("push")
        
    elif chara == "]" and "pop" not in translation:
        translation.append("pop")
    
    return translation

def generateAxiom(variablesList, constantsList , lenght, variableVsConstantOdds):
    """
    generates axiom based on variables and constants

    Parameters
    ----------
    variablesList : list
        list of variables
    constantsList : list
        list of constants
    lenght : int
        lenght of the axiom
    variableVsConstantOdds : float
        chances for a character to be a variable instead of an constant
        
    Returns
    -------
    str
        the axiom
    """
    axiom = []
    
    if "]" in constantsList:
        constantsList.remove("]")
    
    for i in range(lenght):
        if uniform(0, 1) <= variableVsConstantOdds:
            pick = randint(0, len(variablesList)-1)
            axiom.append(variablesList[pick])
        else:
            pick = randint(0, len(constantsList)-1)
            axiom.append(constantsList[pick])
    
    count = 0   
    while count < len(axiom):
        if axiom[count] == "[":
            pick = randint(count+1, len(axiom))
            axiom.insert(pick, "]")
        count += 1
        
    strAxiom = "".join(axiom)
    while "[]" in strAxiom:
        strAxiom = strAxiom.replace("[]", "")
    return strAxiom
     
def addUpOdds(listOfOdds):
    """
    function that add's up the odss in a list of odds
        (   e.g.
            [0.35, 0.25, 0.225, 0.125, 0.05] is a list of odds (note: sum is 1 (=100%))
            [0.35, 0.6,  0.825, 0.95,  1] is list of added odds
        )

    Parameters
    ----------
    listOfOdds : list
        list of odds

    Returns
    -------
    list    
        list of added odds
    """
    for i in range(1,len(listOfOdds)):
        listOfOdds[i] = round(listOfOdds[i] + listOfOdds[i-1],3)
    listOfOdds.insert(0, 0)
    return listOfOdds

def chooseInstruction(instructions, listOfOdds):
    """
    function that chooses an instruction from a list of added odds
        (   e.g.
            [0.35, 0.25, 0.225, 0.125, 0.05] is a list of odds (note: sum is 1 (=100%))
            [0.35, 0.6,  0.825, 0.95,  1] is list of added odds
        )
    

    Parameters
    ----------
    instructions : list
        list of instructions
    listOfOdds : list
        list of odds (added)

    Returns
    -------
    str
        instruction
    """
    target = uniform(0, 1)
    for i in range(len(instructions)):
        if listOfOdds[i] <= target <= listOfOdds[i+1]:
            return instructions[i]
        
def saveToFile(filename, config):
    """
    function that saves the random config to file

    Parameters
    ----------
    filename : str name of the file
        [description]
    config : dict
        dict of the config; contains all the info required to make an l-system
    """
    with open(filename, "w") as writeFile:
        writeFile.writelines(json.dumps(config, ensure_ascii=False, sort_keys=False, indent=4))  
         
if __name__ == "__main__":
    main()  




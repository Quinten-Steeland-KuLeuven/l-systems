import datetime
from random import randint, uniform
import json
import sys

from ls_json import readJsonFile
from ls_checks import getAllValidColors
from ls_user_input import returnPathIfJsonExists

def generateRandomConfig(settingsFilename=None):
    filename, config = generateConfig(settingsFilename)
    return filename

def main(settingsFilename=None):
    
    filename, config = generateConfig(settingsFilename)
    
    print(config)
    print("Done:", filename)

def generateConfig(settingsFilename):
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
        instructionsOdds = settings.get("instrucionsOdds")
        
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
    
    """             #availableColors = ["yellow", "gold", "orange", "red",
                       "maroon", "violet", "magenta", "purple",
                       "navy", "blue", "skyblue", "cyan",
                       "turquoise", "lightgreen", "green", "darkgreen",
                       "chocolate", "brown", "black", "gray"] 
    global MAX_AMOUNT_MOVE
    global MAX_ITEMS_PER_TRANSLATION
    global MAX_LEN_RULES
    MAX_LEN_RULES = (5*(len(availableCharacters)+len(availableConstants))//12)+1
    MAX_AMOUNT_MOVE = 30
    MAX_ITEMS_PER_TRANSLATION = 7
    

    
    

    AmountCharacters = randint(1,24)
    AmountConstants = randint(2, 16)

    selectedCharacters = []
    selectedConstants = []

    counter = 0
    while counter < AmountCharacters:
        pick = randint(0, len(availableCharacters)-1)
        selectedCharacters += availableCharacters[pick]
        availableCharacters.pop(pick)
        counter += 1
        
    counter = 0
    while counter < AmountConstants:
        pick = randint(0, len(availableConstants)-1)
        selectedConstants += availableConstants[pick]
        availableConstants.pop(pick)
        counter += 1
    
    

    rules = dict()

    for chara in selectedCharacters:
        rules[chara] = generateRule(selectedCharacters,selectedConstants)
        
    translations = dict()
        
    for chara in selectedCharacters:
        translations[chara] = generateTranslation(chara, availableInstructions, availableColors)
    
    for chara in selectedConstants:
        translations[chara] = generateTranslation(chara, availableInstructions, availableColors)
        
    if "[" in selectedConstants:
        translations["]"] = generateTranslation(chara, availableInstructions, availableColors)
        selectedConstants.append("]")
    
    config = dict()
    
    config["variables"] = selectedCharacters
    config["constants"] = selectedConstants
    config["axiom"] = generateAxiom(selectedCharacters, selectedConstants)
    config["rules"] = rules
    config["translations"] = translations
    
    with open(filename, "w") as configFile:
        json.dump(config, configFile)
        configFile.close()
    
    return filename, config

def generateRule(selectedCharacters,selectedConstants):
    rule = []
    while rule == []:
        amount = randint(0, MAX_LEN_RULES)
        for i in range(amount):
            if randint(0, 1) == 1:
                pick = randint(0, len(selectedCharacters)-1)
                rule += selectedCharacters[pick]
            else:
                pick = randint(0, len(selectedConstants)-1)
                rule += selectedConstants[pick]
        
        if rule != []:       
            for count, chara in enumerate(rule):
                if chara == "[":
                    pick = randint(count+1, len(rule))
                    rule.insert(pick, "]")
               
    strRule = "".join(rule)
    strRule = strRule.replace("[]", "")
    return strRule

def generateTranslation(chara, availableOptions, availableColors):
    translation = []
    while translation == []:
               
        counter = 0
        amount = randint(1, MAX_ITEMS_PER_TRANSLATION)
        while counter < amount:
            pick = randint(0, len(availableOptions)-1)
            if availableOptions[pick] != "nop":
                translation.append(availableOptions[pick])
            else: 
                if "nop" not in translation:
                    translation.append(availableOptions[pick])
                else:
                    amount += 1
            if translation[-1] == "color":
                translation.append(pickRandomColor(availableColors))
            elif translation[-1] == "angle":
                translation.append(randint(-359, 359))
            elif translation[-1] == "forward" or translation[-1] == "draw":
                translation.append(randint(-MAX_AMOUNT_MOVE, MAX_AMOUNT_MOVE))
    
            counter += 1
        
        if chara == "[":
            index = randint(0, len(translation)-1)
            if index != 0:
                previous = translation[index-1]
                if previous == "color" or previous == "angle" or previous == "forward" or previous == "draw":
                    index += 1
            translation.insert(index, "push")
        elif chara == "]":
            index = randint(0, len(translation)-1)
            if index != 0:
                previous = translation[index-1]
                if previous == "color" or previous == "angle" or previous == "forward" or previous == "draw":
                    index += 1
            translation.insert(index, "pop")
            
    if len(translation) > MAX_ITEMS_PER_TRANSLATION and "nop" in translation:
        translation.remove("nop")
            
    return translation

def pickRandomColor(availableColors):
    pick = randint(0, len(availableColors)-1)
    return availableColors[pick]

def generateAxiom(selectedCharacters,selectedConstants):
    axiom = ""
    amount = randint(0, (len(selectedCharacters)+len(selectedConstants)))
    
    pick = randint(0, len(selectedCharacters)-1)
    axiom += selectedCharacters[pick]
    for i in range(amount):
        if randint(0, 1) == 1:
            pick = randint(0, len(selectedCharacters)-1)
            axiom += selectedCharacters[pick]
        else:
            pick = randint(0, len(selectedConstants)-1)
            axiom += selectedConstants[pick]
                
    return axiom """


def generateRandomColor():
    return "#%06x" % randint(0, 0xFFFFFF)

def pickAmountOfItemsFromList(availableItemsList, amountToPick, returnFirstStr=False):
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
            for count, chara in enumerate(rule):
                if chara == "[":
                    pick = randint(count+1, len(rule))
                    rule.insert(pick, "]")
               
    strRule = "".join(rule)
    while "[]" in strRule:
        strRule = strRule.replace("[]", "")
    return strRule

def generateTranslation(instructions, instructionsOdds, useColors, amountMove, amountAngle, variableVsConstantOdds, lenght, chara=None):
    translation = []
    oddsList = addUpOdds(list(instructionsOdds))
    while translation == []:
        for i in range(lenght):
            
            if chara == "[" and uniform(0, lenght) <= 1/lenght:
                translation.append("push")
                i += 1
                
            elif chara == "]" and uniform(0, lenght) <= 1/lenght:
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

def generateAxiom(selectedVariables, selectedConstants, lenght, variableVsConstantOdds):
    axiom = ""
    for i in range(lenght):
        if uniform(0, 1) <= variableVsConstantOdds:
            pick = randint(0, len(selectedVariables)-1)
            axiom += selectedVariables[pick]
        else:
            pick = randint(0, len(selectedConstants)-1)
            axiom += selectedConstants[pick]
    return axiom

     
def addUpOdds(listOfOdds):
    for i in range(1,len(listOfOdds)):
        listOfOdds[i] = round(listOfOdds[i] + listOfOdds[i-1],3)
    listOfOdds.insert(0, 0)
    return listOfOdds

def chooseInstruction(instructions, listOfOdds):
    target = uniform(0, 1)
    for i in range(len(instructions)):
        if listOfOdds[i] <= target <= listOfOdds[i+1]:
            return instructions[i]
        
def saveToFile(filename, config):
    with open(filename, "w") as writeFile:
        writeFile.writelines(json.dumps(config, ensure_ascii=False, sort_keys=False, indent=4))  
         
if __name__ == "__main__":
    main()  




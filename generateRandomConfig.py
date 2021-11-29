import datetime
from random import randint
import json
import sys

from ls_json import readJsonFile
from ls_checks import getAllValidColors

""" 
generate random config file for lSystem
Quick and dirty, not final
"""

def generateRandomConfig():
    filename, config = generateConfig()
    return filename

def main():
    
    filename, config = generateConfig()
    
    print(config)
    print("Done:", filename)

def generateConfig():
    filename = "./Random_configs/C_" + datetime.datetime.now().isoformat(sep="T",timespec='seconds') + ".json"
    availableCharacters = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    availableConstants = ["+","-","|",",",".","!","@","#","$","%","^","&","*","=","_","~","[","<",">","/","\\","`","?","{","}","0","1","2","3","4","5","6","7","8","9",":",";","º","£","€","¿","¡","«","»","×","±","÷","²","¦"]
    availableOptions = ["angle","draw","forward","color","nop"]
    availableColors = getAllValidColors()
    """ #availableColors = ["yellow", "gold", "orange", "red",
                       "maroon", "violet", "magenta", "purple",
                       "navy", "blue", "skyblue", "cyan",
                       "turquoise", "lightgreen", "green", "darkgreen",
                       "chocolate", "brown", "black", "gray"] """
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
        translations[chara] = generateTranslation(chara, availableOptions, availableColors)
    
    for chara in selectedConstants:
        translations[chara] = generateTranslation(chara, availableOptions, availableColors)
        
    if "[" in selectedConstants:
        translations["]"] = generateTranslation(chara, availableOptions, availableColors)
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
                
    return axiom

def generateRandomColor():
    return "#%06x" % randint(0, 0xFFFFFF)

if __name__ == "__main__":
    main()  




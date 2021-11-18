import datetime
from random import randint 
import json

""" 
generate random config file for lSystem
Quick and dirty, not final
"""


def main():
    filename = "./random_configs/C_" + datetime.datetime.now().isoformat(sep="T",timespec='seconds') + ".json"
    availableCharacters = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    availableConstants = ["+","-","|",",",".","!","@","#","$","%","^","&","*","=","_","~","["]
    availableOptions = ["angle","draw","forward","color","nop"]
    availableColors = ["yellow", "gold", "orange", "red",
                       "maroon", "violet", "magenta", "purple",
                       "navy", "blue", "skyblue", "cyan",
                       "turquoise", "lightgreen", "green", "darkgreen",
                       "chocolate", "brown", "black", "gray"]
    global MAX_AMOUNT_MOVE
    global MAX_ITEMS_PER_TRANSLATION
    global MAX_LEN_RULES
    MAX_LEN_RULES = (3*(len(availableCharacters)+len(availableConstants))//8)+1
    MAX_AMOUNT_MOVE = 40
    MAX_ITEMS_PER_TRANSLATION = 6

    AmountCharacters = randint(1,20)
    AmountConstants = randint(2, 15)

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
    
    """ configFile = open(filename, "w")
    configFile.write(str(config))
    configFile.close() """
    with open(filename, "w") as configFile:
        json.dump(config, configFile)
        configFile.close()
    
    print(config)
    
    print("Done:", filename)

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
                translation.append(randint(-180, 180))
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

       
main()  




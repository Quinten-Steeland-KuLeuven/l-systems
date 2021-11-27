#import our own functions
from ls_checks import checkAxiom, checkRules, checkTranslations
from ls_json import readJsonFile

def getConfig(configFilename):
    configDict = readJsonFile(configFilename)
    
    axiom = getAxiomFromConfig(configDict)
    
    rules = getRulesFromConfig(configDict)
    
    translations = getTranslationsFromConfig(configDict)
    
    variables, constants = getVariablesConstantsFromRulesTranslations(rules, translations)
    
    axiom = checkAxiom(variables, constants, axiom, rules, translations)
    rules = checkRules(variables, constants, axiom, rules, translations)
    translations = checkTranslations(variables, constants, axiom, rules, translations)
    
    #TODO remove
    print([variables, constants, axiom, rules, translations])
    
    return variables, constants, axiom, rules, translations

def getAxiomFromConfig(configDict):
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
    axiom = configDict.get("axiom")
    if axiom is None:
        print("Config error: axiom was not found.")
        exit(0)

    if axiom is not str:
        try: 
            axiom = str(axiom)
        except KeyError:
            print("Config error: axiom is not a string.")
            exit(0) 
    return axiom

def getRulesFromConfig(configDict):
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
    rules = configDict.get("rules")
    if rules is None:
        print("Waring: no rules were found.")
        rules = dict()
    
    elif rules is not dict:
        try:
            rules = dict(rules)
        except KeyError:
            print("Config error: bad formating of rules.")
            exit(0) 

    return rules

def getTranslationsFromConfig(configDict):
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
    translations = configDict.get("translations")
    if translations is None:
        print("Config error: no translations were found.")
        exit(0)
    
    if translations is not dict:
        try:
            translations = dict(translations)       
        except KeyError:
            print("Config error: no translations were found.")
            exit(0)
        
    return translations

def getVariablesConstantsFromRulesTranslations(rules, translations):
    
    variables = list(rules.keys())

    constants = list(translations.keys() - rules.keys())
    
    return variables, constants




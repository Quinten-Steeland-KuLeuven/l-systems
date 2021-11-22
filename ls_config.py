#for reading json file
import json

#import our own functions
from ls_checks import checkRulesTranslations, checkVariablesConstantsAxiom

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

#read input data

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
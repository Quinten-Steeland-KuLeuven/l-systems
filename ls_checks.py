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
                

#TODO to use or not to use
#TODO this is/was for the checks of the translations
""" def checkAngle(angle):
    
    if angle >= -360 and angle <= 360:
        return angle
    else:
        print("problem with config file: angle", angle, "not between -360 and 360") """
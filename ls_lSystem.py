def generateLSystem(axiom, rules, translations, iterations):
    """
    generates a basic l system from the config for a certain amount of iterations

    Parameters
    ----------
    variables, constants, axiom, rules, translations : Tuple
        Tuple of: list,      list,      str,   dict,  dict
                  variables, constants, axiom, rules, translations
    iterations : int
        amount of iterations that need to be made
        
    Returns
    -------
    str
        full string of the l-system after all iterations
    """
    currentString = axiom 
    
    print("Generating l-system...")
    
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
        
    return currentString
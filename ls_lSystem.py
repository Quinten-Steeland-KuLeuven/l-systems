def generateLSystem(axiom, rules, translations, iterations):
    """
    function that generates an l-system for x iterations based on an axiom, rules and translations

    Parameters
    ----------
    axiom : str
        the axiom
    rules : dict
        dict of rules
    translations : dict
        dict of translations
    iterations : int
        amount of iterations

    Returns
    -------
    str
        the output l-system after x iterations
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
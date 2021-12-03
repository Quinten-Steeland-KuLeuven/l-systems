#for timestamp
import datetime
#for checking if file exists
import os.path
#for making empty history file
from restoreBackup import clearHistoryFile

def addToHistory(variables, constants, axiom, rules, translations, iterations, lSystem):
    """
    function that saves the data* to a new line in the ./History/History.txt
    (*) data = timing, variables, constants, axiom, rules, translations, iterations and result-string

    Parameters
    ----------
    variables : list 
        list of variables
    constants : list
        list of constants
    axiom : str
        the axiom
    rules : dict
        rules for all variables
    translations : dict
        translations for all characters
    iterations : int
        amount of iterations
    lSystem : str
        string of an l-system

    Returns
    -------
    
    tuple
        str, str
        line of the history file (without the timestamp)
        timestamp
    """
    timestamp = datetime.datetime.now().isoformat(sep=" ",timespec='seconds')
    
    if not os.path.isfile("./History/History.txt"):
        clearHistoryFile()
    historyfile = open("./History/History.txt", "a")
        
    line = f"\n{timestamp}\t"
    
    for elem in variables, constants, axiom, rules, translations:
        line += str(elem) + "\t"
    line += str(iterations) + "\t" + lSystem
    historyfile.write(line)
    
    return line, timestamp

#for timestamp
import datetime

def addToHistory(variables, constants, axiom, rules, translations, iterations, lSystem):
    """
        saves the data to a new line in the History.txt
        data = timing, variables, constants, axiom, rules, translations, iterations and result-string
       Parameters
       ----------
       variables, constants, axiom, rules, translations:
            tuple with data of l-system:
                variables, constants, axioms, rules, translations
        iterations:
            int: amount of iterations
        lSystem:
            str: result-string
    """
    timestamp = datetime.datetime.now().isoformat(sep=" ",timespec='seconds')
    
    historyfile = open("History.txt", "a")
    line = "\n" + timestamp + "\t"
    print(line)
    for elem in variables, constants, axiom, rules, translations:
        line += str(elem) + "\t"
    line += str(iterations) + "\t" + lSystem
    historyfile.write(line)
    
    return line, timestamp
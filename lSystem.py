#for commandline arguments
import sys


#import our own functions
from ls_turtle import runTurtle
from ls_commandline_arguments import processCommandlineArguments
from ls_history import addToHistory
from ls_user_input import getConfigFilename, getIterations
from ls_config import getConfig
from ls_lSystem import generateLSystem
from ls_export import exportImage
from ls_transform import transform
from ls_website import updateWebsite

from generateRandomConfig import generateRandomConfig

def runLSystem(allArguments=sys.argv):
    """
    main loop of the program
    """
    
    configFilename, iterations, exportImageName, showDrawProcess, noProgressbar, closeAfterDrawing, useRandomConfig, useWebsite = processCommandlineArguments(allArguments)
    
    if useRandomConfig is not None:
        configFilename = generateRandomConfig(useRandomConfig)
        print("Using random config", configFilename)
    
    if configFilename is None:
        configFilename = getConfigFilename(None)
    
    if iterations is None:
        iterations = getIterations()
        
    variables, constants, axiom, rules, translations = getConfig(configFilename)
    
    lSystem = generateLSystem(axiom, rules, translations, iterations)

    screen, turtlePosition = runTurtle(lSystem,translations, showDrawProcess, noProgressbar)
    
    addToHistory(variables, constants, axiom, rules, translations, iterations, lSystem)
    
    if exportImageName is not None:
        exportImage(screen, exportImageName, turtlePosition, configFilename, iterations)

    if useWebsite:
        transform()
        updateWebsite()

    if not closeAfterDrawing:
        input("\nPress enter to exit...")
        
def runLSystemInLoop(listOfArguments):
    
    for i in range(listOfArguments[0]):
        print(i)
        runLSystem(listOfArguments)

if __name__ == "__main__":
    runLSystem()
	

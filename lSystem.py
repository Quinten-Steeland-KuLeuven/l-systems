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

def runLsystem(allArguments=sys.argv):
    """
    main loop of the program
    """
    
    configFilename, iterations, exportImageName, showDrawProcess, noProgressbar, closeAfterDrawing, useRandomConfig = processCommandlineArguments(allArguments)
    
    if useRandomConfig == True:
        configFilename = generateRandomConfig()
        print("Using random config", configFilename)
    
    if configFilename == None:
        configFilename = getConfigFilename(None)
    
    if iterations == None:
        iterations = getIterations()
        
    variables, constants, axiom, rules, translations = getConfig(configFilename)
    
    lSystem = generateLSystem(axiom, rules, translations, iterations)

    screen, turtlePosition = runTurtle(lSystem,translations, showDrawProcess, noProgressbar)
    
    addToHistory(variables, constants, axiom, rules, translations, iterations, lSystem)
    
    if exportImageName != None:
        exportImage(screen, exportImageName, turtlePosition, configFilename, iterations)

    transform()
    updateWebsite()

    if closeAfterDrawing == False:
        input("Press enter to exit...")

if __name__ == "__main__":
    runLsystem()
	

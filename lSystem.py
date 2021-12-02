#for commandline arguments
import sys

#import our own functions
#for trutle drawing
from ls_turtle import runTurtle
#fro processing command line arguments
from ls_commandline_arguments import processCommandlineArguments
#for saving history
from ls_history import addToHistory
#for user input
from ls_user_input import getConfigFilename, getIterations
#to read the configfile
from ls_config import getConfig
#for generating the lSystem
from ls_lSystem import generateLSystem
#for exporting the image
from ls_export import exportImage
#for converting eps to svg
from ls_transform import convertEpsToSvg
#for generating a website
from ls_website import updateWebsite
#for generating a random config
from generateRandomConfig import generateRandomConfig

def runLSystem(allArguments=sys.argv):
    """
    main loop of the program

    Parameters
    ----------
    allArguments : list, optional
        list of commandline arguments, by default sys.argv
    """
    
    #process arguments
    configFilename, iterations, exportImageName, showDrawProcess, useProgressbar, closeAfterDrawing, useRandomConfig, useWebsite, exportSvg = processCommandlineArguments(allArguments)
    
    #get config
    if useRandomConfig is not None:
        configFilename = generateRandomConfig(useRandomConfig)
        print("Using random config", configFilename)
    
    if configFilename is None:
        configFilename = getConfigFilename(None)
    
    #   get iterations
    if iterations is None:
        iterations = getIterations()
        
    variables, constants, axiom, rules, translations = getConfig(configFilename)
    
    #generate l-system
    lSystem = generateLSystem(axiom, rules, translations, iterations)

    #draw l-system
    screen, turtlePosition = runTurtle(lSystem,translations, showDrawProcess, useProgressbar, iterations)
    
    #update history file
    addToHistory(variables, constants, axiom, rules, translations, iterations, lSystem)
    
    #export image
    if exportImageName is not None:
        exportImage(screen, exportImageName, turtlePosition, configFilename, iterations)
    
    #convert image
    if exportSvg:
        convertEpsToSvg(False)

    #use website
    if useWebsite:
        convertEpsToSvg()
        updateWebsite()

    if not closeAfterDrawing:
        input("\nPress enter to exit...")
        
def runLSystemInLoop(listOfArguments):
    """
    function to run the program in a loop
        (see loop.py for an example)
    
    Usage
    -----
    for use in another script:
    
    from lSystem import runLSystemInLoop
    
    runLSystemInLoop([x, "-e", "-rc", "-i", "5", "-ca"])
    
    with x amount of times the programs runs

    Parameters
    ----------
    listOfArguments : list
        a list of all the arguments with the first being the amount of loops
    """
    
    for i in range(listOfArguments[0]):
        print(i)
        runLSystem(listOfArguments)

if __name__ == "__main__":
    runLSystem()
	

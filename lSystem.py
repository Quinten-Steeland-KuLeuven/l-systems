#for reading config file
import json
#for drawing l-system
import turtle
#for checking if config file exists
import os
#for timestamp in historyfile
import datetime
#for commandline arguments
import sys


def main():
    configFilename = iterations = exportImageName = None
    showDrawProcess = noProgressbar = closeAfterDrawing = False
    
    if len(sys.argv) > 1:
        configFilename, iterations, exportImageName, showDrawProcess, noProgressbar, closeAfterDrawing = processCommandlineArguments()
    
    if configFilename == None:
        configFilename = getConfigFilename(None)
    
    if iterations == None:
        iterations = getIterations()
        
    configTuple = readConfigFile(configFilename)
    lSystem = generateLSystem(configTuple, iterations)
    screen, turtlePosition = runTurtle(lSystem, configTuple[4], showDrawProcess, noProgressbar)
    addHistory(configTuple, iterations, lSystem)
    
    if exportImageName != None:
        exportImage(screen, exportImageName, turtlePosition, configFilename, iterations)
        
    if closeAfterDrawing == False:
        input("Press enter to exit...")
    exit(0)
    
def processCommandlineArguments():
    configFilename = iterations = exportImageName = None
    showDrawProcess = noProgressbar = closeAfterDrawing = False
    
    helpMessage = """
    All commandline options:
    -h  or  --help                                  Displays help.
    -e  or  --export <filename>                     Exports the turtle drawing to a file.
    -c  or  --config <name of the configfile>       Used to give the config file name to the program.
    -i  or  --iterations [amount]                   Used to give the amount of iterations to the program.
    -sd or  --show_draw_process                     Use this flag to see the turtle move.
    -np or  --no_progress_bar                       Use this flag if you want no progressbar (e.g. for speed).
    -ca or  --close_after_drawing                   Exit immediately after drawing.
    """
    
    counter = 0
    while counter < len(sys.argv)-1:
        counter += 1
        arg = sys.argv[counter]
        
        if arg == "--help" or arg == "-h":
            print(helpMessage)
            exit(0)
            
        elif arg == "--export" or arg == "-e":
            counter += 1
            try: arg = sys.argv[counter]
            except:
                exportImageName = ""
            if arg[0] == "-" or arg == "":
                counter -= 1
                exportImageName = ""
            else:
                exportImageName = arg
                           
        elif arg == "--iterations" or arg == "-i":
            counter += 1
            try: arg = sys.argv[counter]
            except:
                print("Missing an argument.")
                exit(0)
            if arg[0] == "-" or arg == "":
                counter -= 1
            else:
                try: iterations = int(arg)
                except KeyError(): 
                    print("--iterations must be followed by a positive integer.")
                    exit(0)
                    if iterations < 1:
                        print("Iterations must be larger than 0")
                        exit(0)
                        
        elif arg == "--config" or arg == "-c":
            counter += 1
            try: arg = sys.argv[counter]
            except:
                print("Missing an argument.")
                exit(0)
            if arg[0] == "-" or arg == "":
                counter -= 1
            else:
                configFilename = getConfigFilename(arg)
                
        elif arg == "-sd" or arg == "--show_draw_process":
            showDrawProcess = True
            
        elif arg == "-np" or arg == "--no_progress_bar":
            noProgressbar = True
            
        elif arg == "-ca" or arg == "--close_after_drawing":
            closeAfterDrawing = True
            
        else:
            print("Unknown argument: '" + arg + "'  Use --help for help.")
            exit(0)
    
    return configFilename, iterations, exportImageName, showDrawProcess, noProgressbar, closeAfterDrawing
    
def getConfigFilename(nameToCheck):
    """
    function that ask user for name of config file and checks if the file exists

    Returns
    -------
    str
        full path of config file
    """
    if nameToCheck == None:
        userInput = input("Enter config file name: ")
    else: 
        userInput = nameToCheck
        
    homePath = os.environ['HOME']
    
    locations = ["./config_files/", "./", homePath + "/", homePath + "/.lSystems/", homePath + "/.lSystems/config_files/", "./random_configs/" ]
    
    checkIfCacheExists()
    
    configFilename = None
    
    if userInput != "":
        for location in locations:
            if os.path.exists(location + userInput + ".json"):
                configFilename = os.path.abspath(location + userInput + ".json")
                print("Using config file at", configFilename)
                break 
            elif os.path.exists(location + userInput):
                configFilename = os.path.abspath(location + userInput)
                print("Using config file at", configFilename)
                break 
            
        if configFilename == None: 
            print("Config file not found, please check it is placed in the 'config_file' folder.")
            exit(0)
            
    else:
        configFilename = getFromCache("lastUsedConfigFile")
        print("Using config file at", configFilename)
    
    storeInCache("lastUsedConfigFile", configFilename)

    return configFilename

def getIterations():
    """
    function that ask the user for the amount of iterations that will be made.
        checks that it is an int and is bigger than zero

    Returns
    -------
    int
        amount of iterations that the user wants to be made
    """
        
    while True:
        userInput = input("Enter the amount of iterations: ")
        if userInput != "":
            try:
                userInput = int(userInput)
            except:
                print("Not an integer, iterations must be a positive integer.")
                exit(0)
            
            if (userInput > 0):
                break
            else:
                print("Iterations needs to be bigger than zero.")
        else:
            userInput = getFromCache("lastUsedIterations")
            break
            
    storeInCache("lastUsedIterations", userInput)
        
    print(userInput, "iteration(s) will be made.")  
     
    return userInput 
    
def storeInCache(itemName, value):
    """
    Function that stores something in cache:

    Parameters
    ----------
    itemName : str
        name of the key of the value you want to store
    value : any
        what you want to store
    """
    with open("cache.json", "r") as cacheFile:
        cache = json.load(cacheFile)
        cacheFile.close()
    with open("cache.json", "w") as cacheFile:
        cache[itemName] = value
        json.dump(cache, cacheFile)
        cacheFile.close()
        
def getFromCache(itemName):
    """
    get some value from cache

    Parameters
    ----------
    itemName : str
        name of the key of the value you want to get

    Returns
    -------
    any
        the value with key itemName
    """
    with open("cache.json") as cacheFile:
        cache = json.load(cacheFile)
        if itemName in cache.keys():
            response = cache[itemName]
            cacheFile.close()
            
        else:
            print("This has not been cached yet.")
            exit(0)
    return response
    
def checkIfCacheExists():
    """
    function that checks of the cache file exists;
    if it does not exist, it makes one
    """
    if os.path.exists("cache.json") == False:
        cacheFile = open("cache.json", "w")
        cacheFile.write(str(dict()))
        cacheFile.close()

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

#TODO to use or not to use
#TODO this is/was for the checks of the translations
""" def checkAngle(angle):
    
    if angle >= -360 and angle <= 360:
        return angle
    else:
        print("problem with config file: angle", angle, "not between -360 and 360") """
      
def generateLSystem(configTuple, iterations):
    """
    generates a basic l system from the config for a certain amount of iterations

    Parameters
    ----------
    configTuple : Tuple
        Tuple of: list,      list,      str,   dict,  dict
                  variables, constants, axiom, rules, translations
    iterations : int
        amount of iterations that need to be made
        
    Returns
    -------
    str
        full string of the l-system after all iterations
    """
    variables, constants, axiom, rules, translations = configTuple[0], configTuple[1], configTuple[2], configTuple[3], configTuple[4]
    currentString = axiom 
    
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
    
def runTurtle(lSystem, translations, showDrawProcess, noProgressbar):
    """
    Function that sets up the turtle and then calls another function that runs the turle drawing for a given lSystem

    Parameters
    ----------
    lSystem : str
        string of an lSystem
    translations : dict
        dict of translations
    """
    if len(lSystem)<1024:
        print("Iterating over string:", lSystem)
    else:
        print("Iterating over long string (lenght: " + str(len(lSystem)) + ").")
    
    screen, turt = turtleInitiate(showDrawProcess)
    
    screen, turtlePosition = turtleRunMainLoop(screen, turt, lSystem, translations, noProgressbar)
    
    return screen, turtlePosition
    
def turtleRunMainLoop(screen, turt, lSystem, translations, noProgressbar):
    """
    This function runs the turtle to draw an lSystem

    Parameters
    ----------
    screen : 
        turtle screen
    turt : 
        turtle
    lSystem : str
        string of an lSystem
    translations : dict
        dict of translations
    """
    
    storage = []
    turtlePosition = 0,0,0,0
    
    if len(lSystem) > 500000 and noProgressbar == False:
        for chara in progressbar(lSystem," ",100):
            turtlePosition = turtleRunInstructions(screen, turt, lSystem, translations, storage, turtlePosition, chara)
    else:
        for chara in lSystem:
            turtlePosition = turtleRunInstructions(screen, turt, lSystem, translations, storage, turtlePosition, chara)
    
    turtle.update() 
    
    return screen, turtlePosition    

def turtleRunInstructions(screen, turt, lSystem, translations, storage, turtlePosition, chara):
    i = 0
        
    while i < len(translations[chara]):
        if translations[chara][i] in ["angle", "draw", "forward", "color"]:
            if translations[chara][i] == "angle":
                turtleAngle(screen, turt, translations[chara][i+1])
                
            elif translations[chara][i] == "draw":
                turtleDraw(screen, turt, translations[chara][i+1])
                turtlePosition = getTurtlePosition(screen, turt, turtlePosition)
                
            elif translations[chara][i] == "forward":
                turtleMove(screen, turt, translations[chara][i+1])
                turtlePosition = getTurtlePosition(screen, turt, turtlePosition)
                
            elif translations[chara][i] == "color":
                turtleColor(screen, turt, translations[chara][i+1])
            i += 2
            
        else:
            if translations[chara][i] == "push":
                turtlePush(screen, turt, storage)
                
            elif translations[chara][i] == "pop":
                turtlePop(screen, turt, storage)
            i += 1
    
    return turtlePosition
    
def getTurtlePosition(screen, turt, turtlePosition):
    minX = min(turt.pos()[0], turtlePosition[0])
    minY = min(turt.pos()[1], turtlePosition[1])
    maxX = max(turt.pos()[0], turtlePosition[2])
    maxY = max(turt.pos()[1], turtlePosition[3])
    return minX, minY, maxX, maxY
                
def turtleInitiate(showDrawProcess):
    """
    creates a turtle window, sets it's canvas size and spawns a turtle

    Parameters
    ----------
    screenSize : int
        this is used to set the canvas height and width

    Returns
    -------
    tuple
        screen, turt
        the turtle screen, the turtle itself
    """
    
    screenSize = 19200*20
    
    turtle.screensize(canvwidth=screenSize, canvheight=screenSize)
    screen = turtle.getscreen()
    turtle.hideturtle()
    turtle.delay(0)
    if showDrawProcess == False:
        turtle.tracer(0, 0)
    turt = turtle.Turtle()
    turt.speed(0)
    
    #turt.
    return screen, turt

def turtleAngle(screen,turt,angle):
    """
    Changes angle of turtle, positive angle is a left turn

    Parameters
    ----------
    screen : 
        turtle screen
    turt : 
        turtle
    angle : float
        the angle it needs to turn, positive is a left turn
    """
    turt.lt(angle)

def turtleDraw(screen, turt, distance):
    """
    Draws a line with the turtle, positive distance is forward

    Parameters
    ----------
    screen : 
        turtle screen
    turt : 
        turtle
    distance : float
        The lenght of the line it needs to draw
    """
    turt.fd(distance)

def turtleMove(screen, turt, distance):
    """
    Moves the turle forward without drawing a line

    Parameters
    ----------
    screen : 
        turtle screen
    turt : 
        turtle
    distance : float
        The distance it needs to move
    """
    turt.up
    turt.fd(distance)
    turt.down

def turtleColor(screen, turt, color):
    """
    Changes the draw color of the turle

    Parameters
    ----------
    screen : 
        turtle screen
    turt : 
        turtle
    color : str [english color name OR #hex color code with a #]
        color for the turtle
    """
    turt.pencolor(color)

def turtlePush(screen, turt, storage):
    """
    Stores the position, angle and color as a tuple in a storage-list

    Parameters
    ----------
    screen :
        turtle screen
    turt :
        turtle

    """
    try: storage += [(turt.pos(), turt.heading(), turt.color()[1])]
    except: storage = [(turt.pos(), turt.heading(), turt.color()[1])]

def turtlePop(screen, turt, storage):
    """
        moves the turtle, without drawing, to a given position, angle and color.
        The position is given by the last tuple in the storage list

        Parameters
        ----------
        screen :
            turtle screen
        turt :
            turtle
        """
    try:
        turt.penup()
        turt.goto(storage[-1][0])
        turt.setheading(storage[-1][1])
        turt.pencolor(storage[-1][2])
        storage.pop(-1)
        turt.pendown()
    except:
        print("Error: you can't pop more than you push")
        exit(0)

def addHistory(configtuple, iterations, lSystem):
    """
        saves the data to a new line in the History.txt
        data = timing, variables, constants, axiom, rules, translations, iterations and result-string
       Parameters
       ----------
       configtuple:
            tuple with data of l-system:
                variables, constants, axioms, rules, translations
        iterations:
            int: amount of iterations
        lSystem:
            str: result-string
   """

    historyfile = open("History.txt", "a")
    line = "\n" + datetime.datetime.now().isoformat(sep=" ",timespec='seconds') + "\t"
    for elem in configtuple:
        line += str(elem) + "\t"
    line += str(iterations) + "\t" + lSystem
    historyfile.write(line)

""" def askExport(screen):
    
        asks the user if he wants to save the drawing,
        if Yes, saves it to a asked filename

       Parameters
       ----------
       screen :
           turtle screen

    
    answer = input("Save the drawing (Y/n): ")
    if answer == "Y":
        name = input("What should its name be: ")
        if name == "":
            name = datetime.datetime.now().isoformat(sep="T",timespec='seconds')
        exportImage(screen, name) """

def exportImage(screen, exportImageName, turtlePosition, configFilename, iterations):
    """
       saves the drawing to the images map, to a given filename

       Parameters
       ----------
       screen :
           turtle screen
       filename: str
            name of the image
       """
    
    if exportImageName == "":
        exportImageName = datetime.datetime.now().isoformat(sep="T",timespec='seconds') + "_" + configFilename.rsplit("/", 1)[-1][:-5] + "_" + str(iterations)
    if exportImageName[-4:] != ".eps":
        exportImageName += ".eps"
    
    path = './images/'
    completeName = os.path.join(path, exportImageName)
    Cwidth = abs(turtlePosition[2] - turtlePosition[0])+20
    Cheight = abs(turtlePosition[3] - turtlePosition[1])+20
    screen.getcanvas().postscript(x = turtlePosition[0]-10, y = -turtlePosition[3]-10, width = Cwidth, height = Cheight, file = completeName)

#function to display a progressbar. used on long l-systems
#from https://stackoverflow.com/a/34482761
def progressbar(it, prefix="", size=100, file=sys.stdout):
    count = len(it)
    def show(j):
        x = int(size*j/count)
        file.write("%s[%s%s] %i/%i %i%s\r" % (prefix , "◼"*x, "◻"*(size-x), j, count, x, "%"))
        file.flush()        
    show(0)
    for i, item in enumerate(it):
        yield item
        show(i+1)
    file.write("\n")
    file.flush()

main()
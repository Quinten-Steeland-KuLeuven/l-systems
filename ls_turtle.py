#for drawing l-system
import turtle

#import progressbar function
from so_progressbar import progressbar

def runTurtle(lSystem, translations, showDrawProcess, useProgressbar, iterations):
    """
    Function that sets up the turtle and then calls another function that runs the turle drawing for a given lSystem

    Parameters
    ----------
    lSystem : str
        string of an l-system
    translations : dict
        dict with a translation for every character
    showDrawProcess : bool
        if true, it will show the drawing process
    useProgressbar : bool or None
        if None: if lSystem is longer than 500000 characters, use a progressbar
        if True: always use progressbar
        if False: never use progressbar
    iterations : int
        amount of iterations

    Returns
    -------
    tuple:
    screen, turtlePosition
        screen:
            turtle screen
        turtlePosition
            tuple:
                The minX, minY, maxX, maxY coordinates the turtle has visited
    """
    if len(lSystem)<1024:
        print("Iterating over string:", lSystem)
    else:
        print(f"Iterating over long string (lenght: {len(lSystem)}).")
    
    screen, turt = turtleInitiate(showDrawProcess, iterations)
    
    screen, turtlePosition = turtleRunMainLoop(screen, turt, lSystem, translations, useProgressbar)
    
    return screen, turtlePosition
    
def turtleRunMainLoop(screen, turt, lSystem, translations, useProgressbar):
    """
    Main loop of the turtle

    Parameters
    ----------
    screen : Turtle screen
        The turtle screen
    turt : Turtle turtle
        The turtle turtle
    lSystem : str
        String of an lSystem
    translations : dict
        dict with a translation for every character
    useProgressbar : bool or None
        if None: if lSystem is longer than 500000 characters, use a progressbar
        if True: always use progressbar
        if False: never use progressbar

    Returns
    -------
    tuple:
    screen, turtlePosition
        screen:
            turtle screen
        turtlePosition
            tuple:
                The minX, minY, maxX, maxY coordinates the turtle has visited
    """
    
    storage = []
    turtlePosition = 0,0,0,0
    
    if (len(lSystem) > 500000 and useProgressbar is None) or useProgressbar:
        for chara in progressbar(lSystem," ",100):
            turtlePosition = turtleRunInstructions(screen, turt, lSystem, translations, storage, turtlePosition, chara)
    else:
        for chara in lSystem:
            turtlePosition = turtleRunInstructions(screen, turt, lSystem, translations, storage, turtlePosition, chara)
    
    turtle.update() 
    
    return screen, turtlePosition    

def turtleRunInstructions(screen, turt, lSystem, translations, storage, turtlePosition, chara):
    """
    The loop where the turtle draws per character of the lSystem 

    Parameters
    ----------
    screen : Turtle screen
        The turtle screen
    turt : Turtle turtle
        The turtle turtle
    lSystem : str
        String of an lSystem
    translations : dict
        dict with a translation for every character
    storage : list
        List of: turtle position, turtle heading, turtle color
    turtlePosition : tuple
        The minX, minY, maxX, maxY coordinates the turtle has visited
    chara : str
        one character from the lSystem

    Returns
    -------
    turtlePosition
        tuple:
            The minX, minY, maxX, maxY coordinates the turtle has visited
    """
    i = 0 
    while i < len(translations[chara]):
        if translations[chara][i] in ["angle", "draw", "forward", "color", "move"]:
            if translations[chara][i] == "angle":
                turtleAngle(screen, turt, translations[chara][i+1])
                
            elif translations[chara][i] == "draw":
                turtleDraw(screen, turt, translations[chara][i+1])
                turtlePosition = getTurtlePosition(screen, turt, turtlePosition)
                
            elif translations[chara][i] == "forward" or translations[chara][i] == "move":
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
    """
    gets the max or min position of the turtle

    Parameters
    ----------
    screen : Turtle screen
        The turtle screen
    turt : Turtle turtle
        The turtle turtle
    turtlePosition : tuple
        The minX, minY, maxX, maxY coordinates the turtle has visited

    Returns
    -------
    tuple
        minX, minY, maxX, maxY
        the minX, minY, maxX, maxY coordinates of the turtle
    """
    minX = min(turt.pos()[0], turtlePosition[0])
    minY = min(turt.pos()[1], turtlePosition[1])
    maxX = max(turt.pos()[0], turtlePosition[2])
    maxY = max(turt.pos()[1], turtlePosition[3])
    return minX, minY, maxX, maxY
                
def turtleInitiate(showDrawProcess, iterations):
    """
    Creates a turtle window, sets it's canvas size and spawns a turtle

    Parameters
    ----------
    showDrawprocess : bool
        if true, show the drawing process
    iterations : int
        this is used to set the canvas height and width
    

    Returns
    -------
    tuple:
        screen, turt
        screen:
            turtle screen
        turt
            turtle turtle
    """
    
    screenSize = 19200*4*iterations
    
    turtle.screensize(canvwidth=screenSize, canvheight=screenSize)
    screen = turtle.getscreen()
    screen.clear()
    turtle.hideturtle()
    turtle.delay(0)
    if not showDrawProcess:
        turtle.tracer(0, 0)
        screen.tracer(0, 0)
    turt = turtle.Turtle(undobuffersize = 0, visible = False)
    turt.speed(0)
    
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
    except IndexError:
        print("Error: you can't pop more than you push")
        exit(0)
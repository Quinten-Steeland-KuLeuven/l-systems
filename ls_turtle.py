#for drawing l-system
import turtle

#import progressbar function
from so_progressbar import progressbar

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
        print(f"Iterating over long string (lenght: {len(lSystem)}).")
    
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
    screen.clear()
    turtle.hideturtle()
    turtle.delay(0)
    if showDrawProcess == False:
        turtle.tracer(0, 0)
        screen.tracer(0, 0)
    turt = turtle.Turtle(undobuffersize = 1, visible = False)
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
    except:
        print("Error: you can't pop more than you push")
        exit(0)
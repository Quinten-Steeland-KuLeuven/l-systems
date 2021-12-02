#for timestamp
import datetime
#for getting full path
import os

def exportImage(screen, exportImageName, turtlePosition, configFilename, iterations):
    """
    saves the output of the turtle drawing to an eps file

    Parameters
    ----------
    screen : turtle screen
        turtle screen
    exportImageName : str
        name of the image
    turtlePosition : tuple
        max and min coordinates of the turtle
        (used for exporting the correct size of the image)
    configFilename : str 
        name of the config filename
        (used for auto generated name)
    iterations : int
        amount of iterations 
        (used for auto generated name)
    """    
    
    if exportImageName == "":
        exportImageName = datetime.datetime.now().isoformat(sep="T",timespec='seconds') + "_" + configFilename.rsplit("/", 1)[-1][:-5] + "_" + str(iterations)
    if exportImageName[-4:] != ".eps":
        exportImageName += ".eps"
    
    path = './Images/'
    completeName = os.path.join(path, exportImageName)
    Cwidth = abs(turtlePosition[2] - turtlePosition[0])+20
    Cheight = abs(turtlePosition[3] - turtlePosition[1])+20
    screen.getcanvas().postscript(x = turtlePosition[0]-10, y = -turtlePosition[3]-10, width = Cwidth, height = Cheight, file = completeName)


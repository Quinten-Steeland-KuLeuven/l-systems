#for getting file 
import os
#for running programs
import subprocess

def convertEpsToSvg(forWebsite=True):
    """
    function that converts eps file to svg file

    Parameters
    ----------
    forWebsite : bool, optional, by default True
        True:
            the function is called for use of the website, it will copy the file to mostRecent.svg
        False:
            it is not copied to mostRecent.svg
    """
    
    path = "./Images"
    image = getMostRecentFile(path)

    subprocess.run(["ps2pdf", "-dEPSCrop" ,image, image[:-3]+"pdf"])
    subprocess.run(["pdf2svg", image[:-3]+"pdf", image[:-3]+"svg"])
    
    if forWebsite:
        subprocess.run(["cp", image[:-3]+"svg", "./Images/mostRecent.svg"])

def getMostRecentFile(path):
    """
    gets the the path to the most recent file in a directory 

    Parameters
    ----------
    path : str
        path to directory

    Returns
    -------
    str
        path to most recent file
    """
    files = os.listdir(path)
    paths = [os.path.join(path, basename) for basename in files]
    return max(paths, key=os.path.getctime)
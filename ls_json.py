#for reading json file
import json

import os

def readJsonFile(jsonFilename):
    """
    function that reads the content of a json file

    Parameters
    ----------
    jsonFilename : str
        path to json file

    Returns
    -------
    dict
        content of the file
    """    
    if not os.path.exists(jsonFilename):
        print(f"Error: file '{jsonFilename}'' does not exist.")
        exit(0)
    
    with open(jsonFilename, "r") as readFile:
        try:
            fileContent = json.load(readFile)
        except json.decoder.JSONDecodeError:
            print("Error: badly formatted json file.")
            exit(0)

    if fileContent == dict() or fileContent == "" or fileContent == "\n":
        print("Json file is empty.")
        exit(0)

    if type(fileContent) is not dict:
        try:
            fileContent = dict(fileContent)
        except KeyError:
            print("Error: badly formatted json file.")
            exit(0)

    return fileContent

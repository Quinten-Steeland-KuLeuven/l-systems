#for reading json file
import json

import os

def readJsonFile(jsonFilename):
    """
    function that gets everything out of a json file

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

#for reading json file
import json

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
    with open(jsonFilename, "r") as readFile:
        try:
            fileContent = json.load(readFile)
        except json.decoder.JSONDecodeError:
            print("Config error: Badly formated json file.")
            exit(0)

    if fileContent == dict() or fileContent == "" or fileContent == "\n":
        print("Json file is empty.")
        exit(0)

    if type(fileContent) is not dict:
        try:
            fileContent = dict(fileContent)
        except KeyError:
            print("Error: Badly formated json file.")
            exit(0)

    return fileContent

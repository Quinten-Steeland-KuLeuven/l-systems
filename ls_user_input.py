#for checking if files exists
import os

#import our cache functions
from ls_cache import storeInCache, getFromCache

def getConfigFilename(nameToCheck):
    """
    function that ask user for name of config file and checks if the file exists

    Parameters
    ----------
    nameToCheck : str
        name of the file to check 
    
    Returns
    -------
    str
        full path of config file
    """
    if nameToCheck is None:
        userInput = input("Enter config file name: ")
    else: 
        userInput = nameToCheck
        
    homePath = os.environ['HOME']
    
    locations = [
                    "./Config_files/", "./", "./Examples/", homePath + "/", homePath + "/.lSystems/",
                    homePath + "/.lSystems/Config_files/", "./Random_configs/", "./Config_files/", homePath + "/.lSystems/config_files/",
                    "./random_configs/", "./Configs/","./configs/", homePath + "/l-systems/Config_files/",
                    homePath + "./l-systems/config_files/", "/", ""
                ]
    
    configFilename = None
    
    if userInput != "":
        for location in locations:
            configFilename = returnPathIfJsonExists(location, userInput)
            if configFilename is not None:
                break
            
        if configFilename is None: 
            print("Config file not found, please check it is placed in the 'config_file' folder.")
            exit(0)
            
    else:
        configFilename = getFromCache("lastUsedConfigFile")
        print(f"Using config file at {configFilename}")
    
    storeInCache("lastUsedConfigFile", configFilename)

    return configFilename

def getIterations():
    """
    function that ask the user for the amount of iterations that will be made.
        checks that it is an int and is bigger than or equal to zero

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
            except ValueError:
                print("Not an integer, iterations must be a positive integer.")
                exit(0)
            
            if (userInput >= 0):
                break
            else:
                print("Iterations needs to be bigger than or equal zero.")
        else:
            userInput = getFromCache("lastUsedIterations")
            break
            
    storeInCache("lastUsedIterations", userInput)
        
    print(f"{userInput} iteration(s) will be made.")  
     
    return userInput 

def returnPathIfJsonExists(path, filename):
    """
    functions that returns a full path of a json file if it exists

    Parameters
    ----------
    path : str
        path to file to check
    filename : str
        name of file to check

    Returns
    -------
    str
        if file exists, returns full path
    """    
    if os.path.exists(path + filename + ".json"):
        fullPath = os.path.abspath(path + filename + ".json")
        print(f"Using config file at {fullPath}")
        return fullPath
        
    elif os.path.exists(path + filename):
        fullPath = os.path.abspath(path + filename)
        print(f"Using config file at {fullPath}")
        return fullPath
        
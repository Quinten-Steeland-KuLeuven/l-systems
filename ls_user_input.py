#for checking if files exists
import os

#import our cache functions
from ls_cache import storeInCache, getFromCache



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
    
    locations = [
                    "./Examples/", "./Config_files/", "./", homePath + "/", homePath + "/.lSystems/",
                    homePath + "/.lSystems/Config_files/", "./Random_configs/", "./Config_files/", homePath + "/.lSystems/config_files/",
                    "./random_configs/", "./Configs/","./configs/", homePath + "/l-systems/Config_files/",
                    homePath + "./l-systems/config_files/"
                ]
    
    configFilename = None
    
    if userInput != "":
        for location in locations:
            configFilename = returnPathIfJsonExists(location, userInput)
            if configFilename is not None:
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
            except:
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
        
    print(userInput, "iteration(s) will be made.")  
     
    return userInput 

def returnPathIfJsonExists(path, filename):
    if os.path.exists(path + filename + ".json"):
        fullPath = os.path.abspath(path + filename + ".json")
        print("Using config file at", fullPath)
        return fullPath
        
    elif os.path.exists(path + filename):
        fullPath = os.path.abspath(path + filename)
        print("Using config file at", fullPath)
        return fullPath
        
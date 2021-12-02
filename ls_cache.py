#for reading json file
import json
#for checking if file exists
import os

def storeInCache(itemName, value):
    """
    Function that stores something in a cache file:

    Parameters
    ----------
    itemName : str
        name of the key of the value you want to store
    value : any
        what you want to store
    """
    checkIfCacheExists()
    with open("cache.json", "r") as cacheFile:
        cache = json.load(cacheFile)
        cacheFile.close()
    with open("cache.json", "w") as cacheFile:
        cache[itemName] = value
        json.dump(cache, cacheFile)
        cacheFile.close()
        
def getFromCache(itemName):
    """
    get some value from the cache file

    Parameters
    ----------
    itemName : str
        name of the key of the value you want to get

    Returns
    -------
    any
        the value with key itemName
    """
    checkIfCacheExists()
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
    if os.path.exists("cache.json") is False:
        cacheFile = open("cache.json", "w")
        cacheFile.write(str(dict()))
        cacheFile.close()
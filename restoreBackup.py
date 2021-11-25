import os
import subprocess

def main():

    allFiles = sorted(os.listdir("./History_backups"))

    for i, item in enumerate(allFiles):
        i += 1
        print(i,"\t",item)
        
    print("0", "\t", "Clear current History.txt")
    print("-1", "\t", "Backup and Clear current History.txt")
        
    print(42*"-")

    print("Which file would you like to restore: ")

    try: 
        chosenIndex = int(input())
    except KeyError:
        print("Not a number.")
        exit(0)
        
    if chosenIndex < -1:
        print("Must be greater than -2.")
        exit(0)
        
    elif chosenIndex > len(allFiles):
        print("That file does not exist.")
        
    if chosenIndex > 0:
        
        targetFile = allFiles[chosenIndex-1]
        with open("./History_backups/{targetfile}","r") as readFile:
            fileContent = readFile.readlines()
            
        with open("History.txt", "w") as writeFile:
            writeFile.writelines(fileContent)
            
    elif chosenIndex == 0:
        clearHistoryFile()
            
    elif chosenIndex == -1:
        subprocess.run(["./makeBackup.sh"])
        clearHistoryFile()
    
def clearHistoryFile():
    with open("History.txt", "w") as writeFile:
        writeFile.write("<timestamp>\t\t<variables>\t\t<constants>\t\t<axiom>\t\t<rules>\t\t<translations>\t\t<iterations>\t\t<resulting-string>")


if __name__ == "__main__":  
    main()
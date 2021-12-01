#import our own function
from ls_user_input import getConfigFilename

def processCommandlineArguments(allArguments):
    configFilename = iterations = exportImageName = None
    showDrawProcess = noProgressbar = closeAfterDrawing = useRandomConfig = False
    
    helpMessage = """
    All commandline options:
    -h  or  --help                          Displays help.
    -e  or  --export <filename>             Exports the turtle drawing to a file.
    -c  or  --config <configfile name>      Used to give the config file name to the program.
    -i  or  --iterations [amount]           Used to give the amount of iterations to the program.
    -sd or  --show_draw_process             Use this flag to see the turtle move.
    -np or  --no_progress_bar               Use this flag if you want no progressbar (e.g. for speed).
    -ca or  --close_after_drawing           Exit immediately after drawing.
    -rc or  --random_config                 Generate a random l-System
    """
    
    counter = 0
    while counter < len(allArguments)-1:
        counter += 1
        arg = allArguments[counter]
        
        if arg == "--help" or arg == "-h":
            print(helpMessage)
            exit(0)
            
        elif arg == "--export" or arg == "-e":
            counter += 1
            try: arg = allArguments[counter]
            except:
                exportImageName = ""
            if arg[0] == "-" or arg == "":
                counter -= 1
                exportImageName = ""
            else:
                exportImageName = arg
                           
        elif arg == "--iterations" or arg == "-i":
            counter += 1
            try: arg = allArguments[counter]
            except:
                print("Missing an argument.")
                exit(0)
            if arg[0] == "-" or arg == "":
                counter -= 1
            else:
                try: iterations = int(arg)
                except KeyError(): 
                    print("--iterations must be followed by a positive integer.")
                    exit(0)
                        
        elif arg == "--config" or arg == "-c":
            counter += 1
            try: arg = allArguments[counter]
            except:
                print("Missing an argument.")
                exit(0)
            if arg[0] == "-" or arg == "":
                counter -= 1
            else:
                configFilename = getConfigFilename(arg)
                
        elif arg == "-sd" or arg == "--show_draw_process":
            showDrawProcess = True
            
        elif arg == "-np" or arg == "--no_progress_bar":
            noProgressbar = True
            
        elif arg == "-ca" or arg == "--close_after_drawing":
            closeAfterDrawing = True
            
        elif arg == "-rc" or arg == "--random_config":
            useRandomConfig = True
            
        else:
            print(f"Unknown argument: '{arg}'  Use --help for help.")
            exit(0)
    
    return configFilename, iterations, exportImageName, showDrawProcess, noProgressbar, closeAfterDrawing, useRandomConfig
   
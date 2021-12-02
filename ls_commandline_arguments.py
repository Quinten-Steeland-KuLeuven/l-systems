#import our own function
from ls_user_input import getConfigFilename

def processCommandlineArguments(allArguments):
    """
    function that processes commandline arguments

    Parameters
    ----------
    allArguments : list
        list of arguments

    Returns
    -------
    tuple
        configFilename, iterations, exportImageName, showDrawProcess, useProgressbar, closeAfterDrawing, useRandomConfig, useWebsite, exportSvg
        str             int         str              bool             bool            bool               bool             bool        bool
        name of config file         name of export image              use a progressbar                  use a random config          also convert eps to svg
                        amount of iterations         show the draw process            close after drawing                 use a website
    """    
    
    configFilename = iterations = exportImageName = useRandomConfig = useProgressbar = None
    showDrawProcess = closeAfterDrawing = useWebsite = exportSvg = False
    
    helpMessage = """
    All commandline options:
    -h  or  --help                                  Displays help.
    -c  or  --config <config filename>              Used to give the config file name to the program.
    -i  or  --iterations [amount]                   Used to give the amount of iterations to the program.
    -e  or  --export <filename>                     Exports the turtle drawing to an eps file.
    -s  or  --output_svg                            Convert the eps image from eps to svg.
    -sd or  --show_draw_process                     Use this flag to see the turtle move.
    -up or  --use_progress_bar                      Use this flag if you always want a progressbar.
    -np or  --no_progress_bar                       Use this flag if you want no progressbar (e.g. for speed).
    -ca or  --close_after_drawing                   Exit immediately after drawing.
    -rc or  --random_config <settings filename>     Generate a random l-System.
    -uw or  --use_website                           Generate a website with the latest lSystem drawing.
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
            except IndexError:
                exportImageName = ""
            if arg[0] == "-" or arg == "":
                counter -= 1
                exportImageName = ""
            else:
                exportImageName = arg
                           
        elif arg == "--iterations" or arg == "-i":
            counter += 1
            try: arg = allArguments[counter]
            except IndexError:
                print("Missing an argument.")
                exit(0)
            if arg[0] == "-" or arg == "":
                counter -= 1
            else:
                try: iterations = int(arg)
                except KeyError: 
                    print("--iterations must be followed by a positive integer.")
                    exit(0)
                        
        elif arg == "--config" or arg == "-c":
            counter += 1
            try: arg = allArguments[counter]
            except IndexError:
                print("Missing an argument.")
                exit(0)
            if arg[0] == "-" or arg == "":
                counter -= 1
            else:
                configFilename = getConfigFilename(arg)
                            
        elif arg == "-rc" or arg == "--random_config":
            useRandomConfig = "Default"
            counter += 1
            try: 
                arg = allArguments[counter]
            except IndexError:
                useRandomConfig = "Default"
            if arg[0] == "-" or arg == "":
                counter -= 1
            else:
                useRandomConfig = arg
                
        elif arg == "-sd" or arg == "--show_draw_process":
            showDrawProcess = True
            
        elif arg == "-up" or arg == "--use_progress_bar":
            useProgressbar = True
            
        elif arg == "-np" or arg == "--no_progress_bar":
            useProgressbar = False
            
        elif arg == "-ca" or arg == "--close_after_drawing":
            closeAfterDrawing = True

        elif arg == "-uw" or arg == "--use_webiste":
            useWebsite = True

        elif arg == "-s" or arg == "--output_svg":
            exportSvg = True

        else:
            print(f"Unknown argument: '{arg}'  Use --help for help.")
            exit(0)
            
    if useWebsite and exportImageName == None:
        exportImageName = ""
          
    if exportSvg:
        exportImageName = ""
        
    return configFilename, iterations, exportImageName, showDrawProcess, useProgressbar, closeAfterDrawing, useRandomConfig, useWebsite, exportSvg
   
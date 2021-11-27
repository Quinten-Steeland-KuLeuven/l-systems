# l-systems

## Config file format:

```json
{
    "axiom": "A",                           //The axiom
    "rules": {                              //rules per variable
        "A": "BD",
        "B": "A-C",
        "C": "C+A",
        "D": "[E",
        "E": "]"
    },
    "translations" : {                      //translations for all characters
        "A": ["move", 1],
        "B": ["draw", 2],
        "C": ["draw", -1],
        "D": ["nop"],
        "E": ["nop"],
        "+": ["Angle", 25],
        "-": ["angle", -25],
        "[": ["push"],
        "]": ["pop"]
    }
}
```
```
Axiom: str of any combination of variables and constants  
Rules: dict of the rules for the variables  
  formated as follows:  
    str of variable : str of what it will be turned into  
    e.g: "X":"AX"  
Translations: dict of the translations of all variables and constants  
  formated as follows:  
    str of character : list of [str of instruction, optional argument for instruction]  
    e.g: "X":["angle",-12.5]  
```


## Command line options:

```
All commandline options:
    -h  or  --help                                  Displays help.
    -e  or  --export <filename>                     Exports the turtle drawing to a file.
    -c  or  --config <name of the configfile>       Used to give the config file name to the program.
    -i  or  --iterations [amount]                   Used to give the amount of iterations to the program.
    -sd or  --show_draw_process                     Use this flag to see the turtle move.
    -np or  --no_progress_bar                       Use this flag if you want no progressbar (e.g. for speed).
    -ca or  --close_after_drawing                   Exit immediately after drawing.
    -rc or  --random_config                         Generate a random l-System
```

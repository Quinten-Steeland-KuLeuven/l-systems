# l-systems

## Config file format:

```json
{
    "variables": ["A", "B", "C", "D","E"],  //List of all variables
    "constants": ["+", "-", "[", "]"],      //List of all constants
    "axiom": "A",                           //The axiom
    "rules": {                              //rules per variable
        "A": "BD",
        "B": "a-C",
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

Variables: list of characters A-Z  
Constants: list of any characters but not A-Z  
Axiom: str of any combination of variables and constants  
Rules: dict of the rules for the variables  
    formated as follows:  
    str of variable : str of what it will be turned into  
    e.g: "X":"AX"  
Translations: dict of the translations of all variables and constants  
    formated as follows:  
    str of character : list of [str of instruction, optional argument for instruction]  
    e.g: "X":["angle",-12.5]  

# l-systems

## Info:

Program that can draw l-systems.
Features:
- system history
- unit tests
- history backups
- exporting drawings
- web server
- docker
- generate random l-systems

Intended to be run on a unix os (preferably linux)

Learn more about l-systems [here](https://en.wikipedia.org/wiki/L-system).

## Setup:

Clone the Repo:
```
git clone https://github.com/Quinten-Steeland-KuLeuven/l-systems
```
Setup Virtual Python Environment:
```
python3 -m venv lSystem-venv
```
Activate Virtual Environment:
```
source lSystem-venv/bin/activate
```
Install Packages:
```
sudo apt install python3-pip
pip install -r requirements.txt
```
Install other Packages:
```
debian based:
sudo apt-get install python3-tk ghostscript pdf2svg

arch based:
sudo pacman -S tk ghostscript pdf2svg
```

## Usage:

Run:
```
python3 lSystem.py
or
python3 lSystem.py [command line options]
```
See section "Command line options"

## Docker:


If you have installed docker, you can run the following commands in the project folder:
```
sudo apt-get install docker.io
docker build -t l-systems .
```
--------------------------------
If you get the following error:
```
Got permission denied while trying to connect to the Docker daemon socket at unix:///var/run/docker.sock: Post "http://.............": dial unix /var/run/docker.sock: connect: permission denied
```
Run:
```
sudo chmod 666 /var/run/docker.sock
```
If you get the following error:
```
_tkinter.TclError: couldn't connect to display
```
run
```
sudo apt-get install x11-xserver-utils

xhost +
```
--------------------------------

To run the docker file itself, use:
```
./runDocker.sh [arguments]
```

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
```

#This is an example of how you can run the lSystem from another python file

from lSystem import runLSystemInLoop

runLSystemInLoop([500, "-e", "-rc", "-i", "5", "-ca"])
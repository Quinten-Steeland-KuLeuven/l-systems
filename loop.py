#This is a test file
#ignore

from lSystem import runLsystem
for i in range(250):
    print(i)
    runLsystem(["run", "-e", "-rc", "-i", "5", "-ca"])
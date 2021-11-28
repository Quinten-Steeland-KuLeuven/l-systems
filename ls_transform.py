import os
import subprocess

path = "./Images"
def newest(path):
    files = os.listdir(path)
    paths = [os.path.join(path, basename) for basename in files]
    return max(paths, key=os.path.getctime)
image = newest(path)
print(image)
#rc = subprocess.call("./convertEPS.sh", shell = True)
subprocess.run(["ps2pdf", image, image[:-3]+"pdf"])
subprocess.run(["pdf2svg", image[:-3]+"pdf", image[:-3]+"svg"])
subprocess.run(["cp", image[:-3]+"svg", "./Images/mostRecent.svg"])

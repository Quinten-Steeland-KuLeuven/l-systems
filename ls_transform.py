import os
import subprocess
def transform():
    path = "./Images"
    def newest(path):
        files = os.listdir(path)
        paths = [os.path.join(path, basename) for basename in files]
        return max(paths, key=os.path.getctime)
    image = newest(path)

    subprocess.run(["ps2pdf", "-dEPSCrop" ,image, image[:-3]+"pdf"])
    subprocess.run(["pdf2svg", image[:-3]+"pdf", image[:-3]+"svg"])
    subprocess.run(["cp", image[:-3]+"svg", "./Images/mostRecent.svg"])

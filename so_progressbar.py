#function to display a progressbar. used on long l-systems
#from https://stackoverflow.com/a/34482761

import sys

def progressbar(it, prefix="", size=100, file=sys.stdout):
    count = len(it)
    def show(j):
        x = int(size*j/count)
        file.write("%s[%s%s] %i/%i %i%s\r" % (prefix , "◼"*x, "◻"*(size-x), j, count, x, "%"))
        file.flush()        
    show(0)
    for i, item in enumerate(it):
        yield item
        show(i+1)
    file.write("\n")
    file.flush()
    
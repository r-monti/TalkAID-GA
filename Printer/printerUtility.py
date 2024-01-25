import os
import sys


def createTextFile():
    percorso_script = os.path.abspath(sys.argv[0])

    directory = os.path.dirname(percorso_script)
    percorso_file = os.path.join(directory, "results.txt")
    return percorso_file

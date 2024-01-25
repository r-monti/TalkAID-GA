import os
import sys


def createTextFile() -> str:
    """
    Creates the file for printing the result.
    :return: The path to the file.
    """
    percorso_script = os.path.abspath(sys.argv[0])

    directory = os.path.dirname(percorso_script)
    percorso_file = os.path.join(directory, "results.txt")
    return percorso_file

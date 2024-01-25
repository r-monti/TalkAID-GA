from Printer.printerUtility import createTextFile
from datetime import datetime


def printIntoResults(*args):
    path = createTextFile()
    timestamp = f"\n\nTimestamp: {datetime.now()}, process {args[0]}\n"
    with open(path, 'a') as file:
        file.write(timestamp)
        for individual in args[1].getIndividuals():
            riga = f"{individual} Fitness: {individual.fitness()} \n"
            file.write(riga)
    file.close()

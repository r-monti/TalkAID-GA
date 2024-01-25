from Printer.printerUtility import createTextFile
from datetime import datetime


def printIntoResults(processNumber, population):
    path = createTextFile()
    timestamp = f"\n\nTimestamp: {datetime.now()}, process {processNumber}\n"

    with open(path, 'a') as file:
        file.write(timestamp)
        for individual in population.getIndividuals():
            riga = f"{individual} Fitness: {individual.fitness()} \n"
            file.write(riga)
    file.close()

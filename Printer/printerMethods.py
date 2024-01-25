from GA.Population.exercisePopulation import Population
from Printer.printerUtility import createTextFile
from datetime import datetime


def printIntoResults(processNumber: int, population: Population):
    """
    Prints on a file the results of the GA.
    :param processNumber: The process that ran the GA.
    :param population: The population.
    """
    path = createTextFile()
    timestamp = f"\n\nTimestamp: {datetime.now()}, process {processNumber}\n"

    with open(path, 'a') as file:
        file.write(timestamp)
        for individual in population.getIndividuals():
            riga = f"{individual} Fitness: {individual.fitness()} \n"
            file.write(riga)
    file.close()

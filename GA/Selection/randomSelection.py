import random
from GA.Population.exercisePopulation import Population


def randomSelection(population: Population):
    """
    This function generates a new population based on the Random selection algorithm.
    :param population: The starting Population.
    :return: A new Population after selection.
    """
    newP = []
    while len(newP) < len(population):
        newP.append(random.choice(population))
    return newP

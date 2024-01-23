import random


def randomSelection(population):
    """
    This method randomly selects an individual and creates a new population
    :param population: the starting population
    :return: a new population after selection
    """
    newP = []
    while len(newP) < len(population):
        newP.append(random.choice(population))
    return newP

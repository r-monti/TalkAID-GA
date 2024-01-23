import random


def randomSelection(population):
    """
    This function generates a new population based on the Random selection algorithm
    :param population: the starting population
    :return: a new population after selection
    """
    newP = []
    while len(newP) < len(population):
        newP.append(random.choice(population))
    return newP

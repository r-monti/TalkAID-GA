from random import random
from GA.Crossover.crossoverUtility import divide
from GA.Individual.exerciseIndividual import Individual


def nPoint(n: int, i1: Individual, i2: Individual) -> tuple[Individual, Individual]:
    """
    This function will perform n-point crossover with perfect interleaving
    :param n: number of points
    :param i1: the first individual
    :param i2: the second individual
    :return: the two new individuals
    """
    if len(i1) != len(i2):
        raise ValueError("Invalid individual length! They have to be the same.")
    elif n > len(i1):
        raise ValueError("Invalid n value, must be less than the lenght of the individual!")

    dividedI1, dividedI2 = divide(i1.getList(), n), divide(i2.getList(), n)

    newI1 = []
    newI2 = []

    for i, pair in enumerate(zip(dividedI1, dividedI2)):
        if i % 2 == 0:
            newI1.extend(pair[0])
            newI2.extend(pair[1])
        else:
            newI1.extend(pair[1])
            newI2.extend(pair[0])

    i1.setList(newI1)
    i2.setList(newI2)

    return i1, i2


def nPointReverse(n: int, i1: Individual, i2: Individual) -> tuple[Individual, Individual]:
    """
    This function will perform n-point crossover with perfect interleaving but starting with a switch
    :param n: number of points
    :param i1: the first individual
    :param i2: the second individual
    :return: the two new individuals
    """
    if len(i1) != len(i2):
        raise ValueError("Invalid individual length! They have to be the same.")
    elif n > len(i1):
        raise ValueError("Invalid n value, must be less than the lenght of the individual!")

    dividedI1, dividedI2 = divide(i1.getList(), n), divide(i2.getList(), n)

    newI1 = []
    newI2 = []

    for i, pair in enumerate(zip(dividedI1, dividedI2)):
        if i % 2 == 0:
            newI1.extend(pair[1])
            newI2.extend(pair[0])
        else:
            newI1.extend(pair[0])
            newI2.extend(pair[1])

    i1.setList(newI1)
    i2.setList(newI2)

    return i1, i2


def nPointRandom(n: int, i1: Individual, i2: Individual, crossoverProbability: float) -> tuple[Individual, Individual]:
    """
    This function will perform n-point crossover with random interleaving
    :param n: number of points
    :param i1: the first individual
    :param i2: the second individual
    :param crossoverProbability: the probability of crossover
    :return: the two new individuals
    """
    if len(i1) != len(i2):
        raise ValueError("Invalid individual length! They have to be the same.")
    elif n > len(i1):
        raise ValueError("Invalid n value, must be less than the lenght of the individual!")

    dividedI1, dividedI2 = divide(i1.getList(), n), divide(i2.getList(), n)

    newI1 = []
    newI2 = []

    for i, pair in enumerate(zip(dividedI1, dividedI2)):
        if random() < crossoverProbability:
            newI1.extend(pair[1])
            newI2.extend(pair[0])
        else:
            newI1.extend(pair[0])
            newI2.extend(pair[1])

    i1.setList(newI1)
    i2.setList(newI2)

    return i1, i2

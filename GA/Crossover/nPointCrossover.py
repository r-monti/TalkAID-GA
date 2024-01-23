from random import random
from GA.Crossover.crossoverUtility import divide


def nPoint(n, i1, i2):
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

    dividedI1, dividedI2 = divide(i1, n), divide(i2, n)

    newI1 = []
    newI2 = []

    for i, pair in enumerate(zip(dividedI1, dividedI2)):
        if i % 2 == 0:
            newI1.extend(pair[0])
            newI2.extend(pair[1])
        else:
            newI1.extend(pair[1])
            newI2.extend(pair[0])

    return newI1, newI2


def nPointReverse(n, i1, i2):
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

    dividedI1, dividedI2 = divide(i1, n), divide(i2, n)

    newI1 = []
    newI2 = []

    for i, pair in enumerate(zip(dividedI1, dividedI2)):
        if i % 2 == 0:
            newI1.extend(pair[1])
            newI2.extend(pair[0])
        else:
            newI1.extend(pair[0])
            newI2.extend(pair[1])

    return newI1, newI2


def nPointRandom(n, i1, i2, crossoverProbability):
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

    dividedI1, dividedI2 = divide(i1, n), divide(i2, n)

    newI1 = []
    newI2 = []

    for i, pair in enumerate(zip(dividedI1, dividedI2)):
        if random() < crossoverProbability:
            newI1.extend(pair[1])
            newI2.extend(pair[0])
        else:
            newI1.extend(pair[0])
            newI2.extend(pair[1])

    return newI1, newI2

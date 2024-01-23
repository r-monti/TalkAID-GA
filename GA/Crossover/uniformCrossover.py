from random import random
from GA.Crossover.crossoverUtility import divide


def uniformCrossover(i1, i2, crossoverProbability):
    """
    This function will perform uniform crossover
    :param i1: the first individual
    :param i2: the second individual
    :param crossoverProbability: the probability of crossover
    :return: the two new individuals
    """

    if len(i1) != len(i2):
        raise ValueError("Invalid individual length! They have to be the same.")

    dividedI1, dividedI2 = divide(i1, len(i1)), divide(i2, len(i2))

    newI1 = []
    newI2 = []

    for i, pair in enumerate(zip(dividedI1, dividedI2)):
        if random() < crossoverProbability:
            newI1.extend(pair[1])
        else:
            newI1.extend(pair[0])

        if random() < crossoverProbability:
            newI2.extend(pair[0])
        else:
            newI2.extend(pair[1])

    return newI1, newI2

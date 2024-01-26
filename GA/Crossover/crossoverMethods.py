from random import random
from GA.Crossover.crossoverUtility import divide
from GA.Individual.exerciseIndividual import Individual


def nPoint(i1: Individual, i2: Individual, n: int) -> tuple[Individual, Individual]:
    """
    Performs n-point crossover with perfect interleaving.
    :param i1: The first individual.
    :param i2: The second individual.
    :param n: Number of points.
    :return: The two new individuals.
    """
    if len(i1) != len(i2):
        raise ValueError("Invalid individual length! They have to be the same.")
    elif n > len(i1):
        raise ValueError("Invalid n value, must be less than the lenght of the individual!")

    dividedI1, dividedI2 = divide(i1.getList(), n), divide(i2.getList(), n)

    newI1 = list()
    newI2 = list()

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


def nPointReverse(i1: Individual, i2: Individual, n: int) -> tuple[Individual, Individual]:
    """
    Performs n-point crossover with perfect interleaving but starting with a switch.
    :param i1: The first individual.
    :param i2: The second individual.
    :param n: Number of points.
    :return: The two new individuals.
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


def nPointRandom(i1: Individual, i2: Individual, n: int,  crossoverProbability: float) -> tuple[Individual, Individual]:
    """
    Performs n-point crossover with random interleaving.
    :param i1: The first individual.
    :param i2: The second individual.
    :param n: Number of points.
    :param crossoverProbability: The probability of crossover.
    :return: The two new individuals.
    """
    if len(i1) != len(i2):
        raise ValueError("Invalid individual length! They have to be the same.")
    elif n > len(i1):
        raise ValueError("Invalid n value, must be less than the lenght of the individual!")
    elif crossoverProbability < 0 or crossoverProbability > 1:
        raise ValueError("Invalid crossoverProbability! Must be between 0 and 1")

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


def uniformCrossover(i1: Individual, i2: Individual, crossoverProbability: float) -> tuple[Individual, Individual]:
    """
    Performs uniform crossover.
    :param i1: The first individual.
    :param i2: The second individual.
    :param crossoverProbability: The probability of crossover.
    :return: The two new individuals.
    """

    if len(i1) != len(i2):
        raise ValueError("Invalid individual length! They have to be the same.")
    elif crossoverProbability < 0 or crossoverProbability > 1:
        raise ValueError("Invalid crossoverProbability! Must be between 0 and 1")

    dividedI1, dividedI2 = divide(i1.getList(), len(i1)), divide(i2.getList(), len(i2))

    newI1 = []
    newI2 = []

    for pair in zip(dividedI1, dividedI2):
        if random() < crossoverProbability:
            newI1.extend(pair[1])
        else:
            newI1.extend(pair[0])

        if random() < crossoverProbability:
            newI2.extend(pair[0])
        else:
            newI2.extend(pair[1])

    i1.setList(newI1)
    i2.setList(newI2)

    return i1, i2

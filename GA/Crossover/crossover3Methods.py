from random import random
from random import randint
from GA.Crossover.crossoverUtility import divide
from GA.Individual.exerciseIndividual import Individual


def nPoint(i1: Individual, i2: Individual, i3: Individual, n: int) -> tuple[Individual, Individual, Individual]:
    """
    Performs n-point crossover with perfect interleaving.
    :param i1: The first individual.
    :param i2: The second individual.
    :param i3: The third individual.
    :param n: Number of points.
    :return: The three new individuals.
    """
    if len(i1) != len(i2) != len(i3):
        raise ValueError("Invalid individual length! They have to be the same.")
    elif n > len(i1):
        raise ValueError("Invalid n value, must be less than the lenght of the individual!")

    dividedI1, dividedI2, dividedI3 = divide(i1.getList(), n), divide(i2.getList(), n), divide(i3.getList(), n)

    newI1 = list()
    newI2 = list()
    newI3 = list()

    for i, triplet in enumerate(zip(dividedI1, dividedI2, dividedI3)):
        if i % 3 == 0:
            newI1.extend(triplet[0])
            newI2.extend(triplet[1])
            newI3.extend(triplet[2])
        elif i % 3 == 1:
            newI1.extend(triplet[2])
            newI2.extend(triplet[0])
            newI3.extend(triplet[1])
        elif i % 3 == 2:
            newI1.extend(triplet[1])
            newI2.extend(triplet[2])
            newI3.extend(triplet[0])

    i1.setList(newI1)
    i2.setList(newI2)
    i3.setList(newI3)

    return i1, i2, i3


def nPointReverse(i1: Individual, i2: Individual, i3: Individual, n: int) -> tuple[Individual, Individual, Individual]:
    """
    Performs n-point crossover with perfect interleaving but starting with a switch.
    :param i1: The first individual.
    :param i2: The second individual.
    :param i3: The third individual.
    :param n: Number of points.
    :return: The two new individuals.
    """
    if len(i1) != len(i2) != len(i3):
        raise ValueError("Invalid individual length! They have to be the same.")
    elif n > len(i1):
        raise ValueError("Invalid n value, must be less than the lenght of the individual!")

    dividedI1, dividedI2, dividedI3 = divide(i1.getList(), n), divide(i2.getList(), n), divide(i3.getList(), n)

    newI1 = []
    newI2 = []
    newI3 = []

    for i, triplet in enumerate(zip(dividedI1, dividedI2, dividedI3)):
        if i % 3 == 0:
            newI1.extend(triplet[1])
            newI2.extend(triplet[2])
            newI3.extend(triplet[0])
        elif i % 3 == 1:
            newI1.extend(triplet[0])
            newI2.extend(triplet[1])
            newI3.extend(triplet[2])
        elif i % 3 == 2:
            newI1.extend(triplet[2])
            newI2.extend(triplet[0])
            newI3.extend(triplet[1])

    i1.setList(newI1)
    i2.setList(newI2)
    i3.setList(newI3)

    return i1, i2, i3


def nPointRandom(i1: Individual, i2: Individual, i3: Individual, n: int, crossoverProbability: float) -> tuple[Individual, Individual, Individual]:
    """
    Performs n-point crossover with random interleaving.
    :param i1: The first individual.
    :param i2: The second individual.
    :param i3: The third individual.
    :param n: Number of points.
    :param crossoverProbability: The probability of crossover.
    :return: The two new individuals.
    """
    if len(i1) != len(i2) != len(i3):
        raise ValueError("Invalid individual length! They have to be the same.")
    elif n > len(i1):
        raise ValueError("Invalid n value, must be less than the lenght of the individual!")
    elif crossoverProbability < 0 or crossoverProbability > 1:
        raise ValueError("Invalid crossoverProbability! Must be between 0 and 1")

    dividedI1, dividedI2, dividedI3 = divide(i1.getList(), n), divide(i2.getList(), n), divide(i3.getList(), n)

    newI1 = []
    newI2 = []
    newI3 = []

    for triplet in zip(dividedI1, dividedI2, dividedI3):
        if random() < crossoverProbability:
            i = randint(0, 2)
            if i % 3 == 0:
                newI1.extend(triplet[0])
                newI2.extend(triplet[1])
                newI3.extend(triplet[2])
            elif i % 3 == 1:
                newI1.extend(triplet[2])
                newI2.extend(triplet[0])
                newI3.extend(triplet[1])
            elif i % 3 == 2:
                newI1.extend(triplet[1])
                newI2.extend(triplet[2])
                newI3.extend(triplet[0])

    i1.setList(newI1)
    i2.setList(newI2)
    i3.setList(newI3)

    return i1, i2, i3

import random
from GA.Individual.exerciseIndividual import Individual


def find_rank(individuals: list[Individual], subdivision: float) -> Individual:
    """
    Selects the Individual based on the Rank selection algorithm.
    :param individuals: The Individuals sorted from worst to best.
    :param subdivision: The subdivision of the percentile for the selection.
    :return: The selected Individual.
    """
    num = random.randint(1, 100)
    prec = 0
    for i in range(1, len(individuals)):
        if prec < num <= (100/subdivision)*i:
            return Individual(*individuals[i].getList())
        else:
            prec = (100/subdivision)*i

import random
from GA.Evaluation.fitness import individualFitness as evaluate
from GA.Individual.exerciseIndividual import Individual
from GA.Population.exercisePopulation import Population


def rankSelection(population: Population):
    """
    This function generates a new Population based on the Rank selection algorithm.
    :param population: The starting population.
    :return: A new population after selection.
    """
    user = population.getUser()
    for i in range(len(population)):
        evaluate(population[i], user)

    sortedIndividuals = sorted(population.getIndividuals(), key=lambda ind: ind.fitness())

    newPopolation = list()
    size = len(sortedIndividuals)
    subdivision = (size * (size+1))/2

    while len(newPopolation) < len(population):
        newPopolation.append(find_rank(sortedIndividuals, subdivision))
    return sortedIndividuals


def find_rank(individuals: list[Individual], subdivision: float) -> Individual:
    """
    This function selects the Individual based on the Rank selection algorithm.
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

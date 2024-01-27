import random
import GA.Selection.selectionUtility as su
from GA.Individual.exerciseIndividual import Individual
from GA.Population.exercisePopulation import Population
from GA.Evaluation.fitness import individualFitness as evaluate


def randomSelection(population: Population):
    """
    Generates a new population based on the Random selection algorithm.
    :param population: The starting Population.
    :return: A new Population after selection.
    """
    newP = []
    while len(newP) < len(population):

        newP.append(Individual(*random.choice(population)).getList())
    return newP


def rankSelection(population: Population):
    """
    Generates a new Population based on the Rank selection algorithm.
    :param population: The starting population.
    :return: A new population after selection.
    """
    user = population.getUser()
    for i in range(len(population)):
        evaluate(population[i], user)

    sortedIndividuals = sorted(population.getIndividuals(), key=lambda ind: ind.fitness())

    newPopolation = list()
    size = len(sortedIndividuals)
    subdivision = (size * (size + 1)) / 2

    while len(newPopolation) < len(population):
        newPopolation.append(su.find_rank(sortedIndividuals, subdivision))
    return sortedIndividuals


def rouletteWheel(population: Population):
    """
    Generates a new Population based on the Roulette Wheel selection algorithm.
    :param population: The starting Population.
    :return: A new Population after selection.
    """
    user = population.getUser()
    totalFitness = 0
    for i in population.getIndividuals():
        evaluate(i, user)
        totalFitness += i.fitness()

    newIndividuals = list()
    while len(newIndividuals) < len(population):
        value = random.random() * totalFitness
        comulativeFitness = 0
        for i in population.getIndividuals():
            comulativeFitness += i.fitness()
            if comulativeFitness >= value:
                newIndividuals.append(Individual(*i.getList()))
                break

    return newIndividuals

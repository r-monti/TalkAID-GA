from random import random
from GA.Evaluation.fitness import individualFitness as evaluate
from GA.Population.exercisePopulation import Population
from GA.Individual.exerciseIndividual import Individual


def rouletteWheel(population: Population):
    """
    This function generates a new Population based on the Roulette Wheel selection algorithm.
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
        value = random() * totalFitness
        comulativeFitness = 0
        for i in population.getIndividuals():
            comulativeFitness += i.fitness()
            if comulativeFitness >= value:
                newIndividuals.append(Individual(*i.getList()))
                break

    return newIndividuals

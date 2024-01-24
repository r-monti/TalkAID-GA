from GA.Population.exercisePopulation import Population
from GA.Individual.exerciseIndividual import Individual
import GA.Crossover.crossoverMethods as crossover
import random


def executeCrossover(p: Population, crossoverType: crossover, *args) -> list[Individual]:
    """
    This function executes the crossover on a population.
    :param p: The starting population.
    :param crossoverType: The crossover algorithm we want to perform.
    :param args: The arguments to pass to the crossover method as needed.
    :return: The new population.
    """
    newIndividuals = list()
    individuals = p.getIndividuals()
    size = len(p)

    if size % 2 != 0:
        raise ValueError("The size of the population must be even!")
    else:
        for _ in range(round(len(p) / 2)):
            i1 = random.choice(individuals)
            p.removeIndividual(i1)
            i2 = random.choice(individuals)
            p.removeIndividual(i2)
            i1, i2 = crossoverType(i1, i2, *args)
            newIndividuals.append(i1)
            newIndividuals.append(i2)

        return newIndividuals

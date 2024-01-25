from GA.Population.exercisePopulation import Population
from GA.Individual.exerciseIndividual import Individual
import GA.Crossover.crossover3Methods as crossover
import random


def execute3Crossover(p: Population, crossoverType: crossover, *args) -> list[Individual]:
    """
    Executes the crossover on a population taking 3 individuals instead of 2.
    :param p: The starting population.
    :param crossoverType: The crossover algorithm we want to perform.
    :param args: The arguments to pass to the crossover method as needed.
    :return: The new population.
    """
    newIndividuals = list()
    individuals = p.getIndividuals()
    size = len(p)

    if size % 3 != 0:
        raise ValueError("The size of the population must be divisible by 3!")
    else:
        for _ in range(round(len(p) / 3)):
            i1 = random.choice(individuals)
            p.removeIndividual(i1)
            i2 = random.choice(individuals)
            p.removeIndividual(i2)
            i3 = random.choice(individuals)
            p.removeIndividual(i3)
            i1, i2, i3 = crossoverType(i1, i2, i3, *args)
            newIndividuals.append(i1)
            newIndividuals.append(i2)
            newIndividuals.append(i3)

        return newIndividuals

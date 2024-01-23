import random
import DataBase.DBExercise as db


def randomMutation(p, mutationRate):
    """
    This function will randomly mutate an individual in a population
    :param p: the population
    :param mutationRate: probability of mutation
    :return: the population after mutation
    """
    if random.random() < mutationRate:
        i = random.choice(p)
        p = mutate(i, p)

    return p


def mutate(i, population):
    """
    This function will mutate the individual of the population
    :param population: the starting population
    :param i: the individual to replace
    :return: the population with a new individual
    """
    index = population.index(i)
    population[index] = db.seleziona_esercizio_casuale(population.getUserID)

    return population

import random
import DataBase.DBExercise as db
from GA.Population.exercisePopulation import Population
from GA.Individual.exerciseIndividual import Individual


def randomSingleMutation(p: Population, mutationRate: float) -> Population:
    """
    This function will randomly mutate an individual in a population
    :param p: the population
    :param mutationRate: probability of mutation
    :return: the population after mutation
    """
    if random.random() < mutationRate:
        i = random.choice(p.getIndividuals())
        userID = p.getUserId()
        currGeneration = p.getGeneration()
        p.replaceIndividual(i, mutate(i, userID, currGeneration))

    return p


def mutate(i: Individual, userId: int, gen: int) -> Individual:
    """
    This function will mutate a random exercise in an Individual
    :param i: the individual to mutate
    :param userId: the ID of the User
    :param gen: the current generation
    :return: the new Individual after mutation
    """
    oldEx = random.choice(i.getList())
    newEx = db.seleziona_esercizi_casuale(1, userId)
    i.replaceExercise(oldEx, newEx, gen)

    return i


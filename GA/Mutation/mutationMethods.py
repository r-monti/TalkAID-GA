import random
import DataBase.DBExercise as db
from GA.Population.exercisePopulation import Population
from GA.Individual.exerciseIndividual import Individual


def randomSingleMutation(p: Population, mutationRate: float) -> Population:
    """
    This function will randomly mutate an Individual in a Population.
    :param p: The Population to mutate.
    :param mutationRate: Probability of mutation.
    :return: The population after mutation.
    """
    if random.random() < mutationRate:
        i = random.choice(p.getIndividuals())
        userID = p.getUser().getID()
        currGeneration = p.getGeneration()
        p.replaceIndividual(i, mutate(i, userID, currGeneration))

    return p


def mutate(i: Individual, userId: int, gen: int) -> Individual:
    """
    This function will mutate a random exercise in an Individual.
    :param i: The Individual to mutate.
    :param userId: The ID of the User.
    :param gen: The current generation.
    :return: The new Individual after mutation.
    """
    oldEx = random.choice(i.getList())
    newEx = db.select_random_exercise(1, userId)[0]
    i.replaceExercise(oldEx, newEx, gen)

    return i

def worstIndividualMutation(p: Population, mutationRate: float) -> Population:
    """
    This function will mutate the worst Individual in a Population.
    :param p: The Population to mutate.
    :param mutationRate: Probability of mutation.
    :return: The population after mutation.
    """
    individuals = p.getIndividuals()
    minF = individuals[0].fitness()
    indice = 0
    for index, individual in enumerate(individuals):
        if minF > individual.fitness():
            minF = individual.fitness()
            indice = index

    if random.random() < mutationRate:
        i = p.getIndividuals()[indice]
        p.replaceIndividual(i, mu.mutateIndividual(i, p))

    return p

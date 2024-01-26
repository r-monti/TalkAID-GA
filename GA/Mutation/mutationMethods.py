import random
from GA.Population.exercisePopulation import Population
import GA.Mutation.mutationUtility as mu


def randomSingleMutation(p: Population, mutationRate: float) -> Population:
    """
    This function will randomly mutate a gene in an Individual in a Population.
    :param p: The Population to mutate.
    :param mutationRate: Probability of mutation.
    :return: The population after mutation.
    """
    if random.random() < mutationRate:
        i = random.choice(p.getIndividuals())
        p.replaceIndividual(i, mu.mutateEx(i, p))

    return p


def randomIndividualMutation(p: Population, mutationRate: float) -> Population:
    """
    This function will randomly mutate an entire Individual in a Population.
    :param p: The Population to mutate.
    :param mutationRate: Probability of mutation.
    :return: The population after mutation.
    """
    individuals = p.getIndividuals()

    if random.random() < mutationRate:
        i = random.choice(individuals)
        p.replaceIndividual(i, mu.mutateIndividual(i, p))

    return p



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

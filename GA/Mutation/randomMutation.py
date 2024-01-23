import random


def randomMutation(p, mutationRate):
    """
    This function will randomly mutate an individual in a population
    :param p: the population
    :param mutationRate: probability of mutation
    :return: the population after mutation
    """
    if random.random() < mutationRate:
        i = randomSelect(p)
        # mutate(i)


def randomSelect(p):
    """
    This function will randomly select an individual
    :param p: the population
    :return: the individual selected
    """
    random_index = random.randint(0, len(p) - 1)
    return p[random_index]


def mutate(i):
    """
    This function will mutate the individual of the population
    :param i: the individual to replace
    :return: the new individual
    """
    # database.replace(i) # TODO: implement database connection
    pass


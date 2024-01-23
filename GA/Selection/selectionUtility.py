def normalize(fitness, minF, maxF):
    """
    This function normalizes the values of the fitness between 0 and 1
    :param fitness: the fitness to normalize
    :param minF: the minimum value of the fitness for this population
    :param maxF: the maximum value of the fitness for this population
    :return: the population with normalized fitnes
    """
    return (fitness - minF) / (maxF-minF)

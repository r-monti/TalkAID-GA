def rankSelection(population):
    """
    This function generates a new population based on the Rank selection algorithm
    :param population: the starting population
    :return: a new population after selection
    """
    sortedPopulation = sorted(population, key=lambda x: x.getFitnessValue(), reverse=True)
    return sortedPopulation

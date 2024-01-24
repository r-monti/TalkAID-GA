def rankSelection(population):
    """
    This function generates a new Population based on the Rank selection algorithm.
    :param population: The starting population.
    :return: A new population after selection.
    """
    user = population.getUser()
    for i in range(len(population)):
        evaluate(population[i], user)

    sortedIndividuals = sorted(population.getIndividuals(), key=lambda ind: ind.fitness())

    newPopolation = list()
    size = len(sortedIndividuals)
    subdivision = (size * (size+1))/2

    while len(newPopolation) < len(population):
        newPopolation.append(find_rank(sortedIndividuals, subdivision))
    return sortedIndividuals


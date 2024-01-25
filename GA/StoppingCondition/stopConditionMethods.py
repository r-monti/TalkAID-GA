from GA.Population.exercisePopulation import Population


def stoppingCondition(p: Population, lastFitness, unchangedCount: int, increaseRate: float) -> tuple[int, int]:
    """
    Checks whether the GA should stop based on the fitness value.
    :param p: The Population.
    :param lastFitness: The fitness value of the last generation.
    :param unchangedCount: Current number of unchanged generations.
    :param increaseRate: The percentage of fitness needed to continue the generations.
    :return: The updated unchangedCound and the updated lastFitness values to use in the next generation.
    """
    currentFitness = round(p.totalFitness())
    if lastFitness < currentFitness <= lastFitness + (lastFitness * increaseRate):
        unchangedCount += 1
    else:
        unchangedCount = 0
    lastFitness = p.totalFitness()
    return unchangedCount, lastFitness

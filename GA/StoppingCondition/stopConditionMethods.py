from GA.Population.exercisePopulation import Population


def stoppingCondition(p: Population, lastFitness, unchangedCount: int, increaseRate: int) -> tuple[int, int]:
    currentFitness = round(p.totalFitness())
    if lastFitness < currentFitness <= lastFitness + ((lastFitness / 100) * increaseRate):
        unchangedCount += 1
    else:
        unchangedCount = 0
    lastFitness = p.totalFitness()
    return unchangedCount, lastFitness

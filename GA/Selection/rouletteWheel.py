from random import random
from GA.Selection.selectionUtility import normalize


def RouletteWheel(population):
    """
    This funcion selects one individual based on the Roulette Wheel selection algorithm
    :param population: the starting population
    :return: a new population after selection
    """
    # TODO: manca la funzione di fitness EVALUATE per farlo funzionare
    minF, maxF = evaluate(population[0])
    for i in range(1, len(population)):
        population[i].fitness = evaluate(population[i])
        if population[i].fitness < minF:
            minF = population[i].fitness
        elif population[i].fitness > maxF:
            maxF = population[i].fitness
        population[i].normFitness = normalize(population[i].fitness, minF, maxF)

    newPopulation = []
    while len(newPopulation) < len(population):
        for individual in population:
            if random() < individual.normFitness:
                newPopulation.append(individual)

    return newPopulation

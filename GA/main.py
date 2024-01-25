from GA.Initialization.populationInitializer import initialize
from GA.StoppingCondition.stopConditionMethods import stoppingCondition

# from GA.Crossover.crossover import executeCrossover as crossover
# import GA.Crossover.crossoverMethods as cType
from GA.Crossover.crossover3Parents import execute3Crossover as crossover3P
import GA.Crossover.crossover3Methods as c3Type

from Printer.printerMethods import printIntoResults
import GA.Selection.selectionMethods as sType
import GA.Mutation.mutationMethods as mType
from multiprocessing import Pool, cpu_count


def startGA():
    p1 = initialize(6, 5, 904)
    p2 = initialize(6, 5, 914)
    p = [p1, p2]

    pool = Pool(processes=(cpu_count() - 1))

    for index, population in enumerate(p):
        pool.apply_async(GATasks, args=(index, population))

    pool.close()
    pool.join()


def GATasks(processNumber, population):
    gen = 0
    unchangedCount = 0
    lastFitness = 0

    maxGen = 400
    maxEqualsGen = 5
    increaseRate = 1

    print(f"Started process {processNumber}.")
    while gen < maxGen and unchangedCount < maxEqualsGen:
        gen += 1

        print(f"Current generation for P:{processNumber}: {gen}")
        population.setIndividuals(sType.rankSelection(population))
        # population.setIndividuals(crossover(population, cType.nPoint, 2))
        population.setIndividuals(crossover3P(population, c3Type.nPoint, 2))
        mType.randomIndividualMutation(population, 0.5)
        population.incrementGeneration()
        print("--------------------------------------------------------------------")
        unchangedCount, lastFitness = stoppingCondition(population, lastFitness, unchangedCount, increaseRate)

    print(f"\n\nProcess {processNumber} has ended.\n\n")
    printIntoResults(processNumber, population)


if __name__ == '__main__':
    startGA()

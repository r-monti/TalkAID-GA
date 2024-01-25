from GA.Initialization.populationInitializer import initialize as initializeP
from GA.printerUtility import createTextFile
from GA.Crossover.crossover import executeCrossover as crossover
import GA.Selection.selectionMethods as sType
import GA.Crossover.crossoverMethods as cType
import GA.Mutation.mutationMethods as mType
from datetime import datetime
from multiprocessing import Pool, cpu_count


def startGA():
    p1 = initialize(4, 5, 904)
    p2 = initialize(4, 5, 914)
    p = [p1, p2]

    pool = Pool(processes=(cpu_count() - 1))

    for index, population in enumerate(p):
        pool.apply_async(GATasks, args=(index, population))

    pool.close()
    pool.join()


def GATasks(*args):
    gen = 0
    print(f"Started process {args[0]}.")
    while gen < 2:
        gen += 1
        print(f"Current generation for P:{args[0]}: {gen}")
        args[1].setIndividuals(sType.rankSelection(args[1]))
        args[1].setIndividuals(crossover(args[1], cType.nPoint, 2))
        mType.randomIndividualMutation(args[1], 0.5)
        args[1].incrementGeneration()
        print("-----------------------------")
    print(f"Process {args[0]} has ended.")

    path = createTextFile()
    timestamp = f"\n\nTimestamp: {datetime.now()}, process {args[0]}\n"
    with open(path, 'a') as file:
        file.write(timestamp)
        for individual in args[1].getIndividuals():
            riga = f"{individual} Fitness: {individual.fitness()} \n"
            file.write(riga)
    file.close()


if __name__ == '__main__':
    startGA()


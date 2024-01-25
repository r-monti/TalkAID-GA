from GA.Initialization.populationInitializer import initialize
from GA.Selection.rankSelection import rankSelection as selection
from GA.Crossover.crossover import executeCrossover as crossover
import GA.Crossover.crossoverMethods as csType
from GA.Mutation.mutationMethods import randomSingleMutation as mutation

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
    while gen < 50:
        gen += 1
        print(f"Process: {args[0]}")
        print(f"Generation {gen}: P:{args[1]}")
        args[1].setIndividuals(selection(args[1]))
        args[1].setIndividuals(crossover(args[1], csType.nPoint, 2))
        mutation(args[1], 0.5)
        args[1].incrementGeneration()
        print("-----------------------------")

    print(f"\nResult for user {args[1].getUser().getID()}:")
    for individual in args[1].getIndividuals():
        print(individual, "Fitness:", individual.fitness())


if __name__ == '__main__':
    startGA()

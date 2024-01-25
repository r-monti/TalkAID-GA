from GA.Initialization.populationInitializer import initialize
from GA.Selection.rankSelection import rankSelection as selection
from GA.Crossover.crossover import executeCrossover as crossover
import GA.Crossover.crossoverMethods as csType
from GA.Mutation.mutationMethods import randomSingleMutation as mutation
import threading

p = initialize(4, 5, 904)
p2 = initialize(4, 5, 914)


def task(*args):
    print(f"Thread: {args[0]}")
    print(f"Generation {args[1].getGeneration()}: P:{args[1]}")
    args[1].setIndividuals(selection(args[1]))
    args[1].setIndividuals(crossover(args[1], csType.nPoint, 2))
    mutation(args[1], 0.5)
    args[1].incrementGeneration()
    print("-----------------------------")


while p.getGeneration() < 50:
    thread1 = threading.Thread(target=task, args=(1, p))
    thread2 = threading.Thread(target=task, args=(2, p2))
    thread1.start()
    thread2.start()
    thread1.join()
    thread2.join()


print("\nResult:")
for individual in p.getIndividuals():
    print(individual, "Fitness:", individual.fitness())

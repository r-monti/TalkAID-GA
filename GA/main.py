from GA.Initialization.populationInitializer import initialize
from GA.Selection.rouletteWheel import rouletteWheel as selection
from GA.Crossover.crossover import executeCrossover as crossover
import GA.Crossover.crossoverMethods as csType
from GA.Mutation.mutationMethods import randomSingleMutation as mutation

p = initialize(4, 5, 904)

while p.getGeneration() < 100:
    print(f"Generation {p.getGeneration()}: P:{p}")
    p.setIndividuals(selection(p))
    p.setIndividuals(crossover(p, csType.nPoint, 2))
    mutation(p, 0.5)
    p.incrementGeneration()
    print("-----------------------------")


print("\nResult:")
for individual in p.getIndividuals():
    print(individual, "Fitness:", individual.fitness())

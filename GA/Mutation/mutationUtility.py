import random
import DataBase.DBExercise as db
from GA.Population.exercisePopulation import Population
from GA.Individual.exerciseIndividual import Individual
from GA.Evaluation.fitness import individualFitness as evaluate


def mutateEx(i: Individual, p: Population) -> Individual:
    """
    This function will mutate a random exercise in an Individual.
    :param i: The Individual to mutate.
    :param p: The Population of the individual.
    :return: The new Individual after mutation.
    """
    userId = p.getUser().getID()
    gen = p.getGeneration()
    oldEx = random.choice(i.getList())
    newEx = db.select_random_exercise(1, userId)[0]
    i.replaceExercise(oldEx, newEx, gen)
    evaluate(i, p.getUser())

    return i


def mutateIndividual(i: Individual, p: Population):
    """
    This function will mutate the entire Individual.
    :param i: The Individual to mutate.
    :param p: The Population of the Individual.
    :return: The new Individual after mutation.
    """
    userId = p.getUser().getID()
    gen = p.getGeneration()
    newIndividual = Individual(*db.select_random_exercise(len(i.getList()), userId))
    evaluate(newIndividual, p.getUser())
    for ex in newIndividual.getList():
        ex.setGeneration(gen)

    return newIndividual

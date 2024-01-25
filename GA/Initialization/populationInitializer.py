from GA.Population.exercisePopulation import Population
from GA.Individual.exerciseIndividual import Individual
from DataBase.DBExercise import select_random_exercise
from DataBase.DBCreate import createUser


def initialize(pSize: int, iSize: int, userId: int) -> Population:
    """
    This function will initialize the Population, creating pSize Individuals, each with iSize random Exercises.
    :param pSize: The size of the Population.
    :param iSize: The size of an Individual.
    :param userId: The ID of the User.
    :return: a Population.
    """
    lst = list()
    u = createUser(userId)
    for _ in range(pSize):
        lst.append(Individual(*select_random_exercise(iSize, userId)))
    return Population(u, *lst)

from GA.Population.exercisePopulation import Population
from GA.Individual.exerciseIndividual import Individual
from DataBase.DBExercise import seleziona_esercizi_casuale


def initialize(pSize, iSize, userId):
    lst = list()
    for _ in range(pSize):
        lst.append(Individual(seleziona_esercizi_casuale(iSize, userId)))
    return Population(userId, lst)

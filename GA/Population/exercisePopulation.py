from GA.Individual.user import User
from GA.Individual.exerciseIndividual import Individual


class Population:
    """
    This class will contain all the information about the population of exercises to recommend
    """
    def __init__(self, u: User, *args: Individual):
        """
        Initializes the Population object.
        :param u: The User.
        :param args: The Individuals that the Population object will contain.
        """
        self._user = u
        self._entireFitness = 0
        self._currGen = 0
        self._individuals = list()
        for i in args:
            self._individuals.append(i)

    def __len__(self):
        return len(self._individuals)

    def __str__(self):
        return f"Population for user {self._user}: {self._individuals}"

    def __getitem__(self, item: int):
        if self._individuals[item] is not None:
            return self._individuals[item]
        else:
            return None

    def totalFitness(self) -> int:
        """
        Returns the total fitness of the Population.
        :return: the fitness of the Population.
        """
        self._entireFitness = 0
        for individual in self._individuals:
            self._entireFitness += individual.fitness()
        return self._entireFitness

    def replaceIndividual(self, oldIndividual: Individual, newIndividual: Individual):
        """
        Replaces an Individual with a new Individual.
        :param oldIndividual: The Individual to replace.
        :param newIndividual: The new Individual to insert.
        """
        if oldIndividual in self._individuals:
            index = self._individuals.index(oldIndividual)
            self._individuals[index] = newIndividual
        else:
            raise ValueError(f"Invalid Individual_ {Individual}")

    def removeIndividual(self, i: Individual):
        """
        Removes an Individual.
        :param i: The Individual to remove.
        """
        if i in self._individuals:
            self._individuals.remove(i)
        else:
            raise ValueError("Individual not found in the population")

    def getIndividuals(self) -> list[Individual]:
        """
        Returns a list of Individuals.
        :return: The Individuals of the Population.
        """
        return self._individuals

    def setIndividuals(self, newIndividuals: list[Individual]):
        """
        Sets new Individuals removing all the old ones.
        :param newIndividuals: The Individuals to set.
        """
        self._individuals = newIndividuals

    def getUser(self) -> User:
        """
        Returns the User of the Population.
        :return: The User object.
        """
        return self._user

    def incrementGeneration(self):
        """
        Increments the current generation by 1.
        """
        self._currGen += 1

    def getGeneration(self) -> int:
        """
        Returns the current generation.
        :return: The current Generation number.
        """
        return self._currGen

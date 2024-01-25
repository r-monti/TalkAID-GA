from GA.Individual.user import User
from GA.Individual.exerciseIndividual import Individual


class Population:
    """
    This class will contain all the information about the population of exercises to recommend
    """
    def __init__(self, u: User, *args: Individual):
        """
        This method will initialize the Population object.
        :param u: The User.
        :param args: The Individuals that the Population object will contain.
        """
        self._user = u
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

    def replaceIndividual(self, oldIndividual: Individual, newIndividual: Individual):
        """
        This method will replace an Individual with a new Individual.
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
        This method removes an Individual.
        :param i: The Individual to remove.
        """
        if i in self._individuals:
            self._individuals.remove(i)
        else:
            raise ValueError("Individual not found in the population")

    def getIndividuals(self) -> list[Individual]:
        """
        This method returns a list of Individuals.
        :return: The Individuals of the Population.
        """
        return self._individuals

    def setIndividuals(self, newIndividuals: list[Individual]):
        """
        This method sets new Individuals removing all the old ones.
        :param newIndividuals: The Individuals to set.
        """
        self._individuals = newIndividuals

    def getUser(self) -> User:
        """
        This method return the User of the Population.
        :return: The User object.
        """
        return self._user

    def incrementGeneration(self):
        """
        This method increments the current generation by 1.
        """
        self._currGen += 1

    def getGeneration(self) -> int:
        """
        This method return the current generation.
        :return: The current Generation number.
        """
        return self._currGen

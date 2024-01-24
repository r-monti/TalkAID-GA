class Population:
    """
    This class will contain all the information about the population of exercises to recommend
    """
    def __init__(self, userId, *args):
        self._userId = userId
        self._currGen = 0
        self._individuals = list()
        for i in args:
            self._individuals.append(i)

    def __len__(self):
        return len(self._individuals)

    def __str__(self):
        return f"Population for user {self._userId}: {self._individuals}"

    def getIndividualByIndex(self, i):
        if self._individuals[i] is not None:
            return self._individuals[i]
        else:
            return None

    def replaceIndividual(self, oldIndividual, newIndividual):
        index = self._individuals.index(oldIndividual)
        self._individuals[index] = newIndividual

    def getIndividuals(self):
        return self._individuals

    def getUserId(self):
        return self._userId

    def incrementGeneration(self):
        self._currGen += 1

    def getGeneration(self):
        return self._currGen

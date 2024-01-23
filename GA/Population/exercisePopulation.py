class exercisePopulation:
    """
    This class will contain all the information about the population of exercises to recommend
    """
    def __init__(self, userId, *args):
        self._userId = userId
        for index, ex in enumerate(*args):
            setattr(self, f"_i{index}", ex)

    def getIndividual(self, i):
        if hasattr(self, f"_i{i}"):
            return getattr(self, f"_i{i}")
        else:
            return None

    def __str__(self):
        return f"Population for user{self._userId}"

    def printIndividualsGen(self):
        i = 0
        while hasattr(self, f"_i{i}"):
            yield getattr(self, f"_i{i}").str()
            i += 1

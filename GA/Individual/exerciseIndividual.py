class Individual:
    """
    This class represents a single individual
    """
    def __init__(self, *args):
        self._individualFitness = 0
        self._exercises = list()
        for ex in args:
            self._exercises.append(ex)

    def __len__(self):
        return len(self._exercises)

    def __str__(self):
        return f"Individual {id(self)}: {self._exercises}"

    def __repr__(self):
        return f"\nI-{id(self)}: {self._exercises}"

    def getExerciseByIndex(self, i):
        if self._exercises[i] is not None:
            return self._exercises[i]
        else:
            return None

    def replaceExercise(self, oldEx, newEx, gen):
        newEx.setGeneration(gen)
        index = self._exercises.index(oldEx)
        self._exercises[index] = newEx

    def getList(self):
        return self._exercises

    def setList(self, lst):
        self._exercises = lst

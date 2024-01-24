from GA.Individual.exercise import Exercise


class Individual:
    """
    This class represents a single individual
    """
    def __init__(self, *args: Exercise):
        """
        This method will initialize the Individual object.
        :param args: all the Exercises that will form the individual.
        """
        self._individualFitness = 0
        self._exercises = list()
        for ex in args:
            self._exercises.append(ex)

    def __len__(self):
        return len(self._exercises)

    def __iter__(self):
        return iter(self._exercises)

    def __str__(self):
        return f"Individual {id(self)}: {self._exercises}"

    def __repr__(self):
        return f"\nI-{id(self)}: {self._exercises}"

    def fitness(self) -> float:
        """
        This function will calculate and then return the fitness of the Individual.
        :return: The fitness of the Individual formed by the fitness of the exercises in the Individual.
        """
        self._individualFitness = 0
        for ex in self._exercises:
            self._individualFitness += ex.getFitnessValue()
        return self._individualFitness

    def getExerciseByIndex(self, i: int) -> Exercise | None:
        """
        This function returns the exercise with the desired index if it exists.
        :param i: The index of the exercise.
        :return: The Exercise of that index or None if the Exercise does not exist.
        """
        if self._exercises[i] is not None:
            return self._exercises[i]
        else:
            return None

    def replaceExercise(self, oldEx: Exercise, newEx: Exercise, gen: int):
        """
        This function will replace an Exercise with a new Exercise, updating the generation number of the new Exercise.
        :param oldEx: The Exercise to replace.
        :param newEx: The Exercise to insert.
        :param gen: The current generation.
        """
        newEx.setGeneration(gen)
        index = self._exercises.index(oldEx)
        self._exercises[index] = newEx

    def getList(self) -> list[Exercise]:
        """
        This function returns the list of Exercises of the Individual.
        :return: The list of Exercises.
        """
        return self._exercises

    def setList(self, lst: list):
        """
        This function sets a new list of Exercises for the Individual.
        :param lst: The new list of Exercises.
        """
        self._exercises = lst

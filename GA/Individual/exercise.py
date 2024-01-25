class Exercise:
    """
    This class will contain all the necessary information about the exercise.
    """
    def __init__(self, ID: int, exerciseDifficulty: int, target: str, exType: str,
                 lastEvaluation: int | None, lastCompletionDate: str | None, lastFeedback: int | None):
        """
        Initializes the Exercise object.
        :param ID: The ID of the exercise.
        :param exerciseDifficulty: The difficulty of the exercise.
        :param target: The conditions that the exercise aims to help.
        :param exType: The type of exercise.
        :param lastEvaluation: The last evaluation of the exercise.
        :param lastCompletionDate: The last completion date of the exercise.
        :param lastFeedback: The last feedback of the exercise.
        """

        self._fitnessValue = 0
        self._generation = 0
        self._exerciseID = ID
        self._exerciseDifficulty = exerciseDifficulty
        self._target = target
        self._exType = exType
        self._lastEvaluation = lastEvaluation
        self._lastCompletionDate = lastCompletionDate
        self._lastFeedback = lastFeedback

    def __str__(self):
        return "Exercise ID: {}, Exercise Type: {}".format(self._exerciseID, self._exType)

    def __repr__(self):
        return "ID: {}".format(self._exerciseID)

    def getFitnessValue(self) -> float:
        """
        Returns the fitness value of the exercise.
        :return: The fitness value.
        """
        return self._fitnessValue

    def setFitnessValue(self, value: float) -> None:
        """
        Sets the fitness value of the exercise.
        :param value: The new fitness value to set.
        """
        self._fitnessValue = value

    def getGeneration(self) -> int:
        """
        Returns the generation in which the exercise has been inserted.
        :return: The generation value.
        """
        return self._generation

    def setGeneration(self, value: int) -> None:
        """
        Sets the generation in which the exercise has been inserted.
        :param value: The generation value.
        """
        self._generation = value

    def getExerciseID(self) -> int:
        """
        Returns the exercise ID.
        :return: The exercise ID.
        """
        return self._exerciseID

    def getExerciseDifficulty(self) -> int:
        """
        Returns the exercise difficulty.
        :return: The exercise difficulty, between 1 and 10.
        """
        return self._exerciseDifficulty

    def getExerciseTarger(self) -> str:
        """
        Returns the target of the exercise.
        :return: The target of the exercise, usually at least 3 Conditions names.
        """
        return self._target

    def getExerciseType(self) -> str:
        """
        Returns the exercise type.
        :return: The exercise type, between 'READTEXT', 'READIMAGES', 'IMAGESTOTEXT', 'TEXTTOIMAGES', 'CROSSWORD',
        'COMPLETETEXT', 'RIGHTTEXT'.
        """
        return self._exType

    def getLastEvaluation(self) -> int | None:
        """
        Returns the last evaluation of the Exercise.
        :return: The last Evaluation or None if the exercise has not been evaluated yet.
        """
        return self._lastEvaluation

    def getLastCompletionDate(self) -> str | None:
        """
        Returns the last completion date of the Exercise.
        :return: The last CompletionDate or None if the exercise has not been executed yet.
        """
        return self._lastCompletionDate

    def getLastFeedback(self) -> int:
        """
        Returns the last feedback of the Exercise.
        :return: The last feedback, between -1 and +1.
        """
        return self._lastFeedback

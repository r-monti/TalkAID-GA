class Exercise:
    """
    This class will contain all the necessary information about the exercise
    """
    def __init__(self, ID, exerciseDifficulty, target, exType, lastEvaluation, lastCompletionDate, lastFeedback):
        """
        :param ID: the ID of the exercise, int
        :param exerciseDifficulty: the difficulty of the exercise, int between 1,10
        :param target: the condition that the exercise aims to help, tuple(Strings)
        :param exType: the type of exercise, String

        All the next params are based on the last execution of the exercise done by the user
        :param lastEvaluation: the last evaluation of the exercise, int between 0,100
        :param lastCompletionDate: the last completion date of the exercise, date
        :param lastFeedback: the last feedback of the exercise, int between -1,1
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

    def getFitnessValue(self):
        return self._fitnessValue

    def setFitnessValue(self, value):
        self._fitnessValue = value

    def getGeneration(self):
        return self._generation

    def setGeneration(self, value):
        self._generation = value

    def getExerciseID(self):
        return self._exerciseID

    def getExerciseDifficulty(self):
        return self._exerciseDifficulty

    def getExerciseTarger(self):
        return self._target

    def getExerciseType(self):
        return self._exType

    def getLastEvaluation(self):
        return self._lastEvaluation

    def getLastCompletionDate(self):
        return self._lastCompletionDate

    def getLastFeedback(self):
        return self._lastFeedback

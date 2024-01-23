class User:
    """
    This class will contain all the necessary information about the User
    """
    def __init__(self, ID, conditions, exercises):
        """
        :param ID: the id of the user, int
        :param conditions: a dictionary with the conditions and their severities,
                dict{conditionID: (Severity, WritingSeverity, ReadingSeverity)}
        :param exercises: last 50 exercises done,
                dict{exerciseID: (CompletionDate, Evaluation, Feedback, Difficulty, Type)}
        """

        self._ID = ID
        self._conditions = conditions
        self._exercises = exercises

    def getID(self):
        return self._ID

    def getConditions(self):
        return self._conditions.copy()

    def getExercises(self):
        return self._exercises.copy()

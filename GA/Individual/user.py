class User:
    """
    This class will contain all the necessary information about the User.
    """
    def __init__(self, ID: int, conditions: dict, exercises: dict):
        """
        This function will initialize the User object.
        :param ID: The id of the user.
        :param conditions: The conditions and their severities.
        :param exercises:  The last 50 exercises done.
        """

        self._ID = ID
        self._conditions = conditions
        self._exercises = exercises

    def __str__(self):
        return f"User ID: {self._ID}"

    def __repr__(self):
        return f"User ID: {self._ID}"

    def getID(self) -> int:
        """
        This function return the ID of the User.
        :return: The ID of the User.
        """
        return self._ID

    def getConditions(self) -> dict:
        """
        This function returns a copy of the User's conditions.
        :return: The Conditions of the User.
        """
        return self._conditions.copy()

    def getExercises(self) -> dict:
        """
        This function return a copy of the User's exercises.
        :return: The Exercises done by the User.
        """
        return self._exercises.copy()

import statistics as stat
from GA.Individual.user import User


def getExperience(u: User) -> float:
    """
    Calculates the experience of a User based on the median value of the Difficulty of exercises done.
    :param u: The User whose experience is to be calculated.
    :return: The calculated experience.
    """
    data = list()
    exercises = u.getExercises()

    if not exercises:
        return 0

    else:
        for ex in exercises.values():
            data.append(ex.getExerciseDifficulty())

        return stat.median(data)


def getMaxMinExperience(u: User) -> tuple[float, float]:
    """
    Calculates the maximum and the minimum value of the Difficulty of exercises done by the User.
    :param u: The User which information will be calculated for.
    :return: The maximum and minimum value of the Difficulty of exercises done.
    """
    data = list()
    exercises = u.getExercises()

    if not exercises:
        return 2, 1

    else:
        for ex in exercises.values():
            data.append(ex.getExerciseDifficulty())

        return max(data), min(data)


def getMeanSeverity(u: User) -> float:
    """
    Calculates the mean value of the General Severity of the Conditions of the User.
    :param u: The User whose information will be calculated for.
    :return: The mean value of the General Severity.
    """
    data = list()
    conditions = u.getConditions()
    for t in conditions.values():
        data.append(t[0])
    return stat.mean(data)


def getSlope(s: float) -> float:
    """
    Calculates the slope for the increasing Difficulty level.
    :param s: The mean Severity of the Conditions of the User.
    :return: The slope.
    """
    oldMax = 10
    oldMin = 1
    newMin = 0.5
    newMax = 1.5
    return newMin + (s - oldMin) * (newMax - newMin) / (oldMax - oldMin)


def getPositionValue(p: float) -> float:
    """
    Calculates the position value of an Exercise regard the last 50 Exercises done by the User.
    :param p: The position of the Exercise to evaluate.
    :return: The value of that position.
    """
    oldMax = 50
    oldMin = 0
    newMin = 0
    newMax = 100
    return newMin + (p - oldMin) * (newMax - newMin) / (oldMax - oldMin)


def getMeanWritingSeverity(u: User) -> float:
    """
    Calculates the mean value of the Writing Severity of the User.
    :param u: The User whose information will be calculated for.
    :return: The mean value.
    """
    data = list()
    conditions = u.getConditions()
    for tuple_value in conditions.values():
        data.append(tuple_value[1])
    return stat.mean(data)


def getMeanReadingSeverity(u: User) -> float:
    """
    Calculates the mean value of the Reading Severity of the User.
    :param u: The User whose information will be calculated for.
    :return: The mean value.
    """
    data = list()
    for tuple_value in u.getConditions().values():
        data.append(tuple_value[2])
    return stat.mean(data)


def getDaysValue(days: int, oldMax: int):
    """
    Calculates the days value of an Exercise regard the last Completion date.
    :param days: The number of days passed.
    :param oldMax: The maximum number of days passed before giving the maximum value.
    :return: The days value.
    """
    oldMin = 0
    newMin = 0
    newMax = 100
    return newMin + (days - oldMin) * (newMax - newMin) / (oldMax - oldMin)

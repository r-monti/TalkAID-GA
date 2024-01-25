from DataBase.DBExercise import select_done_exercises
from DataBase.DBUser import informationUser
from GA.Individual.user import User


def createUser(userId: int) -> User:
    """
    Creates an istance of User.
    :param userId: The patient's ID.
    :return: An istance of User class with exercise and condition related info.
    """
    info_user = informationUser(userId)
    info_exercise = select_done_exercises(userId)
    u = User(userId, info_user, info_exercise)
    return u

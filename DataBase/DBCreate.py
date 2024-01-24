from DBExercise import seleziona_esercizi_fatti
from DBUser import informationUser
from GA.Individual.user import User


def createUser(userId: int) -> User:
    """
    Creates an istance of User
    :param userId: the patient's ID
    :return: an istance of User class with exercise and condition related info
    """
    info_user = informationUser(userId)
    info_exercise = seleziona_esercizi_fatti(userId)
    u = User(userId, info_user, info_exercise)
    return u

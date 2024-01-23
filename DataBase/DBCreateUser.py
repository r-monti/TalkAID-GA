from DBExercise import seleziona_esercizi_fatti
from DBUser import informationUser
from GA.Individual import user


def createUser(userId):
    """
        Create a istance of User
        :Arg ID: ID of the patient that you want
        :return User: a istance of User class with info of exercise and conditions
    """
    info_user = informationUser(userId)
    info_exercise = seleziona_esercizi_fatti(userId)
    u = user.User(userId, info_user, info_exercise)
    return u

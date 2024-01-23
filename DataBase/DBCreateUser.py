from Exercise import last50_exercise_done
from SelectionUser import takeInfoUser
from GA.Individual import user


def createUser(userId):
    info_user = takeInfoUser(userId)
    info_exercise = last50_exercise_done(userId)
    u = user.User(userId, info_user, info_exercise)
    return u

from datetime import datetime
from GA.Individual.exercise import Exercise
from GA.Individual.user import User
from GA.Individual.exerciseIndividual import Individual
import GA.Evaluation.fitnessUtility as fu

# % of influence for each fitness evaluator (keep between 0 and 3)
F1 = 1  # evaluateBasedFitness -> last Evaluation
F2 = 1  # dateBasedFitness -> last Completion
F3 = 1  # difficultyBasedFitness -> difficulty of exercise
F4 = 1  # severityBasedFitness -> user writing / reading severity and exercise type
F5 = 1  # targetBasedFitness -> exercise Target
F6 = 1  # feedbackBasedFitness -> last Feedback
F7 = 1  # last50Fitness -> if the exercise was done in the last 50 exercises of the user

MDAYS = 14    # used in dateBasedFitness, if the exercise has been done in the last 14 days, it will have a lower value


def fitness(ex: Exercise, u: User) -> float:
    """
    This function calculates the fitness of an Exercise done by a User.
    :param ex: The Exercise to be evaluated.
    :param u: The User instance for the reccomendation.
    :return float: The fitness value.
    """
    f1, f2, f3, f4, f5, f6, f7 = F1, F2, F3, F4, F5, F6, F7

    somma = (f1 * evaluateBasedFitness(ex)) + (f2 * dateBasedFitness(ex, MDAYS)) + (f3 * difficultBasedFitness(ex, u))
    somma += (f4 * severityBasedFitness(ex, u)) + (f5 * targetBasedFitness(ex, u))
    somma += (f6 * feedbackBasedFitness(ex)) + (f7 * last50Fitness(ex, u))

    # somma = (f3 * difficultBasedFitness(ex, u))
    # somma += (f4 * severityBasedFitness(ex, u))
    # somma += (f5 * targetBasedFitness(ex, u)) <- Only exercise info, ignores executions from user

    return somma


def individualFitness(i: Individual, u: User):
    """
    This function updates the fitness value of a single Individual.
    :param i: The Individual to be updated.
    :param u: The User instance.
    :return None: The fitness value is stored locally in the instance.
    """
    for ex in i:
        ex.setFitnessValue(fitness(ex, u))


def evaluateBasedFitness(e: Exercise) -> float:
    """
    This function evaluates the fitness based on the last Evaluation of the exercise. If the exercise has a low
    evaluation, then it will have a high evaluation.
    :param e: The Exercise instance to be evaluated.
    :return: The fitness value.
    """
    if e.getLastEvaluation() is not None:
        value = 100 - e.getLastEvaluation()
    else:
        value = 100
    return value


def dateBasedFitness(e: Exercise, maxDays: int) -> float:
    """
    This function evaluates the fitness based on the last Completion of the exercise. If the exercise has not been done
    recently, then it will have a high evaluation.
    :param e: The Exercise instance to be evaluated.
    :param maxDays: The maximum number of days before maximum evaluation of the exercise.
    :return: The fitness value.
    """
    value = 100
    if e.getLastCompletionDate() is not None:
        completionDate = datetime.strptime(e.getLastCompletionDate(), "%Y-%m-%d")
        data_odierna = datetime.now()
        giorni_passati = (data_odierna - completionDate).days
        if giorni_passati < maxDays:
            value = fu.getDaysValue(giorni_passati, maxDays)
    return value


def difficultBasedFitness(e: Exercise, u: User) -> float:
    """
    This function evaluates the fitness based on the difficulty of the Exercise. First it evaluates the experience of
    the User, then based on the general Severity of the Condition of the user, gives a high evaluation if the Exercise
    difficulty is within the right region of increasing difficulty.
    :param e: The Exercise instance to be evaluated.
    :param u: The User instance.
    :return: The fitness value.
    """
    difficulty = e.getExerciseDifficulty()
    severity = fu.getMeanSeverity(u)
    experience = fu.getExperience(u)
    maxD, minD = fu.getMaxMinExperience(u)

    distance = abs(difficulty - experience)
    slope = fu.getSlope(severity)

    if distance < difficulty <= distance + slope:
        value = 100
    else:
        value = 100 - (distance / (maxD - minD) * 100)
    return value


def severityBasedFitness(e: Exercise, u: User) -> float:
    """
    This function evaluats the fitness based on the User Writing and Reading Severity. It evaluates the Exercise to
    match the User Writing and Reading necessity, giving a high evaluation if the Exercise type matches the User's need.
    :param e: The Exercise instance to be evaluated.
    :param u: The User instance.
    :return: The fitness value.
    """
    if e.getExerciseType() == "READTEXT" or e.getExerciseType() == "TEXTTOIMAGES" or e.getExerciseType() == "READIMAGES":
        value = fu.getMeanReadingSeverity(u)
    else:
        value = fu.getMeanWritingSeverity(u)

    return value * 10


def targetBasedFitness(e: Exercise, u: User) -> float:
    """
    This function evaluates the fitness based on the Exercise target. If the Exercise target matches the User's
    Condition, it gives a high evaluation.
    :param e: The Exercise instance to be evaluated.
    :param u: The User instance.
    :return: The fitness value.
    """
    rightTarget = 0
    for key in u.getConditions().keys():
        if key in e.getExerciseTarger():
            rightTarget += 1

    return (rightTarget / len(e.getExerciseTarger().split(","))) * 100


def feedbackBasedFitness(e: Exercise) -> float:
    """
    This function evaluates the fitness based on the last Feedback of the user. It the feedback is positive, the
    Exercise gets a high evaluation.
    :param e: The Exercise instance to be evaluated.
    :return: The fitness value.
    """
    if e.getLastFeedback() is not None:
        if e.getLastFeedback() > 0:
            return 100
        else:
            return 0
    else:
        return 100


def last50Fitness(e: Exercise, u: User) -> float:
    """
    This function evaluates the fitness based on the last 50 Exercises the User did. If the Exercise wasn't done in the
    last 50 Exercises the User did, it gets a high evaluation.
    :param e: The Exercise instance to be evaluated.
    :param u: The User instance.
    :return: The fitness value.
    """
    if e.getExerciseID() in u.getExercises().keys():
        position = 0
        for index, ID in enumerate(u.getExercises().keys()):
            if ID == e.getExerciseID():
                position = index
                break
        return fu.getPositionValue(position)
    else:
        return 100

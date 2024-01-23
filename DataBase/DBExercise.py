from Connection import Connector  # Se la classe si chiama Connector
import mysql.connector
from GA.Individual.exercise import Exercise
from datetime import date


def seleziona_esercizi_non_fatti(id):
    # Usa la classe Connector per ottenere una connessione
    connessione = Connector.Connector()
    dizionario = []
    try:
        if connessione.get_connection() is not None:
            cursor = connessione.get_connection().cursor(dictionary=True)
            query = """
                    SELECT *
                    FROM exercise_glossary eg
                    WHERE NOT EXISTS (
                        SELECT 1
                        FROM exercise e
                        WHERE e.ID_exercise = eg.ID_exercise AND e.ID_user = %s);
                    """

            parametro = (id,)
            cursor.execute(query, parametro)

            records = cursor.fetchall()

            for record in records:
                esercizzo = Exercise(record["ExerciseName"],
                         record["ExerciseDescription"],
                         record["Type"],
                         record["Difficulty"],
                         record["Target"])
                dizionario.append(esercizzo)
            return dizionario

    except mysql.connector.Error as e:
        print("Error while connecting to MySQL", e)
    finally:
        if connessione.get_connection() is not None:
            cursor.close()
            connessione.get_connection().close()
            print("MySQL connection is closed")


def seleziona_esercizi_fatti(id):
    # Usa la classe Connector per ottenere una connessione
    connessione = Connector.Connector()
    try:
        if connessione.get_connection() is not None:
            cursor = connessione.get_connection().cursor(dictionary=True)
            query = """
                    SELECT e.*, DATEDIFF(CURDATE(), e.CompletionDate) AS DaysSinceCompletion
                    FROM exercise e
                    WHERE e.ID_user = %s AND e.Evaluation < 60;
                    """

            parametro = (id,)
            cursor.execute(query, parametro)

            records = cursor.fetchall()

            for record in records:
                print(str(record['DaysSinceCompletion']) + " " + str(record['ID_exercise']))


    except mysql.connector.Error as e:
        print("Error while connecting to MySQL", e)
    finally:
        if connessione.get_connection() is not None:
            cursor.close()
            connessione.get_connection().close()
            print("MySQL connection is closed")

def last50_Exercise_done(id):
    connessione = Connector.Connector()
    esercizi = {}
    try:
        if connessione.get_connection() is not None:
            cursor = connessione.get_connection().cursor(dictionary=True)
            query = """
                        SELECT
                            e.ID_exercise AS ExerciseID,
                            eg.Difficulty AS ExerciseDifficulty,
                            eg.Type AS ExerciseType,
                            eg.Target AS ExerciseTarget,
                            e.Evaluation AS ExerciseEvaluation,
                            e.CompletionDate AS ExerciseCompletionDate,
                            e.Feedback AS ExerciseFeedback,
                            DATE_FORMAT(e.CompletionDate, '%Y-%m-%d') AS ExerciseCompletionDate,
                            e.Evaluation AS ExerciseEvaluation,
                            e.Feedback AS ExerciseFeedback
                        FROM
                            exercise e
                        JOIN
                            exercise_glossary eg ON e.ID_exercise = eg.ID_exercise
                        WHERE
                            e.ID_user = %s
                        ORDER BY
                            e.CompletionDate DESC
                        LIMIT 50;
                        """

            parametro = (id,)
            cursor.execute(query, parametro)

            records = cursor.fetchall()

            for record in records:
                esercizio = Exercise(record["ExerciseID"],
                                     record["ExerciseDifficulty"],
                                     record["ExerciseTarget"],
                                     record["ExerciseType"],
                                     record["ExerciseEvaluation"],
                                     record["ExerciseCompletionDate"],
                                     record["ExerciseFeedback"])
                esercizi[record["ExerciseID"]] = esercizio
            return esercizi


    except mysql.connector.Error as e:
        print("Error while connecting to MySQL", e)
    finally:
        if connessione.get_connection() is not None:
            cursor.close()
            connessione.get_connection().close()
            print("MySQL connection is closed")
    return None
    return

def last50_exercise_done(id):
    connessione = Connector.Connector()
    esercizi = {}
    try:
        if connessione.get_connection() is not None:
            cursor = connessione.get_connection().cursor(dictionary=True)
            query = """
                    SELECT
                        e.ID_user AS UserID,
                        e.ID_exercise AS ExerciseID,
                        eg.Difficulty AS ExerciseDifficulty,
                        eg.Type AS ExerciseType,
                        e.InsertionDate AS ExerciseInsertionDate,
                        DATE_FORMAT(e.CompletionDate, '%Y-%m-%d') AS ExerciseCompletionDate,
                        e.Evaluation AS ExerciseEvaluation,
                        e.Feedback AS ExerciseFeedback
                    FROM
                        exercise e
                    JOIN
                        exercise_glossary eg ON e.ID_exercise = eg.ID_exercise
                    WHERE
                        e.ID_user = %s
                    ORDER BY
                        e.CompletionDate DESC
                    LIMIT 50;
                    """

            parametro = (id,)
            cursor.execute(query, parametro)

            records = cursor.fetchall()

            for record in records:
                tupla = (record["ExerciseCompletionDate"],
                         record["ExerciseEvaluation"],
                         record["ExerciseFeedback"],
                         record["ExerciseDifficulty"],
                         record["ExerciseType"])
                esercizi[record["ExerciseID"]] = tupla
            return esercizi


    except mysql.connector.Error as e:
        print("Error while connecting to MySQL", e)
    finally:
        if connessione.get_connection() is not None:
            cursor.close()
            connessione.get_connection().close()
            print("MySQL connection is closed")
    return None

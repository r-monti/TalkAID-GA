from Connection import Connector
import mysql.connector
from GA.Individual.exercise import Exercise


def seleziona_esercizi_non_fatti(ID):
    """
    Find exercise not done from patient
    :Arg ID: patient ID for search of exercise not done
    :return list: return a list of exercise class not done from patient
    """
    # Usa la classe Connector per ottenere una connessione
    connessione = Connector.Connector()
    lista = []
    cursor = None
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

            parametro = (ID,)
            cursor.execute(query, parametro)

            records = cursor.fetchall()

            for record in records:
                esercizio = Exercise(record["ID_Exercise"],
                                     record["Difficulty"],
                                     record["Target"],
                                     record["Type"],
                                     None,
                                     None,
                                     None)
                lista.append(esercizio)
            return lista

    except mysql.connector.Error as e:
        print("Error while connecting to MySQL ", e)
        return list()
    finally:
        if connessione.get_connection() is not None:
            if cursor is not None:
                cursor.close()
            connessione.get_connection().close()
            print("MySQL connection is closed.")


def seleziona_esercizi_fatti(ID):
    """
     Find exercises done from Patient
    :Arg ID: patient ID for search the exercises
    :return: dict: dict that contains last 50 exercises from patient
    """
    connessione = Connector.Connector()
    cursor = None
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

            parametro = (ID,)
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
        print("Error while connecting to MySQL ", e)
        return dict()
    finally:
        if connessione.get_connection() is not None:
            if cursor is not None:
                cursor.close()
            connessione.get_connection().close()
            print("MySQL connection is closed.")

def seleziona_esercizio_casuale(ID):
    """
       Select random exercise from DB
       :param:
       :return Exercise: a class Exercise
    """
    connessione = Connector.Connector()
    cursor = None
    try:
        if connessione.get_connection() is not None:
            cursor = connessione.get_connection().cursor(dictionary=True)
            cursor2 = connessione.get_connection().cursor(dictionary=True)
            query = """
                        SELECT *
                        FROM exercise_glossary
                        ORDER BY RAND()
                        LIMIT 1;
                    """
            cursor.execute(query)
            record = cursor.fetchone()

            secondQuery = """
                    SELECT DATE_FORMAT(e.CompletionDate, '%Y-%m-%d') AS ExerciseCompletionDate,
                     e.Evaluation,
                      e.Feedback
                    FROM exercise e
                    JOIN exercise_glossary eg ON e.ID_exercise = eg.ID_exercise
                    WHERE e.ID_user = %s AND e.ID_exercise = %s
                    ORDER BY e.InsertionDate DESC
                    LIMIT 1;
                """
            parametro = (ID, record["ID_exercise"],)
            cursor2.execute(secondQuery, parametro)

            secondRecord = cursor2.fetchone()

            if(secondRecord is not None):
                esercizio = Exercise(record["ID_exercise"],
                                     record["Difficulty"],
                                     record["Target"],
                                     record["Type"],
                                     secondRecord["Evaluation"],
                                     secondRecord["ExerciseCompletionDate"],
                                     secondRecord["Feedback"])
            else:
                esercizio = Exercise(record["ID_exercise"],
                                     record["Difficulty"],
                                     record["Target"],
                                     record["Type"],
                                     None,
                                     None,
                                     None)
            return esercizio

    except mysql.connector.Error as e:
        print("Error while connecting to MySQL ", e)
        return None
    finally:
        if connessione.get_connection() is not None:
            if cursor is not None:
                cursor.close()
            connessione.get_connection().close()
            print("MySQL connection is closed.")

import mysql.connector
from Connection.DBConnector import Connector
from GA.Individual.exercise import Exercise


def seleziona_esercizi_non_fatti(ID: int) -> list:
    """
    Finds exercise not done by the User
    :param ID: the patient's ID
    :return: a list of exercise class not done from the User
    """
    connessione = Connector()
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


def seleziona_esercizi_fatti(ID: int) -> dict:
    """
    Finds exercises done from the User
    :param ID: the patient's ID
    :return: a dict that contains the last 50 exercises done
    """
    connessione = Connector()
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


def seleziona_esercizi_casuale(n: int, ID: int) -> list[Exercise]:
    """
    Selects random exercises from DB
    :param n: the number of exercises to retrieve
    :param ID: the patient's ID
    :return: a list of Exercise instances
    """
    connessione = Connector()
    lst = list()
    cursor = None
    try:
        if connessione.get_connection() is not None:
            cursor = connessione.get_connection().cursor(dictionary=True)
            query = """
                        SELECT
                          eg_random.ID_exercise,
                          eg_random.Difficulty,
                          eg_random.Target,
                          eg_random.Type,
                          DATE_FORMAT(e.CompletionDate, '%Y-%m-%d') AS ExerciseCompletionDate,
                          e.Evaluation,
                          e.Feedback
                        FROM (
                          SELECT *
                          FROM exercise_glossary
                          ORDER BY RAND()
                          LIMIT %s
                        ) AS eg_random
                        LEFT JOIN exercise e ON eg_random.ID_exercise = e.ID_exercise
                          AND e.ID_user = %s
                          AND e.InsertionDate = (
                            SELECT MAX(InsertionDate)
                            FROM exercise
                            WHERE ID_exercise = eg_random.ID_exercise
                              AND ID_user = %s
                          )
                        ORDER BY e.InsertionDate DESC;
                    """
            parametro = (n, ID, ID,)
            cursor.execute(query, parametro)
            records = cursor.fetchall()

            if records is not None:
                for record in records:
                    esercizio = Exercise(record["ID_exercise"],
                                         record["Difficulty"],
                                         record["Target"],
                                         record["Type"],
                                         record["Evaluation"],
                                         record["ExerciseCompletionDate"],
                                         record["Feedback"])
                    lst.append(esercizio)

            return lst

    except mysql.connector.Error as e:
        print("Error while connecting to MySQL ", e)
        return list()
    finally:
        if connessione.get_connection() is not None:
            if cursor is not None:
                cursor.close()
            connessione.get_connection().close()
            # print("MySQL connection is closed.")

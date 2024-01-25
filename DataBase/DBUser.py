import mysql.connector
from DataBase.DBConnector import Connector


def informationUser(ID: int) -> dict:
    """
    Takes the Condition's information of a patient.
    :param ID: The patient's ID.
    :return: A dict of all conditions of the patient.
    """
    connessione = Connector()
    cursor = None
    patologie = {}
    try:
        if connessione.get_connection() is not None:
            cursor = connessione.get_connection().cursor(dictionary=True)
            query = """
                    SELECT
                        c.Name,
                        pc.Severity,
                        pc.WritingSeverity,
                        pc.ReadingSeverity
                    FROM
                        patientcondition pc
                    JOIN
                        `condition` c ON pc.ID_condition = c.ID_condition
                    WHERE
                        pc.ID_patient = %s;
                            """
            parametro = (ID,)
            cursor.execute(query, parametro)

            records = cursor.fetchall()

            if len(records) == 0:
                return dict()
            else:
                for record in records:
                    tupla = (record["Severity"],
                             record["WritingSeverity"],
                             record["ReadingSeverity"])
                    patologie[record["Name"]] = tupla
                return patologie

    except mysql.connector.Error as e:
        print("Error while connecting to MySQL ", e)
        return dict()
    finally:
        if connessione.get_connection() is not None:
            if cursor is not None:
                cursor.close()
            connessione.get_connection().close()
            # print("MySQL connection is closed.")

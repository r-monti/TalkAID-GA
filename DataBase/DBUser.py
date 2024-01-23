from Connection import Connector
import mysql.connector


def informationUser(ID):
    """
    Take Condition information of patient
    :Arg ID: ID of the patient that you want the information
    :return List: list of all condition parameter of the patient
    """
    connessione = Connector.Connector()
    cursor = None
    patologie = {}
    try:
        if connessione.get_connection() is not None:
            cursor = connessione.get_connection().cursor(dictionary=True)
            query = """
                    SELECT
                        pc.ID_condition AS ConditionID,
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
                    patologie[record["ConditionID"]] = tupla
                return patologie

    except mysql.connector.Error as e:
        print("Error while connecting to MySQL ", e)
        return None
    finally:
        if connessione.get_connection() is not None:
            if cursor is not None:
                cursor.close()
            connessione.get_connection().close()
            print("MySQL connection is closed.")

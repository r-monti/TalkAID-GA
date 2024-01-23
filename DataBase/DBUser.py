from Connection import Connector # Se la classe si chiama Connector
import mysql.connector

def seleziona_user(id):
    # Usa la classe Connector per ottenere una connessione
    connessione = Connector.Connector()
    try:
        if connessione.get_connection() is not None:
            cursor = connessione.get_connection().cursor(dictionary=True)
            query = "SELECT * FROM user WHERE ID = %s"
            parametro = (id,)
            cursor.execute(query,parametro)

            records = cursor.fetchall()



            if(len(records)==0):
                return None
            else:
                for record in records:
                    print(record["ID_Therapist"])

    except mysql.connector.Error as e:
        print("Error while connecting to MySQL", e)
        return None
    finally:
        if connessione.get_connection() is not None:
            cursor.close()
            connessione.get_connection().close()
            print("MySQL connection is closed")

def takeInfoUser(id):
    connessione = Connector.Connector()
    condizioni={}
    try:
        if connessione.get_connection() is not None:
            cursor = connessione.get_connection().cursor(dictionary=True)
            query = """
                    SELECT
                        pc.ID_condition AS ConditionID,
                        c.DisorderName AS ConditionName,
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
            parametro = (id,)
            cursor.execute(query, parametro)

            records = cursor.fetchall()

            if (len(records) == 0):
                return None
            else:
                for record in records:
                    tupla=(record["Severity"],
                           record["WritingSeverity"],
                           record["ReadingSeverity"])
                    condizioni[record["ConditionID"]]=tupla
                return condizioni

    except mysql.connector.Error as e:
        print("Error while connecting to MySQL", e)
        return None
    finally:
        if connessione.get_connection() is not None:
            cursor.close()
            connessione.get_connection().close()
            print("MySQL connection is closed")
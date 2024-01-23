import mysql.connector
from mysql.connector.errors import Error


class Connector:

    def __init__(self):
        self.connection = None
        try:
            self.connection = mysql.connector.connect(host='35.180.109.183',
                                                      port='3306',
                                                      database='fiatalkaid',
                                                      user='nicro',
                                                      password='pwd',
                                                      )
            if self.connection.is_connected():
                print("Connected to MySQL Server!")

        except mysql.connector.Error as e:
            print("Error while connecting to MySQL, ", e)

    def get_connection(self):
        return self.connection


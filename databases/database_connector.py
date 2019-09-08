import pymysql



# conn = pymysql.connect("localhost", "tomek", "haslo", "pythondb")

class DatabaseConnector:
    def __init__(self):
        self.loginToDBServer("localhost", "tomek", "haslo", "pythondb")
        self.selectFromUsers()

    def loginToDBServer(self, host, user_login, user_password, db_name):
        try:
            # globalny obiekt połączenia z bazą danych
            self.connect = pymysql.connect(host, user_login, user_password, db_name)
            self.c = self.connect.cursor()
            print("Ustanowiono połączenie z bazą danych")
        except:
            print("Błąd połączenia z bazą danych")

    def selectFromUsers(self):
        # zapytanie SQL
        sql_query = "SELECT * FROM users"
        # metoda wykonująca zapytanie
        self.c.execute(sql_query)
        #zwrócenie tabeli wynikowej
        for user in self.c.fetchall():
            print("| %3d | %15s | %15s | %10s | %15.2f | %1s " %
                  (user[0], user[1], user[2], user[3], user[4], user[5])
                  )

DatabaseConnector()
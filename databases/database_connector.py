import pymysql

# conn = pymysql.connect("localhost", "tomek", "haslo", "pythondb")

class DatabaseConnector:
    def __init__(self):
        self.loginToDBServer("localhost", "tomek", "haslo", "pythondb")
        while True:
            menu = input("(S) - select, (I) - insert, (D) - delete, (U) - update, (Q) - exit")
            if menu.upper() == "S":
                self.selectFromUsers()
            elif menu.upper() == "I":
                self.insertIntoUsers(input("Imie"), input("Nazwisko"), input("data urodzenia"), input("pensja"), input("płeć"))
                self.selectFromUsers()
            elif menu.upper() == "D":
                self.deleteFromUsersByID(input("Podaj id rekordu do usunięcia"))
                self.selectFromUsers()
            elif menu.upper() == "U":
                self.updateUsersSalary(input("id: "), input("procent podwyżki: "))
            elif menu.upper() == "Q":
                #zamknięcie połączenia z bazą danych
                self.connect.close()
                break
            else:
                print("Błędny wybór")

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

    def insertIntoUsers(self, name, lastname, birthdate, salary, gender):
        try:
            self.c.execute("insert into users values (default, %s, %s, %s, %s, %s)",
                           (name, lastname, birthdate, salary, gender))
            decision = input("Potwierdź dane (T/N)")
            if decision.upper() == "T":
                # przeniesienie danych z bufora do bazy danych
                self.connect.commit()
            else:
                # wycofanie wprowadzonych danych
                self.connect.rollback()
        except:
            print("błąd danych!")

    def deleteFromUsersByID(self, id):
        try:
            self.c.execute("delete from users where id = %s", id)
            self.connect.commit()
        except:
            print("Błąd danych")

    def updateUsersSalary(self, id, percent):
        try:
            self.c.execute("update users set salary = salary * (1 + %s) where id = %s", (percent, id))
            self.connect.commit()
        except:
            print("Błąd danych")



DatabaseConnector()

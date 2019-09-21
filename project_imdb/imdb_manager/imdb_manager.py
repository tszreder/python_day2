import pymysql


class ImdbManager:


    def __init__(self, host, user, password, database):

        self.conn = pymysql.connect(host = host, user = user, password = password, database=database, charset = "utf8")

        self.c = self.conn.cursor()
        print("Ustanowiono połączenie z bazą danych")
        sql_query = "show tables"
        self.c.execute(sql_query)
        rows = self.c.fetchall()
        for row in rows:
            print(row)


if __name__ == "__main__":
    imdb_manager = ImdbManager(host="localhost", user="tomek", database="imdb_data", password="haslo_imdb")



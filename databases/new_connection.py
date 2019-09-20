import pymysql

con = pymysql.connect('localhost', 'tomek','haslo', 'pythondb')

with con:
    cur = con.cursor()
    cur.execute("SELECT VERSION()")

    version = cur.fetchone()

    print("Database version: {}".format(version[0]))

    cur.execute("Select * from users")
    result = cur.fetchall()
    desc = cur.description
    print(desc)
    for row in result:
        # print(row)
        # print("%s %s %s %s %s %s" % (row[0], row[1], row[2], row[3], row[4], row[5]))
        print("{0} {2} {1} {3} {4} {5}".format(row[0], row[1], row[2], row[3], row[4],row[5]))

    # cur.execute("Select * from users")
    # for i in range(len(cur.description)):
    #     print("Column {}:".format(i + 1))
    #     desc = cur.description[i]
    #     print("  column_name = {}".format(desc[0]))
    #     print("  type = {}".format(desc[1]))
    #     print("  null_ok = {}".format(desc[6]))

def connectToDatabase():
    login = input("Podaj login")
    password = input("Podaj hasło")
    con = pymysql.connect("localhost", login, password, "pythondb2")
    cur = con.cursor()
    cur.execute("select * from users")
    result = cur.fetchall()
    print(result)

connectToDatabase()
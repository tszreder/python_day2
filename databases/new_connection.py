import pymysql

con = pymysql.connect('localhost', 'tomek','haslo', 'pythondb')

with con:
    cur = con.cursor()
    cur.execute("SELECT VERSION()")

    version = cur.fetchone()

    print("Database version: {}".format(version[0]))

    cur.execute("Select * from users")
    result = cur.fetchall()
    for row in result:
        print(row)
        # print("{0} {1} {2} {3}".format(row[0], row[1], row[2]), row[3])

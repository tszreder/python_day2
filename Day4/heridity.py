class User:
    def __init__(self, login, password):
        self.login = login
        self.password = password
        self.permissionSelect = True

    def readPost(self):
        if self.permissionSelect == True:
            print("READING...")

    def __str__(self):
        return  "login: %s password: %s PERMISSIONS: %s"\
                % (self.login, self.password, "SELECT" if self.permissionSelect == True else "")

# moderator dziedziczy po klasie User (ma te same właściwości i metody)
class Moderator(User):
    def __init__(self, login, password):
        self.login = login
        self.password = password
        self.permissionInsert = True

user = User("user", "user")
print(user)






# Admin dziedziczy po klasie Moderator, a pośrednio też User (ma te same właściwości i metody)
class Admin(Moderator):
    pass
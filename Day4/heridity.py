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
                % (self.login, self.password, "SELECT" if self.permissionSelect else "")

# moderator dziedziczy po klasie User (ma te same właściwości i metody)
class Moderator(User):
    def __init__(self, login, password):
        # wywołanie metody __init__() klasy nadrzędnej
        super().__init__(login, password)
        self.permissionInsert = True

    def writePost(self):
        if self.permissionInsert == True:
            print("WRITING...")

    def __str__(self):
        return super().__str__() + "INSERT" if self.permissionInsert else ""

user = User("user", "user")
print(user)
user.readPost()

moderator = Moderator("moderator", "moderator")
print(moderator)
moderator.readPost()
moderator.writePost()






# Admin dziedziczy po klasie Moderator, a pośrednio też User (ma te same właściwości i metody)
class Admin(Moderator):
    pass
class User:
    def __init__(self, login, password):
        self.login = login
        self.password = password
        self.permissionSelect = True

    def readPost(self):
        if self.permissionSelect:
            print("READING...")

    def __str__(self):
        return  "login: %s password: %s PERMISSIONS: %s"\
                % (self.login, self.password, "SELECT " if self.permissionSelect else "")

# moderator dziedziczy po klasie User (ma te same właściwości i metody)
class Moderator(User):
    def __init__(self, login, password):
        # wywołanie metody __init__() klasy nadrzędnej
        super().__init__(login, password)
        self.permissionInsert = True

    def writePost(self):
        if self.permissionInsert:
            print("WRITING...")

    def __str__(self):
        return super().__str__() + "INSERT " if self.permissionInsert else ""

# Admin dziedziczy po klasie Moderator, a pośrednio też User (ma te same właściwości i metody)
class Admin(Moderator):
    def __init__(self, login, password):
        super().__init__(login, password)
        self.permissionDelete = True
        self.permissionUpdate = True

    def __str__(self):
        return super().__str__() + ("DELETE " if self.permissionDelete else "") + ("UPDATE" if self.permissionUpdate else "")

    def deletePost(self):
        if self.permissionDelete:
            print("DELETING...")

    def updatePost(self):
        if self.permissionUpdate:
            print("UPDATING...")

print("####USER####")
user = User("user", "user")
print(user)
user.readPost()
print("####MODERATOR####")
moderator = Moderator("moderator", "moderator")
print(moderator)
moderator.readPost()
moderator.writePost()

print("####ADMIN####")
admin = Admin("admin", "admin")
print(admin)
admin.readPost()
admin.writePost()
admin.updatePost()
admin.deletePost()
admin.permissionDelete = False
print(admin)
admin.deletePost()





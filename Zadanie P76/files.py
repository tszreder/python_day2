from os import *
from datetime import datetime


float = 12234
print(datetime.fromtimestamp(float))

class FileOperation:
    def __init__(self):
        self.direct_path = input("Wprowadź adres bezpośredni: ")
        self.direct_path = self.direct_path.replace("\\", "\\\\")
        chdir(self.direct_path)
        self.getdirectoryContent()

    def getdirectoryContent(self):
        print("| % 40s  | %11s | %20s | %20s" % ("FILENAME", "SIZE", "CREATED", "MODIFIED"))
        for content in listdir("."):
            print("| % 40s  | %8.2f KB | %20s | %20s" %
                  (content,
                   path.getsize(content)/1000,
                   datetime.fromtimestamp(path.getctime(content)),
                   datetime.fromtimestamp(path.getmtime(content)))
                  )

FileOperation()
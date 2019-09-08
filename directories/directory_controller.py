from os import *

print("Direct path: " + getcwd())
print("Zawartość aktualnego katalogu: ", listdir("."))
print("Zawartość aktualnego katalogu: ", listdir("C:\\Users\\B5400\\PycharmProjects\\Day2\\Day3"))



chdir("C:\\Users\\B5400\\PycharmProjects\\Day2\\directories")
print(listdir("."))
# mkdir("generate from Python")
# rmdir("generate from Python")

for file in listdir("."):
    print("%50s | %8.2f KB" % (file, path.getsize(file)/1000))
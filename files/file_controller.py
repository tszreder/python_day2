# utworzenie pliku z uprawnieniami do apisu
file = open("file1.txt", "w")

# print(file.name, file.closed, file.mode)

#zapis do pliku
file.write("Pierwszy zapis do pliku\n")
file.write("Drugi zapis do pliku\n")
file.writelines(['s1\n', 's2\n'])
file.close()

# print(file.name, file.closed, file.mode)

fileAppend = open("file2.txt", "a")
fileAppend.writelines(['1','2','3','4','5','6','7','8\n'])
fileAppend.close()

#odczyt z pliku
fileReader = open("file2.txt", "r")
# print(fileReader.read())
print("zawartość pliku")
# print(fileReader.read(4))

# readlines pozwala zwrócić każdą linię jako element listy
print(fileReader.readlines())

# sprawdzenie pozycji kursora
print("pozycja kursora")
print(fileReader.tell())



# iterowanie po obiekcie pliku
# for line in fileReader:
#     print(line, end="")

fileReader.close()
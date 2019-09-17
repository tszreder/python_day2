from os import listdir

file = open("test.txt", "w", encoding='utf8')
fileReader = open("test.txt", "r", encoding='utf8')



def write():
    file.write("ą, b c Ć ó as")
    print(file.name, file.mode, file.closed, file.encoding)
    file.close()
    print(file.name, file.mode, file.closed, file.encoding)

# def read():
#     print(fileReader.readlines())
#     print(fileReader.tell())
#     print(fileReader.seek(0,0))
#     print(fileReader.seek(5,0))
#     print(fileReader.read())
#     print(fileReader.tell())
#     # print(fileReader.)
#     fileReader.close()

def saveResults():
    fw = open("results.txt", "a", encoding="utf16")
    variable1 = input("wpisz jakieś slowo")
    variable2 = input("wpisz drugie słowo")
    fw.seek(0)
    fw.write(variable1 + variable2 )
    list = '\n' + variable1 + '\n' + variable2
    fw.writelines(list)

    fw.close()

def readResults():
    fr = open("results.txt", "r", encoding="utf16")
    print(fr.read())
    print(fr.tell())

def createResultFile():
    resFile = open("result2.txt", "w+", encoding="utf16")
    print(resFile.name, resFile.closed)
    result1 = input("wpisz wynik")
    resFile.write(result1)
    resFile.close()
    print(resFile.name, resFile.closed)

def readSelectedFile():
    a = listdir(".")
    print(*a, sep="\n")
    fileToRead = input("który plik otworzyć?")
    activeFile = open(fileToRead + '.txt', 'r', encoding='utf16')
    print(activeFile.read())

if __name__ == "__main__":
    # write()
    # saveResults()
    # readResults()
    # read()
    # createResultFile()
    readSelectedFile()
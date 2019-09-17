file = open("test.txt", "w", encoding='utf8')
fileReader = open("test.txt", "r", encoding='utf8')

def write():
    file.write("ą, b c Ć ó as")
    print(file.name, file.mode, file.closed, file.encoding)
    file.close()
    print(file.name, file.mode, file.closed, file.encoding)

def read():
    print(fileReader.readlines())
    print(fileReader.tell())
    print(fileReader.seek(0,0))
    print(fileReader.seek(5,0))
    print(fileReader.read())
    print(fileReader.tell())
    # print(fileReader.)
    fileReader.close()

if __name__ == "__main__":
    write()
    read()
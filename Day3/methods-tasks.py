# P57 - zaimplementuj silnię - n! = n * (n-1) * (n-2) * ... * 1
from math import sqrt
from random import choices


def factorial(n):
    result = n
    if n < 0:
        return "Error, n musi być liczbą naturalną"
    if n == 0:
        return 1
    for factor in range(1,n):
        result *= factor
        # print(factor)
    return result

print(factorial(8))

# rekurencyjnie (funkcja odwołuje się do samej siebie)

def factorialRec(n):
    if n == 1:
        return 1
    return n * factorialRec(n - 1)

print(factorialRec(4))

'''
fR(4)
1) fR(4) = 4 * fR(3)
2) fR(4) = 4 * 3 * fR(2)
3) fR(4) = 4 * 3 * 2 * 1
'''

# import timeit
# timeit.timeit('char in text', setup='text = "sample string"; char = "g"')

# timeit.timeit('"-".join(str(n) for n in range(100))', number=100)
# timeit.timeit('"-".join([str(n) for n in range(100)])', number=100)
# timeit.timeit('"-".join(map(str, range(100)))', number=100)

#P58
# Oblicz zadany element ciągu Fibonacciego, każdy kolejny element to suma dwóch poprzednich dla 0 = 0, dla 1 = 1

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(6))

def fibonacci2(n):
    fib = []
    sum = 0
    for index, value in enumerate(range(0, n+1)):
        if index == 0:
            fib.append(0)
        elif index == 1:
            fib.append(1)
        else:
            fib.append(fib[index - 1] + fib[index - 2])
        sum += fib[index]
    return fib, fib[n], sum

print(fibonacci2(15))

print(range(0,3))

names = ["Ala", "Ola", "Ela"]
for name in names:
    print(name)

for i, name in enumerate(names):
    print(i, name)

'''
Ćwiczenie P59
Napisz funkcję, która wygeneruje losowe zdanie zawierające podaną liczbę
(domyślnie 5) losowo wygenerowanych wyrazów.
'''

content = "Ciąg został omówiony w roku 1202 przez Leonarda z Pizy, zwanego Fibonaccim, " \
"w dziele Liber abaci jako rozwiązanie zadania o rozmnażaniu się królików. " \
"Nazwę ciąg Fibonacciego spopularyzował w XIX w. Edouard Lucas"

'''
1. Podziel zdanie na wyrazy
2. Losuj wyrazy i przypisuj je do nowo wygenerowanego zdania
'''

def splitSentenceBySeparator(content, separator = " "):
    return content.split(separator)

def createSentenceByListOfWords(listOfWords):
    sentence = ""
    for word in listOfWords:
        sentence += word +" "
    return sentence + "."

def generateSentence(content, n=5):
    words = splitSentenceBySeparator(content, " ")
    generatedSentence = choices(words, k = n)
    return createSentenceByListOfWords(generatedSentence)

print(splitSentenceBySeparator(content))
print(generateSentence(content))

'''
Ćwiczenie P60
Napisz program do wyliczania odległości między dwoma punktami na płaszczyźnie.
'''

def distance(Ax, Ay, Bx, By):
    distanceX = Ax - Bx
    distanceY = Ay - By
    return sqrt((distanceX**2 + distanceY**2))

print(distance(1,1,2,2))

'''
Ćwiczenie P61
Zdefiniuj funkcję, która dla podanych trzech parametrów:
 n=numer elementu ciągu,
 a1=wartość pierwszego elementu ciągu (domyślnie 1),
 q=wartość iloczynu ciągu geometrycznego (domyślnie 2)
Zwróci sumę i n-ty element ciągu geometrycznego. 

an = a1 * q ** (n-1)
'''

def geometric(n, a1 = 1, q = 2):
    result = a1 * q ** (n-1)
    return result

def geometric2(n, a1 = 1, q = 2):
    ciag = []
    sum = 0
    for index in range(1, n + 1):
        value = a1 * q ** (index-1)
        ciag.append(value)
        sum += value
    return ciag, sum


def geometric3(n, a1 = 1, q = 2):
    suma = 0
    for index in range(1, n + 1):
        curValue = a1 * q ** (index-1)
        suma += curValue
    return curValue, suma


print(geometric3(n=5, a1=2, q=3))

'''
Ćwiczenie P62
Zdefiniuj funkcję, która dla dowolnej liczby parametrów zwróci ich średnią
arytmetyczną (lub 0 dla 0 parametrów).
'''

def averagePar(*parameters):
    total = 0
    for parameter in parameters:
        total += parameter
    return total / len(parameters)

print(averagePar(1,2,3,4,5))


'''
Ćwiczenie P63
 Napisz funkcję generującą kod HTML dla napisu:
<span style="color: color_name; font-size: value; “>content</span>
 Użytkownik może podać wartości poszczególnych parametrów, jeśli tego nie zrobi
przypisywane są wartości domyślne.
Dodatkowo doddaj argument określający ile razy ma się wygenerować dana treść
'''


def generateHTML(content, color_name = "black", fontSize = 12, rowNumber = 1):
    html = '<span style="color: %s; font-size: %s; “>%s</span>\n' % (color_name, fontSize, content)
    return html * rowNumber

posts = ["Post1", "Post2", "Post3", "Post4"]

def generateHTML2(posts, color_name = "black", fontSize = 12, rowNumber = 1):
    html_content = ""
    for post in posts:
        html_content += '<span style="color: %s; font-size: %s; “>%s</span>\n' % (color_name, fontSize, post)
    return html_content

print(generateHTML2(posts, "red", 16,5))


'''
Ćwiczenie P64
 Napisz funkcję, która będzie wyświetlała przy każdym kolejnym wywołaniu na
przemian nazwy dwóch kolorów: biały i czarny.
'''


def generateHTMLwithBackground(posts, color_name = "black", fontSize = 12):
    html_content = ""
    backgroundColor = "black"
    for post in posts:
        html_content += '<span style="color: %s; font-size: %s; background-color: %s “>%s</span>\n' % \
                        (color_name, fontSize, backgroundColor, post)
        if backgroundColor == "black":
            backgroundColor = "white"
        else:
            backgroundColor = "black"
    return html_content

print(generateHTMLwithBackground(posts, "red", 16))

color = "black"
def differentColors():
    global color # odwołuje się do globalnej zmiennej zadeklarowanej poza funkcją
    if color == "black":
        color = "white"
    else:
        color = "black"
    return color

def differentColorsLocal():
    color = "black" # przy kazdym uruchomieniu funkcji ustawia kolor na black
    if color == "black":
        color = "white" # zmienia black na white i zawsze wypisz white, bo kolejnej zmiany już nie ma
    else:
        color = "black"
    return color

print(differentColors())
print(differentColors())
print(differentColors())
print(differentColors())
print(differentColors())
print(differentColors())


'''
Ćwiczenie P65
 Napisz funkcję, która będzie sumowała wszystkie te elementy tablicy które są większe
od żądane j wartości.
 Użytkownik podaje wartość progu MinSup (domyślnie 0) i ilość
generowanych elementów tablicy
 Elementy tablicy przy każdym uruchomieniu programu są generowane
losowo z zakresu od -1000 do 1000
 Niech funkcja zwróci wszystkie elementy większe od wartości progowej oraz wartość
ich sumy.
'''


def tableSum(minSup, maxSup, tableSize):
    generatedNumbers = choices(range(-1000, 1000),k = tableSize)
    sum = 0
    returnedNumbers = []
    for number in generatedNumbers:
        if minSup < number < maxSup:
            sum += number
            returnedNumbers.append(number)
    return generatedNumbers, returnedNumbers, sum, sum/len(returnedNumbers)


print(tableSum(-900, 900, 10))



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








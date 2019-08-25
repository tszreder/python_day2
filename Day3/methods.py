from time import localtime

returnedValue = localtime()
print(returnedValue)

products = ["A", "B", "C"]
productPrice = [1.99, 2.33, 3.44]

# metoda prezentująca przyjmująca argumenty i nie zwracająca wartości
def printSeqence(sequence):
    for element in sequence:
        print(element, end= " ")
    print()

# printSeqence(products)
# printSeqence(productPrice)
# printSeqence([1,2,4,5,6,7,8])

data = [1, 23, 4, 2, 4, 5, 4] #do znormalizowania od 0 do 1

'''
1. Szukanie min i max [1, 23]
2. a = |min przedziału - max przedziału| / |min wartość - max wartość|
3. b = 1 - (a * max wartość)
'''

def findMin(data):
    return min(data)

def findMax(data):
    return max(data)

def findExt(data):
    return min(data), max(data)


def normalizeDataset(data, lowBorder = 0, topborder = 1):
    normalizedData = []
    for element in data:
        a = abs(lowBorder - topborder)/abs(findExt(data)[0]- findExt(data)[1])
        b = topborder - (a * findExt(data)[1])
        normalizedData.append(a * element + b)
    return normalizedData

def printDataset(data):
    for element in data:
        print("%6.3f" % element, end=" ")
    print()

printDataset(data)
printDataset(normalizeDataset(data))
printDataset(normalizeDataset(data, -1, 1))



# Dowolna liczba argumentów

def gradedsAvg(*grades):
    sum = 0
    for grade in grades:
        sum += grade
    return sum / len(grades)

print(gradedsAvg(1,2,3,6,4), gradedsAvg(1,2), gradedsAvg(4,5,3,4,4,5,5))
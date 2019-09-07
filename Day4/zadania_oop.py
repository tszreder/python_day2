#P66
# Napisz program, który posłuży do obliczania BMI zawodnika
# Utwórz klasę Zawodnik zawierającą metodę do obliczania BMI
# Utwórz obiekt reprezentujący zawodnika
# Wywołaj metodę klasową, która zwróci wartość BMI
from random import choice, sample


class Player:
    def __init__(self, name, height, weight):
        self.name = name
        self.height = height
        self.weight = weight

    def calculateBMI(self):
        return self.weight / pow(self.height/100, 2)

    def __str__(self):
        return "name: %-10s height: %-3d cm  weight: %-2d kg  BMI: %-10.2f" % (self.name, self.height,self.weight, self.calculateBMI())



p1 = Player("Piotr", 180, 80)
p2 = Player("Jan", 140, 60)
print(p1)
print(p2)

# P68
# Napisz program lotto, który losuje bez zwracania 6 spośród 49 liczb i wypisuje je na ekran.
# Zmodyfikuj poprzedni program w taki sposób, by wyświetlał wylosowane liczby od najmniejszej do największej.

class Lotto:

    def __init__(self):
        self.result = []

    def draw(self):
        self.result = sample(range(50), k = 6)
        print(self.__str__())

    def sorting(self):
        self.result.sort(reverse = True)
        print(self.__str__())

    def __str__(self):
        return self.result

# losowanie = sample(range(50), k = 6)
# print(losowanie)

lotto1 = Lotto()
lotto1.draw()
lotto1.sorting()
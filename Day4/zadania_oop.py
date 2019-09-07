#P66
# Napisz program, który posłuży do obliczania BMI zawodnika
# Utwórz klasę Zawodnik zawierającą metodę do obliczania BMI
# Utwórz obiekt reprezentujący zawodnika
# Wywołaj metodę klasową, która zwróci wartość BMI
from datetime import datetime
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
        return "%s data losowania: %s" % (self.result, datetime.today().strftime("%d %m %Y"))
        # return (self.result, datetime.date.today())

# losowanie = sample(range(50), k = 6)
# print(losowanie)

lotto1 = Lotto()
lotto1.draw()
lotto1.sorting()

# P71
# Napisz program wykorzystując mechanizm dziedziczenia zawierającego:
#  Klasę bazową o nazwie Produkt zawierającą konstruktor i metodę wyświetlającą nazwę i cenę produktu.
#  Klasę Oprogramowanie rozszerzającą klasę Produkt zawierającą konstruktor i metodę wyświetlającą nazwę, cenę, język i system.
#  Klasę Szkolenia rozszerzającą klasę Oprogramowanie zawierającą konstruktor i metodę wyświetlającą nazwę, cenę, język, system i termin.
#  Przetestuj działanie klas na podstawie utworzonych obiektów klasy Oprogramowanie i klasy Szkolenia.

class Produkt:
    def __init__(self, nazwa, cena):
        self.nazwa = nazwa
        self.cena = cena

    def __str__(self):
        return "nazwa produktu to: %-10s cena wynosi: %-4i PLN " % (self.nazwa, self.cena)

class Oprogramowanie(Produkt):
    def __init__(self, nazwa, cena, jezyk, system):
        super().__init__(nazwa, cena)
        self.jezyk = jezyk
        self.system = system

    def __str__(self):
        return super().__str__() + "jezyk oprogramowania to: %-5s system to: %-10s" % (self.jezyk, self.system)

class Szkolenie(Oprogramowanie):
    def __init__(self, nazwa, cena, jezyk, system, termin):
        super().__init__(nazwa, cena, jezyk, system)
        self.termin = termin

    def __str__(self):
        return super().__str__() + "termin to: %-10s" % (self.termin)

print ("########## ZADANIE P71 ############")
produkt = Produkt("owoc", 30)
print(produkt)
program = Oprogramowanie("Saper", 200, "c++", "Windows")
print(program)
szkolenie = Szkolenie("Excel", 900, "Java", "Linux", "2019-09-29")
print(szkolenie)

# P72
#  Napisz prostą klasę zawierającą pola kolorów składające się z wartości RGB.
#  Przypisz do tych pól dowolne wartości wykorzystując konstruktor klasy
#  Zrzutuj te parametry RGB na napis i wypisz je poza klasą.
#  Dodatkowo dodaj kolor zielony i czerwony aby otrzymać kolor żółty – zastosuj operator __add__

class RGB:

    def __init__(self, R, G, B):
        self.R = R
        self.G = G
        self.B = B

    def __str__(self):
        return "R: %3i G: %3i B: %3i" % (self.R, self.G, self.B)

    def __add__(self, other):
        newRGB = RGB(self.R + other.R if self.R + other.R <= 255 else 255,
                     self.G + other.G if self.G + other.G <= 255 else 255,
                     self.B + other.B if self.B + other.B <= 255 else 255)
        return newRGB

black = RGB(255,255,255)
print(black)
red = RGB(255,0,0)
green = RGB(0,255,0)
print(red + green)
print(green + green)
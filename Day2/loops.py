#While else
import random

services = ["GitHub", "Google", "Facebook"]

i = 0
while i < len(services): #fragment kodu wykonywany warunkowo
    print(services[i])
    i += 1
else:
    print("...") #fragment kodu wykonywany zawsze

# for in - oblicz średnią arytmentyczną 1000 losowych wartości z przedziału od 1 d0 10

#import random
suma = 0
for liczba in range(0, 1000):
    suma += random.randint(1, 10)

print(suma/1000)


# przypisz 12 osób do 4 grup i w każdej grupie wylosuj jednego lidera
#V1
osoby = ["AN", "TSz", "MP", "ZJ", "PM", "PM", "AP", "FŚ", "MT", "AR", "IS", "MS", "MK"]
grupy = [1,1,1,2,2,2,3,3,3,4,4,4]
print(len(osoby))
grupy = random.sample(grupy,12)
print(grupy)
przydzial = dict(zip(osoby, grupy))
print(przydzial)

#V2
osoby = set(["AN", "TSz", "MP", "ZJ", "PM", "PM", "AP", "FŚ", "MT", "AR", "IS", "MS", "MK"])
group_dict = {}
i = 1
while len(osoby) > 0:
    grupa = random.sample(osoby, 3)
    for osoba in grupa:
        group_dict[osoba] = str(i)
        osoby.discard(osoba)
    group_dict[random.choice(grupa)] = str(i) + "L"
    i += 1
print(group_dict)

#Continue & break

i = 0
for liczba in range(1,10,1):
    print("Obieg:" + str(i+1))
    if liczba == 5:
        print("XXX")
        break
    i += 1

# while(True):
#     if input("Co chcesz zrobić? Q - wyjście").upper() == "Q":
#         print("przerwanie")
#         break
import random
lista  = range(-10,10,1)
los = random.sample(set(lista), 5)
licznik = 5.5
# for i in los:
#     print("Wylosowana wartość: %i" %i )
#     if i == 0:
#         print("Nie można dzielić przez zero")
#         continue
#     print("Wynik operacji: %.2f" % (licznik/i))

for i in los:
    print("Wylosowana wartość: %i" %i )
    try:
        print("Wynik operacji: %.2f" % (licznik/i))
    except:
        print("Nie można dzielić przez zero")
import random
tab = [1,2,3]

numbers = []
for c in range(100):
    if c % 2:
        numbers.append(random.randint(1,c))

print(numbers)

numbers = [x for x in range(10)]
numbers = [random.randint(1,100) for x in range(10)]
numbers = [random.randint(1,x) for x in range(100) if x % 2]
numbers_2 = [random.randint(1,x) if x % 2 else '' for x in range(100)]

numbers_3 = []
for x in range(100):
    if x % 2:
        numbers_3.append(random.randint(1,x))
    else:
        numbers_3.append('')

print(numbers_3)


# napisać list comprehension, które wybierze liczby podzielne przez z numbers
numbers_4 = [x for x in numbers if x % 3 == 0]
print(numbers_4)

data = [
    ('Jan','Kowalski', 33455, 435),
    ('Adam','Kowalski', 12345, 34.5),
    ('Jan','Kowalczyk', 12095, 78),
    ('Anna','Nowak', 28345, 10.57)
]

# saldo typu decimal, sparametryzować nazwisko (1,2,3,4), trzy pierwsze liczby z numeru indeksu jako tuple

from decimal import Decimal

new_data = []
names = {x[1] for x in data}
names = {x: n for n, x in enumerate(names)} # przepisać na pętle for


for row in data:
    saldo = Decimal(row[-1])
    nazwisko = names[row[1]]
    indeks = int(str(row[-2])[:3])
    new_row = (saldo, nazwisko, indeks)
    new_data.append(new_row)

print(new_data)

new_data_comp = [
                    (
                        Decimal(row[-1]),
                        names[row[1]],
                        int(str(row[-2])[:3])
                     )
                    for row in data
                ]

print(new_data_comp)

# print(names.get('Kowalski2', "nie ma takiego klucza w slowniku")) # zwraca wartość defaultowa jak nie znajdzie
#
# try:
#     print(names['Kowalski2'])
# except KeyError:
#     print("nie ma takiego klucza w slowniku")


result = [Decimal(row[-1]) for row in data]

# print(result)

c = [1,2,3]
x = [0,2,4,8]
p = [sum([cn * xn**i for i, cn in enumerate(c)]) for xn in tab]
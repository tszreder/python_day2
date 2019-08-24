# for x in range(5,100, 10):
#     print("%4i%6i%8i" % (x, x**2, x**3))

'''
Ćwiczenie P55
 Woda zamarza przy 32 stopniach Fahrenheita, a wrze przy 212 stopniach
Fahrenheita.
 Napisz program, który wyświetli tabelę przeliczeń stopni Celsjusza na stopnie
Fahrenheita w zakresie od –20 do +40 stopni Celsjusza (co 5 stopni). Pamiętaj o
wyświetlaniu znaku plus/minus przy temperaturze.
'''

# celsjusz = input("podaj temp w stopniach celsjusza")
# fahrenheit = 9/5 * int(celsjusz) + 32
# print(fahrenheit)

c_to_f = {}

for temp_c in range(-20, 45, 2):
    c_to_f[temp_c] = 9/5 * int(temp_c) + 32
    print("%+4iC | %+6.1fF" % (temp_c, c_to_f[temp_c]))
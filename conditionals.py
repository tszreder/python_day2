# Wyrażenie trójargumentowe

a = 25
b = 30

print(b) if a<b else print(a)

'''
P48
Napisz program, który wczyta od użytkownika liczbę całkowitą i bez użycia instrukcji if
wyświetli informację, czy jest to liczba parzysta, czy nieparzysta
'''

#print("PARZYSTA" if int(input("Podaj liczbę: ")) % 2 == 0 else "NIEPARZYSTA")

# instrukcja try to podstawowa obsługa błędów
'''
try:
    print("NIEPARZYSTA" if int(input("Podaj liczbę: ")) % 2 else "PARZYSTA")
except:
    print("TO NIE JEST LICZBA")
'''

'''
Ćwiczenie P49
 Wykonaj prosty test poprawności logowania
 Jeżeli użytkownik podał login: admin i hasło: admin – przejdź do panelu
administratora
 Jeżeli użytkownik podał login: user i hasło: user – przejdź do panelu
użytkownika
 W przeciwnym razie wyświetl stosowny komunikat
'''


#Logowanie na podstawie listy użytkowników
# Jeżeli błędne hasło będzie podane 3 razy u użytkownika to zablokuj mu konto
# isLogged = False
# for user in users:
#     if login == user[0] and password == user[1]:
#         isLogged = True
#         if user[2] == "ROLE_ADMIN":
#             print("Panel Admina")
#             break
#         else:
#             print("PANEL USERA")
#             break
# print("" if isLogged else "Błędny login lub hasło")

users = [
        ["mk","mk123","ROLE_ADMIN", True, 0],
        ["kk","kk123","ROLE_USER", True, 0],
        ["ll","ll123","ROLE_USER", True, 0]
         ]


isLogged = False
while(isLogged == False):
    login = input("Podaj login")
    for user in users:
        #sprawddzam czy jest taki użytkownik
        if login == user[0] and user[3] == True:
            password = input("Podaj hasło")
            #sprawdzam czy podał dobre hasło
            if password == user[1]:
                isLogged = True
                # sprawdzam uprawnienia
                if user[2] == "ROLE_ADMIN":
                    print("PANEL ADMINISTRATORA")
                    break
                else:
                    print("PANEL USERA")
                    break
            else:
                print("BŁĘDNE HASŁO")
                user[4] +=1
                if user[4] == 3:
                    user[3] = False
                break
        elif login == user[0] and user[3] == False:
            print("KONTO ZABLOKOWANE!")
            break
    # if isLogged == False:
    #     print("BŁĘDNY LOGIN")

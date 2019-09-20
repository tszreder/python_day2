from Zadanie_P75.measurements import Measurement_List
ml = Measurement_List()

while (True):
    menu = input("Co chcesz zrobić? \n (M) - zrób pomiar \n (Z) - zapisz pomiar \n (A) - dopisz pomiar do plliku \n (Q) - wyjdź")
    if menu.upper() == "M":
        user = input("Przedstaw się: ")
        result = int(input("Podaj wynik liczbowy: "))
        ml.makeMeasurement(user, result)
    elif menu.upper() == "Z":
        filename = input("Wybierz nazwę pliku do zapisu (bez rozszerzenia)")
        ml.saveMeasurement(filename)
    elif menu.upper() == 'A':
        filename = input("Wybierz nazwę pliku do którego chcesz dopisać wyniki")
        ml.addNewMeasurement(filename)
    elif menu.upper() == "Q":
        print("Dziękujemy za dokonanie pomiarów")
        break
    else:
        print("Błędny wybór")
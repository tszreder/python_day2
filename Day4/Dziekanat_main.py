#CLI - command line interface
from Day4.Dziekanat_solution import StudentController
dziekanat = StudentController()

while(True):
    menu = input("APLIKACJA DZIEKANAT\n"
                 "(D) - dodaj nowego studenta\n(U) - usuń studenta\n(Z) - zaktualizuj oceny\n"
                 "(O) - wyczyść oceny studenta\n(W) - wypisz listę studentów\n(Q) - wyjdź z programu")

    if menu.upper() == "D":
        name = input("Podaj imię: ")
        nazwisko = input("Podaj nazwisko: ")
        dziekanat.addStudent(name, nazwisko)
    elif menu.upper() == "U":
        print(dziekanat)
        index_no = int(input("Podaj numer indeksu do usunięcia: "))
        dziekanat.deleteStudentByindex(index_no)
    elif menu.upper() == "Z":
        print(dziekanat)
        try:
            selected_student = int(input("Wybierz numer indeksu studenta, któremu chcesz dodać oceny: "))
            grades = input("Podaj listę ocen po przecinku: ")
            grades = grades.split(",")
            #konwersja ocen do liczb całkowitych
            i = 0
            while i < len(grades):
                grades[i] = int(grades[i])
                i += 1
            #wywołanie metody addGrades
            dziekanat.addGradesToStudent(selected_student, grades)
        except:
            print("Błąd danych! Nie można wykonać konwersji")
    elif menu.upper() == "O":
        print(dziekanat)
        try:
            selected_student = int(input("Wybierz numer indeksu studenta, któremu chcesz usunąć oceny: "))
            dziekanat.deleteStudentGraddesByIndex(selected_student)
        except:
            print("Błędny numer indeksu!")
    elif menu.upper() == "W":
        print(dziekanat)
    elif menu.upper() == "Q":
        break
    else:
        print("Błędny wybór")
import gc
# P67
# Wykorzystując obiektowość napisz program DZIEKANAT, który:
# Umożliwia przypisanie ocen do studenta identyfikowanego przez:
# Nr_indeksu
# Imię
# Nazwisko
# Przechowywanie tych danych w sekwencji i wykonanie takich operacji jak:
# Wprowadzanie nowego studenta
# Wyświetlanie wprowadzonych studentów
# Usuwanie studenta

class Student:
    def __init__(self, Imie, Nazwisko, Nr_indeksu):
        self.Imie = Imie
        self.Nazwisko = Nazwisko
        self.Nr_indeksu = Nr_indeksu
        self.oceny = []
        students.append(self)

    def __str__(self):
        return "Numer indeksu: %6s | Imię: %-10s | Nazwisko: %-10s" % (self.Nr_indeksu, self.Imie, self.Nazwisko)

    def wypisz_studentow(self):
        for student in students:
            print("Numer indeksu: %6s | Imię: %-10s | Nazwisko: %-10s" % (student.Nr_indeksu, student.Imie, student.Nazwisko))
            print(student)

students = []
finish = True
while finish:
    gui = input("Co chcesz zrobić? 1 - dodaj nowego studenta, 2 - wypisz wszystkich studentów, 0 - wyjdź")
    if gui == str(0):
        finish = False
        print("koniec")
    elif gui == str(1):
        student1 = Student(input("Podaj imie"), input("Podaj nazwisko"), input("Podaj nr ideksu"))
    elif gui == str(2):
        for student in students:
            print(student)


# student2 = Student("Tomasz", "Szreder", 123456)
# print(student2)


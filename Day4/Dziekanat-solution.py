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

last_insert_index = 0

class Student:
    def __init__(self, Imie, Nazwisko):
        self.Imie = Imie
        self.Nazwisko = Nazwisko
        # inkrementacja glbalnej wartosci - automatyczne nadawanie numeru indeksu
        global last_insert_index
        self.Nr_indeksu = last_insert_index + 1
        # pusta lista ocen
        self.oceny = []
        students.append(self)

    def __str__(self):
        return "Numer indeksu: %06d | Imię: %-10s | Nazwisko: %-10s | Oceny: %10s" %\
               (self.Nr_indeksu, self.Imie, self.Nazwisko, self.oceny)

class StudentController:
    def __init__(self):
        self.students = []
    def __str__(self):
        output = ""
        for student in self.students:
            output += student.__str__() + "\n"
        return output
    #metoda dodająca studenta do listy
    def addStudent(self, Imie, Nazwisko):
        student = Student(Imie, Nazwisko)
        self.students.append(student)


finish = True
while finish:
    gui = input("Co chcesz zrobić? 1 - dodaj nowego studenta, 2 - wypisz wszystkich studentów, 0 - wyjdź")
    if gui == str(0):
        finish = False
        print("koniec")
    elif gui == str(1):
        student1 = Student(input("Podaj imie"), input("Podaj nazwisko"))
    elif gui == str(2):
        for student in students:
            print(student)


student2 = Student("Tomasz", "Szreder", 123456)
dodaj_oceny(student2)
print(student2)


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
    def __init__(self, name, lastname):
        self.name = name
        self.lastname = lastname
        # inkrementacja glbalnej wartosci - automatyczne nadawanie numeru indeksu
        global last_insert_index
        self.index_no = last_insert_index + 1
        # pusta lista ocen
        self.oceny = []

    def __str__(self):
        return "Numer indeksu: %06d | Imię: %-10s | Nazwisko: %-10s | Oceny: %10s" %\
               (self.index_no, self.name, self.lastname, self.oceny)

class StudentController:
    def __init__(self):
        self.students = []
    def __str__(self):
        output = ""
        for student in self.students:
            output += student.__str__() + "\n"
        return output

    #metoda dodająca studenta do listy
    def addStudent(self, name, lastname):
        student = Student(name, lastname)
        self.students.append(student)

    # metoda wyszukująca studenta
    def findStudentByIndex(self, index_no):
        for student in self.students:
            if index_no == student.index_no:
                return student
            return None

    #metoda usuwająca studenta z listy
    def deleteStudentByindex(self, index_no):
        deletedStudent = self.findStudentByIndex(index_no)
        if deletedStudent != None:
            self.students.remove(deletedStudent)
            print("usunięto studenta")
        print("nie ma takiego studenta")

dziekanat = StudentController()
dziekanat.addStudent("test", "test")
dziekanat.addStudent("test", "test")
dziekanat.addStudent("test", "test")
dziekanat.addStudent("test", "test")

print(dziekanat)

# finish = True
# while finish:
#     gui = input("Co chcesz zrobić? 1 - dodaj nowego studenta, 2 - wypisz wszystkich studentów, 0 - wyjdź")
#     if gui == str(0):
#         finish = False
#         print("koniec")
#     elif gui == str(1):
#         student1 = Student(input("Podaj imie"), input("Podaj nazwisko"))
#     elif gui == str(2):
#         for student in students:
#             print(student)
#
#
# student2 = Student("Tomasz", "Szreder", 123456)
# dodaj_oceny(student2)
# print(student2)


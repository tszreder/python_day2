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
        last_insert_index += 1
        self.index_no = last_insert_index
        # pusta lista ocen
        self.grades = []

    def __str__(self):
        return "Numer indeksu: %06d | %-10s | %-10s | %10s | %5.2f" %\
               (self.index_no, self.name, self.lastname, self.grades, self.calculateAvg())

    def calculateAvg(self):
        sum = 0
        for grade in self.grades:
            sum += grade
        if len(self.grades) == 0:
            return 0
        return sum / len(self.grades)

class StudentController:
    # metoda tworząca konktroler (dziekanat)
    def __init__(self):
        self.students = []

    # metoda wypisująca listę wszystkich studentów
    def __str__(self):
        output = ""
        sum = 0
        studentHasGrade = 0
        for student in self.students:
            output += student.__str__() + "\n"
            if len(student.grades) != 0:
                sum += student.calculateAvg()
                studentHasGrade += 1
        # średnia ocen wszystkich studentów
        if studentHasGrade == 0:
            output += "ŚREDNIA STUDENTÓW Z OCENAMI: %5.2F" % (0)
        else:
            output += "ŚREDNIA STUDENTÓW Z OCENAMI: %5.2F" % (sum / studentHasGrade)
        return output

    #metoda dodająca studenta do listy
    def addStudent(self, name, lastname):
        #utworzenie obiektu klasy student
        student = Student(name, lastname)
        #dodanie obiketu do listy
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
            print("usunięto studenta" + deletedStudent.__str__())
        else:
            print("nie ma takiego studenta")

    #dodawanie ocen do studenta
    def addGradesToStudent(self, index_no, new_grades):
        foundStudent = self.findStudentByIndex(index_no)
        if foundStudent != None:
            foundStudent.grades.extend(new_grades)
            print("zaktualizowano listę ocen")

    # usuwanie ocen studenta
    def deleteStudentGraddesByIndex(self,index_no):
        foundStudent = self.findStudentByIndex(index_no)
        if foundStudent != None:
            foundStudent.grades = []
            print("wyczyszczona lista ocen")





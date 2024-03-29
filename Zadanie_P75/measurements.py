from datetime import datetime


class Measurement:
    def __init__(self, user, result):
        self.user = user
        self.date = datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
        self.result = result

    def __str__(self):
        return "%15s | %15s | %6i" % (self.user, self.date, self.result)

class Measurement_List:
    def __init__(self):
        self.measurements = []

    def __str__(self):
        output = ""
        for measurement in self.measurements:
            output += measurement.__str__() + "\n"
        return output

    def makeMeasurement(self, user, result):
        """
        funkcja tworzy nowy pomiar
        :param user: nazwa użytkownika, który dokonał pomiaru
        :param result: wynik pomiaru, który chcemy zapisać
        :return: None
        """
        measure = Measurement(user, result)
        self.measurements.append(measure)

    def saveMeasurement(self, filename):
        file = open(filename +".txt", mode="w+", encoding="utf16")
        for measurement in self.measurements:
            file.write(measurement.__str__() + "\n")
        file.close()

    def addNewMeasurement(self, filename):
        file = open(filename +".txt", mode="a+", encoding="utf16")
        for measurement in self.measurements:
            file.write(measurement.__str__() + "\n")
        file.close()

a = 'Tomek'
b = 1



# # measure = Measurement("Tomek", 12)
# ml = Measurement_List()
# ml.makeMeasurement(a,b)
# # ml.makeMeasurement("tomek", 12)
# # ml.makeMeasurement("Jan", 3)
# # ml.saveMeasurement()
# # ml.addNewMeasurement()
# print(ml)
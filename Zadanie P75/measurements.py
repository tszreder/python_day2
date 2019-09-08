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

    def addMeasurement(self, user, result):
        measure = Measurement(user, result)
        self.measurements.append(measure)

measure = Measurement("Tomek", 12)
print(measure)
class Auto:
    # pola obiektowe
    # marka = "Audi"
    # model = "A4"
    # cena = 200000

    def __init__(self, marka, model, cena):
        self.marka = marka
        self.model = model
        self.cena = cena

    #metody obiektowe
    def getAuto(self):
        print("Marka: %s model: %s cena %.2f" % (self.marka, self.model, self.cena))

    def setCena(self, nowa_cena):
        self.cena = nowa_cena

# tworzenie obiektu klasy auto
a1 = Auto("BMW", "5", 400000)
# a1.marka = 'VW'
# a1.model = "Passat"
# a1.cena = 50000
a2 = Auto("Toyota", "Avensis", 50000)
a1.getAuto()
a1.setCena(60000)
a1.getAuto()
a2.getAuto()


print(a1)
print(a2)


class AutoFactory:
    autos = []
    def createAuto(self, marka, model, cena):
        a = Auto(marka, model, cena)
        self.autos.append(a)
        print("Dodano auto: ", end= " ")
        a.getAuto()
    def addAuto(self, auto):
        self.autos.append(auto)
    def changePrices(self, changePercent):
        for auto in self.autos:
            auto.setCena(auto.cena * (1 + changePercent/100))
    def showAutos(self):
        for auto in self.autos:
            auto.getAuto()
    def comparePrices(self, auto1, auto2):
        print("porównujemy:")
        auto1.getAuto()
        auto2.getAuto()
        if auto1.cena >= auto2.cena:
            print("Auto: " + auto1.marka + " jest droższe")
        else:
            print("Auto: " + auto2.marka + " jest droższe")

factory = AutoFactory()
factory.addAuto(a1)
factory.addAuto(a2)
factory.showAutos()
factory.changePrices(10)
factory.showAutos()
factory.createAuto("Honda", "Civic", 12000)
factory.showAutos()
factory.comparePrices(a1, a2)
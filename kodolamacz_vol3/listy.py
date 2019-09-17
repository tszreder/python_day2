def czyPalindrom(wyraz):
    lista = list(wyraz)
    odlista = list(reversed(lista))
    if lista == odlista:
        return True
    else:
        return False

print(czyPalindrom('kok'))

def czyAnagram(wyraz1, wyraz2):
    lista1 = list(wyraz1)
    lista2 = list(wyraz2)
    print(lista1)
    print(lista2)
    lista1.sort()
    lista2.sort()
    print(lista1)
    print(lista2)

    if lista1.sort() == lista2.sort():
        return True
    else:
        return False

print(czyAnagram("takafghj", "jtgah"))

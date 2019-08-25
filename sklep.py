'''
Ćwiczenie P50
 Napisz program do obsługi zamówień w sklepie internetowym:
 W sklepie sprzedawane są 3 produkty: A, B, C
 Posiadają one swoje:
 ID: 1, 2, 3
 Nazwa: A, B, C
 Cenę: 3.50, 2.99, 9.99
 Ilość magazynową: 10, 5, 1
 Zaprojektuj menu zamówień w sklepie:
 Użytkownik zamawia towar po jego unikatowym ID
 Użytkownik może zamówić ilość nie większą niż dostępność na magazynie
 Użytkownik może w po zrealizowaniu zamówienia zamówić kolejne produkty
 Efektem zakończenia zamawiania produktów jest:
 Paragon zawierający informację jakie produkty zamówił użytkownik
 Kwota do zapłaty
 Pamiętaj o walidacji danych!
'''

#produkty
products = {
    1: ["A", 49.99, 5],
    2: ["B", 13.99, 4],
    3: ["C", 16.99, 9]
}

'''
1. menu zamowien (while...)
2. zamówienie produktu po id w określonej ilości
3. gdy zamówienie może być dodane do koszyka to zmniejszamy stan magazynu
4. eksport paragonu wraz z kwotą do zapłaty
'''

# sesja_trwa = True
basket = {}
print(products)
sesja_trwa = True
while(sesja_trwa == True):
    item = int(input("Wpisz id produktu, 0 - koniec zakupów"))
    print("%3s | %20s | %5s | %3s| %6s" % ("ID", "PRODUKT", "CENA", "ILOŚĆ", "SUMA"))
    if item in products:
        print("zakup możliwy")
        amount = int(input("Podaj ilość produktu"))
        if amount <= products[item][2]:
            print("Dodano do koszyka")
            order = [products[item][0],products[item][1], amount]
            basket[item] = order
            print(basket)
            products[item][2] = products[item][2] - amount

        else:
            print("nie ma tyle towaru na magazynie")
    elif item == 0:
        sum = 0
        for key in basket.keys():
            sum += basket[key][1] * basket[key][2]
            print("%3i | %20s | %5.2f | %3i | %6.2f" %
                  (key,basket[key][0],basket[key][1],basket[key][2], basket[key][1] * basket[key][2]))
        print("Do zapłaty: " + str(sum) + " PLN")
        sesja_trwa = False
    else:
        print("nie ma takiego produktu")
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

order = int(input("Wpisz id produktu, który chcesz dodać do koszyka"))
# while(sesja_trwa == True):
#     for product in products:

if order in products:
    print("zakup możliwy")
    amount = int(input("Podaj ilość produktu"))
    print(amount)
    if amount <= products[order][2]:
        print("Można kupić taką ilość")
        zam = products[order]
        zam[2] = amount
        basket[order] = zam
        print(basket)
        products[order][2] = products[order][2] - amount
        print(products)


    else:
        print("nie ma tyle towaru na magazynie")
else:
    print("nie ma takiego produktu")
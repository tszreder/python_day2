from math import ceil, floor


def potega(podstawa, wykladnik):
    wynik = 1
    i = 1
    while i <= wykladnik:
        wynik *= podstawa
        i += 1
    return wynik

print(potega(2,5))

def silnia(podstawa):
    if podstawa == 0:
        wynik = 1
    elif podstawa == 1:
        wynik = 1
    else:
        wynik = podstawa * silnia(podstawa - 1)
    return wynik

print(silnia(5))




def list_sum_recursive(input_list):
    # Base case
    if input_list == []:
        return 0

    # Recursive case
    # Decompose the original problem into simpler instances of the same problem
    # by making use of the fact that the input is a recursive data structure
    # and can be deﬁned in terms of a smaller version of itself
    else:
        head = input_list[0]
        smaller_list = input_list[1:]
        return head + list_sum_recursive(smaller_list)

print(list_sum_recursive([2,3,4,5,6]))

# def fibonacci(n):
#     print("Calculating F", "(", n, ")")
#
#     if n == 0:
#         return  0
#     elif n == 1:
#         return 1
#     else:
#         return fibonacci(n-1) + fibonacci(n - 2)
#
# print(fibonacci(4))


def sprytne_potegowanie(podstawa, wykladnik):
    if wykladnik == 1:
        return podstawa
    elif wykladnik == 0:
        return 1
    else:
        polowa =sprytne_potegowanie (podstawa, wykladnik // 2)
        if wykladnik % 2 == 0:
            return polowa * polowa
        else:
            return polowa * polowa * podstawa

print(potega(2,10))
print(sprytne_potegowanie(2,10))
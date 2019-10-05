import numpy as np

tab = np.arange(1,16)
# print(tab)
#
# tab = np.arange(15).reshape(3,5)
# print(tab)
#
# result = tab[2]
# print(result)
#
# result = tab[1][-2]
# print(result)
print(tab.size)

#sprawdzić wymiar, size, typ obiektu i typ danych

c = np.array([[1, 2],[3, 4]], dtype=complex)
print(c.size)
print(type(c))
print(c.dtype)
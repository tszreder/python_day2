import matplotlib.pyplot as plt

n = 100
data2 = [(x**2, i) for i, x in enumerate(range(n))]
data3 = [(i, x**2) for i, x in enumerate(range(n))]
data = [(x, x**2) for x in range(n)]

print(data)
print(data2)

x = [x[0] for x in data]
y = [x[1] for x in data]

plt.plot(x,y)
plt.plot(data)
plt.show()
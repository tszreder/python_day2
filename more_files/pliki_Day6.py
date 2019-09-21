#zapisywanie do pliku
F = open("zwierzeta.txt", "w", encoding="utf16") # domyślny tryb to read

for param in ["name", "mode", "closed"]:
    print(getattr(F, param))

# do sprawdzenia getattr

F.write("ZWIERZETA\n")
animals = ["słoń", "lew", "pingwin"]
F.writelines([animal + "\n" for animal in animals])

# readlines
F = open("zwierzeta.txt", "r", encoding="utf16")
for el in F.readlines():
    print(el)

print(F.tell())


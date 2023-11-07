"""
escribir un programa que añada valores a una lista mientras que su longitud sea menor a 120;
mostrar la lista
usar WHILE y FOR
"""
# con WHILE
"""
coleccion = []
x = 0
while len(coleccion) < 120:
    coleccion.append(x)
    x += 1
print(coleccion)
"""
# con FOR
coleccion = []
for i in range(0, 120):
    coleccion.append(i)
print(coleccion)


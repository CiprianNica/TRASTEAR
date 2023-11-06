cantantes = ['2pac', 'drake', 'bad bunny', 'julio iglesias']
numeros = [1, 2, 5, 8, 3, 4]

# ordenar
#print(numeros)
numeros.sort()
#print(numeros)

# añadir elementos
cantantes.append('phoenix')
cantantes.insert(1, 'Bisbal')
#print(cantantes)

# eliminar elementos
cantantes.pop(1)
cantantes.remove('phoenix')
print(cantantes)

# dar la vuelta a una lista
print(numeros)
numeros.reverse()
print(numeros)
# cuantas veces aparece un elem
print(numeros.count(8))
numeros.append(8)
print(numeros.count(8))
# conseguir un indice
print(cantantes.index('drake'))
# unir 2 listas
cantantes.extend(numeros)
print(cantantes)
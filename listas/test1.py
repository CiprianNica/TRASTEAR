"""
# definir listas

peliculas = []
peliculas = ['Batman', 'El señor de los anillos', 'Spiderman']
print(peliculas)

cantantes = list(('2Pac', 'Drake', 'Lopez'))
print(cantantes)

years = list(range(2020, 2025))
print(years)

# añadir elem a una lista: append

cantantes.append('Jay-Z')
print(cantantes)
"""
"""
# recorer lista
peliculas = []
nueva_pelicula = ""
while nueva_pelicula != 'parar':
    nueva_pelicula = input('Introd una pelicula nnueva: ')
    if nueva_pelicula != 'parar':
        peliculas.append(nueva_pelicula)
    
for pelicula in peliculas:
    print(f"{peliculas.index(pelicula)+1}. {pelicula}")
    
"""
# listas multidimensionale

contactos = [
    ['Antonio', 'antonio@antonio.com'],
    ['Luis', 'luis@luis.com'],
    ['Salvador', 'salvador@salvador.com']
]
for contacto in contactos:
    for elem in contacto:
        if contacto.index(elem) == 0:
            print(f"Nombre: {elem}")
        else:
            print(f"Email: {elem}\n")


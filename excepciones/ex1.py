# busqueda en una lista
def is_numero(numero):
    try:
        numero = int(numero)
        result = True
    except ValueError:
        result = False
    return result

lista = [1, 45, 78, 57, 89, 100, 123, 789]
busqueda = input('Introduce el numero: ')

while not is_numero(busqueda):
    busqueda = input(f"ERROR, '{busqueda}' no es un numero, intentalo otra vez:")
    
if int(busqueda) in lista:
    print(f"el numero {busqueda} esta en la posicion {lista.index(busqueda)} de nuestra lista.")
else:
    print(f"el numero {busqueda} no esta en nuestra lista.")

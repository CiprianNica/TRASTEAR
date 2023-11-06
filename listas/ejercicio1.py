"""
hacer un programa que tenga una lista
de 8 numeros y haga lo siguente:
- recorrer la lista y mostrarla
- ordenarla y mostrarla
- mostrar su longitud
- buscar algun elemento que el usuario pida por teclado 
"""
numeros = [10, 2, 6, 78, 90, 45, -23, 34, 56]
# recorer la lista y mostrarla
print("\n")
for numero in numeros:
    print(f"numero {numeros.index(numero)} es : {numero}")
    
# ordenarla y mostrarla
print(f"\nlista neordenada es: {numeros}\n")
numeros.sort()
print(f"lista ordenada es: {numeros}\n")

# mostrar su longitud
print(f"la lista {numeros} tiene {len(numeros)} elementos. ")

# buscar algun elem que el usuario pide
elem = int(input("introd elem a buscar en lista: "))
if elem in numeros:
    print(f"numero {elem} esta en nuestra lista")
else:
    print(f"numero {elem} NO esta en nuestra lista")
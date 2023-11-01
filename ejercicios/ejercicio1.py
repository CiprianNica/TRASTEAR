"""
    escribir un programa que muestre los cuadrados de los 60 primeros numeros naturales
"""
# con while
contador = 0
while contador <= 60:
    cuadrado = contador * contador
    print(f"cuadrado de {contador} es: {cuadrado}")
    contador += 1

# con for
print("---------------------------- con FOR ------------------------------------")
for i in range(0, 61):
    print(f"cuadrado de {i} es: {i**2}")
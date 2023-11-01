"""
hacer un programa que muestre todos los numeros entre dos numeros que diga el usuario
"""

numero1 = int(input('introd el primer numero: '))
numero2 = int(input('introd el segundo numero: '))

if numero1 < numero2:
    while numero1 <= numero2:
        print(numero1)
        numero1 += 1
else:
    while numero1 >= numero2:
        print(numero2)
        numero2 += 1
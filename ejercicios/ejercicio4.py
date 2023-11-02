"""
un programa que muestre todos los numeros impares entre dos numeros que decida el usuario
"""
numero1 = int(input('introd el primer numero: '))
numero2 = int(input('introd el segundo numero:'))

for i in range(numero1, numero2+1):
    if i % 2 != 0:
        print(i)
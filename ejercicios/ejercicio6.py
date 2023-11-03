"""
hacer un programa que pida numeros al usuario indefinidamente hasta meter el numero 111
"""
contador = input('introduce un numero: ')
while contador != '111':
    print(f'el numero es: {contador}')
    contador = input('reintroduce otro numero: ')
print('FIIIN DE PROGRAMA')
    
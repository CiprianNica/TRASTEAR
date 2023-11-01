"""
pedir dos numeros al usuario y hacer todas las operaciones basicas de una calculadora y mostrarlo por la pantalla
"""

numero1 = int(input("introd el primer numero: "))
numero2 = int(input("introd segundo numero: "))
operacion = input("que operacion quieres hacer (s = suma, r = resta, d = division, m = multiplicacion)")

if operacion == 's':
    result = numero1 + numero2
    operacion = 'suma'
elif operacion == 'r':
    operacion = 'resta'
    if numero1 > numero2:
        result = numero1 - numero2
    else:
        result = numero2 - numero1
elif operacion == 'm':
    result = numero1 * numero2
    operacion = 'multiplicacion'
elif operacion == 'd':
    operacion = 'division'
    if numero2 == 0:
        result = 'no se puede dividir por zero'
    else:
        result = numero1 / numero2
print(f"resultado de la {operacion} es: {result}")
"""
los modulos son funcionalidades ya hechas para reutilizar
podemos conseguir modulos que ya vienen en el lenguaje, en el internet o podemos crear nuestros modulos
"""
""" # importar modulo proprio
from mimodulo import *

holaMundo('Victro')
suma(3, 5)

# importar modulo datetime
import datetime

print(datetime.date.today())
print(datetime.datetime.now().strftime("%a %d.%b.%y"))

# modulo random
import random
print(f"numero aleatorio entre 15 y 56: {random.randint(15, 56)}") """

import operaciones

a, b, c, d = (1, 2, 2, 4)

suma = operaciones.suma(a, b)
division = operaciones.division(b, a)
multi = operaciones.multiplicacion(c, d)
division = operaciones.division(d, c)
print(f"{a} + {b} = {suma}")
print(f"{b} - {a} = {division}")
print(f"{c} * {d} = {multi}")
print(f"{d} / {c} = {division}")

print("---------- reloj ------------")
import reloj
print(reloj.view_reloj)
"""
el programa tiene que pedir la nota de 15 alumnos y sacar por
pantalla cuantos han aprobado y cuantos han suspendido
"""

aprobados = 0
suspendidos = 0
alumno = 1
while alumno <= 15:
    nota = input(f'alumno {alumno} tiene la nota: ')
    while not nota in ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10'):
        print('ERROR, NOTA ERRONEA !!!!')
        nota = input(f'alumno {alumno} tiene la nota: ')
    if int(nota) > 5:
        aprobados += 1
    else:
        suspendidos += 1
    alumno += 1
print(f"aprobados: {aprobados}")
print(f"suspendidos: {suspendidos}")
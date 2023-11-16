from io import open
import pathlib


# abrir archivo
ruta = str(pathlib.Path().absolute()) + "/fichero_texto.txt"
archivo = open(ruta, "a+")

# escribir
archivo.write("soy un texto metido desde Python\n")

# close
archivo.close()



# leer contenido
ruta = str(pathlib.Path().absolute()) + "/fichero_texto.txt"
archivo = open(ruta, "r")
#contenido = archivo.read()
#print(contenido)

# leer contenido y guardarlo en una lista
lista = archivo.readlines()
archivo.close()

for registro in lista:
    print(registro)
    
    
# copiar
import shutil

""" ruta_original = str(pathlib.Path().absolute()) + "/fichero_texto.txt"
ruta_nueva = str(pathlib.Path().absolute()) + "/fichero_texto_nuevo.txt"
#ruta_alternativa ="../sistema_archivos/fichero_nuevo.txt"
ruta_alternativa =str(pathlib.Path().absolute()) + "/../sistema_archivos/fichero_nuevo.txt"

shutil.copyfile(ruta_original, ruta_nueva)
shutil.copyfile(ruta_original, ruta_alternativa)
"""
# mover
"""
ruta_original = str(pathlib.Path().absolute()) + "/fichero_texto.txt"
ruta_nueva = "../sistema_archivos/fichero_rename.txt"
shutil.move(ruta_original, ruta_nueva)
"""
# eliminar
import os
#ruta_eliminar = str(pathlib.Path().absolute()) + "/fichero_nuevo.txt"
#os.remove(ruta_eliminar)

# comprobar si un fichero existe
import os.path
ruta_comprobar = os.path.abspath("./") + "/fichero_texto_nuevo.txt"
if os.path.isfile(ruta_comprobar):
    print("ruta existe")
else:
    print('ruta no existe')
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

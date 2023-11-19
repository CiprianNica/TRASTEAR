import os
import shutil

# crear carpeta
if not os.path.isdir("./mi_carpeta"):
    os.mkdir("./mi_carpeta")
else:
    print("Ya existe !!")
    
# borrar carpeta
#os.rmdir("./mi_carpeta")

# copiar carpeta
ruta_original = "./mi_carpeta"
ruta_nueva = "./mi_carpeta_COPIADA"
if not os.path.isdir("mi_carpeta_COPIADA"):
    shutil.copytree(ruta_original, ruta_nueva)

#eliminar
#if os.path.isdir("./mi_carpeta_COPIADA"):
    #os.rmdir("./mi_carpeta_COPIADA")

print("contenido de mi carpeta: ")
ficheros = os.listdir("./mi_carpeta")
for fichero in ficheros:
    print(f"fichero {ficheros.index(fichero)}: {fichero}")

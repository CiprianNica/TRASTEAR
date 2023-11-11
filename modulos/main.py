"""
los modulos son funcionalidades ya hechas para reutilizar
podemos conseguir modulos que ya vienen en el lenguaje, en el internet o podemos crear nuestros modulos
"""
# importar modulo proprio
from mimodulo import *

holaMundo('Victro')
suma(3, 5)

# importar modulo datetime
import datetime

print(datetime.date.today())
print(datetime.datetime.now().strftime("%d.%m.%y"))



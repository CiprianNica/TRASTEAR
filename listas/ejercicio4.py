"""
crear un script que tenga 4 variab: lista, string, entero, booleano
imprima un mensaje segun el tipo de cada variab; usar funciones...
"""

def es_type(param):
    es_type = type(param)
    return es_type

lista = ['es', 'una', 'lista']
string = 'este es un string'
entero = 2345
bool = True

print(f"variab 'lista' es de tipul {es_type(lista)}")
print(f"variab 'string' es de tipul {es_type(string)}")
print(f"variab 'entero' es de tipul {es_type(entero)}")
print(f"variab 'bool' es de tipul {es_type(bool)}")


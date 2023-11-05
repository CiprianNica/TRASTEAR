# funciones dentro de otra funciones

def getNombre(nombre):
    texto = f"El nombre es: {nombre}"
    return texto

def getApellido(apellido):
    texto = f"El apellido es: {apellido}"
    return texto

def devuelveTodo(nombre, apellido):
    texto = getNombre(nombre) + "\n" + getApellido(apellido)
    return texto

print(devuelveTodo('Victor', 'Verde'))
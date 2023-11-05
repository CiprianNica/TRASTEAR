def getEmpleado(nombre, dni = None):
    print('EMPLEADO')
    print(f"Nombre: {nombre}")
    if dni != None:
        print(f"DNI: {dni}")
    print("\n")
nombre = input("intro el nombre: ")
dni = input('introd el dni: ')
getEmpleado(nombre)
getEmpleado(nombre, dni)

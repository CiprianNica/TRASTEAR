# IF anidados

print('\n################ EJEMPLO 3 ####################')

nombre = "Victor Blabla"
ciudad = "Madrid"
continente = "Europa"
edad = 55
mayoria_edad = 18
"""
if edad >= mayoria_edad:
    print(f"{nombre} es mayor de edad !")
    if continente != "Europa":
        print("El usuario no es europeo")
    else:
        print(f"Es europeo y de {ciudad}")
else:
    print(f"{nombre} NO es mayor de edad.")
"""
dia = int(input("introd el numero de dia: "))
if dia == 1:
    print('es lunes')
elif dia == 2:
    print('es martes')
elif dia == 3:
    print('es miercoles')
elif dia == 4:
    print('es jueves')
elif dia == 5:
    print("es viernes.")
elif dia == 6 or dia == 7:
    print("Ya, es fin de semana")
else:
    print("numero de dia incorecto")
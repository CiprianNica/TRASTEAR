def get_int():
    is_number = False
    number = input("give me a integer number: ")
    while not is_number:
        try:
            number = int(number)
            is_number = True
        except ValueError:
            print("not a valid integer, try again...")
            number = input("give me again a integer number: ")
            is_number = False
    return number

try:
    numero = int(input("introd el numero para elevarlo al cuadrado: "))
    print("el cuadrado es:" + numero * numero)

except TypeError:
    print("debes convertir tus cadena a enteros en el codigo !!!")
except ValueError:
    print("introd un numero correcto")

except Exception as e:
    print(f"ha ocurrido un error : {type(e).__name__}")

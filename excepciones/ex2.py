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

""" try:
    numero = int(input("introd el numero para elevarlo al cuadrado: "))
    print("el cuadrado es:" + numero * numero)

except TypeError:
    print("debes convertir tus cadena a enteros en el codigo !!!")
except ValueError:
    print("introd un numero correcto")

except Exception as e:
    print(f"ha ocurrido un error : {type(e).__name__}")
"""
class NotIntError(Exception):
    def __init__(self, value, message = "This module only works with integers. Sorry!"):
        self.value = value
        self.message = message
        super().__init__(self.message)
    def __str__(self) -> str:
        return f"{self.value} -> {self.message}"

values = (4, 7, 2.11, 9)
try:
    for value in values:
        if not isinstance(value, int):
            raise NotIntError(value)
except NotIntError as e:
    print(e)
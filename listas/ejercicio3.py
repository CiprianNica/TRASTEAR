"""
programa que compruebe si una variable esta vacia;
si esta vacia, rellenala con texto en minuscula y monstalo en minuscula.
"""
texto = " c "
if texto == "":
    texto = input('introd el texto: ').lower()
    print(f"texto en mayuscula: {texto.upper()}")
else:
    print(f"La variable no esta vacia, contiene '{texto}'")
    
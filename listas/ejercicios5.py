"""
crear una lista con el contenido de esta tabla:
accion:        aventura:               deportes:
gta              asasins                  fifa21
cod              crash                   pro21
pugb             princd of persia        motogp 21

mostrar esta inf ordenada
"""

tabla = [
    {
        'categoria': 'ACCION',
        'juegos': ['GTA', 'COD', 'PUGB']
    },
    {
        'categoria': 'AVENTURA',
        'juegos': ['ASASINS', 'CRASH', 'PRINCE OF PERSIA']
    },
    {
        'categoria': 'DEPORTTES',
        'juegos': ['FIFA21', 'PRO21', 'MOTOGP21']
    }
]
print()
for categoria in tabla:
    print(f"-------------------{categoria['categoria']}--------------------")
    for juego in categoria['juegos']:
        print(juego)
    
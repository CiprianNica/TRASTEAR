
"""desarollar un reloj 'h : min : seg' """
import datetime
def view_reloj():
    hora = datetime.datetime.today().strftime("%H:%M:%S")
    return hora


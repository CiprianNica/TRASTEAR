# definir una clase (molde para crear mas objetos de ese tipo)

class Coche:
    
    # atributos o propriedads(variables)
    # caracteristicas del coche
    
    color = "Rojo"
    marca = "Ferrari"
    modelo = "Aventador"
    velocidad = 100
    caballaje = 500
    plazas = 2
    
    # Motodos, acciones que hace el objeto(coche) (funciones)
    def acelerar(self, aumentoVelocicad):
        self.velocidad += aumentoVelocicad
        
    def frenar(self, bajadaVelocidad = 20):
        self.velocidad -= bajadaVelocidad
        
    def getVelocidad(self):
        return self.velocidad
    
    def setColor(self, color):
        self.color = color
    def getColor(self):
        return self.color
    
    def setModelo(self, modelo):
        self.modelo = modelo
    def getModelo(self):
        return self.modelo
    
    
        
    
# fin definicion clase

# crear objetos (instanciar clase)
coche = Coche()
print(coche.marca, coche.modelo, coche.color)
print(f"velocidad actual: {coche.getVelocidad()}")
coche.acelerar(30)
coche.acelerar(20)
coche.acelerar(40)
coche.acelerar(20)
print(f"velocidad nueva: {coche.getVelocidad()}")
coche.frenar(20)
print(f"velocidad despues de frenar: {coche.getVelocidad()}")

coche.setModelo("Maranelo")
print(coche.getModelo())

coche.setColor("Amarillo")
print(coche.getColor())

# crear mas objetos

coche2 = Coche()
print(coche2.getColor())

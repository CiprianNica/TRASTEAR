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
    
    # constructor
    def __init__(self, color, marca, modelo, velocidad, caballaje, plazas):
        self.color = color
        self.marca = marca
        self.modelo = modelo
        self.velocidad = velocidad
        self.caballaje = caballaje
        self.plazas = plazas
        
    
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
    def getMarca(self):
        return self.marca
    
    def getInfo(self):
        info = self.getMarca() + " " + self.getModelo() + " " + self.getColor()
        return info
        
    
# fin definicion clase


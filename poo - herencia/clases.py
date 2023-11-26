class Persona:
    """
    nombre
    apellidos
    altura
    edad
    """
    def setNombre(self, nombre):
        self.nombre = nombre
    def getNombre(self):
        return self.nombre
    
    def setApellidos(self, apellidos):
        self.apellidos = apellidos
    def getApellidos(self):
        return self.apellidos
    
    def setAltura(self, altura):
        self.altura = altura
    def getAltura(self):
        return self.altura
    
    def setEdad(self, edad):
        self.edad = edad
    def getEdad(self):
        return self.edad
    
    def hablar(self):
        return "Estoy hablando"
    def caminar(self):
        return "Estoy caminando"
    
class Informatico(Persona):
    '''
    lenguajes
    experiencia
    '''
    # constructor
    def __init__(self):
        self.lenguajes = ["HTML", "CSS", "JS"]
        self.experiencia = 4
        
    def getLenguajes(self):
        return self.lenguajes
    def setLenguajes(self, lenguajes):
        for lenguaje in lenguajes:
            self.lenguajes.append(lenguaje)
    def aprender(self, lenguajes):
        return f"Estoy aprendiendo {lenguajes}"
    def programar(self):
        return "esta programando"
    
class Tecnico_Redes(Informatico):
    def __init__(self):
        super().__init__()
        self.auditoriaRedes = "experto"
        self.experiencia = 15
    def auditar(self):
        return "esta auditando una red"
    
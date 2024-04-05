
class Cotxe:

    # Atributs de la classe
    color = 'Vermell'
    marca = 'Seat'
    model = 'Panda'
    velocitat = 120
    potencia = 150
    seients = 4
    atribut_public = 'Soc públic'
    __atribut_privat = 'Soc privat'

    # Constructor
    def __init__(self, color, marca, model, velocitat, potencia, seients):
        self.color = color
        self.marca = marca
        self.model = model
        self.velocitat = velocitat
        self.potencia = potencia
        self.seients = seients

    #Mètodes (accions que pot fer el cotxe)

    def setColor(self, color):
        self.color = color
    
    def setModel(self, model):
        self.model = model
    
    def setMarca(self, marca):
        self.marca = marca

    def accelerar(self):
        self.velocitat += 1

    def frenar(self):
        self.velocitat -= 1

    def getPrivat(self):
        return self.__atribut_privat    
    
    def getVelocitat(self):
        return self.velocitat
    
    def getColor(self):
        return self.color
    
    def getModel(self):
        return self.model
    
    def getMarca(self):
        return self.marca
    
    def getInfo(self):
        info = '----------- Informació General -----------\n'
        info += self.getMarca() +'\n'
        info += self.getModel() +'\n'
        info += self.getColor() +'\n'
        info += str(self.velocitat) +'\n'
        info += str(self.potencia) +'\n'
        info += str(self.seients) +'\n'

        return info
    
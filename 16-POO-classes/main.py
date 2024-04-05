# Primers passos amb la Programació Orientada a Objectes (POO) en Python

# DEfinim una classe

class Cotxe:

    # Atributs de la classe
    color = 'Vermell'
    marca = 'Seat'
    model = 'Panda'
    velocitat = 120
    potencia = 150
    seients = 4

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
    
    def getVelocitat(self):
        return self.velocitat
    
    def getColor(self):
        return self.color
    
    def getModel(self):
        return self.model
    
    def getMarca(self):
        return self.marca
    
# Instancia de la classe

cotxe = Cotxe() # Objecte 1 de Cotxe

print(cotxe.seients, cotxe.getModel(), cotxe.getMarca())
print(cotxe.getVelocitat())
cotxe.accelerar()
print(cotxe.velocitat)
cotxe.frenar()
cotxe.frenar()
print(cotxe.getVelocitat())

print(cotxe.getColor())
cotxe.setColor('Blau')
print(cotxe.getColor())

print(cotxe.getModel())
cotxe.setModel('Leon')
print(cotxe.getModel())

cotxe2 = Cotxe() # Objecte 2 de Cotxe

cotxe2.setMarca('Renault')
cotxe2.setModel('Clio')
cotxe2.setColor('Fucsia')

print('------------------- Cotxe2 -------------------')
print(cotxe2.getMarca(), cotxe2.getModel(), cotxe2.getColor(), cotxe2.potencia, cotxe2.seients)





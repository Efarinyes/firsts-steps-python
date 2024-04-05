

# Mòduls: Funcionalitats predefinides que ens permeten reutiñitzar codi. Podem escriure els nostres propis mòduls

import noumodul # Importa tot el contingut del mòdul
# from noumodul import calculadora # Nomes importem la funcionalitat que ens fa falta
import datetime
import math

print(noumodul.saludar('eduard'))
print(noumodul.calculadora(5,3, False))

# Treballem amb dates 

print(datetime.date.today())

data = datetime.datetime.now()
print(data)
print(data.month)
data_catalana = data.strftime('%d - %B - %Y')
print(data_catalana)

# Mòdul de Matemàtiques
print('Arrel quadrada de 2', math.sqrt(2))
print('Número PI', math.pi)
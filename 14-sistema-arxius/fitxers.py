from io import open
import pathlib
import shutil
import os
import os.path

""" ruta = str(pathlib.Path().absolute()) + '/prova.txt'
arxiu = open(ruta, "a+")
arxiu.write("Contingut nou\n")
arxiu.close() """

""" fitxer = open("llista-jocs.txt", "a+")
llista = ['Oca', 'Parxis', 'Escacs']
for linia in llista:
    fitxer.write(linia + '\n')
fitxer.close() """

ruta = str(pathlib.Path().absolute()) + '/llista-jocs.txt'
arxiu_lectura = open(ruta, "r")

# contingut = arxiu_lectura.read()
# print(contingut)

llista_lectura = arxiu_lectura.readlines()
arxiu_lectura.close()

for element in llista_lectura:
    print('- ' +element)

# Copiar arxius
    
""" ruta_original = str(pathlib.Path().absolute()) + '/llista-jocs.txt'
ruta_final = str(pathlib.Path().absolute()) + '/llista-jocs-copia.txt'
ruta_alternativa = "../07-exercicis/llista-jocs-copia2.txt"
shutil.copyfile( ruta_original, ruta_alternativa)  """

# Moure arxius

# ruta_original = str(pathlib.Path().absolute()) + '/llista-jocs-copia.txt'
# ruta_nova = str(pathlib.Path().absolute()) + '/llista-jocs-NOU.txt'

# shutil.move(ruta_original, ruta_nova)

# Eliminar arxius
ruta_nova = str(pathlib.Path().absolute()) + '/llista-jocs-NOU.txt'
# os.remove( ruta_nova )

print(os.path.abspath('llista-jocs.txt'))

if os.path.isfile(os.path.abspath('./') + '/prova.txt'):
    print('Yes')
else:
    print('No')



import os


# Crear carpeta

if not os.path.isdir('./carpeta_proves'):
    os.mkdir('./carpeta_proves')
else: 
    print('El directori ja existeix')


# Borrar directori
    
# os.rmdir('carpeta_proves')
    
print('Contingut de la carpeta-proves')

contingut = os.listdir('carpeta_proves')
print(contingut)
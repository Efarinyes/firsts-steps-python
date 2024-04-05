# bucles


# comptador = 0

resultat = 0

for comptador in range(0, 15):
    print('Estic al pas ' + str(comptador))
    resultat += comptador 
    
print('La suma del rang es ' + str(resultat))


# Taules de multiplicar

multiplicant = int(input('De quin número vols la taula? '))
if multiplicant < 1:
    multiplicant = 1
    

print(f'Escribim la taula del { multiplicant }' )

for numero_taula in range(1,11):
    print(f' {multiplicant} X { numero_taula} = { multiplicant * numero_taula} ')
else:
    print('Taula acabada')
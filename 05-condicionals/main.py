# Condicionals

print('############## Exemple 1 ##############' )
# color = input('Quin color tinc amagat? ')
color = 'Vermell'

if color == 'Vermell':
    print('Encertat!!')
    print('El color es Vermell')

else: 
    print('Has fallat...')
    print(f'El color no es { color }')

print('\n############## Exemple 2 ##############' )

any = 2021
# any = int(input('A quin any som?'))


if any >= 2021:
    print(f'Som al 2021 o més endavant ')
else:
    print('És una any anterior al 2021')


print('\n############## Exemple 3 ##############' )

nom = 'Eduard'
edat = 21
ciutat = 'Mataró'
continent = 'Europa'
majoria_edat = 18

if edat >= majoria_edat:
    # instruccions
    print(f'{ nom } és major d\'edat')
    if continent == 'Europa':
        print(f'{nom} és de {ciutat} que pertany a {continent}')
    else:
        print(f'{ nom } no és europeu')

else: 
    print(f'{ nom } no te la majoria d\'edat')


print('\n############## Exemple 4 ##############' )

dia = int( input( 'Indtrodueix el número del dia de la setmana: '))

if dia == 1:
    print('És dilluns')

elif dia == 2:
    print('És dimarts')
elif dia == 3:
    print('És dimecres')
elif dia == 4:
    print('És dijous')
elif dia == 5:
    print('És divendres')

else: 
    print('Ja és cap de setmana')

print('\n############## Exemple 5 ##############' )

edat_minima = 18
edat_maxima = 65
edat_actual = int(input('Quina edat tens? '))

if edat_actual >= edat_minima and edat_actual <= edat_maxima:
    print('Pots treballar')
else:
    print('No pots treballar')

print('\n############## Exemple 6 ##############' )

pais = 'Mèxic'

if pais == 'Mèxic' or pais == 'Argentina' or pais == 'Hoduras':
    print(f'A {pais} es parla castellà')
else:
    print(f'A { pais } no es parla castellà')

print('\n############## Exemple 7 ##############' )

pais = 'Vietnam'

if  not ( pais ==  'Mèxic' or pais == 'Argentina' or pais == 'Hoduras'):
    print(f'A {pais} no es parla castellà')
else:
    print(f'A { pais } es parla castellà')



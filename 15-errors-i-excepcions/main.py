# Captura d'execpcions i tractament d'errors de possibles errades de codi
""" try:
    nom = input('Com et dius? ')
    if len(nom ) > 1:
        nom_usuari = 'Et dius: ' + nom
    print(nom_usuari)
except:
    print('Tenim un error')
else:
    print('Tot correcte')
finally:
    print('Final de programa') """

# Multiples errors i exepcions
""" try:
    num = int(input('Introdueix un número per fer el seu quadrat: '))
    print(' El quadrat de ' + str(num) + ' és ' + str(num*num))

# except ValueError:
#     print( 'Nomes puc fer quadrats de números ')
    
# except TypeError:
#     print(' Ha de ser un número, prova de convertir-lo')
    
except Exception as e:
    print( 'Hi hagut un error', type(e).__name__)
 """

# Excepcions personalitzades

try:

    nom = input('Com et dius? ')
    edat = int(input('I quantys anys tens? '))

    if edat < 5 or edat > 120:
        raise ValueError('No realistic')
    elif len(nom) <=1:
        raise ValueError('Quin nom més curt, no?')
    else:
        print(f'Benvingut, { nom }')
except ValueError:
    print('Errors en la introducció de les dades')



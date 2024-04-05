# Funcions: Conjunt d'instruccions agrupades que resolen un seguit d'instruccions les vegades que s'invoqui

print('\n############ Exemple 1 ############\n')

def mostrarNom():
    print('Eduard\n')
    print('Pep\n')
    print('Ramon\n')
    print('Joana\n')
    print('Maria\n')

# mostrarNom()

print('\n############ Exemple 2 - Paràmetres ############\n')

def mostrarElTeuNom( nom, edat ):
    print(f'El teu nom es: {nom} ')
    if edat >= 18:
        print('Ets major d\'edat')
    else: 
        print('Creix!!!!')

# nom = input('Com et dius? ')
# edat = int(input('Quanta anys tens?: '))
# mostrarElTeuNom(nom, edat)

print('\n############ Exemple 3 ############\n')

def taulaDeMultiplicar(factor):
    print(f'La taula del {factor} \n')
    for comptador in range(1,11):
        print(f'{ comptador } X { factor} = { comptador * factor} ')
    print('\n')

factor = int(input('De quin número vols la taula?: '))
taulaDeMultiplicar(factor)

# Imprimim totes les taules de multiplicar de 1 a 10
print('-----------------------------------')
for num_taula in range(1,11):
    taulaDeMultiplicar(num_taula)


# Funcions amb paràmetres opcionals

def getEmpleats(nom, identificador = None ):
    print('TREBALLADOR')
    print(f'NOM: { nom }')
    if identificador != None:
        print(f'IDENTIFICADOR: { identificador }')

getEmpleats('Eduard', 'ADF123')
print('\n')

# Funcions amb paràmetres opcionals i retorn de resultats - montem una calculadora

def calculadora(num1, num2, basicas = False):
    suma = num1 + num2
    resta = num1 - num2
    multi = num1 * num2
    divisio = num1 / num2

    cadena = ''
    if basicas != False:
        cadena += 'Suma: ' + str(suma)
        cadena += '\n'
        cadena += 'Resta ' + str(resta)
        cadena += '\n'
    else:
        cadena += 'Multiplicació: ' + str(multi)
        cadena += '\n'
        cadena += 'Divisió ' + str(divisio)

    return cadena

print(calculadora(3,5, False))
print('\n')

# Funcions anidades

def getNom(nom):
    text = f'El nom es: { nom }'
    return text

def getCognom(cognom):
    text = f'I de cognom: {cognom }'
    return text

def nomComplert(nom, cognom):
    text = getNom(nom) + '\n' + getCognom(cognom)
    return text

print(nomComplert('Eduard', 'Farinyes'))
print('\n')

# Funcions lambda

quin_any_es = lambda any: f"Som a l'any { any }"

print(quin_any_es(2030))



# Un conjunt de dades [ clau - valor] molt semblat a un Array associatiu o un objecte JSON

persona = {
    'nom': 'Eduard',
    'cognoms': 'Farinyes Gasalla',
    'correu': 'eduard@eduard.com'
}
persona['Adreça'] = 'Mataró - Maresme'

print(type(persona))
print(persona)

print(persona['correu'])

# Diccionaris niats dins de llistes

contactes = [
    {
        'nom': 'Eduard',
        'cognoms': 'Farinyes Gasalla',
        'correu': 'eduard@eduard.com'
    },
    {
        'nom': 'Lluís',
        'cognoms': 'Manyoses Grau',
        'correu': 'manyoses@mayoses.com'
    },
    {
        'nom': 'Federic',
        'cognoms': 'Garcia Lorca',
        'correu': 'lorca@lorca.com'
    }
]

print(type(contactes))
print(contactes)   

print(contactes[1]['nom'])

for contacte in contactes:
    print('----------------------------------')
    print(f"Nom: { contacte['nom']}" )
    print(f"Cognoms: { contacte['cognoms']}" )
    print(f"Correu: { contacte['correu']}" )
    print('----------------------------------')
 

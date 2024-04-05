# Ordenar el codi. Primer les funcions, després les variables ( recomenació Codi Clean )
# Podem accedir a les variables globals des de les funcions sempre i quan estiguin definides avans d'imbocar la funció

def primera_funcio():
    return 'Com estas ' + nom + cognoms + '?'

def segona_funcio():
    return 'Segur que be!'

nom = 'Eduard '
cognoms = 'Farinyes Gasalla'

# print(f'Hola { nom } { cognoms }')
print(primera_funcio())
print(segona_funcio())
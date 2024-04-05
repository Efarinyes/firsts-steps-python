
musics = ['Haldor Mar', 'Ramoncin', 'Raimon', 'Lluís Llach']
numeros = [ 20,34,62,4,7,9,10,12,13,65,456, 1, 2 ]

# endreçar llista
print(numeros)
numeros.sort()
print(numeros)

# Afegir elements - mètodes

musics.append('Serrat')
musics.insert( 3, 'Dausà')
print(musics)

# Borrar elements d'una llista

musics.pop(1)
musics.remove('Serrat')
print(musics)

# CApgirar una llista
print(numeros)
numeros.reverse()
print(numeros)

# Verificar que un element existeix en una llista

print('Dausà' in musics)

# Comptar elements d'uan llista

print(len(numeros))

# Elements reptitis en una llista
numeros.append(1)
print(numeros.count(1))

# Averiguar Index d'un element
print(musics)
print(musics.index('Dausà'))

# Associar llistes
musics.extend(numeros)
print(musics)
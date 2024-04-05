# Llistes (arrays): Conjunt de dades agrupades en un sol nom. Poden ser accessibles per l'índex 

peliculas = ['Batman', 'Superman', 'Spiderman', 'Star Treck']
musics = list(('Haldor Mar', 'Ramoncin', 'Raimon', 'Lluís Llach'))
anys = list(range(1985, 2024))
llista_mixta = [ 'Eduard', 234, 4.5, False, 'hola']

# print(peliculas)
# print(musics)
# print(anys)
# print(llista_mixta)

# Treballem le llistes amb els seus índexs.

print(peliculas[2])
print(peliculas[-2])

print(musics[1:3])
print(peliculas[1:])
musics[1] = 'Maria del Mar Bonet'
print(peliculas[1])

musics.append('Peret')
print(musics)

# Recòrrer llistes

print('************* Llistat de películes *************\n')

nou_film = ''
while nou_film != 'aturat':
    nou_film = input('Indica una película: ')
    
    if nou_film != 'aturat':
        peliculas.append(nou_film)

for pelicula in peliculas:
    print(f" {peliculas.index(pelicula) + 1} - { pelicula }" ) 

# LListes multidimencionals
    
print('\n************* Llistat de Contactes *************\n')

contactes = [
    [
        'Pep', 
        'pep@pep.com'
    ],
    [
        'Josep', 
        'josep@pjosep.com'
    ],
    [
        'Maria', 
        'maria@maria.com'
    ],
    [
        'Joan', 
        'joan@joan.com'
    ],
    [
        'Eduard', 
        'eduard@eduard.com'
    ],

]
# print(contactes)

for contacte in contactes:
  for element in contacte:
    if contacte.index(element) == 0:
        print(f'Nom: { element }')
    else:
       print(f'Correu: { element }')
  print('\n')


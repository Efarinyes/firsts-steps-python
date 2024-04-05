""" Exercici 1:
Fer un programa que contingui una llista de 8 números enters y:
    - recorrer la llista i mostrar-la per pantalla
    - DEfinir una funció que recorri una lliusta de numeros i la mostri com string
    - Ordenar la llista y mostrar-la per poantalla
    - Mostrarla seva longitud
    - Cercar un item a partir d'una petició d'usuari """

nums = [ 3,1,4,67,28,33,98, 8 ]

def mostrarLlista(llista):
    resultat = ""
    for element in llista: 
        resultat += str(element)
        resultat += '\n'
    return resultat
print(mostrarLlista(nums))

# for num in nums:
#     print(num) # Recorrer llista i mostrar-la

nums.sort() # Ordenar LLista
print(mostrarLlista(nums)) # Mostrar llista Ordenada
print(len(nums)) # Mosttar número elements de la llista

try:
    print('Trobar num a la llista')

    peticio = int(input('Està aquest num a la llista? '))

    comproba = isinstance(peticio, int)

    while not comproba or peticio <= 0:
        peticio = int(input('Està aquest num a la llista? '))
    else:
        print(f'Has introduït el número: { peticio }')

    print(f'Trobar a la llista el número {peticio}')

    cerca = nums.index(peticio)
    print(f'El número buscat és a la llista amb l\'index { cerca }' )
except:
    print('El num no es troba a la llista ')

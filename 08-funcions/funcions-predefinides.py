# Funcions predefinides en Python 

nom = 'Eduard'

# per mostrar variables, cadenes de text, etc.. per pantalla (consola)
print(nom)

# mostra el tipus de dada de uan variable 'type()'
print(type(nom))

# Detectar el tipus d'una variable
comprobar = isinstance(nom, str)

if comprobar:
    print(f'{nom} es una cadena de text')
else:
    print(f' {nom} no es una cadena de text')

if not isinstance(nom, float):
    print(f'{nom} no és una variable numèrica de coma flotant')
else:
    print(f'{nom} es un número decimal')

# strip() mètode de les cdadenes de text que neteja els espais d'un string contingut en una variable
frase = '        En un lugar de la mancha         ' 
print(frase)
print(frase.strip())

# del Elimina la variable i e seu contingut que segueix
any = 2024
print(any)
del any
# print(any)

# Comprobar si una variable te contingut
text = '   fff   '
if len(text) <=0:
    print('variable buida')
else:
    print('si que te contingut', len(text))

# Trobar un caràcter dins d'una cadena de text
frase = 'Això és increible'
print(frase.find('és')) # Retorna la primera posició on comença el terme a buscar

# Substituir contingut d'una cadena de text
frase_nova = frase.replace('increible', 'superior')
print(frase_nova)

# Convertir a majuscules o minuscules
text_caotic = 'AIxÒ eS UN caOs'
text_majuscules = text_caotic.upper()
text_minuscula = text_caotic.lower()

print(text_caotic)
print(text_majuscules)
print(text_minuscula)
text_nou=text_minuscula.capitalize()
print(text_nou)

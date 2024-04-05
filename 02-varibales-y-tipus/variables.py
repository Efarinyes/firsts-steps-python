

"""
Variable, contenidors d'informació  
que a dins guarden dades.
en podem crear tantes com sigui menester i 
hi podem guardar diferents tipus de dades

"""
# Definició de variables i assignació d'un valor
text = 'Aprenent python'
text2 = 'A Udemy'

# Mostrar el valor de les variables
print(text)
print(text2)

num = 135
decimal = 12.7

print(num)
print(decimal)

print('-------------------------------')

# cambiem valor de les variables

num = 98
decimal = 8.4

print(num)
print(decimal)

# Concatenació de variables

nom = 'Eduard'
cognoms = 'Farinyes Gasalla'
edat = 62

print( nom + ' '+ cognoms + ' ' + str(edat))

print(f'{nom} {cognoms} - {str(edat)}')

print('Hola, em dic {} {} i tinc {} anys'.format(nom, cognoms, edat))


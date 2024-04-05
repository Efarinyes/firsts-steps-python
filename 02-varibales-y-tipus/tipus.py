# Tipus de dades
# Definició de variables
res = None
cadena = 'Hola mon!'
enter = 12
decimal = 34.66
falsocert = False
llistatint = [ 10, 34, 55, 155, 233 ] 
llistatstr = [ 'Python', 'React', 'javaScript', 'Java', 'Angular', 'Vue']
llistadecimal = [ 12.4, 45.6, 66.3, 78.3 ]
llistamix = [ 56.6, 'Hola', 66, 'Mon']
senseCambis = ('Curs', 'de ', 'Python')
diccionari = {
    'nom':'Eduard',
    'cognoms':'Farinyes Gasalla',
    'curs': 'Python'
}
rang = range(9)
dades_byte = b'Comprovant'


# Imprimim les variables
print(res) #NoneType
print(cadena) #str
print(enter) #int
print(decimal) #float
print(falsocert) #bool
print(llistatint) #list[int]
print(llistatstr) #list[str]
print(llistadecimal) #list[float]
print(llistamix) #list
print(senseCambis) #tuple
print(diccionari) #dict[str, str]
print(rang)
print(dades_byte)

# Imprimim el tipus de la variable amb el mètode  type()
print('---------------------')
print(type(res))
print(type(cadena))
print(type(enter))
print(type(decimal))
print(type(falsocert))
print(type(llistatint))
print(type(llistatstr))
print(type(llistadecimal))
print(type(llistamix))
print(type(senseCambis))
print(type(diccionari))
print(type(rang))
print(type(dades_byte))
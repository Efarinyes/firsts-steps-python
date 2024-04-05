# Variables globals i locals

# Variables locals

frase = 'En un lugar de la mancha'
print(frase)

def holaMon():
    frase = 'Hola Mon'
    print(frase)
    
    global any
    any = 2023
    print(any)

holaMon()
print('Des de fora: ', str(any))
# Afegir elements a una llista mentre la seva longitud sigui menor a 120

# Solució amb la importació de llibreries
""" import random #Modul que ens permet generar nums aleatoris

llista = []
while len(llista) < 120:
    element = random.randint(0,200)
    llista.append(element)
    print(f"El element { len(llista )- 1} es: {element}")
else:
    print(llista)
    print(len(llista))
    llista.sort()
    print(llista) """

# Solució sense llibreries - Bucle while

llista = []
comptador = 1

while len(llista) < 120:
    llista.append(comptador)
    comptador += 1
print(llista)

# Solució amb bucle for

coleccio = []

for comptador in range(0, 120):
    coleccio.append(f'element - { comptador }')
    print(f"Anem per l'element { coleccio[comptador]}")

print(coleccio[114])
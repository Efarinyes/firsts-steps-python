
# Bucle while


comptador = 1
pantalla = str(0)
while comptador <= 100:
    pantalla = pantalla + ', ' + str(comptador)
    
    comptador += 1
print(pantalla)

print('######### taula de multiplicar #########')

num_usuari = int(input('De quin número vols la taula? '))
if num_usuari < 1:
    num_usuari = 1

segon_comptador = 1

while segon_comptador <= 10:
    print(f'{num_usuari} X { segon_comptador } = { num_usuari * segon_comptador }')
    segon_comptador +=1
else:
    print('Fins aqui hi prou!!!')

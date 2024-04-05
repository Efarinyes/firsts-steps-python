
# mostrar tots els números parells del 1 al 100

comptador = 2

while comptador <=100:
    print(comptador)
    comptador += 2

print('solució amb bucle for')


factor = 1
for factor in range(1,101):

    if factor % 2 == 0:

        print(factor)
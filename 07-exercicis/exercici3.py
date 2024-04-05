# imprimir per consola el quadrat dels primers 61 números naturals
print('\nSolució amb bucle while\n')

comptador = 1

while comptador <= 61:
    print(f'El quadrat de { comptador} es: { comptador ** 2}')
    comptador += 1

print('\nSolució amb bucle for\n')

for num in range(1, 62):
    print(f'El quadrat del { num } es: { num ** 2}')
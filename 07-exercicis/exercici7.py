# Mostrar tots els números sanassos entre dos números donats

num1 = int(input('Primer número? '))
num2 = int(input('Segon número? '))

print(f'\nImprimir tots el numeros imparells entre {num1} i { num2 }\n')

comptador = num1

if num1 < num2:
    while comptador <= num2:
        print(f'El número { comptador } és imparell')
        comptador += 2
else:
    print('El primer número ha de ser més petit que el segon')
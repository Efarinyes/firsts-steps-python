
# Escriu per consola els números existents entre dos números introduïts

num1 = int(input('Introdueix el primer numero: '))
num2 = int(input('Introdueix el segon número: '))

if num1 < num2:
    for nums in range(num1 , num2 + 1):
        print(nums)
else:
    print( 'No puc comptar al reves ')



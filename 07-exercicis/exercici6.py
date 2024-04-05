# Mostra totes les taules de multiplicar des de 1 fins a 10

for factor in range(1,11):
    print(f'Taula del { factor }')
    for num in range(1, 11):
        print(f'la taula del { factor } es: { num * factor}')
    print('\n')
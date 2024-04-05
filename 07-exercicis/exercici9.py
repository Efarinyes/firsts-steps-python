# Demanar un número fis que coincideixi amb 111. Mostrar els números introduïts


num_secret = 111

num = int(input('Introdueix un número: '))

while num != num_secret:
    print(f'El número ingressat és { num } però no es correcte')
    num = int(input('Inteta-ho de nou: '))

print(f'Has encertat, el número amagat es { num_secret }')


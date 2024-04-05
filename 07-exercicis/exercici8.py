# Treure per pantalla el tan per cent d'un número donat i un percentatge facilitat

num = int(input('\nIntrodueix el número: '))
percentatge = int(input('\nIntrodueix el tan per cent a descomptar: '))

resultat = (num * percentatge) / 100

print(f'\nEl { percentatge }% de { num } és: { resultat }')
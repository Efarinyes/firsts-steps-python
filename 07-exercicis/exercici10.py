# Demanar les notes d'una classe i mostrar el total d'aprobats i el de suspesos

comptador = 1
aprobats = 0
suspesos = 0
num_alumnes = int(input('Quants alumnes hi ha al cusrs?: '))

while comptador <= num_alumnes:
    nota = float(input(f"Nota de l'alumne {comptador}: "))

    if nota < 5:
        suspesos += 1
    else:
        aprobats += 1
    comptador += 1
print(num_alumnes)
print(f'Alumnes aprobats: {aprobats} - Alumnes suspesos: {suspesos}')
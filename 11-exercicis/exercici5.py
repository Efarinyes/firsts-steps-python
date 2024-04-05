# Montar una llista de jocs amb els següents continguts:
# ACCIO:        GTA, COD, PUGB
# Aventures:    Assassins,  CRASH,   Prince of Persia
# Esports;      FIFA 23,    PRO 23,    Moto GP 23
# Mostratr la informació ordenada ( categoria: elements)

videojocs = [
    {
        "categoria": 'Acció',
        "jocs": [ 'GTA', 'COD', 'PUGB']
    },
    {
        "categoria": 'Aventures',
        "jocs": [ 'Assassins',  'CRASH', 'Prince of Persia' ]
    },
    {
        "categoria": 'Esports',
        "jocs": [ 'FIFA 23', 'PRO 23', 'Moto GP 23' ]
    }
   
]

for categoria in videojocs:
    print(f'----------------- { categoria["categoria"]} ------------------ ')
    for joc in categoria['jocs']:
        print(joc)

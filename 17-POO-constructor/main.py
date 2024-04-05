from cotxe import Cotxe

automobil = Cotxe('Verd', 'Renault', 'Clio', 120, 145, 4)
automobil2 = Cotxe('Groc', 'Seat', 'Leon', 120, 200, 5)
automobil3 = Cotxe('Negre', 'BMW', 'Sport Sity', 220, 250, 4)
automobil4 = Cotxe('Groc', 'Citroën', 'C3', 120, 150, 5)
automobil5 = Cotxe('Blanc', 'Mitshubishi', 'Space Wagon', 130, 175, 7)

print(automobil.getInfo())

automobil.accelerar()
automobil.accelerar()
automobil.accelerar()
automobil.accelerar()

print(automobil.getInfo())
print(automobil2.getInfo())
print(automobil3.getInfo())
print(automobil4.getInfo())
print(automobil5.getInfo())

if type(automobil2) == Cotxe:
    print('correcte')
else:
    print('No correcte')

print(automobil.atribut_public)
print(automobil.getPrivat())
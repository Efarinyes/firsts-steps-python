# SETS: Una agrupació de dades que no te índex ni ordre

persones = {
    'Joan',
    'Albert',
    'Emili',
    'Felip'
}
print(type(persones))
print(persones)

# Mètodes de SET

persones.add('Jordi') # Afegir un element al SET
print(persones)
persones.remove('Albert') # Elimina un elent del SET
print(persones)
import classes

persona = classes.Persona()
persona.setNom('Eduard')
persona.setCognoms('Farinyes Gasalla')
persona.setEdat('50 anys')
persona.setEstatura('165cm')

print(f'Tenim conectat a {persona.getNom() } { persona.getCognoms()}')
print(persona.parlar())

informatic = classes.Informatic()

informatic.setNom('Adela')
informatic.setCognoms('Montull')
print(informatic.getLlenguatges())
informatic.aprendre('Java')
print(f'Avui programa: {informatic.getNom()} {informatic.getCognoms()}')
print(informatic.getLlenguatges())
informatic.aprendre('Perl')
print(informatic.getLlenguatges())

print(informatic.arreglar())

tecnic = classes.TecnicInformatic()
tecnic.setNom('Pere')
tecnic.setCognoms('Cullera')



print(tecnic.auditarXarxes, tecnic.experienciaXarxes, tecnic.getNom(), tecnic.getCognoms(), tecnic.getLlenguatges())
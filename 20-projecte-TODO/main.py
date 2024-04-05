# Aplicació de TODO de consola amb python. Inclou Registre usuaris i Login
# Permet introduir Notas, editar-les i borrar-les

from usuaris import accions

print("""
    Aqui pots fer:
      
      - Registrar-te ( escriu registre )
      - Entrar ( escriu login )
""")

fesAixo = accions.Accions()

accio = input("Què vols fer?: ")

if accio == 'registre':
    fesAixo.registre()
    
elif accio == 'login':
    fesAixo.login()

else:
    print("Introdueix una opcio vàlida")
    
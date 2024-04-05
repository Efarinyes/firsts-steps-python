import usuaris.usuari as model
import todos.accions

class Accions:

    def registre(self):

        print("\nD'acord, procedim amb el registre")
        nom = input("Com et dius? ")
        cognoms = input("I quins son els teus cognoms? ")
        email = input("Necessitem un correu vàlid: ")
        password = input("Introdueix la teva contrassenya: ")

        usuari = model.Usuari(nom, cognoms, email, password)
        registre = usuari.registrar()

        if registre[0] >= 1:

            print('---------------------- EXIT ---------------------------------------------')
            print(f'Procedim a registrar-te, {registre[1].nom} {registre[1].cognoms } amb el correu { registre[1].email }')
            print('-------------------------------------------------------------------')
        else: 
            print('-------------------- ERROR ---------------------------')
            print("Error en el registre")
            print('-----------------------------------------------')

    def login(self):
        print("\nHauras d'introduir les teves credencials")

        try:
            email = input("Introdueix el correu: ")
            password = input("Introdueix la contrassenya: ")

            usuari = model.Usuari('', '', email, password)
            login = usuari.identificar()

            if email == login[3]:
                print('------------------ EXIT -----------------------------')
                print(f'Hola { login[1] }, Benvingut a la gestio de TODOS ')
                print('-----------------------------------------------')
                self.proximesAccions(login)
        except TypeError:
            print('-------------------- ERROR ---------------------------')
            # print(type(e))
            # print(type(e).__name__)
            print('Identificació errònea!!. Torna-ho a probar')
            print('------------------------------------------------------')

    def proximesAccions(self, usuari):

        print("""
            Aqui pots fer:
            - Nou TODO( escriu todo )
            - Llistar TODO's( escriu llistar )
            - Borrar TODO ( escriu eliminar )
            - Sortir ( escriu sortir )
        """)
        accio = input('Que vols fer? ')

        fes = todos.accions.TodoAccions()

        if accio == 'todo':
            fes.crear(usuari)
            self.proximesAccions(usuari)
        elif accio == 'llistar':
            fes.mostrar(usuari)
            self.proximesAccions(usuari)
        elif accio == 'eliminar':
            fes.borrar(usuari)
            self.proximesAccions(usuari)
        else:
            print(f'Adeu { usuari[1] }')
            exit()

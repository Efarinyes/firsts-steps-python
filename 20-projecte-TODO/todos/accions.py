
import todos.todo as model

class TodoAccions:

    def crear(self, usuari):

        print(f'\n------------------ Prfecte { usuari[1]}, creem un TODO -----------------------------')
        titol = input('Indica el nom del TODO ' )
        contingut = input('De què es tracta el TODO? ')

        todo = model.Todo( usuari[0], titol, contingut )
        guardar = todo.guardar()

        if guardar[0] >= 1:
            print('--------------------------------------------------------')
            print(f"\n TODO {todo.titol} guardat correctament, { usuari[1]}")
            print('--------------------------------------------------------')
        else:
            print('------------------------------------------------------')
            print("Upss!!. S'ha produit un error")
            print('------------------------------------------------------')

    def mostrar(self, usuari):
        print(f"\nD'acors, {usuari[1]}, llistem les teves notes: ")

        todo = model.Todo(usuari[0])

        todos = todo.llistar()
        
        for apunt in todos:
            print('--------------------------------------------------------')
            print(apunt[2])
            print(apunt[3])
            print('--------------------------------------------------------')

    def borrar(self, usuari):
        print(f"D'acord { usuari[1]}, Borrarem notes")
        titol = input("Quin titol te la nota a borrar? ")

        nota = model.Todo(usuari[0], titol)

        eliminar = nota.eliminar(titol)

        if eliminar[0] >= 1:
            print(f"Nota { nota.titol} borrada amb èxit ")
        else:
            print('No em borrat la nota. Error imprevist')


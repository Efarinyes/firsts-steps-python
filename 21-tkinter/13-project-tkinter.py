"""
Projecte:
- Una finestra de tamany fixe i no redimensionable (fet)
- Un menú d'opcions ( Inici, Afegir, Informació, Sortir)
- Diverses pantalles
- Formulari per afegir items
- Guardar el items temporalment
- Mostrar els items llistats a la pantalla principal 'Home'
- Opcio de sortir de l'aplicació
"""

from tkinter import *
from tkinter import ttk

# Definim la finestra
finestra = Tk()
#finestra.geometry('750x550')
finestra.minsize(750, 550)
finestra.title('Menus i opcions')
finestra.resizable(0,0)

# variables
products = []
name_data = StringVar()
price_data = StringVar()

def add_product():
    products.append([
        name_data.get(),
        price_data.get(),
        add_description_entry.get('1.0', 'end-1c')
    ])
    name_data.set('')
    price_data.set('')
    add_description_entry.delete('1.0', END)

    print(products)
    home()

# Camps del formulari afegir
add_frame = Frame(finestra)
add_name_label = Label(add_frame, text='Producte: ')
add_name_entry = Entry(add_frame, textvariable=name_data)
add_price_label = Label(add_frame, text='Introdueix el preu')
add_price_entry = Entry(add_frame, textvariable=price_data)
add_description_label = Label(add_frame, text='Descripció: ')
add_description_entry = Text(add_frame)
boto = Button(add_frame, text='Guardar', command=add_product)




# Definim les pantalles
def home():
    #netejar()
    # Montem la pantalla
    
    home_label.config(
        bg='gray',
        fg='white',
        font=('Courier', 30),
        padx=250,
        pady=20
    )
    home_label.grid(row=0, column=0)
    
    products_box.grid(row=1, column=0)

    # LLista de productes
    """
    Mostra llistat de productes sense 'ttk.Treeview'
    for product in products:
        if len(product) == 3:
            product.append('add')
            Label(products_box, text=product[0]).grid()
            Label(products_box, text=product[1]).grid()
            Label(products_box, text=product[2]).grid()
            Label(products_box, text='---------------------------').grid()
    """
    for product in products:
        if len(product) == 3:
            product.append('add')
            products_box.insert('', 0, text=product[0], values=(product[1]))

    # Tanquem la resta de pantalles
    add_label.grid_remove()
    add_frame.grid_remove()
    info_label.grid_remove()
    data_label.grid_remove()
    return True

def add():
    #netejar()
    
    add_label.config(
        bg='gray',
        fg='white',
        font=('Courier', 30),
        padx=280,
        pady=20
    )
    add_label.grid(row=0, column=0, columnspan=10)

    # Formulari
    add_frame.grid(row=1)
    add_name_label.grid(row=1, column=0, padx=5, pady=5, sticky=E)
    add_name_entry.grid(row=1, column=1, padx=5, pady=5, sticky=W)
    add_price_label.grid(row=2, column=0, padx=5, pady=5, sticky=E)
    add_price_entry.grid(row=2, column=1, padx=5, pady=5, sticky=W)
    add_description_label.grid(row=3, column=0, padx=5, pady=5, sticky=NE)
    add_description_entry.grid(row=3, column=1, padx=5, pady=5, sticky=W)
    add_description_entry.config(
        background='bisque',
        width=23,
        height=5,
        font=("Courier", 12),
        padx=15,
        pady=15
    )
    # Tanquem la resta de pantalles
    home_label.grid_remove()
    info_label.grid_remove()
    data_label.grid_remove()
    products_box.grid_remove()
    products_box.grid_remove()

    boto.grid(row=5, column=1, padx=5, pady=5, sticky=NW)
    boto.config(
        highlightbackground='gray', # Posem color de fons al boto ( ni 'bg', ni 'background' funcionen en Mac pel color de fons dels botons)
        fg='white',
        font=('Courier', 14),
        padx=10,
        pady=10
    )

    return True

def info():
    #netejar()
    
    info_label.config(
        bg='gray',
        fg='white',
        font=('Courier', 30),
        padx=320,
        pady=20
    )
    info_label.grid(row=0, column=0)
    data_label.grid(row=2, column=0)

    # Tanquem la resta de pantalles
    add_label.grid_remove()
    home_label.grid_remove()
    add_frame.grid_remove()
    # products_box.grid_remove()
    products_box.grid_remove()
    
    return True


# Definim els labels de les pantalles
home_label = Label(finestra, text='Pàgina Inicial')
#products_box = Frame(finestra, width=450)

products_box = ttk.Treeview(height=12, columns=3)
products_box.grid(row=1, column=0, columnspan=3)
products_box.heading('#0', text='Producte', anchor=CENTER)
products_box.heading('#1', text='Preu', anchor=CENTER)

add_label = Label(finestra, text='Afegir Item')
info_label = Label(finestra, text='Qui som?')
data_label = Label(finestra, text='Creat per Eduard Farinyes amb Tkinter | 2024')

#carreguem la pantalla inicial
home()

# Definim el Menu superior
menubar = Menu(finestra)
finestra.config(menu=menubar)

file_menu = Menu(menubar)
file_menu.add_command(
    label='Home',
    command=home
)

afegir_menu = Menu(menubar)
afegir_menu.add_command(label='Afegir', command=add)

info_menu = Menu(menubar)
info_menu.add_command(label='Qui som?', command=info)

sortir_menu = Menu(menubar)
sortir_menu.add_command(
    label='Sortir',
    command=finestra.quit
    )

menubar.add_cascade(
    label='Inici',
    menu=file_menu
    # underline=0
)
menubar.add_cascade(
    label='Afegir',
    menu=afegir_menu
)
menubar.add_cascade(
    label='Informació',
    menu=info_menu
)
menubar.add_cascade(
    label='Sortir',
    menu=sortir_menu
)

# Carreguem la finestra
finestra.mainloop()
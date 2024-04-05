from tkinter import *

finestra = Tk()
finestra.geometry('750x550')
finestra.title('Menus i opcions')

menubar = Menu(finestra)
finestra.config(menu=menubar)

file_menu = Menu(menubar)

#Opciones del desplegable 'file' 
file_menu.add_command(
    label= 'Arxiu Nou'
)
file_menu.add_command(
    label='Carpeta Nova'
)
file_menu.add_separator()
file_menu.add_command(
    label='Obrir Arxiu'
)
file_menu.add_command(
    label='Obrir Carpeta'
)
# Primer submenu
sub_menu = Menu(file_menu)
sub_menu.add_command(
    label='Vies de teclat'
)
# Submenu opciones tema
colors_menu = Menu(sub_menu)
colors_menu.add_command(
    label='Fosc'
)
colors_menu.add_command(
    label='Clar'
)
sub_menu.add_cascade(
    label='Configuració Tema',
    menu=colors_menu
)

sub_menu.add_command(
    label='Més...'
)

file_menu.add_cascade(
    label='Preferencies',
    menu=sub_menu
)

file_menu.add_separator()
file_menu.add_command(
    label='Sortir',
    command=finestra.destroy
)
#Opciones del desplegable 'Select' 
select_menu = Menu(menubar) 
select_menu.add_command(
    label='Editar Arxiu'
)
select_menu.add_command(
    label='Editar Carpeta'
)
select_menu.add_separator()
select_menu.add_command(
    label='Eliminar Arxiu'
)
select_menu.add_command(
    label='Eliminar Carpeta'
)

help_menu = Menu(menubar)
help_menu.add_command(
    label='Ajuda'
)

# Mostramos el contenido del desplegable 'File'
menubar.add_cascade(
    label='File',
    menu=file_menu,
    # underline=0
)

# Mostramos el contenido del desplegable 'Select'
menubar.add_cascade(
    label='Select',
    menu=select_menu,
    # underline=0
)

# Mostramos el contenido del desplegable 'Help'
menubar.add_cascade(
    label='Help',
    menu=help_menu,
    # underline=0
)

finestra.mainloop()


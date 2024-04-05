from tkinter import *

finestra = Tk()
finestra.title('Formularis 2')
finestra.geometry('750x550')
finestra.config(
    bg='lightgray'
)
titolForm = Label(finestra, text='Formularis 2')
titolForm.config(
    bg='gray',
    fg='white',
    font=('Courier', 22),
    pady=10,
    width=40
)
titolForm.grid( row=0, column=0, columnspan=12, sticky=N)

# Options Check

web = IntVar()
backend = IntVar()

def mostrarOpcio():
    txt = ''
    if web.get():
        txt += 'Programador Web '
    if backend.get():
        if web.get():

            txt += ' i Especialista BackEnd '
        else:
            txt += 'Especialista BackEnd '

    mostrarTria.config(
        text=txt,
        bg='gray', 
        fg='white'
        )

optionsLabel = Label(finestra, text='Tria una opció de feina: ')
optionsLabel.config(
    font=('Courier', 16),
    bg='lightgray',
    pady=5, 
    width=30
    
)
optionsLabel.grid(row=1, column=0, sticky=W)

# Opcions a triar
option1 = Checkbutton(
    finestra, 
    text='Programador Web',
    variable=web,
    onvalue=1,
    offvalue=0,
    command=mostrarOpcio
    
    )
option1.config(
    font=('Courier', 14),
    bg='lightgray',
    width=30,
    pady=5,
    padx=10
)
option1.grid(row=2, column=0, sticky=W, )

option2 = Checkbutton(
    finestra, 
    text='Especialista BackEnd',
    variable=backend,
    onvalue=1,
    offvalue=0,
    command=mostrarOpcio
    )

option2.config(
    font=('Courier', 14),
    bg='lightgray',
    width=30,
    pady=5,
    padx=10
)
option2.grid(row=3, column=0, sticky=W)

mostrarTria = Label(finestra)
mostrarTria.grid(row=4, column=0)

# Radio Check

def marcarOpcio():
    opcioMarcada.config(
        text=option.get()
    )

option = StringVar()
option.set(None)

radioLabel = Label( finestra, text='Tria una opció: ')
radioLabel.config(
    font=('Courier', 16),
    bg='lightgray',
    pady=5, 
    width=20
)
radioLabel.grid(row=5, column=0, sticky=W)

Radiobutton(finestra, text='Home',value='Home', bg='lightgray', font=('Courier', 14), variable=option, command=marcarOpcio).grid(row=6, column=0, sticky=W)
Radiobutton(finestra, text='Dona', value='Dona', bg='lightgray', font=('Courier', 14), variable=option, command=marcarOpcio).grid(row=7, column=0, sticky=W)
Radiobutton(finestra, text='Altres', value='Altres', bg='lightgray', font=('Courier', 14), variable=option, command=marcarOpcio).grid(row=8, column=0, sticky=W)

opcioMarcada = Label(finestra, bg='gray', fg='white')
opcioMarcada.config(
    font=('Courier', 20)
    
)
opcioMarcada.grid(row=9, column=0, sticky=E)

# Option Menu
def marcarDesplegable():
    opcioSeleccionada.config(
        text = opcio.get()
    )

opcio = StringVar()
opcio.set('Item1')

labelMenu = Label(finestra, text='Desplega i tria')
labelMenu.config(
    font=('Courier', 16),
    bg='lightgray',
    pady=5, 
    width=20
)
labelMenu.grid(row=10, column=0, sticky=W)

select = OptionMenu(finestra, opcio, 'Item1', 'Item2', 'Item3', 'Item4')
select.grid(row=11, column=0, sticky=W)

Button(finestra, text='Veure Opcio', command=marcarDesplegable).grid(row=11, column=1, sticky=W)

opcioSeleccionada = Label(finestra)
opcioSeleccionada.config(
    font=('Courier', 20)
)
opcioSeleccionada.grid(row=11, column=2, sticky=E)

finestra.mainloop()
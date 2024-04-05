# Tkinter: Mòdul per crear interfaces gràfiques d'usuari

from tkinter import *
import os.path
# from tkinter import ttk

class ProgramaTkinter:
    def __init__(self):
        self.title = 'Finestra amb Tkinter'
        self.icon = './img/icono.ico'
        self.icon_alt = './21-tkinter/img/icono.ico'
        self.size = '700x400'
        self.resizable = False

    def carregar(self):

        # Creem una finestra principal
        finestra = Tk()
        self.finestra = finestra
        # Variem el tamany de la finestra
        finestra.geometry(self.size)

        # Impedim la redimensió de la finestra
        if self.resizable:
            finestra.resizable(1,1)
        else:
            finestra.resizable(0,0)

        # Coloquem un favicon a la finestra NO FUNCIONA

        finestra.title(self.title)

        ruta_icone = os.path.abspath(self.icon)
        if not os.path.isfile:
            ruta_icone = os.path.abspath(self.icon_alt)

        finestra.iconbitmap(ruta_icone)

        text = Label(finestra, text=ruta_icone)
        text.pack()

        # Arrenquem i mostrem la finestra fins que l'usuari la tanqui.Aquest mètode sempre va el darrer, ja que es el que arrenvca la finestra.
        #finestra.mainloop()

    def addText(self, data):
        text = Label(self.finestra, text=data)
        text.pack()

    def mostrar(self):
        self.finestra.mainloop()

# intanciar classe

programaTkinter = ProgramaTkinter()

programaTkinter.carregar()
programaTkinter.addText('Hola soc un text')
programaTkinter.addText('I jo un altre')
programaTkinter.addText('Estem tots a una finestra')
programaTkinter.mostrar()









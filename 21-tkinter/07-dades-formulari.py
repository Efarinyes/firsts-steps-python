from tkinter import *

finestra = Tk()
finestra.geometry("600x600")
finestra.config(
    bd=20,
    
)

def getEntrada():
    resultat.set(entrada.get())
    if len(resultat.get()) >=1:
        text_recollit.config(
        bg='purple',
        fg='white'
    )


entrada = StringVar()
resultat = StringVar()

Label(finestra, text='Introdueix un text').pack(anchor=NW)
Entry(finestra, textvariable=entrada).pack(anchor=NW)

Label(finestra, text='Text entrada: ').pack(anchor=NW)
text_recollit = Label(finestra, textvariable=resultat)

text_recollit.pack(anchor=NW)
Button(finestra, text='Enviar', command=getEntrada).pack(anchor=NW)


finestra.mainloop()
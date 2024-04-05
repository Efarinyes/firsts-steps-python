
from tkinter import *

finestra = Tk()
finestra.geometry('500x450')

text = Label(finestra, text='Soc un text')
text.config(
    fg='white',
    bg='black',
    padx=90,
    pady=20,
    font=('Courier', 28)
)
text.pack()

text = Label(finestra, text="Dins d'una finestra")
text.config(
    padx=51,
    pady=5,
    bg='gray',
    height=3
)
text.pack(anchor=CENTER)

def proves(nom, cognoms, pais):
    return f'Hola { nom } { cognoms } quin temps fa per { pais }'

text = Label(finestra, text=proves(cognoms='Farinyes i Gasalla', nom='Eduard', pais='Catalunya'))
text.config(
    padx=20,
    pady=5,
    bg='pink',
    height=3,
    cursor='circle'
)
text.pack(anchor=CENTER)

finestra.mainloop()


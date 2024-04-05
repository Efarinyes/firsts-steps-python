from tkinter import *

finestra = Tk()
# finestra.geometry('700x550')


text = Label(finestra, text='Conjunt de textos')
text.config(
    fg='white',
    bg='black',
    # padx=90,
    # pady=5,
    font=('Courier', 28),
    height=3
)
text.pack( side=TOP, fill=X, expand=YES)

text = Label(finestra, text="Dins d'una finestra (1)")
text.config(
    padx=10,
    pady=20,
    bg='gray',
    height=3
)
# text.pack(anchor=SE)
text.pack(side=TOP, fill=X, expand=YES)

text = Label(finestra, text='Hola, soc un text (2)')
text.config(
    padx=10,
    pady=20,
    bg='pink',
    height=3,
    cursor='circle'
)
text.pack(side=LEFT, fill=X, expand=YES)

text = Label(finestra, text='Hola, soc un altre text (3)')
text.config(
    padx=10,
    pady=20,
    bg='orange',
    height=3,
    cursor='spider'
)
text.pack(side=LEFT)
text = Label(finestra, text='Jo també soc un text (4)')
text.config(
    padx=10,
    pady=20,
    bg='yellow',
    height=3,
    cursor='spider'
)
text.pack(side=LEFT, fill=X, expand=YES)

finestra.mainloop()

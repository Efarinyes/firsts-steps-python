from tkinter import *

finestra = Tk()

finestra.geometry('650x650')
finestra.title('Formularis amb Tkinter')

# Text capçalera formulari
titol_form = Label(finestra, text='Encapçalament del formulari')
titol_form.config(
    font=('Courier', 28),
    bg='#cfcfcf',
    padx=10,
    pady=10
)
titol_form.grid(row=0, column=0, columnspan=12, sticky=W)

# Nom del camp de text (etiquetes label)
etiqueta_primer_camp = Label(finestra, text='Nom')
etiqueta_primer_camp.config(
    font=('Courier', 20)
)
etiqueta_primer_camp.grid(row=1, column=0, sticky=W, padx=5, pady=5)

etiqueta_segon_camp = Label(finestra, text='Cognoms')
etiqueta_segon_camp.config(
    font=('Courier', 20)
)
etiqueta_segon_camp.grid(row=2, column=0, sticky=W, padx=5, pady=5)

etiqueta_tercer_camp = Label(finestra, text='Correu')
etiqueta_tercer_camp.config(
    font=('Courier', 20)
)
etiqueta_tercer_camp.grid(row=3, column=0, sticky=W, padx=5, pady=5)

etiqueta_text_comentari = Label(finestra, text='Comentaris:')
etiqueta_text_comentari.config(
    font=('Courier', 20),
    justify=LEFT
)
etiqueta_text_comentari.grid(row=4, column=0, sticky=W, padx=5, pady=5)

# Camps del formulari
primer_camp = Entry(finestra)
primer_camp.grid(row=1, column=1, sticky=W)

segon_camp = Entry(finestra)
segon_camp.grid(row=2, column=1, sticky=W)

tercer_camp = Entry(finestra)
tercer_camp.grid(row=3, column=1, sticky=W)

text_comentari = Text(finestra)
text_comentari.config(  
    width=30,
    height=5,
    bg = 'lightgray',
 )
text_comentari.grid(row=4, column=1, sticky=W)

# Botons

Label(finestra).grid(row=5, column=1, sticky="nswe" )
boto = Button(finestra, text='Enviar')
boto.config(
    
    # bg='black',
     background='green',
     fg='brown',
     padx=15,
     pady=15
 )

boto.grid(row=6, column=1, sticky=W)    

finestra.mainloop()


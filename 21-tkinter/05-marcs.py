from tkinter import *

finestra = Tk()
finestra.title('Frames amb Tkinter')
finestra.geometry('600x600')
finestra.config(
    padx=0,
    pady=0
)

marc_pare = Frame(finestra, width=175, height=175)
marc_pare.config(
    bg='white'
)
marc_pare.pack( side=BOTTOM, anchor=S, fill=X, expand=YES )

marc = Frame(marc_pare, width=185, height=185)
marc.config(
    bg='red',
    bd=4,
    relief=SOLID
)
marc.pack( side=RIGHT)
marc.pack_propagate(False)
redText = Label(marc, text='Text de la caixa vermella')
redText.config(
    bg='red',
    fg='white',
    font=('Times', 14),
    anchor=CENTER
)
redText.pack(fill=Y, expand=Y)

marc = Frame(marc_pare, width=185, height=185)
marc.config(
    bg='blue',
    bd=4,
    relief=RAISED
)
marc.pack( side=LEFT)
marc.pack_propagate(False)
baluMari = Label(marc, text='Text de la caixa blau Marí')
baluMari.config(
    bg='blue',
    fg='white',
    font=('Times', 14),
   
    anchor=CENTER
)
baluMari.pack(fill=Y, expand=Y)

marc_pare2 = Frame(finestra, width=175, height=175)
marc_pare2.config(
    bg='white'
)
marc_pare2.pack( side=TOP, anchor=N, fill=X, expand=YES )

marc = Frame(marc_pare2, width=175, height=175)
marc.config(
    bg='pink',
    bd=4,
    relief=SOLID
)
marc.pack( side=RIGHT)
marc.pack_propagate(False)
pinkText = Label(marc, text='El Text de la caixa rosa')
pinkText.config(
    bg='pink',
    fg='black',
    font=('Times', 14),
    
    anchor=CENTER
)
pinkText.pack(fill=Y, expand=Y)

marc = Frame(marc_pare2, width=175, height=175)
marc.config(
    bg='lightblue',
    bd=4,
    relief=RAISED
)
marc.pack( side=LEFT)
marc.pack_propagate(False)
blauCel = Label(marc, text='Text de la caixa blaucel')
blauCel.config(
    bg='lightblue',
    fg='black',
    font=('Times', 14),
    
    anchor=CENTER
)
blauCel.pack(fill=Y, expand=Y)


finestra.mainloop() 
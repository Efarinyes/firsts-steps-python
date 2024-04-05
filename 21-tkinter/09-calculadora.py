# Calculadora: Ha de tenir dos camps de text, quatre botons per les operacions i mostrar resultats en un Alert

from tkinter import *
from tkinter import messagebox as MessageBox

finestra = Tk()
finestra.title('Calculadora')
finestra.geometry('700x500')
finestra.config(
    pady=55
)


num1 = StringVar()
num2 = StringVar()
resultat = StringVar()

def convertirFloat(original_function):
    def wrapper_func():
        try:
            return original_function()
        except: 
            MessageBox.showinfo('Eps!!', 'Només puc operar amb números')
            num1.set('')
            num2.set('')
        
    return wrapper_func

@convertirFloat
def sumar():
    
        resultat.set(float(num1.get()) + float(num2.get()))
        mostraResultat()

@convertirFloat
def restar():
    
        resultat.set(float(num1.get()) - float(num2.get()))
        mostraResultat()

@convertirFloat
def multiplicar():
   
        resultat.set(float(num1.get()) * float(num2.get()))
        mostraResultat()

@convertirFloat
def dividir():
    
        resultat.set(float(num1.get()) / float(num2.get()))
        mostraResultat()

def mostraResultat():
    
    MessageBox.showinfo('Resultat', f'El resultat de la operacio es { resultat.get()}')
    num1.set('')
    num2.set('')

marcCalculadora = Frame(finestra, width=450, height=200)
marcCalculadora.config(
    bd=2,
    relief=SOLID,
    padx=10,
    pady=10
)
marcCalculadora.pack(side=TOP, anchor=CENTER)
marcCalculadora.propagate(False)

Label(marcCalculadora, text='Primer número: ').pack(pady=5)
Entry(marcCalculadora, textvariable=num1).pack()

Label(marcCalculadora, text='Segon número: ').pack(pady=5)
Entry(marcCalculadora, textvariable=num2).pack()

Label(finestra, text='').pack()

Button(marcCalculadora, text='Suma', command=sumar).pack(side=LEFT, fill=X, expand=YES)
Button(marcCalculadora, text='Restar', command=restar).pack(side=LEFT, fill=X, expand=YES)
Button(marcCalculadora, text='Multiplicar', command=multiplicar).pack(side=LEFT, fill=X, expand=YES)
Button(marcCalculadora, text='Dividir', command=dividir).pack(side=LEFT, fill=X, expand=YES)

finestra.mainloop()
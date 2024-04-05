# Calculadora: Ha de tenir dos camps de text, quatre botons per les operacions i mostrar resultats en un Alert

from tkinter import *
from tkinter import messagebox as MessageBox

class Calculadora:
    
    def __init__(self, alertes):

        self.num1 = StringVar()
        self.num2 = StringVar()
        self.resultat = StringVar()
        self.alertes = alertes

    def convertirFloat(self, numero):
      
            try:
                self.result = float(numero)
            except: 
                self.result = 0
                self.alertes.showinfo('Eps!!', 'Només puc operar amb números')
                self.num1.set('')
                self.num2.set('')
            return self.result

    
    def sumar(self):
        
            self.resultat.set(self.convertirFloat(self.num1.get()) + self.convertirFloat(self.num2.get()))
            self.mostraResultat()

  
    def restar(self):
        
            self.resultat.set(self.convertirFloat(self.num1.get()) - self.convertirFloat(self.num2.get()))
            self.mostraResultat()

    
    def multiplicar(self):
    
            self.resultat.set(self.convertirFloat(self.num1.get()) * self.convertirFloat(self.num2.get()))
            self.mostraResultat()

   
    def dividir(self):
        
            self.resultat.set(self.convertirFloat(self.num1.get()) / self.convertirFloat(self.num2.get()))
            self.mostraResultat()

    def mostraResultat(self):
    
        self.alertes.showinfo('Resultat', f'El resultat de la operacio es { self.resultat.get()}')
        self.num1.set('')
        self.num2.set('')

finestra = Tk()
finestra.title('Calculadora')
finestra.geometry('700x500')
finestra.config(
    pady=55
)

calculadora = Calculadora(MessageBox) 

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
Entry(marcCalculadora, textvariable=calculadora.num1).pack()

Label(marcCalculadora, text='Segon número: ').pack(pady=5)
Entry(marcCalculadora, textvariable=calculadora.num2).pack()

Label(finestra, text='').pack()

Button(marcCalculadora, text='Suma', command=calculadora.sumar).pack(side=LEFT, fill=X, expand=YES)
Button(marcCalculadora, text='Restar', command=calculadora.restar).pack(side=LEFT, fill=X, expand=YES)
Button(marcCalculadora, text='Multiplicar', command=calculadora.multiplicar).pack(side=LEFT, fill=X, expand=YES)
Button(marcCalculadora, text='Dividir', command=calculadora.dividir).pack(side=LEFT, fill=X, expand=YES)

finestra.mainloop()
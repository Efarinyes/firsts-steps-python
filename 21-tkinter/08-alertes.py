from tkinter import *
from tkinter import messagebox as MessageBox

finestra = Tk()
finestra.geometry('500x450')
finestra.title('Alertes - Tkinter')

def mostrarAlertaInfo():
    MessageBox.showinfo('Alerta!!!', 'Això es una alerta...')

def mostrarAlertaWarning():
    MessageBox.showwarning('Warning', 'Alerta de possible perill')

def mostrarAlertaError():
    MessageBox.showerror('Error', 'Alerta Error')

def sortir(nom):
    result = MessageBox.askquestion('Sortir', 'Seguir al programa?')
    if result != 'yes':
        MessageBox.showinfo('Adeu', f'Fins la propera {nom}')
        finestra.destroy()

label = Label(finestra, text='Prem els botons per veure el missatge', font=('Courier 15 bold'))
label.pack(pady=20)

Button(finestra, text='Mostra alerta INFO', command=mostrarAlertaInfo).pack()
Button(finestra, text='Mostra alerta WAR', command=mostrarAlertaWarning).pack()
Button(finestra, text='Mostrar alerta ERR', command=mostrarAlertaError).pack()
Button(finestra, text='Sortir', command= lambda:sortir('Eduard')).pack()



finestra.mainloop()


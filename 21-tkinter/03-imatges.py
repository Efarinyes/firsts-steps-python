from tkinter import *
from PIL import Image, ImageTk

finestra = Tk()
finestra.geometry('700x500')

text = Label(finestra, text='En aquesta finestra carreguem imatges')
text.config(
    fg='white',
    bg='black',
    padx=90,
    pady=20,
    font=('Times', 28)
)
text.pack()

img = Image.open('./img/Diez.Furest-4.gif')
imgnew = img.resize((250, 175))

mostra = ImageTk.PhotoImage(imgnew)
Label(finestra, image=mostra).pack()

finestra.mainloop()
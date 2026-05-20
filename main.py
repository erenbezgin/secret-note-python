from tkinter import *

FONT = ("Verdana", 10, "italic")
pencere = Tk()
pencere.title("Secret Notes")
pencere.config(padx=30, pady=30)
pencere.minsize(400, 700)

# logo
foto = PhotoImage(file=r"C:\Users\Eren\Desktop\secret-note-python\secret.png")
foto_kucuk = foto.subsample(2, 2)
fotobuton = Button(image=foto_kucuk)
fotobuton
fotobuton.pack()
# baslık
baslık = Label(text="Enter your title", font=FONT)
baslık.pack()
baslıkkutu = Entry(width=30)
baslıkkutu.pack()
baslıkkutu.focus()

# not
notuyarı = Label(text="Enter your Note", font=FONT)
notuyarı.pack()
notgir = Text(width=50, height=25)
notgir.pack()
notgir.config(padx=30, pady=30)
# sifre
sifre = Label(text="Enter Password", font=FONT)
sifre.pack()
sifrekutu = Entry(width=30)
sifrekutu.pack()
# butonlar
kayıt = Button(text="Save and Encrypt", font=FONT)
kayıt.pack()
coz = Button(text="Decrypt", font=FONT)
coz.pack()

# ayakta tut
pencere.mainloop()

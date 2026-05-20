from tkinter import *
from tkinter import messagebox
import base64


def encode(key, clear):
    enc = []
    for i in range(len(clear)):
        key_c = key[i % len(key)]
        enc_c = chr((ord(clear[i]) + ord(key_c)) % 256)
        enc.append(enc_c)
    return base64.urlsafe_b64encode("".join(enc).encode()).decode()


def decode(key, enc):
    dec = []
    enc = base64.urlsafe_b64decode(enc).decode()
    for i in range(len(enc)):
        key_c = key[i % len(key)]
        dec_c = chr((256 + ord(enc[i]) - ord(key_c)) % 256)
        dec.append(dec_c)
    return "".join(dec)


def kayıtvesifre():
    baslık = baslıkkutu.get()
    mesaj = notgir.get("1.0", END)
    sifre = sifrekutu.get()
    if len(baslık) == 0 or len(mesaj) == 0 or len(sifre) == 0:
        messagebox.showwarning(title="ERROR!!!", message="please enter all info")
    else:
        mesaj_encrypted = encode(sifre, mesaj)
        # sifreleme ve kayıt
        try:
            with open("gizli.txt", "a") as data_file:
                data_file.write(f"\n{baslık}\n{mesaj_encrypted}")
        except:
            with open("gizli.txt", "a") as data_file:
                data_file.write(f"\n{baslık}\n{mesaj_encrypted}")
        finally:
            baslıkkutu.delete(0, END)
            sifrekutu.delete(0, END)
            notgir.delete("1.0", END)


def sifrecoz():
    sifrelenmismesaj = notgir.get("1.0", END)
    sifre = sifrekutu.get()
    if len(sifrelenmismesaj) == 0 or len(sifre) == 0:
        messagebox.showwarning(title="ERROR!!!", message="please enter all info")
    else:
        try:
            cozulmus_mesaj = decode(sifre, sifrelenmismesaj)
            notgir.delete("1.0", END)
            notgir.insert("1.0", cozulmus_mesaj)
        except:
            messagebox.showwarning(
                title="ERROR!!!", message="please enter encrypted text "
            )


# font ve pencere
FONT = ("Verdana", 20, "italic")
pencere = Tk()
pencere.title("Secret Notes")
pencere.config(padx=30, pady=30)
pencere.minsize(400, 600)

# logo
foto = PhotoImage(file="secret.png")
foto_kucuk = foto.subsample(2, 2)
fotobuton = Label(image=foto_kucuk)
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
kayıt = Button(text="Save and Encrypt", font=FONT, command=kayıtvesifre)
kayıt.pack()
coz = Button(text="Decrypt", font=FONT, command=sifrecoz)
coz.pack()

# ayakta tut
pencere.mainloop()

from tkinter import *
import random
def yeniOyun():
    global a
    a = random.randint(1, 3)  # 1-2-3
    secenek.set("-")
    secenekpc.set("-")
    sonuc = Label(arayuz, text="       "*3, font="Times 15")
    sonuc.place(x=150, y=30)
    tas.config(state=NORMAL)
    kagit.config(state=NORMAL)
    makas.config(state=NORMAL)

def tasButton():
    tas.config(state=DISABLED)
    kagit.config(state=DISABLED)
    makas.config(state=DISABLED)
    secenek.set("TAŞ")
    if a==1:
        secenekpc.set("TAŞ")
        sonuc = Label(arayuz, text="Berabere", font="Times 15",fg="#363636")
        sonuc.place(x=150, y=30)
    elif a==2:
        secenekpc.set("KAĞIT")
        sonuc = Label(arayuz, text="Kaybettiniz!", font="Times 15",fg="red")
        sonuc.place(x=150, y=30)
    elif a == 3:
        secenekpc.set("MAKAS")
        sonuc = Label(arayuz, text="Kazandınız!", font="Times 15",fg="#ffa500")
        sonuc.place(x=150, y=30)

    arayuz.after(3000, yeniOyun)
def kagitButton():
    tas.config(state=DISABLED)
    kagit.config(state=DISABLED)
    makas.config(state=DISABLED)
    secenek.set("KAĞIT")
    if a==1:
        secenekpc.set("TAŞ")
        sonuc = Label(arayuz, text="Kazandınız!", font="Times 15",fg="#ffa500")
        sonuc.place(x=150, y=30)
    elif a==2:
        secenekpc.set("KAĞIT")
        sonuc = Label(arayuz, text="Berabere", font="Times 15",fg="#363636")
        sonuc.place(x=150, y=30)
    elif a == 3:
        secenekpc.set("MAKAS")
        sonuc = Label(arayuz, text="Kaybettiniz!", font="Times 15",fg="red")
        sonuc.place(x=150, y=30)

    arayuz.after(3000, yeniOyun)
def makasButton():
    tas.config(state=DISABLED)
    kagit.config(state=DISABLED)
    makas.config(state=DISABLED)
    secenek.set("MAKAS")
    if a == 1:
        secenekpc.set("TAŞ")
        sonuc = Label(arayuz, text="Kaybettiniz!", font="Times 15",fg="red")
        sonuc.place(x=150, y=30)
    elif a == 2:
        secenekpc.set("KAĞIT")
        sonuc = Label(arayuz, text="Kazandınız!", font="Times 15",fg="#ffa500")
        sonuc.place(x=150, y=30)
    elif a == 3:
        secenekpc.set("MAKAS")
        sonuc = Label(arayuz, text="Berabere", font="Times 15",fg="#363636")
        sonuc.place(x=150, y=30)

    arayuz.after(3000, yeniOyun)

arayuz = Tk()
arayuz.title("OYUN")
arayuz.geometry("400x200")
arayuz.resizable(height=FALSE, width=FALSE)

secenek = StringVar()
secenekpc = StringVar()

soru = Label(arayuz, text="Birini seçin", font="Times 15")
soru.pack()
kullaniciSecim = Label(arayuz, text="Seçimim", font="Times 15")
kullaniciSecim.place(x=30,y=30)
bilgisayarSecim = Label(arayuz, text="Bilgisayar", font="Times 15")
bilgisayarSecim.place(x=280,y=30)
seceneklabel = Label(arayuz,textvariable=secenek,font="Times 15")
seceneklabel.place(x=30,y=60)
secenekpclabel = Label(arayuz,textvariable=secenekpc,font="Times 15")
secenekpclabel.place(x=280,y=60)
sonuc = Label(arayuz, text="", font="Times 15")
sonuc.place(x=150, y=30)

tas = Button(arayuz, text="TAŞ", padx=5, pady=3,command=tasButton,activebackground="#b9d3ee",cursor="question_arrow")
tas.pack(side=LEFT,padx=50,pady=10)
kagit = Button(arayuz, text="KAĞIT", padx=5, pady=3,command=kagitButton,activebackground="#b9d3ee",cursor="question_arrow")
kagit.pack(side=LEFT,padx=25,pady=10)
makas = Button(arayuz, text="MAKAS", padx=5, pady=3,command=makasButton,activebackground="#b9d3ee",cursor="question_arrow")
makas.pack(side=LEFT,padx=50,pady=10)

yeniOyun()

mainloop()
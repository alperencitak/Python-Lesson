from tkinter import *
from tkinter import messagebox

def ekleButon():

    def listeGuncelle():
        liste.delete(0,END)
        liste.insert(END, "İSİM" + " " * 40 + "|" + " " * 14 + "NOT")
        liste.insert(END, "-"*95)
        for i in range(len(isimler)):
            sayi = 50 - len(isimler)
            liste.insert(END," " + f"{isimler[i]}" + " "*sayi + f"{notlar[i]}")

    def girisKaydet():
        kayitİsim = girisİsim.get()
        isimler.append(kayitİsim)
        kayitNot = girisNot.get()
        notlar.append(kayitNot)
        listeGuncelle()
        eklePencere.destroy()
        messagebox.showinfo("","Öğrenci Kaydedildi.")


    eklePencere = Toplevel()
    eklePencere.title("Öğrenci Ekleme")
    eklePencere.geometry("160x180+200+200")
    eklePencere.resizable(width=FALSE,height=FALSE)

    ekleİsim = Label(eklePencere,text="Öğrenci İsim",font="Times 12")
    ekleİsim.place(x=10,y=5)
    ekleNot = Label(eklePencere, text="Aldığı not", font="Times 12")
    ekleNot.place(x=10, y=50)

    girisİsim = Entry(eklePencere, width=20)
    girisİsim.place(x=10, y=30)
    girisNot = Entry(eklePencere, width=10)
    girisNot.place(x=10, y=75)

    kaydetButon = Button(eklePencere,text="KAYDET",command=girisKaydet)
    kaydetButon.place(x=50,y=120)

anaPencere = Tk()
anaPencere.title("Öğrenci Not Sistemi")
anaPencere.geometry("640x480+300+150")
anaPencere.resizable(width=FALSE,height=FALSE)

isimler=[]
notlar=[]

liste = Listbox(width=55,height=8,font="Helvatica 10",)
liste.place(x=17,y=250)

liste.insert(END, "İSİM" + " " * 40 + "|" + " " * 14 + "NOT")
liste.insert(END, "-"*95)

ekle = Button(anaPencere,text="EKLE",command=ekleButon,width=6,height=1)
ekle.place(x=25,y=200)






mainloop()

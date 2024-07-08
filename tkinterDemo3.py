from tkinter import *
from tkinter import ttk

pencere = Tk()
menu = Menu(pencere)

dosya = Menu(menu, tearoff = 0)
menu.add_cascade(label = "Dosya", menu = dosya)
dosya.add_command(label="Yeni Dosya", command= None)
dosya.add_command(label="Dosya Aç", command= None)
dosya.add_command(label="Kaydet", command= None)
dosya.add_command(label="Çıkış", command= pencere.destroy)
pencere.config(menu=menu)

deger = StringVar()
gunler = ttk.Combobox(pencere, width=20, textvariable= deger)
gunler['values'] = ('Pazartesi','Salı','Çarşamba','Perşembe','Cuma','Cumartesi','Pazar')
gunler.pack()

metin = Text(pencere, width=30, height=7)
metin.pack()

def ekle_metin(ornek_metin):
    if ornek_metin:
        metin.insert(END,ornek_metin[0])
        pencere.after(125, ekle_metin, ornek_metin[1:])

ekle_metin("        Hello Tkinter!")





pencere.mainloop()

from tkinter import messagebox
from tkinter import *

mirror = Tk()
mirror.geometry("800x600")
mirror.resizable(False, False)


# Label(mirror, text="ilk metin", bg="red").pack(fill=X,pady=5)
# Label(mirror, text="ikinci metin", bg="green").pack(fill=X,pady=5)
# Label(mirror, text="üçüncü metin", bg="blue").pack(fill=X,pady=5)

# Label(mirror, text="ilk metin", bg="red").place(x=5,y=5)
# Label(mirror, text="ikinci metin", bg="green").place(x=100,y=5)
# Label(mirror, text="üçüncü metin", bg="blue").place(x=200,y=5)

# Label(mirror, text="grid test", bg="red").grid(column=0,row=0,padx=5)
# Label(mirror, text="grid test 2", bg="green").grid(column=1,row=1,pady=10)
# Label(mirror, text="grid test 3", bg="blue").grid(column=2,row=2)

def hosgeldin():
    hgLabel.config(text=f"Hosgeldin {entry1.get()}!")


Label(mirror, text="Ad Soyad: ").grid(column=0, row=3)
entry1 = Entry(mirror)
entry1.grid(column=1, row=3, pady=10)
hgLabel = Label(mirror)
hgLabel.grid(column=4, row=3)
signInButton = Button(mirror, text="Sign In", command=hosgeldin)
signInButton.grid(column=1, row=5)

frame = Frame(mirror)
frame.grid(column=1, row=7)
frameButton = Button(frame, text="B1")
frameButton.pack()

listBox = Listbox(frame, bg="blue", fg="white", height=5, width=15)
listBox.insert(0,"Seçim 1")
listBox.insert(1,"Seçim 2")
listBox.insert(2,"Seçim 3")
listBox.insert(3,"Seçim 4")
listBox.insert(4,"Seçim 5")
listBox.pack()
listBox.delete(2)

button = Button(frame, text="show", command=messagebox.askretrycancel)
# showinfo() Kullanıcıya bilgi penceresi gösterir
# showerror() Kullanıcıya hata penceresi gösterir
# showwarning() Kullanıcıya uyarı penceresi gösterir
# askquestion() Kullanıcıya evet hayır cevabı almak için soru penceresi gösterir
# askyesno() Kullanıcıya bazı eylemler almak için evet hayır cevaplı soru sorar
# askokcancel() Kullanıcıya tamam ve iptal cevaplı soru sorar
# askretrycancel() Kullanıcıya tekrar dene ve iptal cevaplı soru sorar
button.pack()

def secim():
    secilen = f"Seçtiğiniz araç: {str(var.get())}"
    secimLabel.config(text=secilen)

var = IntVar()
r1 = Radiobutton(frame, text="radio1", variable=var, value=1, command=secim) # variable aynı olunca sadece biri seçiliyor
r2 = Radiobutton(frame, text="radio2", variable=var, value=2, command=secim)
r3 = Radiobutton(frame, text="radio3", variable=var, value=3, command=secim)
r1.pack(),r2.pack(),r3.pack()
secimLabel = Label(frame)
secimLabel.pack()

mirror.mainloop()

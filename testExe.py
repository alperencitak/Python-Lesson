from tkinter import *
from tkinter import messagebox

def Button1F():
    newwindow = Toplevel()
    newwindow.title("Destek")
    newwindow.geometry("250x100+200+210")
    newwindow.resizable(width=FALSE, height=FALSE)
    label2 = Label(newwindow,text="Sorun ne?",font="Helvetica 12 bold",fg="black")
    label2.pack(padx=0,pady=1)
    sorun_entry = (Entry(newwindow,width=25,textvariable=StringVar()))
    sorun_entry.pack(padx=1,pady=1)

    def sorunKayit():
        sorun = sorun_entry.get()
        with open("sorunlar.txt","a") as sorunDosya:
            sorunDosya.write(sorun + "\n")
        messagebox.showinfo("", "Sorun başarıyla kaydedildi.")
        newwindow.destroy()
        window.destroy()

    kaydet = Button(newwindow,text="Kaydet",padx=5,pady=3,command=sorunKayit,activebackground="green")
    kaydet.pack(padx=3,pady=2)


def Button2F():
    messagebox.showinfo("","TAMAM")
    window.destroy()


window = Tk()
window.title("Test Sürüm")
window.geometry("400x200+500+200")
window.resizable(width=FALSE, height=FALSE)

label1 = Label(window,text="Test başarılı mı?",font="Helvetica 12 bold",fg="black")
label1.pack(padx=1,pady=4)

buttonFrame = Frame(window)
buttonFrame.pack(pady=1)

evet = Button(window, text="EVET", padx=6, pady=3, command=Button2F,activebackground="blue",cursor="question_arrow")
evet.pack(side=LEFT, padx=100, pady=1)

hayir = Button(window, text="HAYIR", padx=2, pady=3, command=Button1F,activebackground="red",cursor="question_arrow")
hayir.pack(side=LEFT, padx=5, pady=1)

window.mainloop()

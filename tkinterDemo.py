from tkinter import messagebox
from tkinter import *

mirror = Tk()
mirror.title("Demo")
mirror.geometry("640x480")
mirror.resizable(False, False)


def showInfo():
    messagebox.showinfo("Information", "This is info")
    mirror.destroy()

def disabledButton2():
    button2.config(state=DISABLED)

def removeLine():
    canvas1.delete(line)

button1 = Button(
    mirror,
    text="Tıkla",
    command=showInfo,
    bg="black",
    foreground="white"
)
button2 = Button(
    mirror,
    text="2. Buton",
    state=NORMAL,
    command=disabledButton2
)
button3 = Button(
    mirror,
    text="button3",
    borderwidth=5,
    command=removeLine
)

label1 = Label(
    mirror,
    text="Tıklamalık ->"
)

canvas1 = Canvas(
    mirror,
    width=200,
    height=100,
    relief="ridge",
    borderwidth=2
)
canvas1.pack()
line = canvas1.create_line(0,0,200,100, fill="red", dash=3)
canvas1.itemconfig(line, fill="blue")
canvas1.delete(line)
line = canvas1.create_rectangle(20,30,100,90)
canvas1.delete(line)
line = canvas1.create_oval(20,30,100,90)
canvas1.delete(line)
line = canvas1.create_polygon(20,90,60,30,100,90, outline="green")
canvas1.delete(line)
# line = canvas1.create_image() # just .ppm file
line = canvas1.create_text(100,90,text="Hello GUI")
canvas1.delete(line)
bitmaps = ["error", "gray12", "gray25", "gray50", "gray75",
           "hourglass", "info", "questhead", "question", "warning"]
line = canvas1.create_bitmap(60,50,bitmap = bitmaps[6])
canvas1.delete(line)
line = canvas1.create_arc(20,20,200,200,start=0,extent=180, fill="red")

var = IntVar()

cb = Checkbutton(
    mirror,
    text="Seçim",
    variable=var
)

button1.pack(pady=20, side=LEFT, padx=160)
button2.pack(pady=20, side=LEFT, padx=60)
button3.place(x=100,y=400,width=100,height=50)
label1.place(x=80,y=230)
cb.pack()

mirror.mainloop()

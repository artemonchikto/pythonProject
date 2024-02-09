from config import*
from app import window, bg
from tkinter import Button, Frame, PhotoImage, Canvas
import os
bg.configure(file = os.path.join(BASEDIR, 'фон.png'))
mainframe = Frame(window)
mainframe.pack(fill='both', expand=True)

canvas = Canvas(mainframe,width=WIDTH, height=HEIGHT )
canvas.create_image(0, 0, image = bg, anchor = 'nw')
canvas.pack(fill='both', expand=True)

def button1click():
    from app.task1 import task1
    mainframe.destroy()
    task1()
button1 = Button(mainframe, text = 'Тело падает вниз', font = ('Courier New', 25), width=27, command = button1click)
button1.place(x = WIDTH/2-button1.winfo_reqwidth()/2, y = HEIGHT/2-button1.winfo_reqheight()*2-30)

button2 = Button(mainframe, text = 'Тело брошено вверх', font = ('Courier New', 25), width=27)
button2.place(x = WIDTH/2-button2.winfo_reqwidth()/2, y = HEIGHT/2-button2.winfo_reqheight()-10)

button3 = Button(mainframe, text = 'Тело брошено горизонтально', font = ('Courier New', 25))
button3.place(x = WIDTH/2-button3.winfo_reqwidth()/2, y = HEIGHT/2+button3.winfo_reqheight()-50)

button4 = Button(mainframe, text = 'Тело брошено под углом', font = ('Courier New', 25), width=27)
button4.place(x = WIDTH/2-button4.winfo_reqwidth()/2, y = HEIGHT/2+button4.winfo_reqheight()+35)








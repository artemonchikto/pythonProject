import pygame as p
import numpy as np
import matplotlib.pyplot as plt
from app import window, bg
from tkinter import Frame, Button, Entry, Canvas, PhotoImage, BooleanVar
from config import *
from tkinter.ttk import Combobox, Checkbutton

bg.configure(file=os.path.join(BASEDIR, 'фон1.png'))
frame1 = Frame(window)
frame1.pack(fill='both', expand=True)

canvas = Canvas(frame1, width=WIDTH, height=HEIGHT)
canvas.create_image(0, 0, image=bg, anchor='nw')
canvas.pack(fill='both', expand=True)
canvas.create_text(WIDTH / 2, 40, text='Тело брошено вертикально вверх', font=('Courier New', 30), )
canvas.create_text(WIDTH / 8, 100, text='Входные данные', font=('Courier New', 20), )
canvas.create_text(WIDTH / 8 * 5.25, 100, text='Выходные данные', font=('Courier New', 20), )

button1 = Button(frame1, text = 'Расчёт', font = ('Courier New', 20), width=8)
button1.place(x = 5, y = HEIGHT-button1.winfo_reqheight()*2-10)

button2 = Button(frame1, text='Назад', font=('Courier New', 20), width=8)
button2.place(x=5, y=HEIGHT - button2.winfo_reqheight() - 5)
canvas.create_line((0, 70), (WIDTH, 70))
canvas.create_line((WIDTH / 3, 70), (WIDTH / 3, HEIGHT))

button3 = Button(frame1, text='Показать анимацию', font=('Courier New', 20), width=18)
button3.place(x=WIDTH - button3.winfo_reqwidth() - 5, y=HEIGHT - button1.winfo_reqheight() * 2 - 10)

button4 = Button(frame1, text='Показать графики', font=('Courier New', 20), width=18)
button4.place(x=WIDTH - button4.winfo_reqwidth() - 5, y=HEIGHT - button2.winfo_reqheight() - 5)
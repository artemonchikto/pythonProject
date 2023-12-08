import pygame as p
import numpy as np
import matplotlib.pyplot as plt
from app import window
from tkinter import Frame, Button, Label, Radiobutton, Entry, Canvas, PhotoImage, BooleanVar
from config import *
from tkinter.ttk import Combobox, Checkbutton
#<a href="https://ru.freepik.com/free-photo/weathered-concrete-surface-background_15440240.htm#from_view=detail_alsolike">Изображение от rawpixel.com</a> на Freepik


bg = PhotoImage(file = os.path.join(BASEDIR, 'фон1.png'))
frame1 = Frame(window)
frame1.pack(fill='both', expand=True)

canvas = Canvas(frame1, width=WIDTH, height=HEIGHT)
canvas.create_image(0, 0, image = bg, anchor = 'nw')
canvas.pack(fill='both', expand=True)
canvas.create_text(WIDTH/2, 40, text = 'Тело падает вниз(свободное падение)', font = ('Courier New', 30),)
canvas.create_text(WIDTH/8, 100, text = 'Входные данные', font = ('Courier New', 20),)
canvas.create_text(WIDTH/8*5.25, 100, text = 'Выходные данные', font = ('Courier New', 20),)

button1 = Button(frame1, text = 'Расчёт', font = ('Courier New', 20), width=8)
button1.place(x = 5, y = HEIGHT-button1.winfo_reqheight()*2-10)

button2 = Button(frame1, text = 'Назад', font = ('Courier New', 20), width=8)
button2.place(x = 5, y = HEIGHT-button2.winfo_reqheight()-5)
canvas.create_line((0, 70), (WIDTH, 70))
canvas.create_line((WIDTH/3, 70), (WIDTH/3, HEIGHT))

button3 = Button(frame1, text = 'Показать анимацию', font = ('Courier New', 20), width=18)
button3.place(x = WIDTH-button3.winfo_reqwidth()-5, y = HEIGHT-button1.winfo_reqheight()*2-10)

button4 = Button(frame1, text = 'Показать графики', font = ('Courier New', 20), width=18)
button4.place(x = WIDTH-button4.winfo_reqwidth()-5, y = HEIGHT-button2.winfo_reqheight()-5)

input_h = Entry(frame1, width=18, font = ('Courier New', 15))
input_h.place(x = 50, y = HEIGHT/5)

canvas.create_text(32, HEIGHT/5+14, text='H=', font = ('Courier New', 20))

h_edizm = Combobox(frame1, values=['мм',  'см',  'м',  'км'], width=4, font =('Courier New', 15))
h_edizm.place(x = 270, y = HEIGHT/5)
h_edizm.current(2)

input_t = Entry(frame1, width=18, font = ('Courier New', 15))
input_t.place(x = 50, y = HEIGHT/4)

canvas.create_text(32, HEIGHT/4+14, text='t=', font = ('Courier New', 20))

t_edizm = Combobox(frame1, values=['мс',  'с',  'мин',  'ч'], width=4, font =('Courier New', 15))
t_edizm.place(x = 270, y = HEIGHT/4)
t_edizm.current(1)

input_v = Entry(frame1, width=18, font = ('Courier New', 15))
input_v.place(x = 50, y = HEIGHT/4+35)

canvas.create_text(32, HEIGHT/4+35+14, text='v=', font = ('Courier New', 20))

v_edizm = Combobox(frame1, values=['м/с',  'км/ч'], width=4, font =('Courier New', 15))
v_edizm.place(x = 270, y = HEIGHT/4+35)
v_edizm.current(0)

canvas.create_text(70, HEIGHT/3+30, text = 'Найти:', font = ('Courier New', 20))

state1 = BooleanVar()
state1.set(False)
check_h = Checkbutton(frame1, variable=state1)
check_h.place(x = 50, y = HEIGHT/3+50)
canvas.create_text(140, HEIGHT/3+60, text = 'H(Высота)', font =  ('Courier New', 18))

state2 = BooleanVar()
state2.set(False)
check_v = Checkbutton(frame1, variable=state2)
check_v.place(x = 50, y = HEIGHT/3+90)
canvas.create_text(155, HEIGHT/3+100, text = 'V(Скорость)', font =  ('Courier New', 18))

state3 = BooleanVar()
state3.set(False)
check_t = Checkbutton(frame1, variable=state3)
check_t.place(x = 50, y = HEIGHT/3+130)
canvas.create_text(135, HEIGHT/3+140, text = 'T(Время)', font =  ('Courier New', 18))

def solve():
    global h, t, v
    if state1.get():
        if input_t.get()!='':
            t = float(input_t.get())*T[t_edizm.get()]
            h = g*t**2/2
            print(h)#TODO УБРАТЬ ПОСЛЕ ТЕСТИРОВАНИЯ REMOVE DELETE
        elif input_v.get()!='':
            v = float(input_v.get())*V[v_edizm.get()]
            t = v/g
            h = g*t**2/2
            print(h, t)#TODO УБРАТЬ ПОСЛЕ ТЕСТИРОВАНИЯ REMOVE DELETE
        else:
            pass#TODO вывеcти информацию в решение
    if state3.get():
        if input_v.get()!='':
            v = float(input_v.get()) * V[v_edizm.get()]
            t = v/g
            print(t)#TODO потом надо убрать!!!!!!!!!
        elif input_h.get()!='':
            h = float(input_h.get()) * H[h_edizm.get()]
            t = (2*h/g)**0.5
            print(t)#TODO убрать позже!!!!!
        else:
            pass#TODO Вывести!
    if state2.get():
        if input_h.get()!='':
            h = float(input_h.get()) * H[h_edizm.get()]
            t = (2*h/g)**0.5
            v = g*t
            print(v)#TODO убрать позже!!!!!
        elif input_t.get()!='':
            t = float(input_t.get()) * T[t_edizm.get()]
            v = g*t
            print(v)  # TODO убрать позже!!!!!
        else:
            pass#todo !
button1.config(command = solve)

def graph():#построение графика
    global t, v, h
    N = round(t/0.1)
    t_array = np.linspace(0, t, N)
    v_array = g*t_array
    h_array = h-g*t_array**2/2
    if state2.get():
        plt.figure(1)
        plt.plot(t_array, v_array)
        plt.xlabel('t(время), с')
        plt.ylabel('v(скорость), м/с')
        plt.grid(True)
    if state1.get():
        plt.figure(2)
        plt.plot(t_array, h_array)
        plt.xlabel('t(время), с')
        plt.ylabel('h(высота), м')
        plt.grid(True)
    plt.show()
button4.config(command=graph)

def animation():#Построение анимации
    global t, v, h
    p.init()
    display = p.display.set_mode((WIDTH, HEIGHT))
    clock =p.time.Clock()
    p.display.set_caption('Тело падает вниз')
    run = True
    bg = p.image.load(os.path.join(BASEDIR, 'фон-для-анимации.png'))
    rect_bg = bg.get_rect()
    xlabel = p.Rect(150, HEIGHT-50, 800, 4)
    ylabel = p.Rect(150, HEIGHT-650-50, 4, 650)
    ball = p.sprite.Sprite()
    ball.image = p.image.load(os.path.join(BASEDIR, 'шар.png'))
    ball.image = p.transform.scale(ball.image, (30, 30))
    ball.rect = ball.image.get_rect()
    ball.rect.centerx = 150+800/2
    all_sprites = p.sprite.Group()
    m = 650/20000
    ball.rect.centery = HEIGHT-h*m-50
    mt = 1/60
    ball.t = 0
    ball.v = 0
    def falling():
        ball.t+=mt
        ball.v = g*ball.t*m
        ball.rect.centery = g*ball.t**2/2
        if ball.rect.bottom>HEIGHT-50:
            ball.rect.bottom = HEIGHT-50
    ball.update=falling
    all_sprites.add(ball)
    while run:
        clock.tick(FPS)
        #обработка событий
        for event in p.event.get():
            if event.type == p.QUIT:
                run = False
        #Изменение положения падающего тела
        all_sprites.update()
        #визуализация, отрисовка, рендеринг и тд и тп
        display.fill((0, 0, 0))
        display.blit(bg, rect_bg)
        p.draw.rect(display, (0, 0, 0), xlabel)
        p.draw.rect(display, (0, 0, 0), ylabel)
        all_sprites.draw(display)
        p.display.update()

    p.quit()
button3.config(command = animation)














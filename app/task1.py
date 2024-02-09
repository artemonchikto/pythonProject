import pygame as p
import numpy as np
import matplotlib.pyplot as plt
from app import window, bg
from tkinter import Frame, Button, Entry, Canvas, PhotoImage, BooleanVar
from config import *
from tkinter.ttk import Combobox, Checkbutton
def task1():

    bg.configure(file = os.path.join(BASEDIR, 'фон1.png'))
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

    def backmenu():
        frame1.destroy()
        bg.configure(file=os.path.join(BASEDIR, 'фон.png'))
        mainframe = Frame(window)
        mainframe.pack(fill='both', expand=True)

        canvas = Canvas(mainframe, width=WIDTH, height=HEIGHT)
        canvas.create_image(0, 0, image=bg, anchor='nw')
        canvas.pack(fill='both', expand=True)

        def button1click():
            mainframe.destroy()
            task1()

        button1 = Button(mainframe, text='Тело падает вниз', font=('Courier New', 25), width=27, command=button1click)
        button1.place(x=WIDTH / 2 - button1.winfo_reqwidth() / 2, y=HEIGHT / 2 - button1.winfo_reqheight() * 2 - 30)

        button2 = Button(mainframe, text='Тело брошено вверх', font=('Courier New', 25), width=27)
        button2.place(x=WIDTH / 2 - button2.winfo_reqwidth() / 2, y=HEIGHT / 2 - button2.winfo_reqheight() - 10)

        button3 = Button(mainframe, text='Тело брошено горизонтально', font=('Courier New', 25))
        button3.place(x=WIDTH / 2 - button3.winfo_reqwidth() / 2, y=HEIGHT / 2 + button3.winfo_reqheight() - 50)

        button4 = Button(mainframe, text='Тело брошено под углом', font=('Courier New', 25), width=27)
        button4.place(x=WIDTH / 2 - button4.winfo_reqwidth() / 2, y=HEIGHT / 2 + button4.winfo_reqheight() + 35)

    button2 = Button(frame1, text = 'Назад', font = ('Courier New', 20), width=8, command=backmenu)
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

    canvas2 = Canvas(frame1, width=690, height=450, highlightthickness = 0)
    bg2 = PhotoImage(file = os.path.join(BASEDIR, 'фон3_0.png'))
    grafik = PhotoImage(file = os.path.join(BASEDIR, 'фон3.png'))
    canvas2.create_image(0, 0, image = bg2, anchor = 'nw')
    canvas2.create_image(500, 0, image = grafik, anchor = 'nw')
    canvas2.place(x = 370, y = 130)

    def solve():
        canvas2.delete('all')
        canvas2.create_image(0, 0, image=bg2, anchor='nw')
        canvas2.create_image(500, 0, image=grafik, anchor='nw')
        global h, t, v
        h, t, v = 0, 0, 0
        a = '1234567890.'
        if set(input_t.get())-set(a):
            canvas2.create_text(5, 12, text = 'Ошибка в поле ввода t', font = ('Courier New', 24), anchor='nw', fill = 'red')
        elif set(input_h.get())-set(a):
            canvas2.create_text(5, 12, text = 'Ошибка в поле ввода h', font = ('Courier New', 24), anchor='nw', fill = 'red')
        elif set(input_v.get())-set(a):
            canvas2.create_text(5, 12, text = 'Ошибка в поле ввода v', font = ('Courier New', 24), anchor='nw', fill = 'red')
        else:

            if state1.get() and input_h.get() == '':
                if input_t.get()!='':
                    t = float(input_t.get())*T[t_edizm.get()]
                    h = g*t**2/2
                    text = f'''Решение:
    Sу=Vоу*t+ay*t^2/2; Voy = 0; 
    ay = -g; Sy = -h
    h = g*t^2/2
    h = {g}*{t}^2/2 = {round(h, 2)} м
                    '''
                    canvas2.create_text(5, 10, text = text, font = ('Courier New', 20), anchor='nw')
                elif input_v.get()!='':
                    v = float(input_v.get())*V[v_edizm.get()]
                    t = v/g
                    h = g*t**2/2
                    text = f'''Решение:
    Vу=Voу+ay*t; Vy = -V;
    Voy = 0; ay = -g; 
    V = g*t => t = V/g
    t = {v}/{g} = {round(t, 2)} c
    Sу=Vоу*t+ay*t^2/2; Sy = -h
    h = g*t^2/2
    h = {g}*{t}^2/2 = {round(h, 2)} м
    '''
                    canvas2.create_text(5, 10, text = text, font = ('Courier New', 20), anchor='nw')
                else:
                    canvas2.create_text(5, 10, text = 'Недостаточно данных', font = ('Courier New', 24), anchor='nw', fill = 'red')
            if state3.get():
                if input_v.get()!='':
                    v = float(input_v.get()) * V[v_edizm.get()]
                    if t ==0:
                        t = v / g
                        text = f'''Решение:
    Vу=Voу+ay*t; Vy = -V;
    Voy = 0; ay = -g; 
    V = g*t => t = V/g
    t = {v}/{g} = {round(t, 2)} c'''
                        canvas2.create_text(5, 10, text = text, font = ('Courier New', 20), anchor='nw')
                elif input_h.get()!='':
                    h = float(input_h.get()) * H[h_edizm.get()]
                    if t ==0:
                        t = (2 * h / g) ** 0.5
                        text = f'''Решение:
    Sу=Vоу*t+ay*t^2/2; Voy = 0; 
    ay = -g; Sy = -h
    h = g*t^2/2
    t = √(2*h/g)
    t = √(2*{h}/{g}) = {round(t, 2)} c'''
                        canvas2.create_text(5, 10, text = text, font = ('Courier New', 20), anchor='nw')
                else:
                    canvas2.create_text(5, 10, text='Недостаточно данных', font=('Courier New', 24), anchor='nw', fill='red')
            if state2.get():
                if input_h.get()!='':
                    h = float(input_h.get()) * H[h_edizm.get()]
                    if t == 0 and v == 0:
                        t = (2 * h / g) ** 0.5
                        v = g * t
                        text = f'''Решение:
    Sу=Vоу*t+ay*t^2/2; Voy = 0; 
    ay = -g; Sy = -h;
    h = g*t^2/2;
    t = √(2*h/g);
    t = √(2*{h}/{g}) = {round(t, 2)} c
    Vу=Voу+ay*t; Vy = -V;
    Voy = 0; ay = -g; 
    V = g*t;
    v = {g}*{t} = {round(v)} м/с'''
                        canvas2.create_text(5, 10, text = text, font = ('Courier New', 20), anchor='nw')
                    elif v ==0:
                        v = g * t
                        text = f'''
    Vу=Voу+ay*t; Vy = -V;
    Voy = 0; ay = -g; 
    V = g*t;
    v = {g}*{t} = {round(v)} м/с   '''
                        canvas2.create_text(5, 155, text=text, font=('Courier New', 20), anchor='nw')
                elif input_t.get()!='':
                    t = float(input_t.get()) * T[t_edizm.get()]
                    if v==0 and not state1.get():
                        v = g * t
                        text = f'''Решение:
    Vу=Voу+ay*t; Vy = -V;
    Voy = 0; ay = -g; 
    V = g*t
    v = {g}*{t} = {round(v)} м/с'''
                        canvas2.create_text(5, 10, text=text, font=('Courier New', 20), anchor='nw')
                    elif v ==0:
                        v = g * t
                        text = f'''
    Vу=Voу+ay*t; Vy = -V;
    Voy = 0; ay = -g; 
    V = g*t
    v = {g}*{t} = {round(v)} м/с'''
                        canvas2.create_text(5, 150, text=text, font=('Courier New', 20), anchor='nw')
                else:
                    canvas2.create_text(5, 10, text='Недостаточно данных', font=('Courier New', 24), anchor='nw', fill='red')
    button1.config(command = solve)

    def graph():#построение графика
        global t, v, h
        solve()
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
        solve()
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
        ball.rect.centery = HEIGHT-650-50
        ball.flag = False
        mt = 1/60
        ball.t = 0
        ball.v = 0
        def draw_arrow(surface, start, length):
            end = (start[0], start[1]+length)
            p.draw.line(surface, (0, 0, 0), start, end, 2)
            p.draw.polygon(surface,(0, 0, 0), (end,
                           (end[0]+5, end[1]),
                           (end[0], end[1]+5),
                           (end[0]-5,end[1]),
                           end))
        def falling():
            if ball.flag:
                ball.t+=mt
                ball.v = g*ball.t
                ball.rect.centery = HEIGHT-650 + g*ball.t**2/2 -50


                if ball.rect.bottom>HEIGHT-50:
                    ball.rect.bottom = HEIGHT-50
                    ball.flag=False
        ball.update=falling
        all_sprites.add(ball)
        play_button = p.sprite.Sprite()
        play_button.image = p.image.load(os.path.join(BASEDIR, 'кнопка запуска анимации.png'))
        play_button.image = p.transform.scale(play_button.image, (80, 80))
        play_button.rect = play_button.image.get_rect()
        play_button.rect.centerx = WIDTH-90
        play_button.rect.centery = HEIGHT - 80
        all_sprites.add(play_button)
        while run:
            clock.tick(FPS)
            #обработка событий
            for event in p.event.get():
                if event.type == p.MOUSEBUTTONUP:
                    if event.button == 1:
                        if play_button.rect.left<=event.pos[0]<=play_button.rect.right and play_button.rect.top<=event.pos[1]<=play_button.rect.bottom:
                            ball.t = 0
                            ball.v = 0
                            ball.rect.centerx = 150 + 800 / 2
                            ball.rect.centery = HEIGHT - 650 - 50
                            ball.flag = True
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
            draw_arrow(display, ball.rect.center, ball.v / (2 * 640 / g) ** 0.5/g * 50)
            p.display.update()


        p.quit()
    button3.config(command = animation)














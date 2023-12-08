import os
BASEDIR = os.path.abspath(os.path.dirname(__file__))
HEIGHT = 720
WIDTH = 1080
NAME = 'Расчет задач по кинематике'
g = 9.81
H = {
    'км':1000,
    'м':1,
    'см':0.01,
    'мм':0.001
}

V = {
    'м/с':1,
    'км/ч':1000/3600
}

T = {
    'ч':3600,
    'мин':60,
    'с':1,
    'мс':0.001
}

h = 0
v = 0
t = 0

FPS = 100
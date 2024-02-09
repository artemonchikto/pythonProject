from tkinter import Tk, PhotoImage
from config import*

window = Tk()
window.geometry(f'{WIDTH}x{HEIGHT}')
window.title(NAME)
window.resizable(False, False)
bg = PhotoImage(file = os.path.join(BASEDIR, 'фон.png'))

from app import task2



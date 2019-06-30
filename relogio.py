from time import strftime
from tkinter import Label


def tempo():
    clock['text'] = strftime('%H:%M:%S')
    clock.after(100, tempo)  # passando a propria funcao para ser executada novamente apos 100 milissegundos
    return tempo


clock = Label()
clock['text'] = strftime('%H:%M:%S')
clock['font'] = 'Helvetica 24 bold'
clock.pack()
tempo()
clock.mainloop()

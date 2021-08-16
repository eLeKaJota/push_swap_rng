from tkinter import *
from tkinter import scrolledtext
import random


def random_gen():
    i = 0
    txt_res.delete('1.0', END)
    while i < int(in_cantidad.get()):
        res = random.randint(int(in_desde.get()), int(in_hasta.get()))
        txt_res.insert(INSERT, res)
        txt_res.insert(INSERT, " ")
        i += 1


if __name__ == '__main__':
    window = Tk()
    window.title("Random")
    txt_cantidad = Label(window, text="Cantidad de números: ")
    in_cantidad = Entry(window)
    txt_desde = Label(window, text="Desde: ")
    in_desde = Entry(window)
    txt_hasta = Label(window, text="Hasta: ")
    in_hasta = Entry(window)
    btn_gen = Button(window, text="Generar", width=30, command=random_gen)
    txt_res = scrolledtext.ScrolledText(window, width=40, height=10)
    txt_cantidad.grid(column=0, row=0, pady=5)
    txt_desde.grid(column=0, row=1, pady=5)
    txt_hasta.grid(column=0, row=2, pady=5)
    in_cantidad.grid(column=1, row=0, padx=5)
    in_desde.grid(column=1, row=1, padx=5)
    in_hasta.grid(column=1, row=2, padx=5)
    btn_gen.grid(column=0, row=3, columnspan=2, padx=10, pady=10)
    txt_res.grid(column=0, row=4, columnspan=2, padx=10, pady=10)
    window.mainloop()


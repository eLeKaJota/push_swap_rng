from tkinter import *
from tkinter import scrolledtext
import random


def random_gen():
    i = 0
    txt_res.delete('1.0', END)
    numbers = []
    n_cant = int(in_cantidad.get())
    while i < n_cant:
        repe = False
        res = random.randint(int(in_desde.get()), int(in_hasta.get()))
        for e in numbers:
            if e == res:
                n_cant += 1
                repe = True
        if not repe:
            numbers.append(res)
        i += 1
    if chk_arg_state.get():
        txt_res.insert(INSERT, 'ARG="')
        for k, e in enumerate(numbers):
            txt_res.insert(INSERT, e)
            if k != len(numbers) - 1:
                txt_res.insert(INSERT, " ")
        txt_res.insert(INSERT, '"; ')
    if chk_push_state.get():
        txt_res.insert(INSERT, "./push_swap ")
        if chk_arg_state.get():
            txt_res.insert(INSERT, "$ARG")
        else:
            for k, e in enumerate(numbers):
                txt_res.insert(INSERT, e)
                if k != len(numbers) - 1:
                    txt_res.insert(INSERT, " ")
    else:
        for k, e in enumerate(numbers):
            txt_res.insert(INSERT, e)
            if k != len(numbers) - 1:
                txt_res.insert(INSERT, " ")
    if chk_checker_state.get():
        txt_res.insert(INSERT, " | ./checker_Mac ")
        if chk_arg_state.get():
            txt_res.insert(INSERT, "$ARG")
        else:
            for k, e in enumerate(numbers):
                txt_res.insert(INSERT, e)
                if k != len(numbers) - 1:
                    txt_res.insert(INSERT, " ")
    if chk_wc_state.get():
        txt_res.insert(INSERT, " | wc -l")


def copy_gen():
    window.clipboard_clear()
    window.clipboard_append(txt_res.get("1.0", END))


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
    chk_push_state = BooleanVar()
    chk_push_state.set(True)
    chk_push = Checkbutton(window, text="./push_swap", var=chk_push_state)
    chk_checker_state = BooleanVar()
    chk_checker_state.set(False)
    chk_checker = Checkbutton(window, text="| ./checker_Mac", var=chk_checker_state)
    chk_arg_state = BooleanVar()
    chk_arg_state.set(False)
    chk_arg = Checkbutton(window, text='$ARG=""', var=chk_arg_state)
    chk_wc_state = BooleanVar()
    chk_wc_state.set(False)
    chk_wc = Checkbutton(window, text='| wc -l', var=chk_wc_state)
    btn_copy = Button(window, text="Copiar", width=30, command=copy_gen)
    txt_cantidad.grid(column=0, row=0, pady=5, sticky=W)
    txt_desde.grid(column=0, row=1, pady=5, sticky=W)
    txt_hasta.grid(column=0, row=2, pady=5, sticky=W)
    in_cantidad.grid(column=1, row=0, padx=5, columnspan=2, sticky=W)
    in_desde.grid(column=1, row=1, padx=5, columnspan=2, sticky=W)
    in_hasta.grid(column=1, row=2, padx=5, columnspan=2, sticky=W)
    chk_push.grid(column=0, row=3, sticky=W)
    chk_checker.grid(column=1, row=3, sticky=W)
    chk_arg.grid(column=2, row=3, padx=5, sticky=W)
    chk_wc.grid(column=0, row=4, sticky=W)
    btn_gen.grid(column=0, row=5, columnspan=3, padx=10, pady=10)
    txt_res.grid(column=0, row=6, columnspan=3, padx=10, pady=10)
    btn_copy.grid(column=0, row=7, columnspan=3, padx=10, pady=10)
    window.mainloop()


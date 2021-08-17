from tkinter import *
from tkinter import scrolledtext
import random

def is_integer(n):
    try:
        float(n)
    except ValueError:
        return False
    else:
        return float(n).is_integer()

def error():
    txt_res.delete('1.0', END)
    if not is_integer(in_cantidad.get()):
        txt_res.insert(INSERT, '"Cantidad de números" no es un entero')
        return True
    if not is_integer(in_desde.get()):
        txt_res.insert(INSERT, '"Desde" no es un entero')
        return True
    if not is_integer(in_hasta.get()):
        txt_res.insert(INSERT, '"Hasta" no es un entero')
        return True
    if int(in_desde.get()) > int(in_hasta.get()):
        txt_res.insert(INSERT, '"Desde" debe ser menor que "Hasta"')
        return True
    if int(in_hasta.get()) - int(in_desde.get()) < int(in_cantidad.get()):
        txt_res.insert(INSERT, 'El rango de los números ("Desde" y "Hasta") debe ser mayor que la cantidad de números')
        return True
    return False

def random_gen():
    if error():
        return
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
        if not chk_arg_state.get() and not chk_checker_state.get() and not chk_wc_state.get():
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
    window.title("Push_Swap RnG")
    window.resizable(False, False)
    txt_cantidad = Label(window, text="Cantidad de números: ")
    in_cantidad = Entry(window, width=40)
    txt_desde = Label(window, text="Desde: ")
    in_desde = Entry(window, width=40)
    txt_hasta = Label(window, text="Hasta: ")
    in_hasta = Entry(window, width=40)
    btn_gen = Button(window, text="Generar", width=50, command=random_gen)
    txt_res = scrolledtext.ScrolledText(window, width=55, height=10)
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
    btn_copy = Button(window, text="Copiar", width=35, command=copy_gen)
    txt_cantidad.grid(column=0, row=0, pady=10, sticky=W, padx=5)
    txt_desde.grid(column=0, row=1, pady=10, sticky=W, padx=5)
    txt_hasta.grid(column=0, row=2, pady=10, sticky=W, padx=5)
    in_cantidad.grid(column=1, row=0, padx=5, columnspan=3)
    in_desde.grid(column=1, row=1, padx=5, columnspan=3)
    in_hasta.grid(column=1, row=2, padx=5, columnspan=3)
    chk_push.grid(column=0, row=3, sticky=W, pady=10)
    chk_checker.grid(column=1, row=3, sticky=W)
    chk_arg.grid(column=2, row=3, sticky=W)
    chk_wc.grid(column=3, row=3, sticky=W, padx=10)
    btn_gen.grid(column=0, row=4, columnspan=4, padx=10, pady=5)
    txt_res.grid(column=0, row=5, columnspan=4, padx=10, pady=5)
    btn_copy.grid(column=0, row=6, columnspan=4, padx=10, pady=5)
    window.mainloop()


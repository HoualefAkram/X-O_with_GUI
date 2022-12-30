from tkinter import *
from tkinter import messagebox
from time import sleep

window = Tk()
current_button = IntVar()
XO = IntVar()
frame = Frame(master=window)
frame.pack()
v0, v1, v2, v3, v4, v5, v6, v7, v8 = 0, 0, 0, 0, 0, 0, 0, 0, 0
t = ["", "", "", "", "", "", "", "", ""]
rounds = 0
p1, p2 = "", ""


def end_game():
    global rounds, t, p1, p2
    if rounds % 2 == 0:
        l = Label(master=window, text="Player 2 WON!", fg="red", font=("Ink Free", 20, "bold"))
        l.pack()
        window.update()
        sleep(2)
        t = ["", "", "", "", "", "", "", "", ""]
        p1, p2 = "", ""
        make_buttons(0, 0, 0, 0, 0, 0, 0, 0, 0)
        rounds = 0
        l.destroy()

    else:
        l = Label(master=window, text="Player 1 WON!", fg="red", font=("Ink Free", 20, "bold"))
        l.pack()
        window.update()
        sleep(2)
        t = ["", "", "", "", "", "", "", "", ""]
        p1, p2 = "", ""
        make_buttons(0, 0, 0, 0, 0, 0, 0, 0, 0)
        rounds = 0
        l.destroy()


def someone_won():
    for i, j, k in zip(range(0, 7, 3), range(1, 8, 3), range(2, 9, 3)):
        if t[i] == t[j] == t[k] == "X" or t[i] == t[j] == t[k] == "O":
            return True
    for l, m, n in zip(range(0, 3), range(3, 6), range(6, 9)):
        if t[l] == t[m] == t[n] == "X" or t[l] == t[m] == t[n] == "O":
            return True
    if t[0] == t[4] == t[8] == "X" or t[0] == t[4] == t[8] == "O" or t[2] == t[4] == t[6] == "X" or t[2] == t[4] == t[
        6] == "O":
        return True


def check_game():
    global rounds, t, p1, p2
    for i, j, k in zip(range(0, 7, 3), range(1, 8, 3), range(2, 9, 3)):
        if t[i] == t[j] == t[k] == "X" or t[i] == t[j] == t[k] == "O":
            end_game()
    for l, m, n in zip(range(0, 3), range(3, 6), range(6, 9)):
        if t[l] == t[m] == t[n] == "X" or t[l] == t[m] == t[n] == "O":
            end_game()
    if t[0] == t[4] == t[8] == "X" or t[0] == t[4] == t[8] == "O" or t[2] == t[4] == t[6] == "X" or t[2] == t[4] == t[
        6] == "O":
        end_game()
    if rounds == 9 and not someone_won():
        l = Label(master=window, text="Draw!", fg="red", font=("Ink Free", 20, "bold"))
        l.pack()
        window.update()
        sleep(2)
        t = ["", "", "", "", "", "", "", "", ""]
        p1, p2 = "", ""
        make_buttons(0, 0, 0, 0, 0, 0, 0, 0, 0)
        rounds = 0
        l.destroy()


def f0():
    global v0, v1, v2, v3, v4, v5, v6, v7, v8
    v0, v1, v2, v3, v4, v5, v6, v7, v8 = 1, 0, 0, 0, 0, 0, 0, 0, 0
    make_buttons(1, 0, 0, 0, 0, 0, 0, 0, 0)


def f1():
    global v0, v1, v2, v3, v4, v5, v6, v7, v8
    v0, v1, v2, v3, v4, v5, v6, v7, v8 = 0, 1, 0, 0, 0, 0, 0, 0, 0
    make_buttons(0, 1, 0, 0, 0, 0, 0, 0, 0)


def f2():
    global v0, v1, v2, v3, v4, v5, v6, v7, v8
    v0, v1, v2, v3, v4, v5, v6, v7, v8 = 0, 0, 1, 0, 0, 0, 0, 0, 0
    make_buttons(0, 0, 1, 0, 0, 0, 0, 0, 0)


def f3():
    global v0, v1, v2, v3, v4, v5, v6, v7, v8
    v0, v1, v2, v3, v4, v5, v6, v7, v8 = 0, 0, 0, 1, 0, 0, 0, 0, 0
    make_buttons(0, 0, 0, 1, 0, 0, 0, 0, 0)


def f4():
    global v0, v1, v2, v3, v4, v5, v6, v7, v8
    v0, v1, v2, v3, v4, v5, v6, v7, v8 = 0, 0, 0, 0, 1, 0, 0, 0, 0
    make_buttons(0, 0, 0, 0, 1, 0, 0, 0, 0)


def f5():
    global v0, v1, v2, v3, v4, v5, v6, v7, v8
    v0, v1, v2, v3, v4, v5, v6, v7, v8 = 0, 0, 0, 0, 0, 1, 0, 0, 0
    make_buttons(0, 0, 0, 0, 0, 1, 0, 0, 0)


def f6():
    global v0, v1, v2, v3, v4, v5, v6, v7, v8
    v0, v1, v2, v3, v4, v5, v6, v7, v8 = 0, 0, 0, 0, 0, 0, 1, 0, 0
    make_buttons(0, 0, 0, 0, 0, 0, 1, 0, 0)


def f7():
    global v0, v1, v2, v3, v4, v5, v6, v7, v8
    v0, v1, v2, v3, v4, v5, v6, v7, v8 = 0, 0, 0, 0, 0, 0, 0, 1, 0
    make_buttons(0, 0, 0, 0, 0, 0, 0, 1, 0)


def f8():
    global v0, v1, v2, v3, v4, v5, v6, v7, v8
    v0, v1, v2, v3, v4, v5, v6, v7, v8 = 0, 0, 0, 0, 0, 0, 0, 0, 1
    make_buttons(0, 0, 0, 0, 0, 0, 0, 0, 1)


def insert_x():
    counter = 0
    global v0, v1, v2, v3, v4, v5, v6, v7, v8, rounds, p1, p2
    rounds += 1
    if rounds % 2 == 0:
        if p1 == "x":
            messagebox.showerror(title="Error!", message="Not Your Sign!")
            rounds -= 1
            return
    if rounds % 2 != 0:
        if p2 == "x":
            messagebox.showerror(title="Error!", message="Not Your Sign!")
            rounds -= 1
            return
    for i in [v0, v1, v2, v3, v4, v5, v6, v7, v8]:
        if i == 1:
            if t[counter] != '':
                messagebox.showerror(title="Error", message="Already Used!")
                rounds -= 1
                return
            t[counter] = "X"
        counter += 1
    make_buttons(0, 0, 0, 0, 0, 0, 0, 0, 0)
    if rounds == 1:
        p1 = "x"
        p2 = "o"
    check_game()


def insert_o():
    counter = 0
    global v0, v1, v2, v3, v4, v5, v6, v7, v8, rounds, p1, p2
    rounds += 1
    if rounds % 2 == 0:
        if p1 == "o":
            messagebox.showerror(title="Error!", message="Not Your Sign!")
            rounds -= 1
            return
    if rounds % 2 != 0:
        if p2 == "o":
            messagebox.showerror(title="Error!", message="Not Your Sign!")
            rounds -= 1
            return
    for i in [v0, v1, v2, v3, v4, v5, v6, v7, v8]:
        if i == 1:
            if t[counter] != '':
                messagebox.showerror(title="Error", message="Already Used!")
                rounds -= 1
                return
            t[counter] = "O"
        counter += 1
    make_buttons(0, 0, 0, 0, 0, 0, 0, 0, 0)
    if rounds == 1:
        p1 = "o"
        p2 = "x"
    check_game()


def make_buttons(c1, c2, c3, c4, c5, c6, c7, c8, c9):
    global b1, b2, b3, b4, b5, b6, b7, b8, b9  # NOQA
    c1 = "white" if c1 == 0 else 'light grey'
    c2 = "white" if c2 == 0 else 'light grey'
    c3 = "white" if c3 == 0 else 'light grey'
    c4 = "white" if c4 == 0 else 'light grey'
    c5 = "white" if c5 == 0 else 'light grey'
    c6 = "white" if c6 == 0 else 'light grey'
    c7 = "white" if c7 == 0 else 'light grey'
    c8 = "white" if c8 == 0 else 'light grey'
    c9 = "white" if c9 == 0 else 'light grey'
    b1 = Button(master=frame, width=10, height=5, text=t[0], command=f0, bg=c1).grid(row=0, column=0)  # NOQA
    b2 = Button(master=frame, width=10, height=5, text=t[1], command=f1, bg=c2).grid(row=0, column=1)  # NOQA
    b3 = Button(master=frame, width=10, height=5, text=t[2], command=f2, bg=c3).grid(row=0, column=2)  # NOQA
    b4 = Button(master=frame, width=10, height=5, text=t[3], command=f3, bg=c4).grid(row=1, column=0)  # NOQA
    b5 = Button(master=frame, width=10, height=5, text=t[4], command=f4, bg=c5).grid(row=1, column=1)  # NOQA
    b6 = Button(master=frame, width=10, height=5, text=t[5], command=f5, bg=c6).grid(row=1, column=2)  # NOQA
    b7 = Button(master=frame, width=10, height=5, text=t[6], command=f6, bg=c7).grid(row=2, column=0)  # NOQA
    b8 = Button(master=frame, width=10, height=5, text=t[7], command=f7, bg=c8).grid(row=2, column=1)  # NOQA
    b9 = Button(master=frame, width=10, height=5, text=t[8], command=f8, bg=c9).grid(row=2, column=2)  # NOQA


make_buttons(0, 0, 0, 0, 0, 0, 0, 0, 0)
frame.config(bg="grey")
label1 = Label(master=frame, width=10, height=5, bg="grey").grid(row=0, column=3)  # NOQA
label2 = Label(master=frame, width=10, height=5, bg="grey").grid(row=2, column=3)  # NOQA
label3 = Label(master=frame, width=10, height=5, bg="grey").grid(row=1, column=3)  # NOQA
label4 = Label(master=frame, width=10, height=5, bg="grey").grid(row=1, column=4)  # NOQA
bx = Button(master=frame, text='X', font=("Ariel", 9, "bold"), width=10, height=5, command=insert_x).grid(row=0,  # NOQA
                                                                                                          column=4)
bo = Button(master=frame, text='O', font=("Ariel", 9, "bold"), width=10, height=5, command=insert_o).grid(row=2,  # NOQA
                                                                                                          column=4)
window.mainloop()

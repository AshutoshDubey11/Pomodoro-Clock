from tkinter import *
from tkinter import messagebox
import math

PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
m = 0


def res():
    global m
    m += 1
    if m % 8 == 0:
        countdown(LONG_BREAK_MIN*60)
        label1.config(text="Break", foreground=RED)
        messagebox.showinfo(title="Break", message="You can take a 20 min break now.")
    elif m % 2 == 0:
        countdown(SHORT_BREAK_MIN*60)
        label1.config(text="Break", foreground=PINK)
        messagebox.showinfo(title="Break", message="You can take a 5 min break now.")
    else:
        countdown(WORK_MIN*60)
        label1.config(text="Work", foreground=GREEN)
        messagebox.showinfo(title="Work", message="Hurry Up. Start working.")


def countdown(count):

    count_min = math.floor(count/60)
    sec = count % 60
    if sec >= 10:
        canvas.itemconfig(text_write, text=f"{count_min}:{sec}")
    elif sec < 10:
        canvas.itemconfig(text_write, text=f"{count_min}:0{sec}")
    if count > 0:
        global timer
        timer = window.after(1000, countdown, count-1)
    else:
        res()
        mark = ""
        for r in range(math.floor(m/2)):
            mark += "✔"
        label2.config(text=mark)


def re():
    window.after_cancel(timer)
    canvas.itemconfig(text_write, text="00:00")
    label1.config(text="Timer")
    label2.config(text="")
    global m
    m = 0


# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("tomato")
window.config(padx=100, pady=50, background=YELLOW)


label1 = Label(text="Timer")
label1.config(background=YELLOW, foreground=GREEN, font=(FONT_NAME, 35, "bold"))
label1.grid(column=2, row=1)

label2 = Label()
label2.config(background=YELLOW, foreground=GREEN, font=(FONT_NAME, 15, "bold"))
label2.grid(column=2, row=4)

canvas = Canvas(width=200, height=224, background=YELLOW, highlightthickness=0)
tomato = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato)
text_write = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=2, row=2)


start_button = Button(text="Start", command=res)
# start_button.config()
start_button.grid(column=1, row=3)

reset_button = Button(text="Reset", command=re)
reset_button.grid(column=3, row=3)


window.mainloop()

from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 1
SHORT_BREAK_MIN = 1
LONG_BREAK_MIN = 20
repeat = 0
timer = None
# ---------------------------- TIMER RESET ------------------------------- # 
def timer_reset():
    console.after_cancel(timer)
    canvas.itemconfig(default_time, text="00:00")
    label1.config(text="Timer")
    label2.config(text="")
    global repeat
    repeat = 0
# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_count():
    global repeat
    repeat += 1
    working_time = WORK_MIN * 60
    short_break = SHORT_BREAK_MIN * 60
    long_break = LONG_BREAK_MIN * 60
    if repeat % 8 == 0:
        count_down(long_break)
        label1.config(text='Long break', fg=RED)
    elif repeat % 2 == 0:
        count_down(short_break)
        label1.config(text='Short break', fg=PINK)
    else:
        count_down(working_time)
        label1.config(text='Working', fg=GREEN)
        # if repeat % 2 == 0:
         # label2 = Label(text='✓',)
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    minutes_counter = math.floor(count / 60)
    seconds_counter = count % 60
    if seconds_counter < 10:
        seconds_counter = f"0{seconds_counter}"

    canvas.itemconfig(default_time, text=f"{minutes_counter}:{seconds_counter}")
    if count > 0:
        global timer
        timer = console.after(1000, count_down, count -1)
    else:
        start_count()
        check = ""
        work_done = math.floor(repeat/2)
        for i in range(work_done):
            check += '✓'
        label2.config(text=check)
# ---------------------------- UI SETUP ------------------------------- #
"""In this project I used the wild card to import all classes of the tkinter module"""
console = Tk()
console.title('Pomodoro GUI Application')
console.config(padx=105, pady=50, bg=GREEN)
# start_count(5)

canvas = Canvas(width=300, height=300, bg=YELLOW, highlightthickness=0)
canvas_image = PhotoImage(file='tomato.png')
canvas.create_image(150, 150, image=canvas_image,)
default_time = canvas.create_text(145, 170, text="00:00", fill="green", font=(FONT_NAME, 35, "bold"))
canvas.grid()

label1 = Label(text='Timer', fg=RED, font=(FONT_NAME, 20, 'bold'))
label1.place(x=65, y=0)

# check_image = PhotoImage(file='check_button.jpg')
label2 = Label(fg=RED)
label2.place(x=140, y=270)

button1 = Button(text='Start', command=start_count)
button1.place(x=20, y=260)

button2 = Button(text="Reset", command=timer_reset)
button2.place(x=240, y=260)


console.mainloop()
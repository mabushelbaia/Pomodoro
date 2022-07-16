from ast import Import
from cgitb import reset
from tkinter import *
from tkinter.font import BOLD
from turtle import bgcolor, right
# ---------------------------- CONSTANTS ------------------------------- #
MAIN = "#231955"
SECONDARY = "#1F4690"
ACCENT1 = "#E8AA42"
ACCENT2 = "#FFE5B4"
WHITE = "#FFFFFF"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None
# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    window.after_cancel(timer)
    Title.config(text="Timer", font=("Courier", 20, BOLD))
    Timer.config(text="00:00")
    global reps
    reps = 0
# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1
    if reps%8 == 0:
        Title.config(text="Take a long break!", font=("Courier", 20, BOLD))
        count_down(LONG_BREAK_MIN*60)
    elif reps%2 == 0:
        Title.config(text="Take a short break!", font=("Courier", 20, BOLD))
        count_down(SHORT_BREAK_MIN*60)
    else:
        Title.config(text="Work time!", font=("Courier", 20, BOLD))
        count_down(WORK_MIN*60)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    global timer
    Timer.config(text=f"{int(count//60):02d}:{int(count%60):02d}")
    if count > 0:
        timer = window.after(1000, count_down, count-1)
    else:  
        start_timer()
        marks = ""
        for _ in reps // 2:  # Work Sessions
            marks += "✔️"
        check_marks.config(text=marks)
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro Timer")
window.geometry("300x400")
window.config(padx=30, pady=30)
window.configure(background=MAIN)


Title = Label(text="Timer", font=(FONT_NAME, 20, BOLD), bg=MAIN, fg=WHITE)
Timer = Label(text="00:00", font=(FONT_NAME, 60, BOLD), bg=MAIN, fg=WHITE)
Title.pack()
Timer.pack()


start_bt = Button(text="Start", font=(FONT_NAME, 20, BOLD), bg=ACCENT1, fg=WHITE, command=start_timer)
resert_bt = Button(text="Reset", font=(FONT_NAME, 20, BOLD), bg=ACCENT1, fg=WHITE, command=reset_timer)
check_marks = Label(text="", font=(FONT_NAME, 20, BOLD), bg=MAIN, fg=WHITE)
start_bt.pack(side="left")
resert_bt.pack(side="right")
check_marks.pack()



window.mainloop()

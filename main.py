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

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro Timer")
Title = Label(text="Timer", font=(FONT_NAME, 20, BOLD), bg=MAIN, fg=WHITE)
Timer = Label(text="00:00", font=(FONT_NAME, 60, BOLD), bg=MAIN, fg=WHITE)
Title.pack()
Timer.pack()
window.geometry("300x400")

start_bt = Button(text="Start", font=(FONT_NAME, 20, BOLD), bg=ACCENT1, fg=WHITE)
resert_bt = Button(text="Reset", font=(FONT_NAME, 20, BOLD), bg=ACCENT1, fg=WHITE)
start_bt.pack(side="left")
resert_bt.pack(side="right")


window.config(padx=30, pady=30)
window.configure(background=MAIN)
window.mainloop()

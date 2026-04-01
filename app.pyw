import tkinter as tk
from tkinter import *

number = 0

def clicker():
    global number
    number += 1
    ShowInfo["text"] = "You have clicked " + str(number) + " times."

window = tk.Tk()
window.title('Developer Anger Button')
window.geometry('870x100')
window.configure(bg='lightblue')
image = PhotoImage(file="logo.png")
window.iconphoto(True, tk.PhotoImage(file="logo.png"))

Label = tk.Label(window, text="Take out all your anger from a bug or error on this button.You setup is expensive,it doesnt deserve to get beaten.",bg = "lightblue",font = "Arial 12 bold")
ClickingButton = tk.Button(window,text = "HIT ME!", bg = "gold" , command = clicker)
ShowInfo = tk.Label(window,text = "Click the button to release your stress." , bg = "lightblue" , font = "Arial 12 bold")
label = tk.Label(window , text = "Even the most annoying of code,errors and bugs are solved with patience and time.", bg="lightblue", font = "Arial 12 bold")

Label.pack()
ClickingButton.pack()
ShowInfo.pack()
label.pack()

window.mainloop()
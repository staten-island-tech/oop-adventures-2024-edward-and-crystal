import random
import tkinter as tk
from tkinter import font
window = tk.Tk()
window.geometry('900x900')
window.title('SUPER AWESOME AND VERY REAL GAME by Edward and Crystal!!')

textfont = font.Font(family='Comic Sans MS', size=100, weight='normal')

def math():
    buttonvalue = random.randint(1, 10) * random.randint(1, 10)
    print(buttonvalue)

button = tk.Button(window, text="MATH!bruh", command=math, height=10, width=10)
button.pack(side='top', padx= 4, pady=4)

button = tk.Button(window, text="MATH!", command=math, height=10, width=10)
button.pack(side='top', padx= 4, pady=4)


window.mainloop()
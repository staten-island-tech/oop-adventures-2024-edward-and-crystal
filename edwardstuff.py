import tkinter as tk
from tkinter import font

window = tk.Tk()
window.title('SUPER AWESOME AND VERY REAL GAME by Edward and Crystal!!')
window.geometry('400x400')

textfont = font.Font(family='Comic Sans MS', size=100, weight='normal')

textbox = tk.Text(window, width=400, height=400)
textbox.pack(side=tk.BOTTOM, pady= 400)
window.mainloop()
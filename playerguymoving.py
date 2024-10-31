import tkinter as tk

def left():
    global x
    x += 10
    button.place(x=x, y=50)

def right():
    global x
    x -= 10
    button.place(x=x, y=50)

def up():
    global y
    y += 10
    button.place(x=x, y=50)

def down():
    global y
    y -= 10
    button.place(x=x, y=50)

window = tk.Tk()
window.title("Moving Button")

x = 10

playerguy = tk.Label(text='guy')
playerguy.pack()

button = tk.Button(window, text="down", command=down)
button.place(x=x, y=50)

window.mainloop()
import tkinter as tk

playercoordinates = (1, 2)
window = tk.Tk()

def Move(x):
    if x == 1:
        y = playercoordinates[1] + 1
        playercoordinates.set(playercoordinates[0], y)
    elif x == 2:
        y = playercoordinates[1] - 1
        playercoordinates.set(playercoordinates[0], y)
    elif x == 3:
        x = playercoordinates[0] + 1
        playercoordinates.set(x, playercoordinates[1])
    elif x == 4:
        x = playercoordinates[0] - 1
        playercoordinates.set(x, playercoordinates[1])


upbutton = tk.Button(window, text='UP', command=lambda: Move(1))
downbutton = tk.Button(window, text='DOWN', command=lambda: Move(1))
leftbutton = tk.Button(window, text='LEFT', command=lambda: Move(1))
rightbutton = tk.Button(window, text='RIGHT', command=lambda: Move(1))

upbutton.pack()
downbutton.pack()
leftbutton.pack()
rightbutton.pack()

while True:
    upbutton.pack()
    downbutton.pack()
    leftbutton.pack()
    rightbutton.pack()
    window.wait_variable(playercoordinates)
    playercoordinates = playercoordinates.get()
    
    print(playercoordinates)

import tkinter as tk

playercoordinates = [1, 2]
window = tk.Tk()
window.title('HI')

print(playercoordinates[1])

def Move(x):
    global playercoordinates
    if x == 1:
        y = int(playercoordinates[1]) + 1
        playercoordinates = [playercoordinates[0], y]
    elif x == 2:
        y = int(playercoordinates[1]) - 1
        playercoordinates = [playercoordinates[0], y]
    elif x == 3:
        x = int(playercoordinates[0]) + 1
        playercoordinates = [x, playercoordinates[1]]
    elif x == 4:
        x = int(playercoordinates[0]) - 1
        playercoordinates = [(x, playercoordinates[1])]


upbutton = tk.Button(window, text='UP', command=lambda: Move(1))
downbutton = tk.Button(window, text='DOWN', command=lambda: Move(2))
leftbutton = tk.Button(window, text='LEFT', command=lambda: Move(3))
rightbutton = tk.Button(window, text='RIGHT', command=lambda: Move(4))

upbutton.pack()
downbutton.pack()
leftbutton.pack()
rightbutton.pack()

for i in range(10):
    upbutton.pack()
    downbutton.pack( )
    leftbutton.pack()
    rightbutton.pack()
    window.wait_variable(playercoordinates)
    playercoordinates = playercoordinates.get()
    upbutton.destroy()
    downbutton.destroy()
    leftbutton.destroy()
    rightbutton.destroy()
    print(playercoordinates)

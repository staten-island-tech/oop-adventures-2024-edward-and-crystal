import tkinter as tk
import random

window = tk.Tk()
window.title("MATH!")
window.geometry('400x200')

def add():
    print(random.randint(1,50) + random.randint(1,10))
def subtract():
    print(random.randint(1,50) - random.randint(1,10))
def multiply():
    print(random.randint(1,50) * random.randint(1,10))
def divide():
    number = random.randint(1, 50) / random.randint(1, 10)
    print(round(number, 2))
def randomoperation():
    operation = random.randint(1,4)
    if operation == 1:
        print(random.randint(1,50) + random.randint(1,10))
    elif operation == 2:
        print(random.randint(1,50) - random.randint(1,10))
    elif operation == 3:
        print(random.randint(1,50) * random.randint(1,10))
    elif operation == 4:
        number = random.randint(1, 50) / random.randint(1, 10)
        print(round(number, 2))
def Joke():
    print('smell!Y!')

button1 = tk.Button(window, text="Add", command=add)
button1.pack(side="left")

button2 = tk.Button(window, text="Subtract", command=subtract)
button2.pack(side="left")

button3 = tk.Button(window, text="Multiply",command=multiply)
button3.pack(side="left")

button4 = tk.Button(window, text="Divide", command=divide)
button4.pack(side="left")

button5 = tk.Button(window, text="Random", command=randomoperation)
button5.pack(side="left")

button6 = tk.Button(window, text="Joke", command=Joke)
button6.pack(side='top', pady=10)

window.mainloop()
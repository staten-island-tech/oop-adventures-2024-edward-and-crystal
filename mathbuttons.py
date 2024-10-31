import tkinter as tk
import random

window = tk.Tk()
window.title("MATH!")
window.geometry('1000x600')

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

spacing = 200
button_width = 85

button1 = tk.Button(window, text="Add    ", command=add)
button1.place(x=10 + button_width * 1 + spacing, y=10)

button2 = tk.Button(window, text="Subtract", command=subtract)
button2.place(x=10 + button_width * 2 + spacing, y=10)

button3 = tk.Button(window, text="Multiply",command=multiply)
button3.place(x=10 + button_width * 3 + spacing, y=10)

button4 = tk.Button(window, text="Divide ", command=divide)
button4.place(x=10 + button_width * 4 + spacing, y=10)

button5 = tk.Button(window, text="Random ", command=randomoperation)
button5.place(x=10 + button_width * 5 + spacing, y=10)

button6 = tk.Button(window, text="Joke   ", command=Joke)
button6.place(x=10 + button_width * 6 + spacing, y=10)

window.mainloop()

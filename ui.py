import tkinter as tk
window = tk.Tk()
window.geometry('1800x900')
window.title('SUPER AWESOME AND VERY REAL GAME by Edward and Crystal!!')
label = tk.Label(window, text='a SUPER AWESOME AND VERY REAL GAME by Edward and Crystal!', font=('Times New Roman', 20))
label.pack(pady=20)
label2 = tk.Label(window, text='Would you like to play this super awesome and very real game?', font=('Times New Roman', 20))
label2.pack(pady=100)

buttonframe = tk.Frame(window)
buttonframe.pack(fill='x') 

def on_yes():
    print("YESSSS was clicked!")
    return "YES"

def on_no():
    label = tk.Label(window, text='NO YOU MUST PLAY', font=('Arial', 10))
    label.pack(pady=20)        
    return True

buttonframe.columnconfigure(0, weight=1)
buttonframe.columnconfigure(1, weight=1)

button_one = tk.Button(buttonframe, text='YESSSS', font=('Arial', 10), command=on_yes)
button_one.grid(row=0, column=0, sticky='ew')

button_two = tk.Button(buttonframe, text='NOOO', font=('Arial', 10), command=on_no)
button_two.grid(row=0, column=1, sticky='ew')


window.mainloop()

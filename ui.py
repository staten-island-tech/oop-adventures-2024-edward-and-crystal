import tkinter as tk

window = tk.Tk()
window.geometry('1800x900')
window.title('SUPER AWESOME AND VERY REAL GAME by Edward and Crystal!!')

def clear_page():
    for widget in window.winfo_children():
        widget.destroy()


def on_no():
    label_no = tk.Label(window, text='NO YOU MUST PLAY. CLICK YES', font=('Arial', 10))
    label_no.pack(pady=20)
    button_no.configure(state=tk.DISABLED)
 
def start_page():
    label = tk.Label(window, text='a SUPER AWESOME AND VERY REAL GAME by Edward and Crystal!', font=('Times New Roman', 20))
    label.pack(pady=20)
    label2 = tk.Label(window, text='Would you like to play this super awesome and very real game?', font=('Times New Roman', 20))
    label2.pack(pady=100)
    buttonframe = tk.Frame(window)
    buttonframe.pack(fill='x') 

    buttonframe.columnconfigure(0, weight=1)
    buttonframe.columnconfigure(1, weight=1)

    global button_yes, button_no
    button_yes = tk.Button(buttonframe, text='YESSSS', font=('Arial', 10), command=tutorial)
    button_yes.grid(row=0, column=0, sticky='ew')

    button_no = tk.Button(buttonframe, text='NOOO', font=('Arial', 10), command=on_no)
    button_no.grid(row=0, column=1, sticky='ew')


def tutorial():
    #name + instructions
    clear_page()
    label = tk.Label(window, font=('Arial', 20))
    label.pack()
    username = tk.StringVar()
    name = tk.Entry(window, textvariable=username)
    name.pack()

start_page()

window.mainloop()

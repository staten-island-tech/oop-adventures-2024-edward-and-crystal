import tkinter as tk

window = tk.Tk()
window.title('a')

def SetVariable(sigma):
    titlevar.set(sigma)
def ChangeTitle():
    global titlevar
    titlevar = tk.StringVar()
    button = tk.Button(window, text='AHAHAHAAHAH', command=lambda: SetVariable('sigma'))
    button.pack()
    window.wait_variable(titlevar)
    titlevar = titlevar.get()
    window.title(titlevar)


ChangeTitle()

window.mainloop()
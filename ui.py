import tkinter as tk

window = tk.Tk()
window.geometry('1800x900')
window.configure(bg='grey')
window.title('SUPER AWESOME AND VERY REAL GAME by Edward and Crystal!!')

def clear_page():
    for widget in window.winfo_children():
        widget.destroy()
 
#says game name, asks if you want to play. if yes, create a save file. if no, they cant do anything until they press yes
def start_page():
    def on_no():
        label_no = tk.Label(window, text='NO YOU MUST PLAY. CLICK YES', font=('Papyrus', 10), bg='grey')
        label_no.pack(pady=20)
        button_no.configure(state=tk.DISABLED)
        
    label = tk.Label(window, text='a SUPER AWESOME AND VERY REAL GAME by Edward and Crystal!', bg='grey', font=('Chiller', 20))
    label.pack(pady=20)
    label2 = tk.Label(window, text='Would you like to play this super awesome and very real game?', bg='grey', font=('Papyrus', 20))
    label2.pack(pady=100)
    buttonframe = tk.Frame(window)
    buttonframe.configure(bg='grey')
    buttonframe.pack(fill='x') 

    buttonframe.columnconfigure(0, weight=1)
    buttonframe.columnconfigure(1, weight=1)

    global button_yes, button_no
    button_yes = tk.Button(buttonframe, text='YESSSS', bg='grey', font=('Papyrus', 10), command=save_files)
    button_yes.grid(row=0, column=0, sticky='ew')

    button_no = tk.Button(buttonframe, text='NOOO', bg='grey', font=('Papyrus', 10), command=on_no)
    button_no.grid(row=0, column=1, sticky='ew')

#naming a save file
def save_files():
    def buttonclicked(button, button_name):
        label = tk.Label(window, text='What do you want to name this file?', bg='grey', font=('Papyrus', 50))
        label.pack()
        name = tk.Entry(window)
        name.pack()
        
        def sure(event):
            new_name = name.get()
            global sure
            sure = tk.Label(window, bg='grey', font='Papyrus', text=f'Are you sure you want "{new_name}" to be the name of your save file?')
            sure.pack()
            global buttonframe
            buttonframe = tk.Frame(window, bg='grey')
            buttonframe.pack()
            button_yes = tk.Button(buttonframe, text='Yes', bg='grey', font=('Papyrus', 10), command=rename)
            button_yes.pack()
            button_no = tk.Button(buttonframe, text='No', bg='grey', font=('Papyrus', 10), command=lambda: buttonclicked(button_no))
            button_no.pack()
                
        def rename(): #when binding it auto puts a argument in so thats why event here
            global buttonframe
            global sure
            buttonframe.pack_forget()
            sure.pack_forget()
            new_name = name.get()
            button.configure(text=f'{button_name}: {new_name}') 
            label.pack_forget()
            name.pack_forget()
            save.pack_forget()
            instructions()

        name.bind('<Return>', sure)
   
    clear_page()
    save = tk.Label(window, pady=10, text='Time to create your save file!', bg='grey', font=('Papyrus', 20))
    save.pack()
    buttonframe = tk.Frame(window)
    buttonframe.configure(bg='grey')
    buttonframe.pack(fill='x')
    savefile_one = tk.Button(buttonframe,  width=20, text='Save File One', bg='grey', font=('Papyrus', 50), command=lambda: buttonclicked(savefile_one, 'Save File One'))
    savefile_one.pack()
    savefile_two = tk.Button(buttonframe,  width=20, text='Save File Two', bg='grey', font=('Papyrus', 50),command=lambda: buttonclicked(savefile_two, 'Save File Two'))
    savefile_two.pack()  
    savefile_three = tk.Button(buttonframe, width=20, text='Save File Three', bg='grey', font=('Papyrus', 50), command=lambda: buttonclicked(savefile_three, 'Save File Three'))
    savefile_three.pack()
  
   
def instructions():
    label = tk.Label(window, text='Write your username', bg='grey', font=('Papyrus', 20))
    label.pack()

    name = tk.Entry(window)
    name.pack()
    
    label2 = tk.Label(window, text='', bg='grey', font=('Papyrus', 30))  #empty text

    def goal(event): #when binding it auto puts a argument in so thats why event here
        label.pack_forget()
        name.pack_forget()
        label2.config(text=f'Hello, {name.get()}! Your goal is to slay your enemies to progress, upgrading yourself along the way.\nGood luck!')
        label2.pack() 
    #when press return/enter, greeting is shown
    name.bind('<Return>', goal)

start_page()

window.mainloop()

import tkinter as tk
window = tk.Tk()
window.geometry('1800x900')
window.title('SUPER AWESOME AND VERY REAL GAME by Edward and Crystal!!')
label = tk.Label(window, text='a SUPER AWESOME AND VERY REAL GAME by Edward and Crystal!', font=('Times New Roman', 20))
label.pack(pady=20)
textbox = tk.Text(window, height=1, font=('Arial', 10))
textbox.pack()
window.mainloop()

import tkinter as tk

# have fun coding all of this monday edward 👍 (I CAN PUT EMOJIS IN VS CODE?)

def battle_action(action):
    action_var.set(action)

def battle():
    global action_var
    
    window = tk.Tk()
    window.title("Battle Mode")
    
    action_var = tk.StringVar()
    
    attack_button = tk.Button(window, text="Attack", command=lambda: battle_action("attack"))
    block_button = tk.Button(window, text="Block", command=lambda: battle_action("block"))
    
    attack_button.pack()
    block_button.pack()
    
    window.wait_variable(action_var)

    action_taken = action_var.get()
    print(f"Action taken: {action_taken}")

print(👍)
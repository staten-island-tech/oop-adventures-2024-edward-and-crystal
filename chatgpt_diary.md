# ChatGPT Coding Diary

## Project Name: Final Project

### Date: 12/18/24 + 1/4/25

---

## 1. **Task/Problem Description**

Briefly describe the problem you're trying to solve or the task you're working on.

1. I need to randomly generate the x and y spawn coordinates of the player. They need to be multiples of 10.
2. Trying to move a LoadRoom function that was in movement.py to rooms.py. I need to import the player x and y values from rooms.py to movement.py. I'm getting a circular import error.
3. I'm trying to run my create save file function, but it's running the load room function, even though I'm only calling the create save file function.

---

## 2. **Initial Approach/Code**

Describe the initial approach you took to solving the problem. If you started writing code, include it here.


1. Do something with random.randint, but I wasn't sure how to make it a multiple of 10.
2. Since the issue had to do with imports, I thought I could just put all the code in one file to not even deal with imports in the first place. However, I realized that would be foolish because it didn't make sense to combine movement and rooms.
3. I suspected I may be somehow running the load save file function, which has the load room function in it, so I tried deleting the load save file function. Still, the load room function ran, so my guess was incorrect

- What was your plan for solving the problem?
- Did you have any initial thoughts or strategies before using ChatGPT?

---

## 3. **Interaction with ChatGPT**

### Questions/Requests to ChatGPT
Write down the questions or requests you made to ChatGPT. 

Also include what code from ChatGPT you are unsure of and craft a question that asks for further clarification. 

1. How to use the random module in python to generate x and y values that are multiples of 10. I'm using pygame.
2. How to fix a circular import?
3. - How to check what file I'm running in python. I'm trying to run one function but another function is somehow running even though I didn't call it. 
   - I copy and pasted my create save file code to ChatGPT and asked what the issue was. 
   - After I comment out both the import statements and the other function, the create save file function works perfectly fine.
---

## 4. **ChatGPT's Suggestions/Code Changes**

Record the code or suggestions ChatGPT provided. Include any changes or improvements ChatGPT suggested and how it influenced your approach.

1. Do characterlocation = pygame.rect(random.randint(1, 100), random.randint(1, 100), 10, 10)
-The way I originally thought about it was to initalize the random x and y values, and then put those variables in the rectangle, but this way saves 2 lines of code.
2. Some of ChatGPT's suggestions were to rearrange my imports or make a third file each file imports from. I thought its suggestions were either too much work or would be a bad way to organize my code. But it did help in precisely defining what a circular import was. I removed a file's imports of another, and I instead initalized my variables in the file I used it in.
3. - It told me how to run a specific file using the terminal. The bug still appeared, showing that the issue wasn't that I was somehow running the wrong file. It told me to add print statements all throughout my code: in the functions and global scope. The print statements didn't show up in the terminal. 
   -   The code below worked, but only in a separate file where I only had my create save file function, which shouldn't be the case because even when I added this suggestion and deleted the rest of the code in the original file, it still ran the load room function.
   ```python 
    try:
        with open('saves.json', 'r') as file:
            savedata = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        # Initialize an empty list if the file doesn't exist or is invalid
        savedata = []
    ```
   
  - It told me that my import statements might be running all the global state code, so I should use a print statement to check. ChatGPT was right. It then recommended I put the global state code under `if __name__ == '__main__'`, but that made it so the imported code wouldn't work properly because it wouldn't initalize the key variables. Then I realized I didn't actually need to import from my other files in savefiles.py. 

- What was ChatGPT's solution or suggestion?
- How did it differ from your original approach?

---
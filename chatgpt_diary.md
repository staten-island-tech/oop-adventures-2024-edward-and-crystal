
# ChatGPT Coding Diary

## Project Name: Final Project

### Date: 12/18/24

---

## 1. **Task/Problem Description**

Briefly describe the problem you're trying to solve or the task you're working on.

1. I need to randomly generate the x and y spawn coordinates of the player. They need to be multiples of 10.
2. Trying to move a LoadRoom function that was in movement.py to rooms.py. I need to import the player x and y values from rooms.py to movement.py. I'm getting a circular import error.

---

## 2. **Initial Approach/Code**

Describe the initial approach you took to solving the problem. If you started writing code, include it here.


1. Do something with random.randint, but I wasn't sure how to make it a multiple of 10.
2. Since the issue had to do with imports, I thought I could just put all the code in one file to not even deal with imports in the first place. However, I realized that would be foolish because it didn't make sense to combine movement and rooms. 

- What was your plan for solving the problem?
- Did you have any initial thoughts or strategies before using ChatGPT?

---

## 3. **Interaction with ChatGPT**

### Questions/Requests to ChatGPT
Write down the questions or requests you made to ChatGPT. 

Also include what code from ChatGPT you are unsure of and craft a question that asks for further clarification. 

1. How to use the random module in python to generate x and y values that are multiples of 10. I'm using pygame.
2. How to fix a circular import?
-

---

## 4. **ChatGPT's Suggestions/Code Changes**

Record the code or suggestions ChatGPT provided. Include any changes or improvements ChatGPT suggested and how it influenced your approach.

1. Do characterlocation = pygame.rect(random.randint(1, 100), random.randint(1, 100), 10, 10)
-The way I originally thought about it was to initalize the random x and y values, and then put those variables in the rectangle, but this way saves 2 lines of code.
2. Some of ChatGPT's suggestions were to rearrange my imports or make a third file each file imports from. I thought its suggestions were either too much work or would be a bad way to organize my code. But it did help in precisely defining what a circular import was. I removed a file's imports of another, and I instead initalized my variables in the file I used it in.

- What was ChatGPT's solution or suggestion?
- How did it differ from your original approach?

---


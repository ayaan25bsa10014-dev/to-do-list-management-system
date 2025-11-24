# ✅ TO-DO LIST PROGRAM (Python)

## 📌 Statement / Purpose
This program is a simple Command-Line **To-Do List Manager** that allows users to add, view, and delete tasks. It also saves tasks to a text file so they persist even after the program exits.

---

## ✅ What This Program Does

### 🗂️ 1. Loads Existing Tasks
- Checks if `task.txt` exists.
- If yes, it loads all previously saved tasks into a list.

### 🆕 2. Adds New Tasks
- Prompts the user to enter a task.
- Stores the task in a list.
- Appends the task to `task.txt` for permanent storage.

### 👀 3. Views All Tasks
- Displays all tasks in a numbered list.
- Shows a message if there are no tasks.

### ❌ 4. Deletes a Task
- Allows the user to select a task number to delete.
- Removes that task from the list.
- Updates the file accordingly.

### 🚪 5. Exits the Program
- Lets the user exit anytime.
- Also asks if they want to continue after each action.

---

## 🧠 Concepts Used
- File Handling (`read`, `write`, `append`)
- Lists for storing tasks
- Loops (`while True`)
- Conditional statements (`if-elif-else`)
- User input handling

---

## 📂 File Used
**task.txt**
- Stores all tasks permanently.
- Automatically created if it doesn’t exist.

---

## ⚠️ Known Issues
- `"/n"` should be `"\n"` for proper new lines.
- Delete function has a logic error and needs correction.

---

## 🎯 Conclusion
This program serves as a beginner-friendly Python project to practice:
- File operations
- Menu-driven programs
- Task management logic

It’s a simple but effective way to learn how data persistence works in Python!


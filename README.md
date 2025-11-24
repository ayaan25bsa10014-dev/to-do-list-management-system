# to-do-list-management-system
📌 Overview

This project is a Python-based To-Do List application that runs in the terminal. It allows users to manage tasks and automatically saves them to a file (task.txt) so they are not lost after exiting the program.

✨ Features
🆕 1. Add Tasks

Users can enter a new task.

The task is added to the list in memory.

It is also saved in the task.txt file for future use.

👀 2. View Tasks

Displays all the tasks added so far.

Shows them in a numbered list for easy reading.

❌ 3. Delete Tasks

Users can choose a task number to delete.

Ensures the list isn’t empty before deletion.

Updates the stored file accordingly.

🚪 4. Exit Program

Allows users to quit safely.

Also gives an additional option to continue or stop after each action.

💾 File Handling

The program checks if task.txt already exists.

If yes, it loads previous tasks into memory.

All new tasks are appended to the same file.

🔁 Loop System

The app runs inside a while True loop.

After each operation, the user can choose to continue or exit.

Ensures nonstop task management until the user quits.

🧠 Key Concepts Used

✅ File Handling (open, read, write)
✅ Lists for storing tasks
✅ Loops & User Input
✅ Conditional Statements
✅ Basic CLI Menu System

🛠️ Known Issues / Improvements

⚠️ Deleting tasks needs improvement (current code has a few bugs).
⚠️ File writing uses "/n" instead of "\n" (newline).
✅ Could add editing tasks, search feature, or better UI in the future.

🎯 Conclusion

This project is a great beginner-friendly Python exercise that teaches:

How to store data,

How to build a menu-driven program,

And how to manage user inputs effectively.
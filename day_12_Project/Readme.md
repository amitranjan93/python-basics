# 🔐 Password Vault (Python)

A simple command-line Password Vault built in Python using Object-Oriented Programming (OOP). This application allows users to securely store, edit, delete, and manage website credentials while persisting data in a text file.

---

## 🚀 Features

- ➕ Add new passwords
- 📋 View all saved passwords
- 🔒 Check password strength
- ✏️ Edit existing passwords
- 🗑️ Delete passwords
- 💾 Automatic file saving
- 📂 Automatically loads saved passwords when the program starts

---

## 🛠️ Technologies Used

- Python 3
- Object-Oriented Programming (OOP)
- File Handling
- Modular Programming

---

## 📁 Project Structure

```
Password-Vault/
│
├── main.py               # Main application
├── password_manager.py   # Password class and business logic
├── file_manager.py       # File loading and saving
├── Password.txt          # Stores password data
└── README.md
```

---

## 📖 How It Works

When the application starts:

1. Loads all saved passwords from `Password.txt`
2. Creates Password objects
3. Displays the main menu

Any changes made are automatically saved to the file.

---

## 💻 Menu

```
========== Password Vault ==========
1. Add Password
2. Show Passwords
3. Check Password Strength
4. Edit Password
5. Delete Password
6. Exit
```

---

## 📚 Concepts Practiced

- Classes & Objects
- Constructors
- Methods
- Lists of Objects
- File Handling
- Reading & Writing Files
- Modules
- Functions
- Loops
- Conditional Statements
- Encapsulation

---

## 🎯 Future Improvements

- Search passwords by website
- Prevent duplicate website entries
- Password generator
- Password hashing
- Master password authentication
- Store data in SQLite database
- GUI version using Tkinter
- Web version using Flask

---

## 👨‍💻 Author

**Amit Ranjan**

Project created as part of my **Project Phoenix** Python learning journey.
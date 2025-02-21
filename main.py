import sqlite3
import tkinter as tk
from AddBook import add_book_window
from DeleteBook import delete_book_window
from IssueBook import issue_book_window
from ReturnBook import return_book_window
from ViewBooks import view_books_window
from History import history_window

def initialize_database():
    conn = sqlite3.connect('library.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS books (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT,
            author TEXT,
            isbn TEXT UNIQUE,
            available INTEGER DEFAULT 1
        )
    ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS issued_books (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            book_id INTEGER,
            issued_to TEXT,
            issue_date TEXT,
            return_date TEXT,
            FOREIGN KEY(book_id) REFERENCES books(id)
        )
    ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS history (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp TEXT DEFAULT (DATETIME('now')),
            action TEXT
        )
    ''')
    conn.commit()
    conn.close()

def main():
    initialize_database()

    root = tk.Tk()
    root.title("Library Management System")
    root.geometry("600x500")
    root.configure(bg="#2b2b2b")
    root.resizable(False, False)

    header_frame = tk.Frame(root, bg="#1f1f1f", height=60)
    header_frame.pack(fill=tk.X)

    header_label = tk.Label(
        header_frame,
        text="Library Management System",
        font=("Arial", 18, "bold"),
        bg="#1f1f1f",
        fg="white"
    )
    header_label.pack(pady=15)

    main_frame = tk.Frame(root, bg="#2b2b2b")
    main_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)

    def on_enter(event):
        event.widget['bg'] = '#2e86de'

    def on_leave(event):
        event.widget['bg'] = '#4d4d4d'

    button_style = {
        "font": ("Arial", 12),
        "bg": "#4d4d4d",
        "fg": "black",
        "activeforeground": "#2e86de",
        "relief": tk.RAISED,
        "width": 25,
        "height": 2
    }

    buttons = [
        ("Add Book", add_book_window),
        ("Delete Book", delete_book_window),
        ("Issue Book", issue_book_window),
        ("Return Book", return_book_window),
        ("View Books", view_books_window),
        ("View History", history_window)
    ]

    for text, command in buttons:
        btn = tk.Button(main_frame, text=text, command=command, **button_style)
        btn.bind("<Enter>", on_enter)
        btn.bind("<Leave>", on_leave)
        btn.pack(pady=10)

    footer_frame = tk.Frame(root, bg="#1f1f1f", height=40)
    footer_frame.pack(fill=tk.X)

    footer_label = tk.Label(
        footer_frame,
        text="Developed by Rayhan & Hridoy - © 2025",
        font=("Arial", 10),
        bg="#1f1f1f",
        fg="white"
    )
    footer_label.pack(pady=5)

    root.mainloop()

if __name__ == "__main__":
    main()

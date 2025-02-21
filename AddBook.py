import sqlite3
import tkinter as tk
from tkinter import messagebox

def add_book_window():
    def add_book():
        title = title_entry.get()
        author = author_entry.get()
        isbn = isbn_entry.get()

        if not title or not author or not isbn:
            messagebox.showerror("Error", "All fields are required")
            return

        conn = sqlite3.connect('library.db')
        cursor = conn.cursor()

        try:
            cursor.execute("INSERT INTO books (title, author, isbn) VALUES (?, ?, ?)", (title, author, isbn))
            cursor.execute("INSERT INTO history (action) VALUES (?)", (f"Added book: {title} (ISBN: {isbn})",))
            conn.commit()
            messagebox.showinfo("Success", "Book added successfully")
        except sqlite3.IntegrityError:
            messagebox.showerror("Error", "ISBN must be unique")
        finally:
            conn.close()
            add_book_window.destroy()

    add_book_window = tk.Toplevel()
    add_book_window.title("Add Book")
    add_book_window.geometry("400x300")
    add_book_window.configure(bg="#2b2b2b")

    tk.Label(add_book_window, text="Add a New Book", font=("Arial", 16, "bold"), bg="#2b2b2b", fg="white").pack(pady=10)

    tk.Label(add_book_window, text="Title", bg="#2b2b2b", fg="white").pack(pady=5)
    title_entry = tk.Entry(add_book_window, width=30)
    title_entry.pack()

    tk.Label(add_book_window, text="Author", bg="#2b2b2b", fg="white").pack(pady=5)
    author_entry = tk.Entry(add_book_window, width=30)
    author_entry.pack()

    tk.Label(add_book_window, text="ISBN", bg="#2b2b2b", fg="white").pack(pady=5)
    isbn_entry = tk.Entry(add_book_window, width=30)
    isbn_entry.pack()

    tk.Button(add_book_window, text="Add Book", command=add_book, bg="#3498db", fg="black", width=20).pack(pady=20)

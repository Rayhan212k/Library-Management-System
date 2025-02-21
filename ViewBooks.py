import sqlite3
import tkinter as tk

def view_books_window():
    def fetch_books():
        conn = sqlite3.connect('library.db')
        cursor = conn.cursor()
        cursor.execute("SELECT id, title, author, isbn, available FROM books")
        rows = cursor.fetchall()
        conn.close()
        return rows

    view_books_window = tk.Toplevel()
    view_books_window.title("View Books")

    tk.Label(view_books_window, text="List of Books", font=("Arial", 14, "bold")).pack(pady=10)

    books_list = tk.Listbox(view_books_window, width=80, height=20)
    books_list.pack()

    books_data = fetch_books()
    for row in books_data:
        text = f"ID: {row[0]}, Title: {row[1]}, Author: {row[2]}, ISBN: {row[3]}, Available: {'Yes' if row[4] else 'No'}"
        books_list.insert(tk.END, text)

    tk.Button(view_books_window, text="Close", command=view_books_window.destroy).pack(pady=10)

import sqlite3
import tkinter as tk
from tkinter import messagebox

def delete_book_window():
    def delete_book():
        book_id = book_id_entry.get()

        if not book_id:
            messagebox.showerror("Error", "Book ID is required")
            return

        conn = sqlite3.connect('library.db')
        cursor = conn.cursor()
        try:
            cursor.execute("SELECT title FROM books WHERE id = ?", (book_id,))
            book = cursor.fetchone()
            if book:
                cursor.execute("DELETE FROM books WHERE id = ?", (book_id,))
                cursor.execute("INSERT INTO history (action) VALUES (?)", (f"Deleted book: {book[0]} (ID: {book_id})",))
                conn.commit()
                messagebox.showinfo("Success", "Book deleted successfully")
            else:
                messagebox.showerror("Error", "Book ID not found")
        finally:
            conn.close()
            delete_book_window.destroy()

    delete_book_window = tk.Toplevel()
    delete_book_window.title("Delete Book")
    delete_book_window.geometry("400x200")
    delete_book_window.configure(bg="#2b2b2b")

    tk.Label(delete_book_window, text="Delete a Book", font=("Arial", 16, "bold"), bg="#2b2b2b", fg="white").pack(pady=10)

    tk.Label(delete_book_window, text="Book ID", bg="#2b2b2b", fg="white").pack(pady=5)
    book_id_entry = tk.Entry(delete_book_window, width=30)
    book_id_entry.pack()

    tk.Button(delete_book_window, text="Delete Book", command=delete_book, bg="#3498db", fg="black", width=20).pack(pady=20)

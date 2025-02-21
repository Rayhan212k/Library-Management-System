import sqlite3
import tkinter as tk
from tkinter import messagebox

def return_book_window():
    def return_book():
        book_id = book_id_entry.get()
        return_date = return_date_entry.get()

        if not book_id or not return_date:
            messagebox.showerror("Error", "All fields are required")
            return

        conn = sqlite3.connect('library.db')
        cursor = conn.cursor()
        try:
            cursor.execute("SELECT id FROM issued_books WHERE book_id = ? AND return_date IS NULL", (book_id,))
            issued_book = cursor.fetchone()

            if not issued_book:
                messagebox.showerror("Error", "Book not currently issued")
            else:
                cursor.execute("UPDATE issued_books SET return_date = ? WHERE id = ?", (return_date, issued_book[0]))
                cursor.execute("UPDATE books SET available = 1 WHERE id = ?", (book_id,))
                cursor.execute("INSERT INTO history (action) VALUES (?)",
                               (f"Returned book ID: {book_id} on {return_date}",))
                conn.commit()
                messagebox.showinfo("Success", "Book returned successfully")
                return_book_window.destroy()
        finally:
            conn.close()

    return_book_window = tk.Toplevel()
    return_book_window.title("Return Book")
    return_book_window.geometry("400x250")
    return_book_window.configure(bg="#2b2b2b")

    tk.Label(return_book_window, text="Return a Book", font=("Arial", 16, "bold"), bg="#2b2b2b", fg="white").pack(pady=10)

    tk.Label(return_book_window, text="Book ID", bg="#2b2b2b", fg="white").pack(pady=5)
    book_id_entry = tk.Entry(return_book_window, width=30)
    book_id_entry.pack()

    tk.Label(return_book_window, text="Return Date", bg="#2b2b2b", fg="white").pack(pady=5)
    return_date_entry = tk.Entry(return_book_window, width=30)
    return_date_entry.pack()

    tk.Button(return_book_window, text="Return Book", command=return_book, bg="#3498db", fg="black", width=20).pack(pady=20)


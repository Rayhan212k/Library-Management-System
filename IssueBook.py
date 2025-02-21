import sqlite3
import tkinter as tk
from tkinter import messagebox

def issue_book_window():
    def issue_book():
        book_id = book_id_entry.get()
        issued_to = issued_to_entry.get()
        issue_date = issue_date_entry.get()

        if not book_id or not issued_to or not issue_date:
            messagebox.showerror("Error", "All fields are required")
            return

        conn = sqlite3.connect('library.db')
        cursor = conn.cursor()
        try:
            cursor.execute("SELECT available FROM books WHERE id = ?", (book_id,))
            book = cursor.fetchone()

            if not book:
                messagebox.showerror("Error", "Book ID not found")
            elif book[0] == 0:
                messagebox.showerror("Error", "Book is not available")
            else:
                cursor.execute("INSERT INTO issued_books (book_id, issued_to, issue_date) VALUES (?, ?, ?)",
                               (book_id, issued_to, issue_date))
                cursor.execute("UPDATE books SET available = 0 WHERE id = ?", (book_id,))
                cursor.execute("INSERT INTO history (action) VALUES (?)",
                               (f"Issued book ID: {book_id} to {issued_to} on {issue_date}",))
                conn.commit()
                messagebox.showinfo("Success", "Book issued successfully")
                issue_book_window.destroy()
        finally:
            conn.close()

    issue_book_window = tk.Toplevel()
    issue_book_window.title("Issue Book")
    issue_book_window.geometry("400x300")
    issue_book_window.configure(bg="#2b2b2b")

    tk.Label(issue_book_window, text="Issue a Book", font=("Arial", 16, "bold"), bg="#2b2b2b", fg="white").pack(pady=10)

    tk.Label(issue_book_window, text="Book ID", bg="#2b2b2b", fg="white").pack(pady=5)
    book_id_entry = tk.Entry(issue_book_window, width=30)
    book_id_entry.pack()

    tk.Label(issue_book_window, text="Issued To", bg="#2b2b2b", fg="white").pack(pady=5)
    issued_to_entry = tk.Entry(issue_book_window, width=30)
    issued_to_entry.pack()

    tk.Label(issue_book_window, text="Issue Date", bg="#2b2b2b", fg="white").pack(pady=5)
    issue_date_entry = tk.Entry(issue_book_window, width=30)
    issue_date_entry.pack()

    tk.Button(issue_book_window, text="Issue Book", command=issue_book, bg="#3498db", fg="black", width=20).pack(pady=20)

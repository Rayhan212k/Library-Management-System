import sqlite3
import tkinter as tk

def history_window():
    def fetch_history():
        conn = sqlite3.connect('library.db')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM history ORDER BY timestamp DESC")
        rows = cursor.fetchall()
        conn.close()
        return rows

    history_window = tk.Toplevel()
    history_window.title("History of Actions")

    tk.Label(history_window, text="History of All Actions", font=("Arial", 14, "bold")).pack(pady=10)

    history_list = tk.Listbox(history_window, width=80, height=20)
    history_list.pack()

    history_data = fetch_history()
    for row in history_data:
        history_list.insert(tk.END, f"[{row[1]}] {row[2]}")

    tk.Button(history_window, text="Close", command=history_window.destroy).pack(pady=10)

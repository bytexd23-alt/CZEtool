import tkinter as tk
from tkinter import messagebox, filedialog
import random

def show_error():
    if repeat_error.get():
        interval = int(interval_entry.get().strip())
        root.after(interval, show_error)

    custom_title = custom_title_entry.get().strip()
    title = custom_title if custom_title else "Critical Error"
    error_reason = random.choice(error_reasons.get().split(','))
    error_phrase = random.choice(error_phrases.get().split(','))
    if selected_icon.get() == 'Custom':
        messagebox.showerror(title, f"{error_reason}\n{error_phrase}", iconbitmap=custom_icon.get())
    else:
        messagebox.showerror(title, f"{error_reason}\n{error_phrase}", icon=selected_icon.get())

def select_icon():
    file_path = filedialog.askopenfilename()
    custom_icon.set(file_path)

root = tk.Tk()
root.title("Crazy Tool")

error_reasons_label = tk.Label(root, text="Error Reasons (comma separated):")
error_reasons = tk.Entry(root)
error_reasons.insert(0, "System overload, Out of memory, Corrupted file, Invalid argument, Timeout, Permission denied")

error_phrases_label = tk.Label(root, text="Error Phrases (comma separated):")
error_phrases = tk.Entry(root)
error_phrases.insert(0, "The operation failed, Error code:, Contact system administrator, Check log for details, Try again later")

custom_title_label = tk.Label(root, text="Custom Title:")
custom_title_entry = tk.Entry(root)

icon_label = tk.Label(root, text="Icon:")
selected_icon = tk.StringVar()
icon_options = [
    ('Critical Error', messagebox.ERROR),
    ('Warning', messagebox.WARNING),
    ('Information', messagebox.INFO),
    ('Question', messagebox.QUESTION),
    ('Custom', 'Custom')
]
for text, value in icon_options:
    tk.Radiobutton(root, text=text, variable=selected_icon, value=value).pack(anchor='w')

custom_icon = tk.StringVar()
select_icon_button = tk.Button(root, text="Select Icon", command=select_icon)

repeat_error = tk.BooleanVar()
tk.Checkbutton(root, text="Repeat Error", variable=repeat_error).pack()

interval_label = tk.Label(root, text="Interval (in milliseconds) (Repeat Error) :")
interval_entry = tk.Entry(root)
interval_entry.insert(0, "10000")

generate_error_button = tk.Button(root, text="Generate Error", command=show_error)

interval_label.pack()
interval_entry.pack()
error_reasons_label.pack()
error_reasons.pack()
error_phrases_label.pack()
error_phrases.pack()
custom_title_label.pack()
custom_title_entry.pack()
icon_label.pack()
select_icon_button.pack() 
generate_error_button.pack()

root.mainloop()

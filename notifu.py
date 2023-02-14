from tkinter import *
from tkinter import filedialog
from win10toast import ToastNotifier
import threading

# create a notification object
toaster = ToastNotifier()

# define the GUI
root = Tk()
root.title("Windows 10 Notification")
root.geometry("400x200")

# define the notification title label and text entry
title_label = Label(root, text="Notification Title:")
title_label.grid(row=0, column=0, padx=10, pady=10)
title_entry = Entry(root, width=30)
title_entry.grid(row=0, column=1, padx=10, pady=10)

# define the notification message label and text entry
message_label = Label(root, text="Notification Message:")
message_label.grid(row=1, column=0, padx=10, pady=10)
message_entry = Entry(root, width=30)
message_entry.grid(row=1, column=1, padx=10, pady=10)

# define the icon path label, text entry, and browse button
icon_label = Label(root, text="Icon Path:")
icon_label.grid(row=2, column=0, padx=10, pady=10)
icon_entry = Entry(root, width=20)
icon_entry.grid(row=2, column=1, padx=10, pady=10)
def browse_icon():
    file_path = filedialog.askopenfilename(title="Select Icon File", filetypes=(("Icon Files", "*.ico"), ("All Files", "*.*")))
    icon_entry.delete(0, END)
    icon_entry.insert(0, file_path)
browse_button = Button(root, text="Browse", command=browse_icon)
browse_button.grid(row=2, column=2, padx=10, pady=10)

# define the display notification button
def display_notification():
    notification_title = title_entry.get()
    notification_message = message_entry.get()
    notification_icon = icon_entry.get()
    threading.Thread(target=toaster.show_toast, args=(notification_title, notification_message), kwargs={"icon_path": notification_icon}).start()

display_button = Button(root, text="Display Notification", command=display_notification)
display_button.grid(row=3, column=1, padx=10, pady=10)

# run the GUI
root.mainloop()

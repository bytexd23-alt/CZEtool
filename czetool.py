import tkinter as tk
import subprocess

def run_python1():
    subprocess.call(["python", "testgui.py"])
    
def run_python2():
    subprocess.call(["python", "notifu.py"])

root = tk.Tk()
root.geometry("300x265")
root.title("Crazy Error Tool!")

button1 = tk.Button(root, text="Run Error Generator", command=run_python1, height=5, width=40)
button2 = tk.Button(root, text="Run Notifaction Generator (10/11)", command=run_python2, height=5, width=40)

button1.pack()
button2.pack()

root.mainloop()

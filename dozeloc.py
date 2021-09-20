import unittest
import tkinter as tk
import tkinter.ttk as ttk
import tkinter.filedialog as tkfd
from pathlib import Path
import sys
import subprocess
import os

class DozelocUI(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.hi_there = tk.Button(self)
        self.hi_there["text"] = "Hello World\n(click me)"
        self.hi_there["command"] = self.say_hi
        self.hi_there.pack(side="top")

        self.quit = tk.Button(self, text="QUIT", fg="red",
                              command=self.master.destroy)
        self.quit.pack(side="bottom")
        self.fc = self.create_file_chooser(self, "Input File")

    def create_file_chooser(self, parent, text):
        frame = ttk.Frame(parent)
        label = ttk.Label(frame, text=text)
        entry = ttk.Entry(frame)
        button = ttk.Button(frame, text="Browse..")
        label.grid(column=0, row=0)
        entry.grid(column=1, row=0)
        button.grid(column=2, row=0)
        return frame

    def say_hi(self):
        print("hi there, everyone!")

if __name__ == "__main__":
    #root = tk.Tk()
    #app = DozelocUI(master=root)
    #app.mainloop()
    initialdir = Path("/home/cslz90/Documents/Lehre/GDI-BiM/bimgdi-cs/2019_wise/uebungen/dozentron")
    test_file = tkfd.askopenfilename(title="Test file", filetypes=[("python code", "*.py")], initialdir=initialdir)
    test_file = Path(test_file)
    solution_file = tkfd.askopenfilename(title="Solution file", filetypes=[("python code", "*.py")], initialdir=initialdir)
    solution_file = Path(solution_file)
    subenv = os.environ.copy()
    if "PYTHONPATH" not in subenv:
        subenv["PYTHONPATH"] = solution_file.parent
    else:
        subenv["PYTHONPATH"] += ":" + (solution_file.parent)
    res = subprocess.run(["python", test_file], env=subenv, timeout=60)
    # print(solution_file.parent)
    # sys.path.append(solution_file.parent)
    # exec(test_file.read_text(encoding="UTF_8"))

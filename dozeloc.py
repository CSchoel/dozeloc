import unittest
import tkinter as tk
import tkinter.ttk as ttk
import tkinter.filedialog as tkfd
from pathlib import Path
import sys
import subprocess
import os

class DozelocUI(ttk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.exercise_chooser = ttk.Combobox(self)
        self.exercise_label = ttk.Label(self, text="Exercise")
        self.solution_label = ttk.Label(self, text="Solution file")
        self.solution_chooser = FileChooser(self)
        self.check_button = ttk.Button(self, text="Check!", command=self.check)
        self.result = tk.Text(self)

        self.exercise_label.grid(row=0, column=0)
        self.exercise_chooser.grid(row=0, column=1, sticky="EW")
        self.solution_label.grid(row=1, column=0)
        self.solution_chooser.grid(row=1, column=1, sticky="EW")
        self.check_button.grid(row=2, column=0, columnspan=2)
        self.result.grid(row=3, column=0, columnspan=2)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=3)

        # self.quit = ttk.Button(self, text="QUIT",
        #                       command=self.master.destroy)
        # self.quit.pack(side="bottom")
    def check(self):
        print("hi there, everyone!")

class FileChooser(ttk.Frame):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.parent = parent
        self.create_widgets()
    def create_widgets(self):
        entry = ttk.Entry(self)
        button = ttk.Button(self, text="Browse..")
        entry.grid(column=0, row=0, sticky="EWNS")
        button.grid(column=1, row=0, sticky="NS")
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=0)


if __name__ == "__main__":
    root = tk.Tk()
    app = DozelocUI(master=root)
    app.mainloop()
    exit(1)
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

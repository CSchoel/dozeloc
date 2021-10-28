import unittest
import tkinter as tk
import tkinter.ttk as ttk
import tkinter.filedialog as tkfd
from pathlib import Path
import sys
import subprocess
import os

class DozelocUI(ttk.Frame):
    def __init__(self, master=None, exdir=Path(".")):
        super().__init__(master)
        self.master = master
        self.pack()
        self.exdir = Path(exdir)
        self.create_widgets()

    def exercises(self, exdir):
        # find folders which contain a folder called "test"
        exercises = [x for x in exdir.iterdir() if x.is_dir() and (x / "test").is_dir()]
        return sorted([x.name for x in exercises])

    def create_widgets(self):
        self.exercise_chooser = ttk.Combobox(self, values=self.exercises(self.exdir), state="readonly")
        self.exercise_chooser.current(0)
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
        ex = self.exdir / self.exercise_chooser.get()
        test = [x for x in (ex / "test").iterdir() if x.suffix == ".py"]
        sol = Path(self.solution_chooser.textvar.get())
        out = "{} + {}".format(ex, sol)
        res = ""
        for t in test:
            res += run_unittest(t, sol)
            res += "\n"
        self.show_result(res)

    def show_result(self, res):
        self.result.delete("1.0", "end")
        self.result.insert("1.0", res)

class FileChooser(ttk.Frame):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.parent = parent
        self.create_widgets()
        self.initialdir = Path(".")
    def create_widgets(self):
        self.textvar = tk.StringVar()
        self.entry = ttk.Entry(self, textvariable=self.textvar)
        self.button = ttk.Button(self, text="Browse..", command=self.browse)
        self.entry.grid(column=0, row=0, sticky="EWNS")
        self.button.grid(column=1, row=0, sticky="NS")
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=0)
    def browse(self):
        fn = tkfd.askopenfilename(title="Open file", filetypes=[("python code", "*.py")], initialdir=self.initialdir)
        self.textvar.set(fn)
        self.initialdir = Path(fn).parent

def run_unittest(test_file, solution_file):
    subenv = os.environ.copy()
    if "PYTHONPATH" not in subenv:
        subenv["PYTHONPATH"] = solution_file.parent
    else:
        subenv["PYTHONPATH"] += ":" + (solution_file.parent)
    res = subprocess.run(["python", test_file], env=subenv, timeout=60, capture_output=True)
    restxt = "" if len(res.stdout) == 0 else "{}\n\n".format(res.stdout.decode("utf-8"))
    restxt += str(res.stderr.decode("utf-8"))
    return restxt

if __name__ == "__main__":
    root = tk.Tk()
    exdir = Path("/home/cslz90/Documents/Lehre/GDI-BiM/bimgdi-cs/2019_wise/uebungen/dozentron")
    app = DozelocUI(master=root, exdir=exdir)
    app.mainloop()

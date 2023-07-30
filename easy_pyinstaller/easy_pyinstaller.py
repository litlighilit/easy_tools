# GUI wrapper of  pyinstaller
import os
from tkinter import Tk, Frame, Entry, Button, Checkbutton, Label, StringVar, LabelFrame
from subprocess import Popen

from shutil import which

NAME = "pyinstaller"
PYINST_PATH = which(NAME)

OPTION_FILE = "cmd_options.json"
PACK_CNF = dict(fill="x", expand=True)
STYLE_CNF = dict(background="#999")


class CnfFrame(Frame):
    def __init__(self, master=None, display=False, cnf={}, **kw):
        super().__init__(master=master, cnf=cnf, **kw)
        self.display = display
        self.cnftitle()
        self.get_options()
        self.cnfexec()

    def cnftitle(self):
        self.titleframe = Frame(self.master)
        Label(self.titleframe, text="pyinstaller").pack(side="left")
        self.titleframe.pack()

    def get_options(self):
        file = os.path.join(os.path.dirname(__file__), OPTION_FILE)
        from json import load

        with open(file) as f:
            options = load(f)
            self.bool_like = options["bool_like"]
            self.str_like = options["str_like"]
        self.cnf_bool_like()
        self.cnf_str_like()

    def cnfexec(self):
        def displayed_do():
            # FIXME This function can't work, as fileno is required
            from tkinter import Toplevel
            from tkstd import Tkstdout, Tkstderr

            top = Toplevel()
            stdout = Tkstdout(top)
            stderr = Tkstderr()
            stderr.fileno = lambda: 1
            stdout.fileno = lambda: 0
            # print(self.args)
            _ = Popen(self.args, executable=PYINST_PATH, stdout=stdout, stderr=stderr)
            stdout.pack()
            top.mainloop()

        def pyinst_exec():
            args = []
            for key in self.bool_like:
                args.append(self.boolvars[key].get())

            for val in self.str_like.values():
                args.append(self.strvars[val].get())

            self.args = args
            if self.display:
                displayed_do()
            else:  # background do
                _ = Popen(self.args, executable=PYINST_PATH)

        Button(self, text="ok", command=pyinst_exec).pack()

    def cnf_bool_like(self):
        self.boolvars = {}
        for key, val in self.bool_like.items():
            self.boolvars[key] = sv = StringVar(self)
            default, option = val
            sv.set(default)
            Checkbutton(
                self.titleframe,
                text=key,
                onvalue=option,
                offvalue=default,
                variable=sv,
            ).pack(side="left")

    def cnf_str_like(self):
        self.strvars = {}
        for key, val in self.str_like.items():
            self.strvars[val] = sv = StringVar(self)
            laberframe = LabelFrame(self, text=key, labelanchor="n")
            Entry(laberframe, textvariable=sv).pack(PACK_CNF)
            laberframe.pack(fill="x", expand=True)


if __name__ == "__main__":
    root = Tk()
    CnfFrame(root, cnf=STYLE_CNF).pack(PACK_CNF)
    root.mainloop()

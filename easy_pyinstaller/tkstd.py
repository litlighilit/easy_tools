import sys
from tkinter.scrolledtext import ScrolledText
from tkinter.messagebox import showerror
from textwrap import TextWrapper
#for error
maxsize=27
wrapper=TextWrapper(maxsize)
class Tkstd(object):
    def f(self,s):
        pass
    
    def write(self,s):
        self.f(s)
    def flush(self):
        #self.f('over')
        pass
class Tkstdout(Tkstd,ScrolledText):
    def f(self,s):
        self.insert('end',s)
class Tkstdout_clear(Tkstdout):
    def f(self,s):
        if s.strip():
            self.delete(1.0,'end')
            super().f(s)

class Tkstderr(Tkstd):
    def __init__(self,title='error',**options):
        self.title=title
        self.options=options
        self.buffer=''
    def f(self,s):
        res=wrapper.fill(s)
        self.buffer+=res
    def flush(self):
        s=self.buffer
        if not s:return
        showerror(self.title,s,**self.options)
        del self.buffer
        self.buffer=''

if __name__=='__main__':
    stdout=Tkstdout()
    stdout.pack()
    sys.stdout=stdout
    print(1,2,3)
    stderror=Tkstderr()
    sys.stderr=stderror
    errorcmd='error'
    def raise_error():
        raise Exception
    ms=300
    stdout.after(ms,raise_error)
    stdout.mainloop()

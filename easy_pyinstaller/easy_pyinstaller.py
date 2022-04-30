import os
from rewpyin import rewrite
from _data import PYINST_PATH

OPTION_FILE="_options.json"
OPTION_PATH=os.path.join(os.path.dirname(__file__),"_options.json")
PACK_CNF=dict(fill="x",expand=True)
STYLE_CNF=dict(background="#999")

from tkinter import Tk,Frame,Entry,Button,Checkbutton,Label,StringVar,LabelFrame
class cnfframe(Frame):
    def __init__(self, master=None,ifpopen=False, cnf={}, **kw):
        super().__init__(master=master, cnf=cnf, **kw)
        self.ifpopen=ifpopen
        self.cnftitle()
        self.get_options()
        self.cnfreset()
        self.cnfexec()
    def cnftitle(self):
        self.titleframe=Frame(self.master)
        Label(self.titleframe,text='pyintaller').pack(side='left')
        self.titleframe.pack()
    def get_options(self):
        from json import load
        with open(OPTION_PATH) as f:
            options=load(f)
            self.bool_like=options["bool_like"]
            self.str_like=options["str_like"]
        self.cnf_bool_like()
        self.cnf_str_like()
    def cnfreset(self):
        def repyi():
            rewrite()
            bt.set('成\n功')
            b_re['state']='disabled'
        bt=StringVar();bt.set('重\n置')
        b_re=Button(self.titleframe,width=0,foreground='#000',disabledforeground='black',relief='groove',font=('黑体',6,),textvariable=bt,command=repyi)
        b_re.pack()
    def cnfexec(self):
        def pyint_exec():
            bool_like=''
            for key,val in self.bool_like.items():
                cmd_str=self.boolvars[key].get()+" "
                bool_like+=cmd_str
            
            str_like=''
            for key,val in self.str_like.items():
                raw=self.strvars[val].get()
                cmd_str=raw and f'{val} {raw} '
                str_like+=cmd_str
            
            cmd_str=f'"{PYINST_PATH}"{str_like}{bool_like}'
            print(cmd_str)
            os.system(cmd_str)
        Button(self,text='ok',command=pyint_exec).pack()
    def cnf_bool_like(self):
        self.boolvars={}
        for key,val in self.bool_like.items():
            self.boolvars[key]=StringVar(self)
            default,option=val
            self.boolvars[key].set(default)
            Checkbutton(self.titleframe,text=key,onvalue=option,offvalue=default,variable=self.boolvars[key]).pack(side='left')
    def cnf_str_like(self):
        self.strvars={}
        for key,val in self.str_like.items():
            self.strvars[val]=StringVar(self)
            laberframe=LabelFrame(self,text=key,labelanchor="n")
            Entry(laberframe,textvariable=self.strvars[val]).pack(PACK_CNF)
            laberframe.pack(fill="x")


if __name__=="__main__":
    root=Tk()
    cnfframe(root,cnf=STYLE_CNF).pack(PACK_CNF)
    root.mainloop()
from tkinter import Tk,Text,Listbox
from tkinter.ttk import Scrollbar,Frame,Entry,LabelFrame
import os,sys

def display(item):
    text.delete(1.0,"end")
    h=os.popen(f"{sys.executable} -c help({item})").read()
    text.insert(1.0,h)
def listshow():
    entry.delete(0,"end")
    select=listbox.get("active")
    display(select)
    entry.insert(0,select)
root=Tk("help")
f1=Frame(root)
labelframe=LabelFrame(f1,text="search",labelanchor="w")
entry=Entry(labelframe)
entry.bind("<Return>",lambda x:display(entry.get()))
entry.pack(side="left",fill="x",expand=True)
labelframe.pack()
scrollbar=Scrollbar(f1)
scrollbar.pack(side="right",fill="y"#,expand=True
)
text=Text(f1)
text.config(yscrollcommand=scrollbar.set,foreground="#003",background="#999")
scrollbar.config(command=text.yview)
text.pack(fill="both",expand=True #!useless
)
f1.pack(side="left",expand=True,fill="both")

f2=Frame(root)
listbox=Listbox(f2)
for i in dir(__builtins__):
    listbox.insert("end",i#,command=lambda:display(i)
    )
listbox.bind("<Button-3>",lambda x:listshow())
listbox.bind("<Double-Button-1>",lambda x:listshow())
scrollbarlist=Scrollbar(f2)
scrollbarlist.pack(side="right",fill="y")
listbox.config(yscrollcommand=scrollbarlist.set)
scrollbarlist.config(command=listbox.yview)

listbox.pack(fill="y",expand=True)
f2.pack(side="right",expand=True,fill="y")
root.mainloop()
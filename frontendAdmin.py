import bend
from tkinter import *

obj=bend.data()

window=Tk()
window.title('RABO')
window.configure(background='dodger blue')
window.resizable(0,0)

def select(event):
    global item
    index=d.curselection()
    item=d.get(index)
    e1.delete(0,END)
    e1.insert(0,item[1])
    e2.delete(0,END)
    e2.insert(0,item[2])
    e4.delete(0,END)
    e4.insert(0,item[3])
    e3.delete(0,END)
    e3.insert(0,item[4])
    e5.delete(0,END)
    e5.insert(0,item[0])
    e6.delete(0,END)
    try:
        e6.insert(0,item[5])
    except IndexError as e:
        e6.insert(0,"")
    

def update():
    obj.update(item[0],e1.get(),e2.get(),e4.get(),e3.get(),e6.get())
    d.delete(0,END)
    d.insert(END,"Updated")

def delete():
    obj.delete(item[0])
    vall()

def vall():
    d.delete(0,END)
    for i in obj.vall():
        d.insert(0,i)
        
def view_students():
    import frontendAdmin2
def search():
    d.delete(0,END)
    for i in obj.search(e1.get(),e2.get(),e4.get(),e3.get()):
        d.insert(0,i)

def add():
    obj.add(e1.get(),e2.get(),e4.get(),e3.get(),e6.get())
    d.delete(0,END)
    d.insert(0,"Added")
    
#----------------------------------------------------------------------------------------------------------------------
class HoverButton(Button):
    def __init__(self, master, **kw):
        Button.__init__(self,master=master,**kw)
        self.defaultBackground = self["background"]
        self.bind("<Enter>", self.on_enter)
        self.bind("<Leave>", self.on_leave)

    def on_enter(self, e):
        self['background'] = self['activebackground']

    def on_leave(self, e):
        self['background'] = self.defaultBackground


#------------------------------------------------------------------------------------------------------------------

l1=Label(window,text="Course",background='dodger blue')
l1.grid(row=0,column=0)

l2=Label(window,text="Author",background='dodger blue')
l2.grid(row=0,column=3)

l3=Label(window,text="Edition",background='dodger blue')
l3.grid(row=1,column=0)

l4=Label(window,text="Quantity availabel",background='dodger blue')
l4.grid(row=1,column=3)

l5=Label(window,text="id",background="dodger blue")
l5.grid(row=2,column=0)

l6=Label(window,text="Link",background="dodger blue")
l6.grid(row=2,column=3)
#------------------------------------------------------------------------------------------------------------------
co=StringVar()
#course
e1=Entry(window,background='light pink',textvariable=co)
e1.grid(row=0,column=1)

au=StringVar()
#author
e2=Entry(window,background='light pink',textvariable=au)
e2.grid(row=0,column=4)

ed=StringVar()
#edition
e3=Entry(window,background='light pink',textvariable=ed)
e3.grid(row=1,column=1)

qu=StringVar()
#quantity
e4=Entry(window,background='light pink',textvariable=qu)
e4.grid(row=1,column=4)

ID=StringVar()
#id
e5=Entry(window,background="light pink",textvariable=ID)
e5.grid(row=2,column=1)

li=StringVar()
#reg
e6=Entry(window,background="light pink",textvariable=li)
e6.grid(row=2,column=4)
#--------------------------------------------------------------------------------------------------------------------
d=Listbox(window,width=40,height=10,background='light pink')
d.grid(row=3,column=0,rowspan=7,columnspan=2,sticky='ew')
#---------------------------------------------------------------------------------------------------------------------
b1=HoverButton(window,text="View All",background='deep sky blue', activebackground='cyan',command=vall)
b1.grid(row=3,column=4,sticky='ew')

b2=HoverButton(window,text="Search",background='deep sky blue', activebackground='cyan',command=search)
b2.grid(row=4,column=4,sticky='ew')

b3=HoverButton(window,text="Add",background='deep sky blue', activebackground='cyan',command=add)
b3.grid(row=5,column=4,sticky='ew')

b4=HoverButton(window,text="Update",background='deep sky blue', activebackground='cyan',command=update)
b4.grid(row=6,column=4,sticky='ew')

b4=HoverButton(window,text="Delete",background='deep sky blue', activebackground='cyan',command=delete)
b4.grid(row=7,column=4,sticky='ew')

b5=HoverButton(window,text="Close",background='deep sky blue', activebackground='cyan',command=window.destroy)
b5.grid(row=8,column=4,sticky='ew')

b6=HoverButton(window,text="View Students",background="deep sky blue",activebackground="cyan",command=view_students)
b6.grid(row=9,column=4,sticky="ew")
#-------------------------------------------------------------------------------------------------------------------------
sb=Scrollbar(window,background='red2')
sb.grid(row=3,column=3,columnspan=1,rowspan=7,sticky='ns')

d.configure(yscrollcommand=sb.set)
sb.configure(command=d.yview)

window.rowconfigure(1,weight=10)
window.columnconfigure(1,weight=10)

d.bind("<<ListboxSelect>>",select)

window.mainloop()

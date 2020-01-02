import bend,recordBend,datetime as dt
from tkinter import *
import webbrowser


book=bend.data()
stud=recordBend.Records()

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

def vall():
    d.delete(0,END)
    for i in book.vall():
        d.insert(0,i)
    

def reg():
    def ok():
        book.reg(int(qu.get()))
        print(sname.get(),passwd.get())
        stud.register(sname.get(),passwd.get(),co.get(),au.get(),ed.get(),dt.datetime.now())
        authenticate.destroy()
        
    authenticate=Toplevel()
    authenticate.title("Authentication")
    
    name=Label(authenticate,text="Type your name: ")
    name.grid(row=0,column=0)
    
    sname=StringVar()
    name_entry=Entry(authenticate,textvariable=sname,background="#ffffff")
    name_entry.grid(row=0,column=1)
    
    password=Label(authenticate,text="Password here: ")
    password.grid(row=1,column=0)
    
    passwd=StringVar()
    password_entry=Entry(authenticate,textvariable=passwd,background="#ffffff")
    password_entry.grid(row=1,column=1)
    
    b=Button(authenticate,text="Ok",command=ok)
    b.grid(row=2,column=1,columnspan=2)
    
    authenticate.mainloop()
    
    d.delete(0,END)
    d.insert(END,"Registered")

def acs():
    for i in book.acs(item[0]):
        for j in i:
            webbrowser.open(j)
            break
        break

def search():
    d.delete(0,END)
    
    for i in book.search(co.get(),au.get(),qu.get(),ed.get()):
        d.insert(0,i)

#-----------------------------------------------------
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


#------------------------------------------------------

l1=Label(window,text="Course",background='dodger blue')
l1.grid(row=0,column=0)

l2=Label(window,text="Author",background='dodger blue')
l2.grid(row=0,column=3)

l3=Label(window,text="Edition",background='dodger blue')
l3.grid(row=1,column=0)

l4=Label(window,text="Quantity availabel",background='dodger blue')
l4.grid(row=1,column=3)
#-------------------------------------------
co=StringVar()
e1=Entry(window,background='light pink',textvariable=co)
e1.grid(row=0,column=1)

au=StringVar()
e2=Entry(window,background='light pink',textvariable=au)
e2.grid(row=0,column=4)

ed=StringVar()
e3=Entry(window,background='light pink',textvariable=ed)
e3.grid(row=1,column=1)

qu=StringVar()
e4=Entry(window,background='light pink',textvariable=qu)
e4.grid(row=1,column=4)
#------------------------------------------
d=Listbox(window,width=40,height=10,background='light pink')
d.grid(row=2,column=0,rowspan=5,columnspan=2,sticky='ew')
#------------------------------------------
b1=HoverButton(window,text="View All",background='deep sky blue', activebackground='cyan',command=vall)
b1.grid(row=2,column=4,sticky='ew')

b2=HoverButton(window,text="Search",background='deep sky blue', activebackground='cyan',command=search)
b2.grid(row=3,column=4,sticky='ew')

b3=HoverButton(window,text="Register",background='deep sky blue', activebackground='cyan',command=reg)
b3.grid(row=4,column=4,sticky='ew')

b4=HoverButton(window,text="Close",background='deep sky blue', activebackground='cyan',command=window.destroy)
b4.grid(row=6,column=4,sticky='ew')

b5=HoverButton(window,text='Access',background='deep sky blue',activebackground='cyan',command=acs)
b5.grid(row=5,column=4,sticky='ew')
#-----------------------------------------
sb=Scrollbar(window,background='red2')
sb.grid(row=2,column=3,columnspan=1,rowspan=5,sticky='ns')

d.configure(yscrollcommand=sb.set)
sb.configure(command=d.yview)

window.rowconfigure(1,weight=10)
window.columnconfigure(1,weight=10)

d.bind("<<ListboxSelect>>",select)

window.mainloop()

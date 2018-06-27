#ques1

import tkinter
from  tkinter import *

def write_text():
    print("HELLO WORLD!!")


container=tkinter.Tk()
container.title("helloworld")
container.geometry("500x500")
'''
Label(container,text="write here",width=20,height=2).grid(row=0)
e1=Entry(container,bg='yellow').grid(row=0,column=1)

btn=tkinter.Button(container,text='EXIT',bg='red',width=7,command=container.quit)
btn.place(x=100,y=50)

#ques2


btn1 = tkinter.Button(container,text="CLICK",bg='red',command=write_text)
btn1.place(x=150,y=50)
mainloop()
'''
#ques3
'''

frame=Frame(container)
frame.pack()
actual=" ASSIGNMENT OF GUI"
def demo_label(label):
    label.config(text=str(actual))

label=Label(frame)
label.pack()
demo_label(label)

redbutton=Button(frame,text='EXIT',command=container.quit)
redbutton.pack(side=RIGHT)
greenbutton=Button(frame,text='DISPLAY',command=write_text)
greenbutton.pack(side=LEFT)


mainloop()
'''

#ques4

Label(container, text="First Name").grid(row=0)
Label(container, text="Last Name").grid(row=1)

e1 = Entry(container)
e2 = Entry(container)

e1.grid(row=0, column=1)
e2.grid(row=1, column=1)
container.mainloop()

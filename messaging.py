from tkinter import *
import sms_backend
import datetime as time

def get_selected_row(event):
    global selected_tuple
    index=list1.curselection()[0]
    selected_tuple=list1.get(index)
    e1.delete(0,END)
    e1.insert(END,selected_tuple[1])
    e2.delete(0,END)
    e2.insert(END,selected_tuple[2])

def view_command():
    list1.delete(0,END)
    for row in sms_backend.view():
        list1.insert(END,row)

def search_command():
    list1.delete(0,END)
    for row in sms_backend.search(content_text.get(),reciepient_number_text.get(), Date_text.get()):
        list1.insert(END,row)

def new_message():
    reciepient1 = e1.get()
    message1 = e2.get()
    sms_backend.send_sms(reciepient1, message1)
    sms_backend.insert(content_text.get(),reciepient_number_text.get())
    list1.delete(0,END)
    list1.insert(END,(content_text.get(),reciepient_number_text.get()))

def delete_command():
    sms_backend.delete(selected_tuple[0])
    list1.delete(0,END)
    for row in sms_backend.view():
        list1.insert(END,row)

def open_contacts_command():
    open 

window=Tk()

window.wm_title("sms_app")

l1=Label(window,text="content")
l1.grid(row=0,column=0)

l2=Label(window,text="reciepient_number")
l2.grid(row=0,column=2)

l3=Label(window, text = "Date")
l3.grid(row=1, column = 0)

content_text=StringVar()
e1=Entry(window,textvariable=content_text)
e1.grid(row=0,column=1)

reciepient_number_text=StringVar()
e2=Entry(window,textvariable=reciepient_number_text)
e2.grid(row=0,column=3)

Date_text=StringVar()
e3 = Entry(window, textvariable = Date_text)
e3.grid(row = 1, column = 1)

list1=Listbox(window, height=6,width=35)
list1.grid(row=2,column=0,rowspan=6,columnspan=2)

sb1=Scrollbar(window)
sb1.grid(row=2,column=2,rowspan=6)

list1.configure(yscrollcommand=sb1.set)
sb1.configure(command=list1.yview)

list1.bind('<<ListboxSelect>>',get_selected_row)

b1=Button(window,text="View all", width=12,command=view_command)
b1.grid(row=2,column=3)

b2=Button(window,text="Search entry", width=12,command=search_command)
b2.grid(row=3,column=3)

b3=Button(window,text="Send SMS", width=12,command=new_message)
b3.grid(row=4,column=3)

# b4=Button(window,text="View All", width=12,command=view_command)
# b4.grid(row=5,column=3)

b5=Button(window,text="Delete selected", width=12,command=delete_command)
b5.grid(row=6,column=3)

b6=Button(window, text = "Open Contacts", width = 12, command = open_contacts_command)
b6.grid(row=7, column=3)

b7=Button(window,text="Close", width=12,command=window.destroy)
b7.grid(row=8,column=3)

window.mainloop()

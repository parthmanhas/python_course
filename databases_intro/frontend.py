from tkinter import *
import backend

def get_selected_row(event):
	global selected_tuple
	try:
		index=lb1.curselection()[0]
		selected_tuple=lb1.get(index)
		print(selected_tuple)
		e1.delete(0,END)
		e1.insert(END,selected_tuple[1])
		e2.delete(0,END)
		e2.insert(END,selected_tuple[2])
		e3.delete(0,END)
		e3.insert(END,selected_tuple[3])
		e4.delete(0,END)
		e4.insert(END,selected_tuple[4])
	except IndexError:
		pass


def view_all():
	lb1.delete(0,END)
	for row in backend.view_all():
		lb1.insert(END,row)

def search_entry():
	lb1.delete(0,END)
	for i in backend.search_entry(title.get(),author.get(),year.get(),isbn.get()):
		lb1.insert(END,i)

def add_entry():
	backend.add_entry(title.get(),author.get(),year.get(),isbn.get())
	lb1.delete(0,END)
	lb1.insert(END,(title.get(),author.get(),year.get(),isbn.get()))

def update():
	backend.update(selected_tuple[0],title.get(),author.get(),year.get(),isbn.get())

def delete():
	backend.delete(selected_tuple[0])
	view_all()


window = Tk()

window.wm_title("BookStore")



l1=Label(window,text="Title")
l1.grid(row=0,column=0)

l1=Label(window,text="Year")
l1.grid(row=1,column=0)

l1=Label(window,text="Author")
l1.grid(row=0,column=2)

l1=Label(window,text="ISBN")
l1.grid(row=1,column=2)

title = StringVar()
e1=Entry(window,textvariable=title)
e1.grid(row=0,column=1)

year = StringVar()
e2=Entry(window,textvariable=year)
e2.grid(row=1,column=1)

author = StringVar()
e3=Entry(window,textvariable=author)
e3.grid(row=0,column=3)

isbn = StringVar()
e4=Entry(window,textvariable=isbn)
e4.grid(row=1,column=3)

lb1 = Listbox(window,height=6,width=35)
lb1.grid(row=2,column=0,rowspan=6,columnspan=2)

lb1.bind('<<ListboxSelect>>',get_selected_row)

sb1 = Scrollbar(window)
sb1.grid(row=2,column=2,rowspan=6)

lb1.configure(yscrollcommand=sb1.set)
sb1.configure(command=lb1.yview)


b1= Button(window,text="View All",width=11,command=view_all)
b1.grid(row=2,column=3)

b1= Button(window,text="Search Entry",width=11,command=search_entry)
b1.grid(row=3,column=3)

b1= Button(window,text="Add Entry",width=11,command=add_entry)
b1.grid(row=4,column=3)

b1= Button(window,text="Update",width=11,command=update)
b1.grid(row=5,column=3)

b1= Button(window,text="Delete",width=11,command=delete)
b1.grid(row=6,column=3)

b1= Button(window,text="Close",width=11,command=window.destroy)
b1.grid(row=7,column=3)

window.mainloop()
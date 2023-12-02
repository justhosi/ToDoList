from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox

#Creat windows
windows = Tk()
#Set the title
windows.title("To Do List")


def add_to_do():
    pass



#Create input point for to do list and position it
entry1 = Entry(windows, width=35, font=("ubuntu", 13))
entry1.grid(row=0, column=0, padx=25, pady=5)
#Create a button for adding a task and position it
btn_add = Button(windows, text="Add to list", command=add_to_do)
btn_add.grid(row=0, column=2, pady=5)
#Create a button for deleting a task and position it
btn_del = Button(windows, text="Delete", command="")
btn_del.grid(row=1, column=2, padx=5, pady=5)
#Create a button for deleting all the tasks and position it
btn_del_all = Button(windows, text="Clear list", command="")
btn_del_all.grid(row=2, column=2, padx=5, pady=5)
#Create a button to show the number of current tasks
btn_show_number = Button(windows, text="Active tasks", command="")
btn_show_number.grid(row=3, column=2, padx=5, pady=5)
#Create a label to show the active tasks on it
lb_tasks = Label(windows, text="", font=("ubuntu, 15"))
lb_tasks.grid(row=1, column=0, padx=5, pady=5) 
#Create a edit button
btn_edit =Button(windows, text="Edit task", command="")
btn_edit.grid(row=4, column=2, padx=5, pady=5)
#Create an "About" button
btn_about =  Button(windows, text="About", command="")
btn_about.grid(row=5, column=2, padx=5, pady=5)
#Create an exit button
btn_exit = Button(windows, text="Exit", command="")
btn_exit.grid(row=6, column=2, padx=5, pady=5)

#Creat a list box
list_box = Listbox(windows, font=("ubuntu, 13"), height=30, width=30)











#Set windows size
windows.geometry("500x650")
#start the main loop
windows.mainloop()
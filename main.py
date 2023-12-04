from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox
from tkinter.simpledialog import askstring

#Creat windows
windows = Tk()
#Set the title
windows.title("To Do List")


#Create a warning for clear all the tasks
def show_warning():
    messagebox.showwarning(title="Warning", message="Are you sure you want\nto clear all the tasks?")
#Create an info message box
def show_info():
    messagebox.showinfo(title="About us", message="Programmer: Hosi Mohi\nEmail: mohamadzadeh@outlook.com")

#function to add the user task entry to the list
def add_to_do():
    user_input = entry1.get()
    list_box.insert(END, user_input)

def del_task():
    selected_task_index = list_box.curselection()
    if not selected_task_index:
        messagebox.showwarning("No Task Selected", "Please select a task to edit.")
        return

    list_box.delete(ACTIVE)

def del_all():
    show_warning()
    list_box.delete(0, END)
    lb_tasks.config(text="The list is cleared")

def show_number():
    n = list_box.index("end")
    lb_tasks.config(text="There is {} task(s) in the list".format(str(n)))

def edit_task():
    selected_task_index = list_box.curselection()

    if not selected_task_index:
        messagebox.showwarning("No Task Selected", "Please select a task to edit")
        return

    selected_task_index = selected_task_index[0]
    current_text = list_box.get(selected_task_index)

    new_text = askstring("Edit Task", "Edit the task:", initialvalue=current_text)

    if new_text is not None:
        list_box.delete(selected_task_index)
        list_box.insert(selected_task_index, new_text)

    

def show_about():
    show_info()

def exit_app():
    windows.destroy()

#Create input point for to do list and position it
entry1 = Entry(windows, width=35, font=("ubuntu", 13))
entry1.pack()
entry1.place(x=10, y=10)
#Create a button for adding a task and position it
btn_add = Button(windows, text="Add to list", command=add_to_do)
btn_add.pack()
btn_add.place(x=390, y=10)
#Create a button for deleting a task and position it
btn_del = Button(windows, text="Delete", command=del_task)
btn_del.pack()
btn_del.place(x=390, y=50)
#Create a button for deleting all the tasks and position it
btn_del_all = Button(windows, text="Clear list", command=del_all)
btn_del_all.pack()
btn_del_all.place(x=390, y=90)
#Create a button to show the number of current tasks
btn_show_number = Button(windows, text="Active tasks", command=show_number)
btn_show_number.pack()
btn_show_number.place(x=390, y=130)
#Create a label to show the active tasks on it
lb_tasks = Label(windows, text="", font=("ubuntu", 15), background="white", foreground="red")
lb_tasks.pack()
lb_tasks.place(x=10,y=45 )
#Create a edit button
btn_edit =Button(windows, text="Edit task", command=edit_task)
btn_edit.pack()
btn_edit.place(x=390, y=170)
#Create an "About" button
btn_about =  Button(windows, text="About", command=show_about)
btn_about.pack()
btn_about.place(x=390, y=210)

#Create an exit button
btn_exit = Button(windows, text="Exit", command=exit_app)
btn_exit.pack()
btn_exit.place(x=390, y=250)

#Creat a list box
list_box = Listbox(windows, font=("ubuntu, 13"),bg="dark grey", fg="yellow", height=30, width=32)
list_box.pack()
list_box.place(x=10, y=80)











#Set windows size
windows.geometry("500x750")
#start the main loop
windows.mainloop()
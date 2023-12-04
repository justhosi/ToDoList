from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox
from tkinter.simpledialog import askstring
import pickle


#Creat windows
windows = Tk()
#Set the title
windows.title("To Do List")

#Create a warning for clear all the tasks
def show_warning():
    resault = messagebox.askyesno(title="Warning", message="Are you sure you want\nto clear all the tasks?")
    return resault
#Create an info message box
def show_info():
    messagebox.showinfo(title="About us", message="Programmer: Hosi Mohi\nEmail: mohamadzadeh@outlook.com")

#function to add the user task entry to the list
def add_to_do():
    user_input = entry1.get()
    list_box.insert(END, user_input)
#Function to delete selected task
def del_task():
    selected_task_index = list_box.curselection()
    if not selected_task_index:
        messagebox.showwarning("No Task Selected", "Please select a task to edit.")
        return

    list_box.delete(ACTIVE)
#Function to clear task list
def del_all():
    if show_warning() is True:
        list_box.delete(0, END)
        lb_tasks.config(text="The list is cleared")
    else:
        return
#Function to show the number of tasks in hand
def show_number():
    n = list_box.index("end")
    lb_tasks.config(text="There is {} task(s) in the list".format(str(n)))
#Function for edit selected task
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

    
#Function to show information about programmer
def show_about():
    show_info()
#Function to save all tasks
def save_tasks():
    content = list_box.get(0, END)
    output_file = open("./data/cache.dat", "wb")
    pickle.dump(content, output_file)

#To save and exit the app
def exit_app():
    save_tasks()
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
#Create a save button
btn_save= Button(windows, text="save", command= save_tasks)
btn_save.pack()
btn_save.place(x=390, y=250)
#Create an exit button
btn_exit = Button(windows, text="Exit", command=exit_app)
btn_exit.pack()
btn_exit.place(x=390, y=290)

#Creat a list box
list_box = Listbox(windows, font=("ubuntu, 13"),bg="dark grey", fg="yellow", height=30, width=32)
list_box.pack()
list_box.place(x=10, y=80)
#Load the data from cache to the list
input_file = open("./data/cache.dat", "rb")
conntent = pickle.load(input_file)
for i in conntent:
    list_box.insert(END, i)



#Set windows size
windows.geometry("500x800")
windows.maxsize(500, 800)
windows.minsize(500, 800)
#start the main loop
windows.mainloop()
from logging import root
import pymongo
from pymongo import collection
from tkinter import *
import tkinter as tk
import tkinter.messagebox as MessageBox
from tkinter import ttk

# database connection


myclient = pymongo.MongoClient()
# ("mongodb+srv://khushi22p:khushi@cluster0.0pihvow.mongodb.net/test")
mydb = myclient["enrollmentsystem"]
mycol = mydb["students"]

# create GUI
root = Tk()
root.geometry("400x400")
root.title("MongoDB CRUD App")


# define functions for CRUD operations
def insert():
    name = name_entry.get()
    email = email_entry.get()
    existing_data = mycol.find_one({"$or": [{"name": name}, {"email": email}]})
    if existing_data:
        existing_name = existing_data.get("name", "")
        existing_email = existing_data.get("email", "")
        if name == existing_name and email == existing_email:
            MessageBox.showerror(
                "Error", f"Data with name '{name}' and email '{email}' already exists."
            )
        elif name == existing_name:
            MessageBox.showerror("Error", f"Data with name '{name}' already exists.")
        else:
            MessageBox.showerror("Error", f"Data with email '{email}' already exists.")
    else:
        new_data = {"name": name, "email": email, "course": course_entry.get()}
        mycol.insert_one(new_data)
        MessageBox.showinfo("Success", "Data inserted successfully.")


def read():
    search_data = {"name": name_entry.get()}
    result = mycol.find_one(search_data)
    if result:
        MessageBox.showinfo(
            "Result",
            f"Name: {result['name']}\nEmail: {result['email']}\nCourse: {result['course']}",
        )
    else:
        MessageBox.showerror("Error", "Data not found.")


def update():
    search_data = {"name": name_entry.get()}
    update_data = {"$set": {"email": email_entry.get(), "course": course_entry.get()}}
    result = mycol.update_one(search_data, update_data)
    if result.modified_count > 0:
        MessageBox.showinfo("Success", "Data updated successfully.")
    else:
        MessageBox.showerror("Error", "Data not found.")


def delete():
    search_data = {"name": name_entry.get()}
    result = mycol.delete_one(search_data)
    if result.deleted_count > 0:
        MessageBox.showinfo("Success", "Data deleted successfully.")
    else:
        MessageBox.showerror("Error", "Data not found.")


# create form fields and buttons
name_label = Label(root, text="Name")
name_label.pack()
name_entry = Entry(root)
name_entry.pack()

email_label = Label(root, text="Email")
email_label.pack()
email_entry = Entry(root)
email_entry.pack()

course_label = Label(root, text="Course")
course_label.pack()
course_entry = Entry(root)
course_entry.pack()

insert_button = Button(root, text="Insert", command=insert)
insert_button.pack()

read_button = Button(root, text="Read", command=read)
read_button.pack()

update_button = Button(root, text="Update", command=update)
update_button.pack()

delete_button = Button(root, text="Delete", command=delete)
delete_button.pack()

root.mainloop()

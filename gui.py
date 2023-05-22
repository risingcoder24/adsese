from tkinter import *
import tkinter.messagebox as MessageBox
import mysql.connector as mysql

def insert():
    id=e_id.get()
    stateName=e_stateName.get()
    capitalCity=e_capitalCity.get()

    if(id=="" or stateName=="" or capitalCity==""):
        MessageBox.showinfo("Insert Status","All fields are required")
    else:
        con=mysql.connect(host="localhost",user="system",password="system",database="states&capital")
        cursor=con.cursor()
        cursor.execute("insert into StateCapital values ('" + id + "', '"+stateName + "', '"+capitalCity+"')")
        cursor.execute("commit")

        e_stateName.delete(0,"end")
        e_capitalCity.delete(0,"end")
        show()
        MessageBox.showinfo("Insert Status","Inserted Successfully")
        con.close()

def delete():
    if(e_id.get()==""):
        MessageBox.showinfo("Delete Status","State Id is compulsary for deleting")
    else:
        con=mysql.connect(host="localhost",user="root",password="knp22104",database="states&capital")
        cursor=con.cursor()
        cursor.execute("delete from StateCapital where id='" + e_id.get() + "'")
        cursor.execute("commit")

        e_stateName.delete(0,"end")
        e_capitalCity.delete(0,"end")
        show()
        MessageBox.showinfo("Delete Status","Deleted Successfully")
        con.close()

def update():
    id=e_id.get()
    stateName=e_stateName.get()
    capitalCity=e_capitalCity.get()

    if(id==""):
        MessageBox.showinfo("Update Status","All fields are required")
    else:
        con=mysql.connect(host="localhost",user="root",password="knp22104",database="states&capital")
        cursor=con.cursor()
        cursor.execute("update StateCapital set stateName='"+stateName+"', capitalCity='"+capitalCity+"'" +"where id="+ id )
        cursor.execute("commit")

        e_stateName.delete(0,"end")
        e_capitalCity.delete(0,"end")
        show()
        MessageBox.showinfo("Update Status","Update Successfully")
        con.close()

def get():
    if(e_id.get()==""):
        MessageBox.showinfo("Fetch Status","State Id is compulsary for deleting")
    else:
        con=mysql.connect(host="localhost",user="root",password="knp22104",database="states&capital")
        cursor=con.cursor()
        cursor.execute("select * from StateCapital where id="+e_id.get())
        rows=cursor.fetchall()

        for row in rows:
            e_stateName.insert(0,row[1])
            e_capitalCity.insert(0,row[2])

        con.close()

def show():
    con=mysql.connect(host="localhost",user="root",password="knp22104",database="states&capital")
    cursor=con.cursor()
    cursor.execute("select * from StateCapital")
    rows=cursor.fetchall()
    list.delete(0,list.size())

    for row in rows:
        insertData=str(row[0])+'     '+row[1]
        list.insert(list.size()+1,insertData)
    con.close()

root=Tk()
root.geometry("600x300")
root.title("Python+Tkinter+Mysql")

id = Label(root,text='Enter State Id',font=('bold',10))
id.place(x=20,y=30)

stateName = Label(root,text='Enter State Name',font=('bold',10))
stateName.place(x=20,y=60)

capitalCity = Label(root,text='Enter State Capital',font=('bold',10))
capitalCity.place(x=20,y=90)

e_id=Entry()
e_id.place(x=150,y=30)

e_stateName=Entry()
e_stateName.place(x=150,y=60)

e_capitalCity=Entry()
e_capitalCity.place(x=150,y=90)

insert=Button(root,text="Insert",font=("italic",10),bg="white",command=insert)
insert.place(x=20,y=140)

delete=Button(root,text="Delete",font=("italic",10),bg="white",command=delete)
delete.place(x=70,y=140)

update=Button(root,text="Update",font=("italic",10),bg="white",command=update)
update.place(x=130,y=140)

get=Button(root,text="Get",font=("italic",10),bg="white",command=get)
get.place(x=190,y=140)

list =Listbox(root)
list.place(x=290,y=30)
show()
root.mainloop()

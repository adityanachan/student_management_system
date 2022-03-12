import tkinter as tk
from tkinter import ttk, messagebox
import mysql.connector
from tkinter import *
def GetValue(event):
    e1.delete(0, END)
    e2.delete(0, END)
    e3.delete(0, END)
    e4.delete(0, END)
    e5.delete(0, END)
    e6.delete(0, END)
    e7.delete(0, END)
    row_id = listBox.selection()[0]
    select = listBox.set(row_id)
    e1.insert(0, select['id'])
    e2.insert(0, select['sname'])
    e3.insert(0, select['email'])
    e4.insert(0, select['gender'])
    e5.insert(0, select['contact'])
    e6.insert(0, select['dob'])
    e7.insert(0, select['address'])
def Add():
    studroll = e1.get()
    studname = e2.get()
    studemail = e3.get()
    studgender = e4.get()
    studcontact = e5.get()
    studdob = e6.get()
    studaddress = e7.get()

    mysqldb = mysql.connector.connect(host="localhost", user="root", password="nachan", database="payroll13")
    mycursor = mysqldb.cursor()  #tem work area

    try:
        sql = "INSERT INTO  registation (id,sname,email,gender,contact,dob,address) VALUES (%s, %s, %s, %s,%s,%s,%s)"
        val = (studroll, studname, studemail,studgender,studcontact,studdob,studaddress)
        mycursor.execute(sql, val)
        mysqldb.commit()    #per save data
        lastid = mycursor.lastrowid
        messagebox.showinfo("information", "Student Data inserted successfully...")
        e1.delete(0, END)
        e2.delete(0, END)
        e3.delete(0, END)
        e4.delete(0, END)
        e5.delete(0, END)
        e6.delete(0, END)
        e7.delete(0, END)
        e1.focus_set()
    except Exception as e:
        print(e)
        mysqldb.rollback()  #data changes
        mysqldb.close()
def update():
    studroll = e1.get()
    studname = e2.get()
    studemail = e3.get()
    studgender = e4.get()
    studcontact = e5.get()
    studdob = e6.get()
    studaddress = e7.get()
    mysqldb = mysql.connector.connect(host="localhost", user="root", password="nachan", database="payroll13")
    mycursor = mysqldb.cursor()
    try:
        sql = "Update  registation set sname= %s,email= %s,gender= %s,contact=%s,dob=%s,address=%s where id= %s"
        val = (studname, studemail,studgender,studcontact,studdob,studaddress,studroll)
        mycursor.execute(sql, val)
        mysqldb.commit()
        lastid = mycursor.lastrowid
        messagebox.showinfo("information", "Record Updateddddd successfully...")

        e1.delete(0, END)
        e2.delete(0, END)
        e3.delete(0, END)
        e4.delete(0, END)
        e5.delete(0, END)
        e6.delete(0, END)
        e7.delete(0, END)
        e1.focus_set()
    except Exception as e:
        print(e)
        mysqldb.rollback()
        mysqldb.close()
def delete():
    studroll = e1.get()
    mysqldb = mysql.connector.connect(host="localhost", user="root", password="nachan", database="payroll13")
    mycursor = mysqldb.cursor()
    try:
        sql = "delete from registation where id = %s"
        val = (studroll,)
        mycursor.execute(sql, val)
        mysqldb.commit()
        lastid = mycursor.lastrowid
        messagebox.showinfo("information", "Record Deleteeeee successfully...")
        e1.delete(0, END)
        e2.delete(0, END)
        e3.delete(0, END)
        e4.delete(0, END)
        e5.delete(0, END)
        e6.delete(0, END)
        e7.delete(0, END)
        e1.focus_set()
    except Exception as e:
        print(e)
        mysqldb.rollback()
        mysqldb.close()

def show():
    mysqldb = mysql.connector.connect(host="localhost", user="root", password="nachan", database="payroll13")
    mycursor = mysqldb.cursor()
    mycursor.execute("SELECT id,sname,email,gender,contact,dob,address FROM registation")
    records = mycursor.fetchall()
    print(records)

    for i, (id,sname,email,gender,contact,dob,address) in enumerate(records, start=1):
        listBox.insert("", "end", values=(id,sname,email,gender,contact,dob,address))
        mysqldb.close()
root = Tk()
root.geometry("1550x800+0+0")
title = Label(root, text="Student Management System", bd=10, relief=GROOVE,
                      font=('times new roman', 40, "bold"), bg='black', fg='red').place(x=400,y=0)
root.configure(background='pink')
global e1
global e2
global e3
global e4
global e5
global e6
global e7
tk.Label(root, text="Roll No",bg='pink', fg='black',font=('times new roman', 20, 'bold')).place(x=10, y=90)
Label(root, text="Name",bg='pink', fg='black',font=('times new roman', 20, 'bold')).place(x=10, y=130)
Label(root, text="Email",bg='pink', fg='black',font=('times new roman', 20, 'bold')).place(x=10, y=170)
Label(root, text="Gender",bg='pink', fg='black',font=('times new roman', 20, 'bold')).place(x=10, y=210)
Label(root, text="Contact",bg='pink', fg='black',font=('times new roman', 20, 'bold')).place(x=400, y=90)
Label(root, text="Dob",bg='pink', fg='black',font=('times new roman', 20, 'bold')).place(x=400, y=130)
Label(root, text="Address",bg='pink', fg='black',font=('times new roman', 20, 'bold')).place(x=400, y=170)
e1 = Entry(root,font=('times new roman', 15, 'bold'))
e1.place(x=140, y=95)
e2 = Entry(root,font=('times new roman', 15, 'bold'))
e2.place(x=140, y=135)
e3 = Entry(root,font=('times new roman', 15, 'bold'))
e3.place(x=140, y=175)
e4 = ttk.Combobox(root,font=('times new roman', 13, 'bold'),state='readonly')
e4['values'] = ('Male', 'Female', 'Other')
e4.place(x=140, y=215)
e5 = Entry(root,font=('times new roman', 15, 'bold'))
e5.place(x=530, y=95)
e6 = Entry(root,font=('times new roman', 15, 'bold'))
e6.place(x=530, y=135)
e7 = Entry(root,font=('times new roman', 15, 'bold'))
e7.place(x=530, y=175)

Button(root, text="Add",font=('times new roman',10,'bold'), command=Add, height=2, width=13,bg='grey').place(x=10, y=260)
Button(root, text="Update",font=('times new roman',10,'bold'), command=update, height=2, width=13,bg='grey').place(x=120, y=260)
Button(root, text="Delete", font=('times new roman',10,'bold'),command=delete, height=2, width=13,bg='grey').place(x=230, y=260)

cols = ('id', 'sname', 'email', 'gender','contact','dob','address')
listBox = ttk.Treeview(root, columns=cols, show='headings')

for col in cols:
    listBox.heading(col, text=col)
    listBox.grid(row=1, column=0, columnspan=2)
    listBox.place(x=10, y=340)

show()
listBox.bind('<Double-Button-1>', GetValue)

root.mainloop()
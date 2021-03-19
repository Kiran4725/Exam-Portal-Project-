from tkinter import *
from PIL import ImageTk,Image,ImageDraw,ImageFont
from tkinter import ttk
from tkinter import messagebox
import mysql.connector as my
import random
from Quesitions import *


w=Tk()
w.title("Exam Portal")
w.geometry("1350x700+0+0")
w.config(bg='white')

#============= Login validation ===================

def login():

    user=u_entry.get()
    pas=p_entry.get()

    if(user==""or pas==""):
        messagebox.showerror("show", "Please fill all the information ")


    conn = my.connect(username='root', password='root', host='localhost', database='exam')
    cur = conn.cursor()
    q = "select username,password from regist"
    cur.execute(q)
    records = cur.fetchall()
    for row in records:
        if user == row[0] and pas == row[1]:
            messagebox.showinfo("Show","Login Successfully !")
            w.destroy()
            start(row[0])
            break

    else:
        messagebox.showerror("Show", "Invalid Username and Password !")

    conn.close()

#============= Register frame  & Logic ==============

def regist():

    def Rclick():
        r=roll_entry.get()
        n=name_entry.get()
        c=cb1.get()
        p=p_e.get()

        num = str(random.randint(11111, 99999))
        username = n + num
        # print(username)

        t = [r, n, c, username,p]

        if (n=="" or r=="" or c=="" or p==""or c=="SELECT YEAR"):
            messagebox.showerror("show", "Please fill all the information ")
        else:
            conn = my.connect(user="root", password='root', host='localhost', database='exam')
            cur = conn.cursor()
            #q="create table regist (roll int,name varchar (25),class varchar (25),username varchar (25),password varchar(25));"
            q = "insert into regist (roll,name,class,username,password)values(%s,%s,%s,%s,%s)"
            cur.execute(q, t)
            conn.commit()
            conn.close()
            messagebox.showinfo("Show", "Register successfully \nNote down your UserName  "+ username +"  Password  "+p)
            r_frame.destroy()



    r_frame = Frame(w, bg="#696969")
    r_frame.place(x=430, y=220, height=400, width=400)

    title = Label(r_frame, text="REGISTER",font=("Timeromanes", 20, "bold"),bg="#696969")
    title.place(x=145, y=40)


    roll = Label(r_frame, text="Roll no",bg="#696969",font=("Times", 13, "bold"))
    roll.place(x=50, y=150)
    roll_entry = Entry(r_frame, width=20)
    roll_entry.place(x=50, y=180)

    name = Label(r_frame, text="Name",bg="#696969",font=("Times", 13, "bold"))
    name.place(x=220, y=150)
    name_entry = Entry(r_frame, width=20)
    name_entry.place(x=220, y=180)

    clas = Label(r_frame, text="Class",bg="#696969",font=("Times", 13, "bold"))
    clas.place(x=50, y=240)
    list1=["FIRST YEAR","SECOND YEAR","THIRD YEAR"]
    cb1 = ttk.Combobox(r_frame, width=17,font=("Times", 10, "bold"))
    cb1['value'] = list1
    cb1.place(x=50, y=270)
    cb1.set("SELECT  YEAR")


    password = Label(r_frame, text="Password",bg="#696969",font=("Times", 13, "bold"))
    password.place(x=220, y=240)
    p_e = Entry(r_frame, width=20,show="*")
    p_e.place(x=220, y=270)


    regist_b = Button(r_frame, text="Registration", width=10,font=("Times", 13, "bold"),command=Rclick)
    regist_b.place(x=260, y=330)



#============ All Images ============

logo=ImageTk.PhotoImage(file="C:/Users/Geeta/PycharmProjects/pythonProject1Questech/project image/Quastech-logo.jpg")
logo_image=Label(w,image=logo).place(x=200,y=0,width=900,height=200)

# sign=PhotoImage(file="C:/Users/Geeta/PycharmProjects/pythonProject1Questech/project image/sign-in.jpg")

u_image=Image.open("C:/Users/Geeta/PycharmProjects/pythonProject1Questech/project image/u.png")
resized=u_image.resize((16,16),Image.ANTIALIAS)
new_image=ImageTk.PhotoImage(resized)

pas=Image.open("C:/Users/Geeta/PycharmProjects/pythonProject1Questech/project image/password.png")
p_resized=pas.resize((16,16),Image.ANTIALIAS)
new_pas=ImageTk.PhotoImage(p_resized)



#============Login ================

frame = Frame(w, bg="#696969")
frame.place(x=450, y=220, height=400, width=400)

title=Label(frame,text="SIGN IN",font=("Timeromanes",20,"bold"),bg="#696969")
title.place(x=145,y=40)


user_name=Label(frame,text="Username",image=new_image,compound=LEFT,bg="#696969",font=("Times", 13, "bold"))
user_name.place(x=70,y=150)
u_entry=Entry(frame,width=20)
u_entry.place(x=70,y=180)

password=Label(frame,text="Password",image=new_pas,compound=LEFT,bg="#696969",font=("Times", 13, "bold"))
password.place(x=70,y=230)
p_entry=Entry(frame,width=20,show="*")
p_entry.place(x=70,y=260)

login_b=Button(frame,text="Login",width=10,font=("Times", 13, "bold"),command=login)
login_b.place(x=70,y=330)
regist_b=Button(frame,text="Register",width=10,font=("Times", 13, "bold"),command=regist)
regist_b.place(x=240,y=330)


w.mainloop()

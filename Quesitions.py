from tkinter import *
from datetime import datetime
from tkinter import messagebox
from PIL import ImageTk, Image
import mysql.connector as my


def stop():
    global correct_answer


    # print(aaa)
    a1 = v1.get()
    a2 = v2.get()
    a3 = v3.get()
    a4 = v4.get()
    a5 = v5.get()
    a6 = v6.get()
    a7 = v7.get()
    a8 = v8.get()
    a9 = v9.get()
    a10 = v10.get()
    a11 = v11.get()
    a12 = v12.get()
    a13 = v13.get()
    a14 = v14.get()
    a15 = v15.get()
    get_answer = [a1, a2, a3, a4, a5, a6, a7, a8, a9, a10, a11, a12, a13, a14, a15]
    r_answer = [4, 2, 4, 4, 1, 1, 3, 3, 2, 2, 2, 2, 3, 1, 2]
    count = 1
    correct_answer = []
    # print(get_answer)
    for i, j in zip(get_answer, r_answer):
        if i == j:
            # print('equal=',i,"===",j,count)
            correct_answer.append(count)
        count = count + 1
    # print(correct_answer)
    # print(len(correct_answer))

    if string=='00:00:00':

        messagebox.showinfo("","Time's UP!")
        t=(aaa,len(correct_answer))
        conn=my.connect(username='root',password='root',host='localhost', database='exam')
        curr=conn.cursor()
        q='insert into student_marks(username,marks)values(%s,%s)'
        curr.execute(q, t)
        conn.commit()
        conn.close()
        msg = 'Your Score is ' + str(len(correct_answer)*2) + '/30'
        messagebox.showinfo('', msg)
        root.destroy()
        exit()

    yn = messagebox.askyesno("Be sure!", "Are you sure you want to submit?")
    print(string)
    if yn==True:
        t=(aaa,len(correct_answer))
        conn=my.connect(username='root',password='root',host='localhost', database='exam')
        curr=conn.cursor()
        q='insert into student_marks(username,marks)values(%s,%s)'
        curr.execute(q, t)
        conn.commit()
        conn.close()
        msg = 'Your Score is ' + str(len(correct_answer)*2) + '/30'
        messagebox.showinfo('', msg)
        root.destroy()


def last():
    global next_b3
    try:
        next_b2.destroy()
        next_b1.destroy()
    except:
        pass

    frame2 = Frame(root, bg="white")
    frame2.place(x=250, y=0, height=910, width=700)

    title = Label(root, text="Questions", font='times 20 bold', bg="white")
    title.place(x=300, y=50)

    l2 = Label(root, text=q11, bg="white")
    l2.place(x=300, y=100)
    r21 = Radiobutton(root, text='A.  Object', indicator=0, value=1, variable=v11, width=20)
    r21.place(x=300, y=125)
    r22 = Radiobutton(root, text='B.  Function', indicator=0, value=2, variable=v11, width=20)
    r22.place(x=450, y=125)
    r23 = Radiobutton(root, text='C.  Attribute', indicator=0, value=3, variable=v11, width=20)
    r23.place(x=300, y=150)
    r24 = Radiobutton(root, text='D.  Argument', indicator=0, value=4, variable=v11, width=20)
    r24.place(x=450, y=150)

    l11 = Label(root, text=q12, bg="white")
    l11.place(x=300, y=200)
    r31 = Radiobutton(root, text='A.  _x = 2', indicator=0, value=1, variable=v12, width=20)
    r31.place(x=300, y=225)
    r32 = Radiobutton(root, text='B.  __x = 3', indicator=0, value=2, variable=v12, width=20)
    r32.place(x=450, y=225)
    r33 = Radiobutton(root, text='C.  __xyz__ = 5', indicator=0, value=3, variable=v12, width=20)
    r33.place(x=300, y=250)
    r34 = Radiobutton(root, text='D.  None of these', indicator=0, value=4, variable=v12, width=20)
    r34.place(x=450, y=250)

    l11 = Label(root, text=q13, bg="white")
    l11.place(x=300, y=300)
    r31 = Radiobutton(root, text='A.  To identify the variable', indicator=0, value=1, variable=v13, width=60)
    r31.place(x=300, y=325)
    r32 = Radiobutton(root, text='B.  It confuses the interpreter', indicator=0, value=2, variable=v13, width=60)
    r32.place(x=300, y=350)
    r33 = Radiobutton(root, text='C.  It indicates a private variable of a class', indicator=0, value=3, variable=v13,
                      width=60)
    r33.place(x=300, y=375)
    r34 = Radiobutton(root, text='D.  None of these', indicator=0, value=4, variable=v13, width=60)
    r34.place(x=300, y=400)

    l11 = Label(root, text=q14, bg="white")
    l11.place(x=300, y=450)
    r31 = Radiobutton(root, text='A.  val', indicator=0, value=1, variable=v14, width=20)
    r31.place(x=300, y=475)
    r32 = Radiobutton(root, text='B.  raise', indicator=0, value=2, variable=v14, width=20)
    r32.place(x=450, y=475)
    r33 = Radiobutton(root, text='C.  try', indicator=0, value=3, variable=v14, width=20)
    r33.place(x=300, y=500)
    r34 = Radiobutton(root, text='D.  with', indicator=0, value=4, variable=v14, width=20)
    r34.place(x=450, y=500)

    l11 = Label(root, text=q15, bg="white")
    l11.place(x=300, y=550)
    r31 = Radiobutton(root, text='A.  All variable names must begin with an underscore.', indicator=0, value=1,
                      variable=v15, width=60)
    r31.place(x=300, y=575)
    r32 = Radiobutton(root, text='B.  Unlimited length ', indicator=0, value=2, variable=v15, width=60)
    r32.place(x=300, y=600)
    r33 = Radiobutton(root, text='C.  The variable name length is a maximum of 2.', indicator=0, value=3, variable=v15,
                      width=60)
    r33.place(x=300, y=625)
    r34 = Radiobutton(root, text='D.  All of the above', indicator=0, value=4, variable=v15, width=60)
    r34.place(x=300, y=650)

    next_b3 = Button(frame_bot, text='Prev Page', font='times 25 bold', bg='grey70', height=1, width=10, command=next)
    next_b3.place(x=70, y=100)


def next():
    global next_b1, next_b2
    try:
        next_b.destroy()
        next_b3.destroy()
    except:
        pass

    frame = Frame(root, bg="white")
    frame.place(x=250, y=0, height=910, width=700)

    title = Label(root, text="Questions", font='times 20 bold', bg="white")
    title.place(x=300, y=50)

    l2 = Label(root, text=q6, bg="white")
    l2.place(x=300, y=100)
    r21 = Radiobutton(root, text='A. 2008', indicator=0, value=1, variable=v6, width=20)
    r21.place(x=300, y=125)
    r22 = Radiobutton(root, text='B. 2000', indicator=0, value=2, variable=v6, width=20)
    r22.place(x=450, y=125)
    r23 = Radiobutton(root, text='C. 2010', indicator=0, value=3, variable=v6, width=20)
    r23.place(x=300, y=150)
    r24 = Radiobutton(root, text='D. 2005', indicator=0, value=4, variable=v6, width=20)
    r24.place(x=450, y=150)

    l2 = Label(root, text=q7, bg="white")
    l2.place(x=300, y=200)
    r21 = Radiobutton(root, text='A.  Key', indicator=0, value=1, variable=v7, width=20)
    r21.place(x=300, y=225)
    r22 = Radiobutton(root, text='B.  Brackets', indicator=0, value=2, variable=v7, width=20)
    r22.place(x=450, y=225)
    r23 = Radiobutton(root, text='C.  Indentation', indicator=0, value=3, variable=v7, width=20)
    r23.place(x=300, y=250)
    r24 = Radiobutton(root, text='D. None of these', indicator=0, value=4, variable=v7, width=20)
    r24.place(x=450, y=250)

    l2 = Label(root, text=q8, bg="white")
    l2.place(x=300, y=300)
    r21 = Radiobutton(root, text='A.    /', indicator=0, value=1, variable=v8, width=20)
    r21.place(x=300, y=325)
    r22 = Radiobutton(root, text='B.    //', indicator=0, value=2, variable=v8, width=20)
    r22.place(x=450, y=325)
    r23 = Radiobutton(root, text='C.    #', indicator=0, value=3, variable=v8, width=20)
    r23.place(x=300, y=350)
    r24 = Radiobutton(root, text='D.    !', indicator=0, value=4, variable=v8, width=20)
    r24.place(x=450, y=350)

    l2 = Label(root, text=q9, bg="white")
    l2.place(x=300, y=400)
    r21 = Radiobutton(root, text='A.  Classes are real-world entities while objects are not real', indicator=0, value=1,
                      variable=v9, width=60)
    r21.place(x=300, y=425)
    r22 = Radiobutton(root, text='B.  Objects are real-world entities while classes are not real', indicator=0, value=2,
                      variable=v9, width=60)
    r22.place(x=300, y=450)
    r23 = Radiobutton(root, text='C.  Both objects and classes are real-world entities', indicator=0, value=3,
                      variable=v9, width=60)
    r23.place(x=300, y=475)
    r24 = Radiobutton(root, text='D.  All of the above', indicator=0, value=4, variable=v9, width=60)
    r24.place(x=300, y=500)

    l2 = Label(root, text=q10, bg="white")
    l2.place(x=300, y=550)
    r21 = Radiobutton(root, text='A.   a ^ b', indicator=0, value=1, variable=v10, width=20)
    r21.place(x=300, y=575)
    r22 = Radiobutton(root, text='B.    a**b', indicator=0, value=2, variable=v10, width=20)
    r22.place(x=450, y=575)
    r23 = Radiobutton(root, text='C.    a ^ ^ b', indicator=0, value=3, variable=v10, width=20)
    r23.place(x=300, y=600)
    r24 = Radiobutton(root, text='D.    a ^ * b', indicator=0, value=4, variable=v10, width=20)
    r24.place(x=450, y=600)

    next_b1 = Button(frame_bot, text='Next Page', font='times 25 bold', bg='grey70', height=1, width=10, command=last)
    next_b1.place(x=70, y=100)
    next_b2 = Button(frame_bot, text='Prev Page', font='times 25 bold', bg='grey70', height=1, width=10, command=submit)
    next_b2.place(x=70, y=200)


def submit():
    global next_b
    # question()
    try:
        next_b2.destroy()
        next_b1.destroy()
    except:
        pass

    lq.destroy()
    s1_radio.destroy()
    s2_radio.destroy()
    s3_radio.destroy()

    frame_middle = Frame(root, bg="white")
    frame_middle.place(x=250, y=0, height=1000, width=740)

    title = Label(root, text="Questions", font='times 20 bold', bg="white")
    title.place(x=300, y=50)

    l1 = Label(root, text=q1, bg="white")
    l1.place(x=300, y=100)
    r11 = Radiobutton(root, text='A.         16', indicator=0, value=1, variable=v1, width=20)
    r11.place(x=300, y=125)
    r12 = Radiobutton(root, text='B.         32', indicator=0, value=2, variable=v1, width=20)
    r12.place(x=450, y=125)
    r13 = Radiobutton(root, text='C.         64', indicator=0, value=3, variable=v1, width=20)
    r13.place(x=300, y=150)
    r14 = Radiobutton(root, text='D.     None', indicator=0, value=4, variable=v1, width=20)
    r14.place(x=450, y=150)
    a1 = v1.get()

    l1 = Label(root, text=q2, bg="white")
    l1.place(x=300, y=200)
    r11 = Radiobutton(root, text='A.  Zim Den', indicator=0, value=1, variable=v2, width=20)
    r11.place(x=300, y=225)
    r12 = Radiobutton(root, text='B.  Guido van Rossum', indicator=0, value=2, variable=v2, width=20)
    r12.place(x=450, y=225)
    r13 = Radiobutton(root, text='C.  Niene Stom', indicator=0, value=3, variable=v2, width=20)
    r13.place(x=300, y=250)
    r14 = Radiobutton(root, text='D.  Wick van Rossum', indicator=0, value=4, variable=v2, width=20)
    r14.place(x=450, y=250)

    l1 = Label(root, text=q3, bg="white")
    l1.place(x=300, y=300)
    r11 = Radiobutton(root, text='A.    1995', indicator=0, value=1, variable=v3, width=20)
    r11.place(x=300, y=325)
    r12 = Radiobutton(root, text='B.    1972', indicator=0, value=2, variable=v3, width=20)
    r12.place(x=450, y=325)
    r13 = Radiobutton(root, text='C.    1981', indicator=0, value=3, variable=v3, width=20)
    r13.place(x=300, y=350)
    r14 = Radiobutton(root, text='D.    1989', indicator=0, value=4, variable=v3, width=20)
    r14.place(x=450, y=350)

    l1 = Label(root, text=q4, bg="white")
    l1.place(x=300, y=400)
    r11 = Radiobutton(root, text='A.    English', indicator=0, value=1, variable=v4, width=20)
    r11.place(x=300, y=425)
    r12 = Radiobutton(root, text='B.    PHP', indicator=0, value=2, variable=v4, width=20)
    r12.place(x=450, y=425)
    r13 = Radiobutton(root, text='C.    C', indicator=0, value=3, variable=v4, width=20)
    r13.place(x=300, y=450)
    r14 = Radiobutton(root, text='D.    All of the above', indicator=0, value=4, variable=v4, width=20)
    r14.place(x=450, y=450)

    l1 = Label(root, text=q5, bg="white")
    l1.place(x=300, y=500)
    r11 = Radiobutton(root, text='A.    .py', indicator=0, value=1, variable=v5, width=20)
    r11.place(x=300, y=525)
    r12 = Radiobutton(root, text='B.    .python', indicator=0, value=2, variable=v5, width=20)
    r12.place(x=450, y=525)
    r13 = Radiobutton(root, text='C.    .python', indicator=0, value=3, variable=v5, width=20)
    r13.place(x=300, y=550)
    r14 = Radiobutton(root, text='D.    None of these', indicator=0, value=4, variable=v5, width=20)
    r14.place(x=450, y=550)

    next_b = Button(frame_bot, text='Next Page', font='times 25 bold', bg='grey70', height=1, width=10, command=next)
    next_b.place(x=70, y=100)
    submit_b = Button(frame_bot, text='Submit', font='times 25 bold', bg='grey70', height=1, width=10, command=stop)
    submit_b.place(x=70, y=300)


def question():
    global q1, q2, q3, q4, q5, q6, q7, q8, q9, q10, q11, q12, q13, q14, q15, v1, v2, v3, v4, v5, v6, v7, v8, v9, v10, v11, v12, v13, v14, v15
    q1 = '1) What is the maximum possible length of an identifier?'
    q2 = '2) Who developed the Python language?'
    q3 = '3) In which year was the Python language developed?'
    q4 = '4) In which language is Python written?'
    q5 = '5) Which one of the following is the correct extension of the Python file?'
    q6 = '6) In which year was the Python 3.0 version developed?'
    q7 = '7) What do we use to define a block of code in Python language?'
    q8 = '8) Which character is used in Python to make a single line comment?'
    q9 = '9) Which of the following statements is correct regarding the object-oriented programming concept in Python?'
    q10 = '10) Which of the following operators is the correct option for power(ab)?'
    q11 = '11) What is the method inside the class in python language?'
    q12 = '12) Which of the following declarations is incorrect?'
    q13 = '13) Why does the name of local variables start with an underscore discouraged?'
    q14 = '14) Which of the following is not a keyword in Python language?'
    q15 = '15) Which of the following statements is correct for variable names in Python language?'
    v1 = IntVar()
    v2 = IntVar()
    v3 = IntVar()
    v4 = IntVar()
    v5 = IntVar()
    v6 = IntVar()
    v7 = IntVar()
    v8 = IntVar()
    v9 = IntVar()
    v10 = IntVar()
    v11 = IntVar()
    v12 = IntVar()
    v13 = IntVar()
    v14 = IntVar()
    v15 = IntVar()


def clock():
    global string, counter,frame_top2
    start_b.destroy()
    tt = datetime.fromtimestamp(counter)
    string = tt.strftime("%H:%M:%S")

    frame_top2 = Frame(root, bg="gray33")
    frame_top2.place(x=1000, y=0, height=250, width=400)
    l = Label(frame_top2, text="Exam Countdown", font='times 20 bold', bg="gray33", fg='white')
    l.place(x=70, y=50)
    l = Label(frame_top2, text="Total Time of Exam : 0 Hour,30 Min", font='times 12 bold', bg="gray33", fg='white')
    l.place(x=60, y=210)
    countup = Label(frame_top2, font='times 30 bold', bg="gray33", fg='white')
    countup.place(x=100, y=130)
    countup.config(text=string)
    countup.after(1000, lambda: [clock()])
    counter -=1
    hours = int(string.rsplit(":")[0])

    if string=='00:00:00' or hours>0:
        frame_top = Frame(root, bg="gray33")
        frame_top.place(x=1000, y=0, height=250, width=400)
        show=Label(frame_top,text="00:00:00\nTime's Up", font='times 30 bold', bg="gray33", fg='white')
        show.place(x=100,y=130)

    if string=='00:00:00':
        # frame_top = Frame(root, bg="gray33")
        # frame_top.place(x=1000, y=0, height=250, width=400)
        stop()


def Button_Start_Python():
    global start_b
    start_b = Button(frame_top, text='Start  Test', font='times 25 bold', bg='grey70',
                     command=lambda: [question(), submit(), clock()])
    start_b.place(x=100, y=130)
    frame_middle = Frame(root, bg="white")
    frame_middle.place(x=250, y=200, height=900, width=740)
    p = "YOUR  PYTHON  SUBJECT  EXAM  \nWILL  BE  START  AFTER \nCLICKING ON ' Start Test ' BUTTON."
    l = Label(root, text=p, font='times 18 bold', bg="white")
    l.place(x=440, y=310)


def Button_Start_Java():
    frame_middle = Frame(root, bg="white")
    frame_middle.place(x=250, y=200, height=900, width=740)
    l = Label(root, text="There Is No Exam For Java Today!", font='times 20 bold', bg="white")
    l.place(x=440, y=310)


def Button_Start_C():
    frame_middle = Frame(root, bg="white")
    frame_middle.place(x=250, y=200, height=900, width=740)
    l = Label(root, text="There Is No Exam For C Today!", font='times 20 bold', bg="white")
    l.place(x=440, y=310)


def start(stud):
    global root, sub, left_frame, lq, s1_radio, s2_radio, s3_radio, frame_top, l, info, countup, frame_bot, counter,aaa
    aaa=stud
    root = Tk()
    root.geometry('1350x700+0+0')
    counter = 70200-1800
    root.config(bg='white')

    sub = IntVar()

    left_frame = Frame(root, bg="Dim gray")
    left_frame.place(x=0, y=0, height=700, width=250)
    lq = Label(left_frame, text="Select Subject", bg="Dim gray", font=("Times", 15, "bold"))
    lq.place(x=20, y=50)
    # l.destroy()
    s1_radio = Radiobutton(left_frame, value=1, text="Python", bg="Dim gray", font='Times" 12 bold', variable=sub,
                           command=Button_Start_Python, indicator=0, width=12)
    s1_radio.place(x=40, y=90)
    s2_radio = Radiobutton(left_frame, value=2, text="C", bg="Dim gray", font='Times" 12 bold', variable=sub,
                           command=Button_Start_C, indicator=0, width=12)
    s2_radio.place(x=40, y=120)
    s3_radio = Radiobutton(left_frame, value=3, text="Java", bg="Dim gray", font='Times" 12 bold', variable=sub,
                           command=Button_Start_Java, indicator=0, width=12)
    s3_radio.place(x=40, y=150)

    frame_top = Frame(root, bg="gray33")
    frame_top.place(x=1000, y=0, height=250, width=400)
    frame_bot = Frame(root, bg="Dim gray")
    frame_bot.place(x=1000, y=250, height=700, width=400)

    l = Label(frame_top, text="Exam Countdown", font='times 20 bold', bg="gray33", fg='white')
    l.place(x=70, y=50)

    info = Label(root, text='Test time will be of 30 minutes\nThere will be 15 Question\n'
                            'Each Question contains 4 Options Out of which you have to select 1 right option\n'
                            'Each Question Contain 1 Marks\n1 page contain 5 question for next 5 question click on next\n\n'
                            'CLICK ON "START TEST" TO START THE TEST\nBest Of Luck',
                 font='Times 15 bold', bg='white', fg='grey35')
    info.place(x=300, y=300)

    logo = Image.open("C:/Users/Geeta/PycharmProjects/pythonProject1Questech/project image/Quastech-logo.jpg")
    resized = logo.resize((730, 200), Image.ANTIALIAS)
    new_image = ImageTk.PhotoImage(resized)
    logo_image = Label(root, image=new_image).place(x=250, y=0, width=730, height=200)

    countup = Label(frame_top, font='times 30 bold', bg="gray33", fg='white')
    countup.place(x=100, y=130)


    l = Label(frame_top, text="Total Time of Exam : 0 Hour,30 Min", font='times 12 bold', bg="gray33", fg='white')
    l.place(x=60, y=210)

    root.mainloop()


# start(1)

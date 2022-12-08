from tkinter import *
from tkinter import font as tkFont

first_num = 0
second_num = 0
sign = ""

def handle_operator(operator):
    global first_num,sign
    first_num = int(user_input.get())
    # clear the screen
    user_input.delete(0,"end")
    # store the sign
    sign = operator

def handle_clear():
    user_input.delete(0, "end")

def handle_equals():
    global second_num
    # fetch the current no and store in second_num
    second_num = int(user_input.get())
    # clear screen
    user_input.delete(0, "end")
    # calculate result
    if sign == "+":
        result = first_num + second_num
    elif sign == "-":
        result = first_num - second_num
    elif sign == "*":
        result = first_num * second_num
    else:
        result = first_num / second_num
    # put it inside user input
    user_input.insert(0,str(result))




root = Tk()

btn_font = tkFont.Font(family='Helvetica', size=14, weight='bold')

root.title("Calculator")

root.minsize(300,500)
root.maxsize(300,500)

root.configure(background="#3498db")

user_input = Entry(root)
user_input.pack(pady=(10,10),ipadx=80,ipady=10)

btn_frame = Frame(root)
btn_frame.pack()

add_btn = Button(btn_frame,text="+",width="5",height="2",command=lambda :handle_operator("+"))
add_btn['font'] = btn_font
add_btn.pack(side=LEFT)

sub_btn = Button(btn_frame,text="-",width="5",height="2",command=lambda :handle_operator("-"))
sub_btn['font'] = btn_font
sub_btn.pack(side=LEFT)

mul_btn = Button(btn_frame,text="*",width="5",height="2",command=lambda :handle_operator("*"))
mul_btn['font'] = btn_font
mul_btn.pack(side=LEFT)

div_btn = Button(btn_frame,text="/",width="5",height="2",command=lambda :handle_operator("/"))
div_btn['font'] = btn_font
div_btn.pack(side=LEFT)

btn_frame2 = Frame(root)
btn_frame2.pack()

clear_btn = Button(btn_frame2,text="Clear",width="11",height="2",command=lambda: handle_clear())
clear_btn['font'] = btn_font
clear_btn.pack(side=LEFT)

equals_btn = Button(btn_frame2,text="=",width="11",height="2",command = lambda: handle_equals())
equals_btn['font'] = btn_font
equals_btn.pack(side=LEFT)

root.mainloop()


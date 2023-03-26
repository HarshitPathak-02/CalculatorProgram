from tkinter import *

def click(event):
    text = event.widget.cget("text")
    print(text)
    if text == "Clear":
        screenval.set("")
    elif text == "<<<":
        screenval.set(f"\b")
        screen.update()
    elif text == "=":
        if screenval.get().isdigit():
            value = int(screenval.get())
        else:
            try:
                value = eval(screen.get())
            except Exception as e :
                print(e)
                value = "Invalid Operation"
        screenval.set(value)
        screen.update()
    else :
        screenval.set(screenval.get() + text)
        screen.update()
    

root = Tk()
root.geometry("500x400")
root.title("Calculator")
root.wm_iconbitmap("calculator.ico")

screenval = StringVar()
screen = Entry(root,textvariable=screenval,font="lucida 20 bold",bg="black",fg="white")
screen.place(x=10,y=10,height=50,width=480)

f = Frame(root,bg="Grey")
f.place(x=10,y=70,height=320,width=280)

b = Button(f,text="9",font="lucida 15 bold",bg="Grey",relief=SUNKEN)
b.place(x=10,y=5,height=70,width=70)
b.bind("<Button-1>",click)

b = Button(f,text="8",font="lucida 15 bold",bg="Grey",relief=SUNKEN)
b.place(x=103,y=5,height=70,width=70)
b.bind("<Button-1>",click)

b = Button(f,text="7",font="lucida 15 bold",bg="Grey",relief=SUNKEN)
b.place(x=197,y=5,height=70,width=70)
b.bind("<Button-1>",click)

b = Button(f,text="6",font="lucida 15 bold",bg="Grey",relief=SUNKEN)
b.place(x=10,y=90,height=70,width=70)
b.bind("<Button-1>",click)

b = Button(f,text="5",font="lucida 15 bold",bg="Grey",relief=SUNKEN)
b.place(x=103,y=90,height=70,width=70)
b.bind("<Button-1>",click)

b = Button(f,text="4",font="lucida 15 bold",bg="Grey",relief=SUNKEN)
b.place(x=197,y=90,height=70,width=70)
b.bind("<Button-1>",click)

b = Button(f,text="3",font="lucida 15 bold",bg="Grey",relief=SUNKEN)
b.place(x=10,y=175,height=70,width=70)
b.bind("<Button-1>",click)

b = Button(f,text="2",font="lucida 15 bold",bg="Grey",relief=SUNKEN)
b.place(x=103,y=175,height=70,width=70)
b.bind("<Button-1>",click)

b = Button(f,text="1",font="lucida 15 bold",bg="Grey",relief=SUNKEN)
b.place(x=197,y=175,height=70,width=70)
b.bind("<Button-1>",click)

b = Button(f,text="0",font="lucida 15 bold",bg="Grey",relief=SUNKEN)
b.place(x=10,y=260,height=55,width=70)
b.bind("<Button-1>",click)

b = Button(f,text=".",font="lucida 15 bold",bg="Grey",relief=SUNKEN)
b.place(x=197,y=260,height=55,width=70)
b.bind("<Button-1>",click)

b = Button(f,text="<<<",font="lucida 15 bold",bg="Grey",relief=SUNKEN)
b.place(x=103,y=260,height=55,width=70)
b.bind("<Button-1>",click)

f2 = Frame(root,bg="grey")
f2.place(x=300,y=70,height=320,width=190)

b = Button(f2,text="Clear",font="lucida 15 bold",bg="Grey",relief=SUNKEN)
b.place(x=10,y=5,height=70,width=80)
b.bind("<Button-1>",click)

b = Button(f2,text="=",font="lucida 15 bold",bg="Grey",relief=SUNKEN)
b.place(x=100,y=5,height=70,width=80)
b.bind("<Button-1>",click)

b = Button(f2,text="-",font="lucida 20 bold",bg="Grey",relief=SUNKEN)
b.place(x=10,y=90,height=70,width=80)
b.bind("<Button-1>",click)

b = Button(f2,text="*",font="lucida 20 bold",bg="Grey",relief=SUNKEN)
b.place(x=100,y=90,height=70,width=80)
b.bind("<Button-1>",click)

b = Button(f2,text="/",font="lucida 15 bold",bg="Grey",relief=SUNKEN)
b.place(x=10,y=175,height=70,width=80)
b.bind("<Button-1>",click)

b = Button(f2,text="%",font="lucida 15 bold",bg="Grey",relief=SUNKEN)
b.place(x=100,y=175,height=70,width=80)
b.bind("<Button-1>",click)

b = Button(f2,text="+",font="lucida 15 bold",bg="Grey",relief=SUNKEN)
b.place(x=10,y=260,height=55,width=170)
b.bind("<Button-1>",click)



root.mainloop()
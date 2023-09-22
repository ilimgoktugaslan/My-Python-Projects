from tkinter import *


def write(x):
    s=len(enter.get())
    enter.insert(s,str(x))

calculation=7
n1=0

def operations(x):
    global calculation
    calculation=x
    global n1
    n1=float(enter.get())
    print(calculation)
    print(n1)
    enter.delete(0,"end")

n2=0

def calculate():
    global n2
    n2=float(enter.get())
    print(n2)
    global calculation
    result=0
    if (calculation==0): result=n1 + n2
    elif (calculation==1): result=n1 - n2
    elif (calculation==2): result=n1 * n2
    elif (calculation==3): result=n1 / n2
    enter.delete(0,"end")
    enter.insert(0,str(result))

window=Tk()
window.title("CALCULATOR")
window.geometry("500x500")
enter=Entry(font="Verdana 14 bold",width=20,justify=RIGHT)
enter.place(x=80,y=20)

b=[]

for i in range(1,10):
    b.append(Button(text=str(i),font="Verdana 14 bold",width=4,command=lambda x=i:write(x)))

counter=0

for i in range(0,3):
    for j in range(0,3):
        b[counter].place(x=80+j*70,y=80+i*70)
        counter+=1

operation=[]

for i in range(0,4):
    operation.append(Button(fg="BLACk",bg="GRAY",font="Verdana 14 bold",width=14,command=lambda x=i:operations(x)))
operation[0]["text"]="+"
operation[1]["text"]="-"
operation[2]["text"]="*"
operation[3]["text"]="/"

for i in range(0,4):
    operation[i].place(x=300,y=80+50*i)

zb=Button(text=0,font="Verdana 14 bold",width=4,command=lambda x=0:write(x))
zb.place(x=80,y=280)
db=Button(text=0,font="Verdana 14 bold",width=4,command=lambda x=".":write(x))
db.place(x=220,y=280)
rb=Button(text="=",fg="BLACK",bg="GRAY",font="Verdana 14 bold",width=4,command=calculate)
rb.place(x=300,y=280)
window.mainloop()


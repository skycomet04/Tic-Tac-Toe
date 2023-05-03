from tkinter import *
from tkinter import messagebox
import time, random as ran 
root=Tk()
root.geometry("692x690")
root.configure(bg="black")
img1=PhotoImage(file="D:/tictactoe/X.png")
img2=PhotoImage(file="D:/tictactoe/0.png")
img3=PhotoImage(file="D:/tictactoe/blank.png")
for i in range(3):
    root.rowconfigure(i,weight=1)
    root.columnconfigure(i,weight=1)
def start():
    global l,label,count,flag,s1,s2,k,s3
    s1=set() # player 1
    s2=set() # player 2 
    s3=[1,2,3,4,5,6,7,8,9]
    l=[]
    flag=True
    k=1
    count=0
    for i in range(3):
        for j in range(3):
            l.append(Button(root,bg='#558787',fg="white",command=lambda x=k:result(x)))
            l[-1].grid(row=i,column=j,sticky="NSEW",padx=2,pady=2)
            l[-1]['image']=img3
            k+=1    
    label=Label(root,text="Player 1",bg="#98F1F2",fg='#558787',font="arial 35 bold")
    label.grid(row=3,column=0,columnspan=3,sticky="NSEW",padx=2,pady=2)


def computer():
    global s3
    if count<=8:
        t=ran.choice(s3)
        if t in s3:
            s3.remove(t)
        #l[t-1]['state']='disable'
        result(t)


def result(k):
    global flag,count,s3
    if flag:
        s1.add(k)
        l[k-1]['image']=img1
        label['text']="Player 2"
    else:
        s2.add(k)
        l[k-1]['image']=img2
        label['text']="Player 1"
    count+=1
    l[k-1]['state']='disable'
    flag=not flag
    if k in s3:
        s3.remove(k)
    if label['text']=="Player 2":
        computer()
    if count>=5:
        for s in wincomb:
            if s.issubset(s1):
                messagebox.showinfo("Result","Player 1 win ")
                start()
            if s.issubset(s2):
                messagebox.showinfo("Result","Player 2 win")
                start()
    if count==9:
        messagebox.showinfo("Result","Game Draw")
        start()
start()
wincomb=[{1,2,3},{4,5,6},{7,8,9},{1,4,7},{2,5,8},{3,6,9},{1,5,9},{3,5,7}] # in this order wont matter as we have taken set 
#created a list of set having wining combinations
root.mainloop()

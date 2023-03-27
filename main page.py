from tkinter import *
root=Tk()
desk_w=root.winfo_screenwidth()
desk_h=root.winfo_screenheight()
w_wid=550
w_ht=500
x=(desk_w-w_wid)/2
y=(desk_h-w_ht)/2
root.geometry("%dx%d+%d+%d" % (w_wid,w_ht,x,y))
for i in range(1):
    root.rowconfigure(i,weight=1)
    root.columnconfigure(i,weight=1)
img=PhotoImage(file="tic-tac.png")
img1=PhotoImage(file="1-1.png")
img2=PhotoImage(file="1-machine.png")
frame=Frame(root,width=600,height=500)
frame.grid(row=0)
b1=Button(frame,image=img,width=600,height=500)
b1.grid(row=0,sticky="NSEW")
Button(b1,fg="#2394AB",text="TIC-TAC-TOE",font="arial 35 bold",bd=0).grid(row=0,sticky="NS",padx=0,pady=0)
Button(b1,image=img1,bd=0).grid(row=1,sticky="NS",padx=0,pady=0)
Button(b1,image=img2,bd=0).grid(row=2,sticky="NS",padx=0,pady=10)
root.mainloop()
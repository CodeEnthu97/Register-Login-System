from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import random
from register import Register_window
from forget import forget_window
import sqlite3




class Login_window:
    def __init__ (self,root):
        self.root=root
        self.root.title("Login")
        self.root.geometry("1350x800+0+0")
        self.root.resizable(False,False)
        self.root.iconbitmap(r"F:\login\image\icon.ico")

        ######### background ########
        self.bg=ImageTk.PhotoImage(file=r"F:\login\image\background.jpg")
        lbl_bg=Label(self.root,image=self.bg)
        lbl_bg.place(x=0,y=0,relwidth=1,relheight=1)
        
        ###### login Frame ######
        frame=Frame(self.root,bg="black")
        frame.place(x=500,y=120,width=400,height=450)

        ###### variable #######
        self.email_var=StringVar()
        self.pass_var=StringVar()

        #####user###
        img1=Image.open(r"F:\login\image\user.png")
        img1=img1.resize((100,100),Image.ANTIALIAS)
        self.userimg=ImageTk.PhotoImage(img1)
        lbl_img1=Label(image=self.userimg,borderwidth=0,bg="black")
        lbl_img1.place(x=650,y=120,width=100,height=100)

        #### Welcome  ANIMATION ####
        self.txt="Welcome Here"
        self.count=0
        self.text=""
        self.color=["blue","red","green"]
        self.heading=Label(self.root,text=self.txt,font=("times new roman",20,"bold"),bg="black",fg="blue",bd=5,relief=FLAT)
        self.heading.place(x=500,y=210,width=380)
        self.slider()
        self.heading_color()

        ### username label & button ####
        username_label=Label(frame,text="username",font=("times new roman",15,"bold"),fg="pink",bg="black")
        username_label.place(x=70,y=155)

        img2=Image.open(r"F:\login\image\w.png")
        self.user_img=ImageTk.PhotoImage(img2)
        lbl_img2=Label(frame,image=self.user_img,borderwidth=0,bg="black")
        lbl_img2.place(x=40,y=155)

        self.username_entry=Entry(frame,font=("times new roman",15,"bold"),fg="black",bg="violet",textvariable=self.email_var)
        self.username_entry.place(x=70,y=190,width=255)

        ############ password ###########
        password_label=Label(frame,text="password",font=("times new roman",15,"bold"),fg="pink",bg="black")
        password_label.place(x=70,y=220)

        img3=Image.open(r"F:\login\image\x.png")
        self.pass_img=ImageTk.PhotoImage(img3)
        lbl_img3=Label(frame,image=self.pass_img,borderwidth=0,bg="black")
        lbl_img3.place(x=40,y=220)

        self.password_entry=Entry(frame,font=("times new roman",15,"bold"),show="*",fg="black",bg="violet",textvariable=self.pass_var)
        self.password_entry.place(x=70,y=250,width=255)

        ######## login button #########
        #login_button=Button(frame,command=self.login,text="log in",font=("times new roman",15,"bold"),fg="pink",bg="purple",bd=3,relief=RIDGE,activebackground="pink",activeforeground="violet")
        #login_button.place(x=128,y=295,width=120,height=35)

        img4=Image.open(r"F:\login\image\login.png")
        registerimage=img4.resize((110,30),Image.ANTIALIAS)
        self.reg_img=ImageTk.PhotoImage(registerimage)
        button_img4=Button(frame,image=self.reg_img,borderwidth=0,bg="black",cursor="hand2",activebackground="black",command=self.login)
        button_img4.place(x=140,y=295,width=110)

        ##### forget & new user button #########
        reg_new_button=Button(frame,text="Create New Account",cursor='hand2',command=self.register_win,font=("times new roman",13,"bold"),fg="pink",bg="black",borderwidth=0,relief=RIDGE,activebackground="black",activeforeground="violet")
        reg_new_button.place(x=15,y=340,width=200,height=35)

        forget_button=Button(frame,text="Forgot Password?",cursor='hand2',command=self.Forget_win,font=("times new roman",13,"bold"),fg="pink",bg="black",borderwidth=0,relief=RIDGE,activebackground="black",activeforeground="violet")
        forget_button.place(x=15,y=370,width=200,height=35)

    def clear(self):
        self.email_var.set("")
        self.pass_var.set("")
        
    



    def slider(self):
        if self.count>=len(self.txt):
            self.count=-1
            self.text=""
            self.heading.config(text=self.text)
        else:
            self.text=self.text+self.txt[self.count]
            self.heading.config(text=self.text)
        self.count+=1
        self.heading.after(100,self.slider)
    def heading_color(self):
        fg=random.choice(self.color)
        self.heading.config(fg=fg)
        self.heading.after(50,self.heading_color)
    
    def login(self):
        if self.email_var.get()=="" or self.pass_var.get()=="":
            messagebox.showerror("Error","All Fields Are Required",parent=self.root)
        else:
            try:
                con=sqlite3.connect(database=r'ajay.db')
                cur=con.cursor()
                cur.execute("Select * from register where Email=? and password=?",(self.email_var.get(),self.pass_var.get(),))
                row=cur.fetchone()
                if row == None:
                    messagebox.showerror("Error","Username or Password is wrong",parent=self.root)
                else:
                    messagebox.showinfo("Success","Successfully login")
                    self.clear()
                    con.close()
                
            except Exception as e:
                messagebox.showerror("Error",f"Error due to:{str(e)}",parent=self.root)








    ################################################################================
    def register_win(self):
        self.window=Toplevel(self.root)
        self.object=Register_window(self.window)
    
    def Forget_win(self):
        self.window=Toplevel(self.root)
        self.object=forget_window(self.window)

        








if __name__ == "__main__":
    root=Tk()
    obj=Login_window(root)
    root.mainloop()
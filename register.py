from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import random
import sqlite3




class Register_window:
    def __init__ (self,root):
        self.root=root
        self.root.title("Register Window")
        self.root.geometry("1350x800+0+0")
        self.root.resizable(False,False)
        self.root.iconbitmap(r"F:\login\image\icon.ico")
        self.root.focus_force()


        ##########################  Variables  ######################################
        self.fname_var=StringVar()
        self.lastname_var=StringVar()
        self.email_var=StringVar()
        self.Contact_var=StringVar()
        self.Securityq_var=StringVar()
        self.ans_var=StringVar()
        self.password_var=StringVar()
        self.conpasword_var=StringVar()
        

        ######### background ########
        self.bg=ImageTk.PhotoImage(file=r"F:\login\image\back.jpg")
        lbl_bg=Label(self.root,image=self.bg)
        lbl_bg.place(x=0,y=0,relwidth=1,relheight=1)
        ######### left image label #######
        self.left_img=ImageTk.PhotoImage(file=r"F:\login\image\left.jpg")
        lbl_leftimg=Label(self.root,image=self.left_img,borderwidth=0)
        lbl_leftimg.place(x=100,y=99,width=480)

        ########## Register here frame ########
        frame=Frame(self.root,bg="black")
        frame.place(x=580,y=100,width=700,height=550)

        #### Welcome ####
        self.txt="Register Here"
        self.count=0
        self.text=""
        self.color=["blue","yellow","red"]
        self.heading=Label(self.root,text=self.txt,font=("times new roman",20,"bold"),bg="black",fg="blue",bd=5,relief=FLAT)
        self.heading.place(x=720,y=110,width=380)
        self.slider()
        self.heading_color()

        ####### 1st row #########
        firstname_label=Label(frame,text="First Name",font=("times new roman",15,"bold"),fg="#FF8040",bg="black")
        firstname_label.place(x=50,y=100)

        self.firstname_entry=Entry(frame,font=("times new roman",15,"bold"),fg="black",bg="#736AFF",textvariable=self.fname_var)
        self.firstname_entry.place(x=50,y=130,width=255)

        lastname_label=Label(frame,text="Last Name",font=("times new roman",15,"bold"),fg="#FF8040",bg="black")
        lastname_label.place(x=400,y=100)

        self.lastname_entry=Entry(frame,font=("times new roman",15,"bold"),fg="black",bg="#736AFF",textvariable=self.lastname_var)
        self.lastname_entry.place(x=400,y=130,width=255)

        ########## 2nd row #########
        email_label=Label(frame,text="Email",font=("times new roman",15,"bold"),fg="#FF8040",bg="black")
        email_label.place(x=50,y=170)

        self.email_entry=Entry(frame,font=("times new roman",15,"bold"),fg="black",bg="#736AFF",textvariable=self.email_var)
        self.email_entry.place(x=50,y=200,width=255)

        contact_label=Label(frame,text="Contact",font=("times new roman",15,"bold"),fg="#FF8040",bg="black")
        contact_label.place(x=400,y=170)

        self.contact_entry=Entry(frame,font=("times new roman",15,"bold"),fg="black",bg="#736AFF",textvariable=self.Contact_var)
        self.contact_entry.place(x=400,y=200,width=255)

        ########## 3rd row #########
        security_label=Label(frame,text="Select Security Question",font=("times new roman",15,"bold"),fg="#FF8040",bg="black")
        security_label.place(x=50,y=240)
           
           ########### combobox ########
        self.security_combo=ttk.Combobox(frame,font=("times new roman",15,"bold"),state="readonly",textvariable=self.Securityq_var)
        self.security_combo["values"]=("Select","Your Birth Place","Your Pet Name","Your Favorite Book")
        self.security_combo.place(x=50,y=270,width=255)
        self.security_combo.current(0)
    
        secans_label=Label(frame,text="Security Answer",font=("times new roman",15,"bold"),fg="#FF8040",bg="black")
        secans_label.place(x=400,y=240)

        self.secans_entry=Entry(frame,font=("times new roman",15,"bold"),fg="black",bg="#736AFF",textvariable=self.ans_var)
        self.secans_entry.place(x=400,y=270,width=255)

        ####### 4th row ######
        pass_label=Label(frame,text="Password",font=("times new roman",15,"bold"),fg="#FF8040",bg="black")
        pass_label.place(x=50,y=360)

        self.pass_entry=Entry(frame,font=("times new roman",15,"bold"),fg="black",bg="#736AFF",textvariable=self.password_var)
        self.pass_entry.place(x=50,y=390,width=255)

        confirm_label=Label(frame,text="Confirm Password",font=("times new roman",15,"bold"),fg="#FF8040",bg="black")
        confirm_label.place(x=400,y=360)

        self.confirm_entry=Entry(frame,font=("times new roman",15,"bold"),fg="black",bg="#736AFF",textvariable=self.conpasword_var)
        self.confirm_entry.place(x=400,y=390,width=255)

        ######## check button #######
        self.check_var=IntVar()
        
        check_btn=Checkbutton(frame,text="I Agree The Terms & Conditions",font=("times new roman",12,"bold"),bg="black",fg="#FF8040",onvalue=1,offvalue=0,activebackground="black",variable=self.check_var)
        check_btn.place(x=50,y=430)

        ########### register button #####
        img4=Image.open(r"F:\login\image\register.png")
        registerimage=img4.resize((100,30),Image.ANTIALIAS)
        self.reg_img=ImageTk.PhotoImage(registerimage)
        button_img4=Button(frame,image=self.reg_img,borderwidth=0,bg="black",cursor="hand2",activebackground="black",command=self.register)
        button_img4.place(x=130,y=480,width=100)

        ########### log in button ######
        '''img5=Image.open(r"F:\login\image\logg.png")
        registerimage=img5.resize((100,50),Image.ANTIALIAS)
        self.login_img=ImageTk.PhotoImage(registerimage)
        button_img4=Button(frame,image=self.login_img,command=self.log_win,borderwidth=0,bg="black",cursor="hand2",activebackground="black")
        button_img4.place(x=470,y=450,width=100)'''



    ###########################  function declaration  #####################################

    def clear(self):
        self.fname_var.set("")
        self.lastname_var.set("")
        self.email_var.set("")
        self.Contact_var.set("")
        self.Securityq_var.set("Select")
        self.ans_var.set("")
        self.password_var.set("")
        self.conpasword_var.set("")
        self.check_var.set(0)



    def register(self):
        if  self.fname_var.get()=="" or self.lastname_var.get()=="" or self.email_var.get()=="" or self.Contact_var.get()=="":
            messagebox.showerror("Error","All Fields are required",parent=self.root)
        elif self.Securityq_var.get()=="Select" or self.ans_var.get()=="":
            messagebox.showerror("Error","Please Select Security Question and ans",parent=self.root)

        elif self.password_var.get() != self.conpasword_var.get():
            messagebox.showerror("Error","Password must be same",parent=self.root)
        elif self.check_var.get() == 0:
            messagebox.showerror("Error","Please check terms and conditions",parent=self.root)

        else:
            try:
                con=sqlite3.connect(database=r'ajay.db')
                cur=con.cursor()
                cur.execute("Select * from register where Email=?",(self.email_var.get(),))
                row=cur.fetchone()
                if row!=None:
                    messagebox.showerror("Error","Email Id already  exists")
                else:
                    cur.execute("INSERT INTO register (First_Name,Last_Name,Email,Contact,Security_q,Security_Ans,Password,Confirm_pass) values(?,?,?,?,?,?,?,?)",
                           (  
                              self.fname_var.get(),
                              self.lastname_var.get(),
                              self.email_var.get(),
                              self.Contact_var.get(),
                              self.Securityq_var.get(),
                              self.ans_var.get(),
                              self.password_var.get(),
                              self.conpasword_var.get(),  
                           ))
                    con.commit()
                    messagebox.showinfo("Success","Successfully Registered")
                    self.clear()
                    con.close()
                    self.root.destroy()



            except Exception as e:
                messagebox.showerror("Error",f"Error due to:{str(e)}",parent=self.root)

        












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


    
    
    








if __name__ == "__main__":
    root=Tk()
    obj=Register_window(root)
    root.mainloop()
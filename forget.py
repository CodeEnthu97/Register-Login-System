from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import sqlite3




class forget_window:

    def __init__(self,root):
        self.root=root
        self.root.geometry("700x500+300+10")

        self.root.title("Registration Form")

        self.root.iconbitmap(r"image/icon.ico")

        self.root.resizable(False, False)

        self.root.focus_force()


        ######### variable #############

        self.email_var=StringVar()
        self.pass_var=StringVar()
        self.confirm_pass_var=StringVar()

        back_color_lbl = Label(self.root, bg="#17202A", borderwidth=6, relief=SUNKEN).place(x=0, y=0, relwidth=1, relheight=1)

        wlc_lbl= Label(self.root,text="*** Welcome User ***",font="timesnewroman 15 bold underline",bg="black",fg="#1ABC9C",borderwidth=8,
        relief=SUNKEN,
        padx=5,
        pady=5,)
        wlc_lbl.place(x=230, y=10, width=300)

        eml_lbl= Label(
        self.root, text="Email :-", font="timesnewroman 15 bold", fg="#F39C12", bg="#17202A"
        ).place(x=90, y=150)

        pass_lbl= Label(
        self.root, text="New Password :-", font="timesnewroman 15 bold", fg="#F39C12", bg="#17202A"
        ).place(x=50, y=220)

        self.eml_entry= Entry(self.root, font="timesnewroman 15 bold", textvariable=self.email_var,fg="black", bg="#839192").place(
        x=210, y=150, width=290, height=35
        )

        self.pass_entry = Entry(self.root, font="timesnewroman 15 bold",textvariable=self.pass_var, fg="black", bg="#839192",)
        self.pass_entry.place(x=210, y=220, width=290, height=35)

        confirm_label=Label(self.root,text="Confirm Password :-",font=("times new roman",15,"bold"),fg="#F39C12",bg="#17202A")
        confirm_label.place(x=32,y=290)

        self.confirm_entry=Entry(self.root,font=("times new roman",15,"bold"),textvariable=self.confirm_pass_var,fg="black",bg="#839192")
        self.confirm_entry.place(x=210,y=290,width=290,height=35)

        self.rst_pass_button= Button(self.root,text="Reset Password",command=self.change_password,font="timesnewroman 14 bold",fg="#1ABC9C",bg="#2C3E50",cursor="hand2")
        self.rst_pass_button.place(x=270, y=350)

        self.cls_button = Button(
        self.root,
        text="Close",
        font="timesnewroman 14 bold",
        fg="#1ABC9C",
        bg="#2C3E50",
        cursor="hand2",
        command=self.root.destroy,
        ).place(x=320, y=400)

        
        self.namee = Label(
        self.root,
        text="@Ajay_creation",
        fg="yellow",
        bg="#17202A",
        font="timesnewroman 10 italic",
        ).place(x=550, y=400)

    ######### function eclaration ########
    def clear(self):
        self.email_var.set("")
        self.pass_var.set("")

    def change_password(self):
        if self.email_var.get()=="" or self.pass_var.get()=="":
            messagebox.showerror("Error","All Fields Are Required",parent=self.root)
        else:
            try:
                con=sqlite3.connect(database=r'ajay.db')
                cur=con.cursor()
                cur.execute("Select * from register where Email=?",(self.email_var.get(),))
                row=cur.fetchone()
                if row == None:
                    messagebox.showerror("Error","Account is not exist",parent=self.root)
                else:
                    con.execute("Update register set Password=?,Confirm_pass=? where Email=?",(self.pass_var.get(),self.confirm_pass_var.get(),self.email_var.get(),))
                    con.commit()
                    messagebox.showinfo("Success","Successfully updated")
                    self.clear()
                    con.close()
                    self.root.destroy()
                
            except Exception as e:
                messagebox.showerror("Error",f"Error due to:{str(e)}",parent=self.root)
        




if __name__ == "__main__":
    root=Tk()
    obj=forget_window(root)
    root.mainloop()


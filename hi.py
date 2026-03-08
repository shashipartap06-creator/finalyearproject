from tkinter import*
from datetime import*
from math import*
import time
from PIL import Image,ImageTk,ImageDraw #pip install pillow
from course import CourseClass
from student import studentClass
from result import resultClass
from report import reportClass
from login import Login_window
from tkinter import messagebox
import sqlite3 
import os
class RMS:
    def __init__(self,root):



        self.root=root
        self.root.title("STUDENT RESULT MANAGEMENT SYSTEM")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg="white")
        img=Image.open("images/logo_p.png")
        self.logo_dash=ImageTk.PhotoImage(img)
        #---------title--------
        title=Label(self.root,text="STUDENT RESULT MANAGEMENT SYSTEM",padx=10,compound=LEFT ,image=self.logo_dash, font=("goudy old style",20,"bold"),bg="#033054",fg="white").place(x=0,y=0,relwidth=1,height=50)
        #---------menu--------
        M_frame=LabelFrame(self.root,text="MENUS",font=("times new roman",15),bg="white")
        M_frame.place(x=10,y=70,width=1340,height=80)
        #-------buttons-----------
        btn_course=Button(M_frame,text="course",font=("goudy old style",15,"bold"),bg="#0b5377",fg="white",command=self.add_course).place(x=20,y=5,width=200,height=40)
        btn_student=Button(M_frame,text="Students",font=("goudy old style",15,"bold"),bg="#0b5377",fg="white",command=self.add_student).place(x=240,y=5,width=200,height=40)
        btn_result=Button(M_frame,text="Result",font=("goudy old style",15,"bold"),bg="#0b5377",fg="white",command=self.add_result).place(x=460,y=5,width=200,height=40)
        btn_view=Button(M_frame,text="View Student Results",font=("goudy old style",15,"bold"),bg="#0b5377",fg="white",command=self.add_report).place(x=680,y=5,width=200,height=40)
        btn_logout=Button(M_frame,text="Log Out",font=("goudy old style",15,"bold"),bg="#0b5377",fg="white",command=self.logout).place(x=900,y=5,width=200,height=40)
        btn_exit=Button(M_frame,text="Exit",font=("goudy old style",15,"bold"),bg="#0b5377",fg="white",command=self.exit_).place(x=1120,y=5,width=200,height=40)
        #-----------content window-----------
        self.bg_img=Image.open("images/bg.png")
        self.bg_img=self.bg_img.resize((920,350),Image.Resampling.LANCZOS)
        self.bg_img=ImageTk.PhotoImage(self.bg_img)

        self.lbl_bg=Label(self.root,image=self.bg_img).place(x=400,y=180,width=920,height=350)
                             
        
        #--------update details-------------

        self.lbl_course=Label(self.root,text="Total Courses\n[0]",font=("goudy old style",20),bd=10,relief=RIDGE,bg="#e43b06",fg="white")
        self.lbl_course.place(x=400,y=520,width=300,height=100)

        self.lbl_student=Label(self.root,text="Total Students\n[0]",font=("goudy old style",20),bd=10,relief=RIDGE,bg="#0676ad",fg="white")
        self.lbl_student.place(x=710,y=520,width=300,height=100)

        self.lbl_result=Label(self.root,text="Total Result\n[0]",font=("goudy old style",20),bd=10,relief=RIDGE,bg="#038074",fg="white")
        self.lbl_result.place(x=1020,y=520,width=300,height=100)




        #---------footer---------- 
        footer=Label(self.root,text="SRMS STUDENT RESULT MANAGEMENT SYSTEM\nContact Us for any Technical issue :987654321",font=("goudy old style",12,),bg="#262626",fg="white").pack(side=BOTTOM,fill=X)
        self.update_details()
        #clock 
        self.lbl=Label(self.root,bg="#08192b",bd=0)
        self.lbl.place(x=10,y=180,width=380,height=380)

        self.update_clock()
        #update clock

    def update_details(self):
        con=sqlite3.connect(database="rms.db")
        cur=con.cursor()
        try:
            cur.execute("select * from course")
            cr=cur.fetchall()
            
            self.lbl_course.config(text=f"Total Courses\n[{str(len(cr))}]")

            cur.execute("select * from student")
            cr=cur.fetchall()
            # self.lbl_student.after(200,self.update_details)
            self.lbl_student.config(text=f"Total Students\n[{str(len(cr))}]")

            cur.execute("select * from result")
            cr=cur.fetchall()
            # self.lbl_result.after(200,self.update_details)
            self.lbl_result.config(text=f"Total Results\n[{str(len(cr))}]")

            self.lbl_course.after(200,self.update_details)
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")
            self.show()



    def update_clock(self):
        # FIX 1: hour/minute/second are properties, not methods — remove ()
        h=datetime.now().hour
        m=datetime.now().minute
        s=datetime.now().second

        hr=(h/12)*360
        # FIX 2: 'min' is a Python built-in — renamed to min_
        min_=(m/60)*360
        sec=(s/60)*360

        self.clockimage(hr,min_,sec)
        # FIX 3: Imagetk → ImageTk (capital T and k)
        self.img=ImageTk.PhotoImage(file="images/clock_new.png")
        self.lbl.config(image=self.img)
        self.lbl.after(200,self.update_clock)

    def clockimage(self,hr,min_,sec):
        clock=Image.new("RGB",(380,380),(8,25,35))
        draw=ImageDraw.Draw(clock)
        # Use c.png as clock face background
        bg=Image.open("images/c.png")
        bg=bg.resize((380,380),Image.Resampling.LANCZOS)
        clock.paste(bg,(0,0))
        draw=ImageDraw.Draw(clock)
        cx, cy = 190, 190
        # Hour hand
        draw.line((cx,cy, cx+50*sin(radians(hr)), cy-50*cos(radians(hr))), fill="#df005e", width=4)
        # Minute hand
        draw.line((cx,cy, cx+80*sin(radians(min_)), cy-80*cos(radians(min_))), fill="#eaff00", width=3)
        # Second hand
        draw.line((cx,cy, cx+100*sin(radians(sec)), cy-100*cos(radians(sec))), fill="#00adff", width=2)
        # Center dot
        draw.ellipse((cx-7,cy-7,cx+7,cy+7), fill="#1ad5d5")
        clock.save("images/clock_new.png")



    def add_course(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=CourseClass(self.new_win)
    
    def add_student(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=studentClass(self.new_win)

    def add_result(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=resultClass(self.new_win)
        
    def add_report(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=reportClass(self.new_win)
    
    def logout(self):
        op=messagebox.askyesno("Confirm","Do you really want to logout?",parent=self.root)
        if op==True:
            self.root.destroy()
            os.system("python login.py")

    def exit_(self):
        op=messagebox.askyesno("Confirm","Do you really want to exit?",parent=self.root)
        if op==True:
            self.root.destroy()
if __name__=="__main__":
    root=Tk()
    obj=RMS(root)
    root.mainloop()

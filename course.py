from tkinter import*
from PIL import Image,ImageTk #pip install pillow
class CourseClass:
    def __init__(self,root):



        self.root=root
        self.root.title("STUDENT RESULT MANAGEMENT SYSTEM")
        self.root.geometry("1200x480+80+170")
        self.root.config(bg="white")
        self.root.focus_force()
        #----------title------
        title=Label(self.root,text="Manage Course Details ",font=("goudy old style",20,"bold"),bg="#033054",fg="white").place(x=10,y=15,width=1180,height=35)
        #---------variables------------
        self.var_course=StringVar()
        self.var_duration=StringVar()
        self.var_charges=StringVar()

        
        #---------widgets-------- 
        lbl_coursename=Label(self.root,text="Course Name",  font=("goudy old style",15,"bold"),bg="white").place(x=10,y=60)
        lbl_duration=Label(self.root,text="Duration",       font=("goudy old style",15,"bold"),bg="white").place(x=10,y=100)
        lbl_charges=Label(self.root,text="Charges",         font=("goudy old style",15,"bold"),bg="white").place(x=10,y=140)
        lbl_description=Label(self.root,text="Description", font=("goudy old style",15,"bold"),bg="white").place(x=10,y=185)

        #--------entry fields--------
        self.txt_courseName=Entry(self.root,textvariable=self.var_course, font=("goudy old style",15,"bold"),bg="lightyellow")
        self.txt_courseName.place(x=150,y=60,width=200)
        txt_duration=Entry(self.root,textvariable=self.var_duration  ,  font=("goudy old style",15,"bold"),bg="lightyellow").place(x=150,y=100,width=200)
        txt_charges=Entry(self.root,textvariable=self.var_charges,    font=("goudy old style",15,"bold"),bg="lightyellow").place(x=150,y=140,width=200)
        self.txt_description=Text(self.root,font=("goudy old style",15,"bold"),bg="lightyellow")
        self.txt_description.place(x=150,y=185,width=500,height=100)









if __name__=="__main__":
    root=Tk()
    obj=CourseClass(root)
    root.mainloop()
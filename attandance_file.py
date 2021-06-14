#-----------------Importing main library---------------------------------------------
from logging import exception
from os import close
from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2


class Presentee:  #_______Creating a main window
    def __init__(self,root):
        self.root=root
        self.root.geometry("1024x720+0+0")
        self.root.title("Attandance-Data")
        #TOP Image 1    
        img2=Image.open(r"pts\Student-Attendance (2).png")
        img2=img2.resize((600,130),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        f_lbl=Label(self.root,image=self.photoimg2)
        f_lbl.place(x=3,y=0,width=600,height=130)


        #TOP Image 2    
        img=Image.open(r"pts\attendanceystem-articles.jpg")
        img=img.resize((760,130),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)

        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=600,y=0,width=760,height=130)
    ##---------BG image
        imgbg=Image.open(r"pts\Sca01.jpg")
        imgbg=imgbg.resize((1360,605),Image.ANTIALIAS)
        self.photoimgbg=ImageTk.PhotoImage(imgbg)

        bg_img=Label(self.root,image=self.photoimgbg)
        bg_img.place(x=3,y=132,width=1360,height=609)    
        ##---Project Title
        title_lbl=Label(bg_img,text="👩‍🎓 Student's Attandance Informations 👨‍🎓",font=("times new roman",27,"bold"),bg="black",fg="red")
        title_lbl.place(x=0,y=0,width=1430,height=40)
        ##----Main Frame
        main_frame=Frame(bg_img,bd=2,bg="black")
        main_frame.place(x=0,y=40,width=1369,height=569)

        ## Lable Frames
        # left side
        Left_frame=LabelFrame(main_frame,bd=2,bg="grey",relief=RIDGE,text="Student's Details",font=("times new roman",12,"bold"))
        Left_frame.place(x=10,y=2,width=660,height=560)
        imgleft=Image.open(r"pts\Facial-Recognition-1024x483.jpg")
        imgleft=imgleft.resize((645,200),Image.ANTIALIAS)
        self.photoimgleft=ImageTk.PhotoImage(imgleft)
        f_lbl=Label(Left_frame,image=self.photoimgleft)
        f_lbl.place(x=5,y=0,width=645,height=200)

        #frame---current 
        Crnt_cors_frame=LabelFrame(Left_frame,bd=2,bg="grey",relief=RIDGE,text="Student Information",font=("times new roman",12,"bold"))
        Crnt_cors_frame.place(x=5,y=200,width=660,height=300)

        #===========Label frame=========================================================== 
        #1Sudent_AttendanceID
        AttenStuId_label=Label(Crnt_cors_frame,text="Attandance-ID:",font=("times new roman",12,"bold"))
        AttenStuId_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)
        AttenStuInfo_entry=ttk.Entry(Crnt_cors_frame,width=20,font=("times new roman",12,"bold"))
        AttenStuInfo_entry.grid(row=0,column=1,padx=10,pady=5,sticky=W)

        #2Sudent Roll No
        RN_label=Label(Crnt_cors_frame,text="Roll Number:",bg='white',font=("times new roman",12,"bold"))
        RN_label.grid(row=0,column=2,padx=10,pady=5)
        RN_entry=ttk.Entry(Crnt_cors_frame,width=20,font=("times new roman",12,"bold"))
        RN_entry.grid(row=0,column=3,padx=10,pady=5,sticky=W)

        #3Name
        NM_label=Label(Crnt_cors_frame,text="Student Name:",bg='white',font=("times new roman",12,"bold"))
        NM_label.grid(row=1,column=0)
        NM_entry=ttk.Entry(Crnt_cors_frame,width=22,font=("times new roman",12,"bold"))
        NM_entry.grid(row=1,column=1,padx=10,pady=5,sticky=W)

        #4Department
        DP_label=Label(Crnt_cors_frame,text="Department:",bg='white',font=("times new roman",12,"bold"))
        DP_label.grid(row=1,column=2)
        DP_entry=ttk.Entry(Crnt_cors_frame,width=22,font=("times new roman",12,"bold"))
        DP_entry.grid(row=1,column=3,padx=10,pady=5,sticky=W)

        #3Time
        TiM_label=Label(Crnt_cors_frame,text="Time:",bg='white',font=("times new roman",12,"bold"))
        TiM_label.grid(row=2,column=0)
        TiM_entry=ttk.Entry(Crnt_cors_frame,width=22,font=("times new roman",12,"bold"))
        TiM_entry.grid(row=2,column=1,padx=10,pady=5,sticky=W)

        #3Date
        DT_label=Label(Crnt_cors_frame,text="Date:",bg='white',font=("times new roman",12,"bold"))
        DT_label.grid(row=2,column=2)
        DT_entry=ttk.Entry(Crnt_cors_frame,width=22,font=("times new roman",12,"bold"))
        DT_entry.grid(row=2,column=3,padx=10,pady=5,sticky=W)

        #3Attendance ComboBox
        Att_label=Label(Crnt_cors_frame,text="Attendance Status",bg='white',font=("times new roman",12,"bold"))
        Att_label.grid(row=3,column=0)

        self.att_status=ttk.Combobox(Crnt_cors_frame,font=("times new roman",12,"bold"),state="readonly",width=18)
        self.att_status["values"]=("Status","Present","Absent")
        self.att_status.current(0)
        self.att_status.grid(row=3,column=1,padx=10,pady=5,sticky=W)

           #Radio Button Frame
        btn_frame=Frame(Crnt_cors_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=0,y=200,width=650,height=35)

        save_btn=Button(btn_frame,text="Import Attendance",width=17,font=("times new roman",12,"bold"),bg="black",fg="yellow")
        save_btn.grid(row=0,column=0)
        
        up_btn=Button(btn_frame,text="Export Attendance",width=17,font=("times new roman",12,"bold"),bg="black",fg="yellow")
        up_btn.grid(row=0,column=1)

        del_btn=Button(btn_frame,text="Update Attendance",width=17,font=("times new roman",12,"bold"),bg="black",fg="yellow")
        del_btn.grid(row=0,column=2)

        res_btn=Button(btn_frame,text="Reset",width=17,font=("times new roman",12,"bold"),bg="black",fg="yellow")
        res_btn.grid(row=0,column=3)




        # Right side Frame
        Right_frame=LabelFrame(main_frame,bd=2,bg="grey",relief=RIDGE,text="Attendace Details",font=("times new roman",12,"bold"))
        Right_frame.place(x=665,y=2,width=677,height=560)

        #frame-for Table
        table_frame=LabelFrame(Right_frame,bd=2,bg="white",relief=RIDGE)
        table_frame.place(x=5,y=5,width=660,height=500)
        #scroll bar
        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.Student_Attend=ttk.Treeview(table_frame,column=("id","roll","name","department","time","date","attendance"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.Student_Attend.xview)
        scroll_y.config(command=self.Student_Attend.yview)

        self.Student_Attend.heading("id",text="Attendance ID")
        self.Student_Attend.heading("roll",text="Roll Number")
        self.Student_Attend.heading("name",text="Name")
        self.Student_Attend.heading("department",text="Department")
        self.Student_Attend.heading("date",text="Time")
        self.Student_Attend.heading("time",text="Date")
        self.Student_Attend.heading("attendance",text="Attendance")

        self.Student_Attend.column("id",width=100)
        self.Student_Attend.column("roll",width=100)
        self.Student_Attend.column("name",width=200)
        self.Student_Attend.column("department",width=100)
        self.Student_Attend.column("date",width=100)
        self.Student_Attend.column("time",width=100)
        self.Student_Attend.column("attendance",width=100)

        self.Student_Attend["show"]="headings"

        self.Student_Attend.pack(fill=BOTH,expand=1)
        



if __name__ == "__main__":
    root=Tk()
    obj=Presentee(root)
    root.mainloop()

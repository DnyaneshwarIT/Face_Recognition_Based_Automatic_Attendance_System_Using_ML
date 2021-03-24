#-----------------Importing main library---------------------------------------------
from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector


class Student:  #_______Creating a main window
    def __init__(self,root):
        self.root=root
        self.root.geometry("1024x720+0+0")
        self.root.title("Student-Data")
        #_________variables
        self.var_dep=StringVar()
        self.var_course=StringVar()
        self.var_year=StringVar()
        self.var_semester=StringVar()
        self.var_std_id=StringVar()
        self.var_std_name=StringVar()
        self.var_div=StringVar()
        self.var_roll=StringVar()
        self.var_gender=StringVar()
        self.var_dob=StringVar()
        self.var_email=StringVar()
        self.var_phone=StringVar()
        self.var_address=StringVar()
        self.var_teacher=StringVar()



    #------------------Main Coding Start-------------------------------------------------------
        #TOP Image 1    
        img=Image.open(r"pts\download.jfif")
        img=img.resize((130,130),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)

        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=130,height=130)
        
        #TOP Image 2    
        img1=Image.open(r"pts\clg.jpeg")
        img1=img1.resize((1100,130),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=130,y=0,width=1000,height=130)

        #TOP Image 3    
        img2=Image.open(r"pts\dims.jfif")
        img2=img2.resize((300,130),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        f_lbl=Label(self.root,image=self.photoimg2)
        f_lbl.place(x=1130,y=0,width=300,height=130)

        ##---------BG image
        imgbg=Image.open(r"pts\bg1.gif")
        imgbg=imgbg.resize((1530,710),Image.ANTIALIAS)
        self.photoimgbg=ImageTk.PhotoImage(imgbg)

        bg_img=Label(self.root,image=self.photoimgbg)
        bg_img.place(x=0,y=130,width=1530,height=710)

        ##---Project Title
        title_lbl=Label(bg_img,text="👩‍🎓 Student's Informations 👨‍🎓",font=("times new roman",27,"bold"),bg="black",fg="red")
        title_lbl.place(x=0,y=0,width=1430,height=53)

        ##----Main Frame
        main_frame=Frame(bg_img,bd=2)
        main_frame.place(x=10,y=60,width=1344,height=600)

        ## Lable Frames
        # left side
        Left_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student's Details",font=("times new roman",12,"bold"))
        Left_frame.place(x=10,y=10,width=660,height=600)
        imgleft=Image.open(r"pts\studentdata.jpg")
        imgleft=imgleft.resize((620,100),Image.ANTIALIAS)
        self.photoimgleft=ImageTk.PhotoImage(imgleft)

        Left_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student's Details",font=("times new roman",12,"bold"))
        Left_frame.place(x=10,y=10,width=660,height=600)

        f_lbl=Label(Left_frame,image=self.photoimgleft)
        f_lbl.place(x=10,y=0,width=620,height=100)

        #frame---current cource
        Crnt_cors_frame=LabelFrame(Left_frame,bd=2,bg="white",relief=RIDGE,text="Course Information",font=("times new roman",12,"bold"))
        Crnt_cors_frame.place(x=5,y=100,width=660,height=125)

        #Lables-in-Combobox---Department
        dep_label=Label(Crnt_cors_frame,text="Department",font=("times new roman",12,"bold"))
        dep_label.grid(row=0,column=0,padx=10,sticky=W)

        dep_combo=ttk.Combobox(Crnt_cors_frame,textvariable=self.var_dep,font=("times new roman",12,"bold"),state="readonly")
        dep_combo["values"]=("Select Department","IT","Computer","E&TC","Civil","Mechanical","Chemical")
        dep_combo.current(0)
        dep_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)
        #Lables-in-Combobox---Year
        yer_label=Label(Crnt_cors_frame,text="Year",font=("times new roman",12,"bold"))
        yer_label.grid(row=0,column=2,padx=10,sticky=W)

        yer_combo=ttk.Combobox(Crnt_cors_frame,textvariable=self.var_year,font=("times new roman",12,"bold"),state="readonly")
        yer_combo["values"]=("Select Year","2018-19","2019-20","2020-21","2021-22")
        yer_combo.current(0)
        yer_combo.grid(row=0,column=3,padx=2,pady=10,sticky=W)
        #Lables-in-Combobox---Class
        cls_label=Label(Crnt_cors_frame,text="Class",font=("times new roman",12,"bold"))
        cls_label.grid(row=1,column=0,padx=10,sticky=W)

        cls_combo=ttk.Combobox(Crnt_cors_frame,textvariable=self.var_course,font=("times new roman",12,"bold"),state="readonly")
        cls_combo["values"]=("Select Course","FE","SE","TE","BE")
        cls_combo.current(0)
        cls_combo.grid(row=1,column=1,padx=2,pady=10,sticky=W)
        #Lables-in-Combobox---Semister
        sem_label=Label(Crnt_cors_frame,text="Semister",font=("times new roman",12,"bold"))
        sem_label.grid(row=1,column=2,padx=10,sticky=W)

        sem_combo=ttk.Combobox(Crnt_cors_frame,textvariable=self.var_semester,font=("times new roman",12,"bold"),state="readonly")
        sem_combo["values"]=("Select Semister","Fist-Sem","Second-Sem")
        sem_combo.current(0)
        sem_combo.grid(row=1,column=3,padx=2,pady=10,sticky=W)

        #frame---Student Info
        StuInfo_frame=LabelFrame(Left_frame,bd=2,bg="white",relief=RIDGE,text="Student Information",font=("times new roman",12,"bold"))
        StuInfo_frame.place(x=5,y=220,width=660,height=295)
        #1Sudent Name
        StuNm_label=Label(StuInfo_frame,text="Student Name",font=("times new roman",12,"bold"))
        StuNm_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)
        StuNm_entry=ttk.Entry(StuInfo_frame,textvariable=self.var_std_name,width=20,font=("times new roman",12,"bold"))
        StuNm_entry.grid(row=0,column=1,padx=10,pady=5,sticky=W)
        #2SudentID
        StuId_label=Label(StuInfo_frame,text="Student-ID",font=("times new roman",12,"bold"))
        StuId_label.grid(row=0,column=2,padx=10,pady=5,sticky=W)
        StuInfo_entry=ttk.Entry(StuInfo_frame,textvariable=self.var_std_id,width=20,font=("times new roman",12,"bold"))
        StuInfo_entry.grid(row=0,column=3,padx=10,pady=5,sticky=W)
        #3 Class Div
        ClsDiv_label=Label(StuInfo_frame,text="Class Division",font=("times new roman",12,"bold"))
        ClsDiv_label.grid(row=1,column=0,padx=10,pady=5,sticky=W)
        ClsDiv_entry=ttk.Entry(StuInfo_frame,textvariable=self.var_div,width=20,font=("times new roman",12,"bold"))
        ClsDiv_entry.grid(row=1,column=1,padx=10,pady=5,sticky=W)
        #4Sudent Roll No
        RN_label=Label(StuInfo_frame,text="Roll Number",font=("times new roman",12,"bold"))
        RN_label.grid(row=1,column=2,padx=10,pady=5,sticky=W)
        RN_entry=ttk.Entry(StuInfo_frame,textvariable=self.var_roll,width=20,font=("times new roman",12,"bold"))
        RN_entry.grid(row=1,column=3,padx=10,pady=5,sticky=W)
        #5Sudent Gender
        Gen_label=Label(StuInfo_frame,text="Gender",font=("times new roman",12,"bold"))
        Gen_label.grid(row=2,column=0,padx=10,pady=5,sticky=W)
        Gen_entry=ttk.Entry(StuInfo_frame,textvariable=self.var_gender,width=20,font=("times new roman",12,"bold"))
        Gen_entry.grid(row=2,column=1,padx=10,pady=5,sticky=W)
        #6Sudent DOB
        Dob_label=Label(StuInfo_frame,text="Date of Birth",font=("times new roman",12,"bold"))
        Dob_label.grid(row=2,column=2,padx=10,pady=5,sticky=W)
        Dob_entry=ttk.Entry(StuInfo_frame,textvariable=self.var_dob,width=20,font=("times new roman",12,"bold"))
        Dob_entry.grid(row=2,column=3,padx=10,pady=5,sticky=W)
        #7Sudent Email
        Email_label=Label(StuInfo_frame,text="Email-ID",font=("times new roman",12,"bold"))
        Email_label.grid(row=3,column=0,padx=10,pady=5,sticky=W)
        Email_entry=ttk.Entry(StuInfo_frame,textvariable=self.var_email,width=20,font=("times new roman",12,"bold"))
        Email_entry.grid(row=3,column=1,padx=10,pady=5,sticky=W)
        #8Sudent Mobile No
        Mob_label=Label(StuInfo_frame,text="Mobile Number",font=("times new roman",12,"bold"))
        Mob_label.grid(row=3,column=2,padx=10,pady=5,sticky=W)
        Mob_entry=ttk.Entry(StuInfo_frame,textvariable=self.var_phone,width=20,font=("times new roman",12,"bold"))
        Mob_entry.grid(row=3,column=3,padx=10,pady=5,sticky=W)
        #9Sudent Address
        Adrs_label=Label(StuInfo_frame,text="Address",font=("times new roman",12,"bold"))
        Adrs_label.grid(row=4,column=0,padx=10,pady=5,sticky=W)
        Adrs_entry=ttk.Entry(StuInfo_frame,textvariable=self.var_address,width=20,font=("times new roman",12,"bold"))
        Adrs_entry.grid(row=4,column=1,padx=10,pady=5,sticky=W)
        #10Sudent Teacher name
        Ctn_label=Label(StuInfo_frame,text="Class Teacher Name",font=("times new roman",12,"bold"))
        Ctn_label.grid(row=4,column=2,padx=10,pady=5,sticky=W)
        Ctn_entry=ttk.Entry(StuInfo_frame,textvariable=self.var_teacher,width=20,font=("times new roman",12,"bold"))
        Ctn_entry.grid(row=4,column=3,padx=10,pady=5,sticky=W)

        #Radio-Buttons
        self.var_radio1=StringVar()
        Radiobutton1=ttk.Radiobutton(StuInfo_frame,textvariable=self.var_radio1,text="Take Photo Sample",value="Yes")
        Radiobutton1.grid(row=6,column=0)
        self.var_radio2=StringVar()
        Radiobutton2=ttk.Radiobutton(StuInfo_frame,textvariable=self.var_radio2,text="No Photo Sample",value="No")
        Radiobutton2.grid(row=6,column=1)

        #Radio Button Frame
        btn_frame=Frame(StuInfo_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=0,y=200,width=650,height=35)
        tps_btn=Button(btn_frame,text="Take a Photo Sample",width=35,font=("times new roman",12,"bold"),bg="black",fg="yellow")
        tps_btn.grid(row=0,column=0)
        update_btn=Button(btn_frame,text="Update a Photo Sample",width=35,font=("times new roman",12,"bold"),bg="black",fg="yellow")
        update_btn.grid(row=0,column=1)

        btn_frame=Frame(StuInfo_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=0,y=237,width=650,height=35)

        save_btn=Button(btn_frame,text="save",command=self.add_data,width=17,font=("times new roman",12,"bold"),bg="black",fg="yellow")
        save_btn.grid(row=0,column=0)

        up_btn=Button(btn_frame,text="Update",width=17,font=("times new roman",12,"bold"),bg="black",fg="yellow")
        up_btn.grid(row=0,column=1)

        del_btn=Button(btn_frame,text="Delete",width=17,font=("times new roman",12,"bold"),bg="black",fg="yellow")
        del_btn.grid(row=0,column=2)

        res_btn=Button(btn_frame,text="Reset",width=17,font=("times new roman",12,"bold"),bg="black",fg="yellow")
        res_btn.grid(row=0,column=3)

        ##Left side close
        ##____________________________________________________________________________________________________________


        # Right side Frame
        Right_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Attendace Details",font=("times new roman",12,"bold"))
        Right_frame.place(x=665,y=10,width=666,height=533)
        # Right side
        img_right=Image.open(r"pts\unnamed.jpg")
        img_right=img_right.resize((620,100),Image.ANTIALIAS)
        self.photoimg_right=ImageTk.PhotoImage(img_right)
        f_lbl=Label(Right_frame,image=self.photoimg_right)
        f_lbl.place(x=10,y=5,width=640,height=100)
        #frame---Search
        ser_frame=LabelFrame(Right_frame,bd=2,bg="white",relief=RIDGE,text="Search Data",font=("times new roman",12,"bold"))
        ser_frame.place(x=5,y=100,width=650,height=70)
        #Lable
        search_label=Label(ser_frame,text=" Search by 👉",font=("times new roman",13,"bold"),bg="black",fg="yellow")
        search_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)
        #Lables-in-Combobox---Semister

        search_combo=ttk.Combobox(ser_frame,font=("times new roman",12,"bold"),state="readonly",width=15)
        search_combo["values"]=("Select","Roll Number","Mobile Number")
        search_combo.current(0)
        search_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)
        #Entry Fild
        Search_entry=ttk.Entry(ser_frame,width=15,font=("times new roman",12,"bold"))
        Search_entry.grid(row=0,column=2,padx=10,pady=5,sticky=W)
        #-------Button
        Search_btn=Button(ser_frame,text="Search",width=10,font=("times new roman",12,"bold"),bg="black",fg="yellow")
        Search_btn.grid(row=0,column=3,padx=4)

        Shoall_btn=Button(ser_frame,text="Show All",width=10,font=("times new roman",12,"bold"),bg="black",fg="yellow")
        Shoall_btn.grid(row=0,column=4,padx=4)

        #frame-for Table
        table_frame=LabelFrame(Right_frame,bd=2,bg="white",relief=RIDGE)
        table_frame.place(x=5,y=170,width=650,height=300)
        #scroll bar
        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.Student_table=ttk.Treeview(table_frame,column=("dept","course","year","sem","id","name","div","roll","gender","dob","email","mobile","address","teacher","photo"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.Student_table.xview)
        scroll_y.config(command=self.Student_table.yview)

        self.Student_table.heading("dept",text="Department")
        self.Student_table.heading("course",text="Course")
        self.Student_table.heading("year",text="Year")
        self.Student_table.heading("sem",text="Semister")
        self.Student_table.heading("id",text="Student ID")
        self.Student_table.heading("name",text="Name")
        self.Student_table.heading("div",text="Division")
        self.Student_table.heading("dob",text="DOB")
        self.Student_table.heading("email",text="Email")
        self.Student_table.heading("mobile",text="Mobile No.")
        self.Student_table.heading("address",text="Address")
        self.Student_table.heading("teacher",text="Teacher")
        self.Student_table.heading("photo",text="Photo Sample Status")
        self.Student_table["show"]="headings"

        self.Student_table.column("dept",width=100)
        self.Student_table.column("course",width=100)
        self.Student_table.column("year",width=100)
        self.Student_table.column("sem",width=100)
        self.Student_table.column("id",width=100)
        self.Student_table.column("name",width=100)
        self.Student_table.column("div",width=100)
        self.Student_table.column("dob",width=100)
        self.Student_table.column("email",width=100)
        self.Student_table.column("mobile",width=100)
        self.Student_table.column("address",width=100)
        self.Student_table.column("teacher",width=100)
        self.Student_table.column("photo",width=100)

        self.Student_table.pack(fill=BOTH,expand=1)

    # Functions for DB_MySql
    def add_data(self):
        if self.var_dep.get()=="Select Department" or self.var_std_name.get()=="" or self.var_std_id.get()=="":
            messagebox.showerror("Error 👾","कृपया नारळ बाहेर फोडा 🧄🥑🥥 ",parent=self.root)
        else:
            messagebox.showinfo(" Data is Saved","Wellcome 🙏")
            #Mysql Database Connecton>>>>




       

        
        






#------------------Main Coding Stop-------------------------------------------------------

if __name__ == "__main__":
    root=Tk()
    obj=Student(root)
    root.mainloop()

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #  # 
#   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #  #
# #                                                                                                                  # #
# #   Project Title: Face Recognition Based Automatic Attendance  System using Machine Learning                      # #
# #   Programming laguage: Python                                                                                    # #
# #   Author: Dnyaneshwar Patil                                                                                      # #
# #   Mail: patildnyaneshwarit@gmail.com                                                                             # #
# #   Date: 12/12/2020                                                                                               # #
# #                                                                                                                  # #
#   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #  #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #  # 

from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from student import Student   #student module 

class Face_Recognition_System:  #_______Creating a main window
    def __init__(self,root):
        self.root=root
        self.root.geometry("1024x720+0+0")
        self.root.title("Face Recognition System")
#------------------Main Coding Start

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
        title_lbl=Label(bg_img,text="Face Recognition Based Automatic Attendance  System using Machine Learning",font=("times new roman",27,"bold"),bg="black",fg="red")
        title_lbl.place(x=0,y=0,width=1430,height=53)

        ## L1 Button---->student_Info------LeftSide
        img4=Image.open(r"pts\camvi.jpg")
        img4=img4.resize((220,100),Image.ANTIALIAS)
        self.photoimg4=ImageTk.PhotoImage(img4)

        b1=Button(bg_img,image=self.photoimg4,command=self.student_details,cursor="hand2")
        b1.place(x=50,y=120,width=220,height=90)
        b11=Button(bg_img,text="Student Info",command=self.student_details,font=("times new roman",18,"bold"),bg="black",fg="red",cursor="hand2")
        b11.place(x=50,y=70,width=220,height=50)

        ## L2 Button---->student_Attendace
        img5=Image.open(r"pts\Sca01.jpg")
        img5=img5.resize((220,100),Image.ANTIALIAS)
        self.photoimg5=ImageTk.PhotoImage(img5)

        b1=Button(bg_img,image=self.photoimg5,cursor="hand2")
        b1.place(x=50,y=270,width=220,height=90)
        b11=Button(bg_img,text="Attendance",font=("times new roman",18,"bold"),bg="black",fg="red",cursor="hand2")
        b11.place(x=50,y=230,width=220,height=50)

        ## L3 Button---->student_Images
        img6=Image.open(r"pts\images.jpg")
        img6=img6.resize((220,100),Image.ANTIALIAS)
        self.photoimg6=ImageTk.PhotoImage(img6)

        b1=Button(bg_img,image=self.photoimg6,cursor="hand2")
        b1.place(x=50,y=430,width=220,height=90)
        b11=Button(bg_img,text="Images",font=("times new roman",18,"bold"),bg="black",fg="red",cursor="hand2")
        b11.place(x=50,y=385,width=220,height=50)

        #----------------------------------------------------------------------------------------------
        ## R1 Button---->sAdministrator------------------RightSide
        img7=Image.open(r"pts\Coding.gif")
        img7=img7.resize((220,100),Image.ANTIALIAS)
        self.photoimg7=ImageTk.PhotoImage(img7)

        ba1=Button(bg_img,image=self.photoimg7,cursor="hand2")
        ba1.place(x=1100,y=120,width=220,height=90)
        ba11=Button(bg_img,text="Administrator",font=("times new roman",18,"bold"),bg="black",fg="red",cursor="hand2")
        ba11.place(x=1100,y=70,width=220,height=50)

        ## R2 Button---->Support
        img8=Image.open(r"pts\support.jpg")
        img8=img8.resize((220,100),Image.ANTIALIAS)
        self.photoimg8=ImageTk.PhotoImage(img8)

        bb1=Button(bg_img,image=self.photoimg8,cursor="hand2")
        bb1.place(x=1100,y=270,width=220,height=90)
        bb11=Button(bg_img,text="Support",font=("times new roman",18,"bold"),bg="black",fg="red",cursor="hand2")
        bb11.place(x=1100,y=230,width=220,height=50)

        ## R3 Button---->Terminate
        imgp=Image.open(r"pts\exit.gif")
        imgp=imgp.resize((220,100),Image.ANTIALIAS)
        self.photoimgp=ImageTk.PhotoImage(imgp)

        bc1=Button(bg_img,image=self.photoimgp,cursor="hand2")
        bc1.place(x=1100,y=430,width=220,height=90)
        bc11=Button(bg_img,text="Terminate",font=("times new roman",18,"bold"),bg="black",fg="red",cursor="hand2")
        bc11.place(x=1100,y=385,width=220,height=50)

        ##----1 Middle Button
        img4m=Image.open(r"pts\train.jpg")
        img4m=img4m.resize((400,180),Image.ANTIALIAS)
        self.photoimg4m=ImageTk.PhotoImage(img4m)

        b1m=Button(bg_img,image=self.photoimg4m,cursor="hand2")
        b1m.place(x=300,y=120,width=400,height=180)
        b11m=Button(bg_img,text="Train Dataset",font=("times new roman",18,"bold"),bg="black",fg="red",cursor="hand2")
        b11m.place(x=300,y=70,width=400,height=50)

        ##----2 Middle Button
        img4m2=Image.open(r"pts\Fr.jpg")
        img4m2=img4m2.resize((400,180),Image.ANTIALIAS)
        self.photoimg4m2=ImageTk.PhotoImage(img4m2)

        b1m2=Button(bg_img,image=self.photoimg4m2,cursor="hand2")
        b1m2.place(x=675,y=341,width=400,height=180)
        b11m2=Button(bg_img,text="Face Recognition",font=("times new roman",18,"bold"),bg="black",fg="red",cursor="hand2")
        b11m2.place(x=675,y=307,width=400,height=50)
      

      # Buttons-----> FUnctions
    def student_details(self):
      self.new_window=Toplevel(self.root)
      self.app=Student(self.new_window)







    















#------------------Main Coding Stop
if __name__ == "__main__":
    root=Tk()
    obj=Face_Recognition_System(root)
    root.mainloop()


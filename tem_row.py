


########################################################################################################################
# #################################################################################################################### #
# #                                                                                                                  # #
# #   Project Title: Face Recognition Based Automatic Attendance  System using Machine Learning                      # #
# #   Programming laguage: Python                                                                                    # #
# #   Author: Dnyaneshwar Patil                                                                                      # #
# #   Mail: patildnyaneshwarit@gmail.com                                                                             # #
# #   Date: 12/12/2020                                                                                               # #
# #                                                                                                                  # #
# #################################################################################################################### #
########################################################################################################################


#-----------------Importing main library---------------------------------------------
from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk



class Face_Recognition_System:  #_______Creating a main window
    def __init__(self,root):
        self.root=root
        self.root.geometry("1024x720+0+0")
        self.root.title("Face Recognition System")

#------------------Main Coding Start-------------------------------------------------------





#------------------Main Coding Stop-------------------------------------------------------
if __name__ == "__main__":
    root=Tk()
    obj=Face_Recognition_System(root)
    root.mainloop()















## 1 Button---->student_Info
        img4=Image.open(r"C:\Users\AJAY\Videos\ML\pts\camvi.jpg")
        img4=img4.resize((220,100),Image.ANTIALIAS)
        self.photoimg4=ImageTk.PhotoImage(img4)

        b1=Button(bg_img,image=self.photoimg4,cursor="hand2")
        b1.place(x=50,y=120,width=220,height=90)
        b11=Button(bg_img,text="Student Info",font=("times new roman",18,"bold"),bg="black",fg="red",cursor="hand2")
        b11.place(x=50,y=70,width=220,height=50)





		Department   
		dep_label.grid(row=0,column=0,padx=10,sticky=W)
		dep_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)
		             
		Years   
		dep_label.grid(row=0,column=2,padx=10,sticky=W)
		dep_combo.grid(row=0,column=3,padx=2,pady=10,sticky=W)
		
		Course        
		dep_label.grid(row=1,column=0,padx=10,sticky=W)
		dep_combo.grid(row=1,column=1,padx=2,pady=10,sticky=W)
		
		Semester     
		dep_label.grid(row=1,column=2,padx=10,sticky=W)
		dep_combo.grid(row=1,column=3,padx=2,pady=10,sticky=W)
		
		
		Dep                  course 
		year                 semester
		
		
		Dep                   year
		course                semester   
		
		
		
		dep_label.grid(row=0,column=2,padx=10,sticky=W)
		dep_combo.grid(row=0,column=3,padx=2,pady=10,sticky=W)            






Sudent Attributes
 
StuID               StuNmae
ClassDiv            Roll No.
Gender              DOB
Emails              Mobile No
Address             Teacher name


StuName          Class Div
StuID            Teacher name
Roll No          Mobile No
DOB              Email 
Gender           Address 

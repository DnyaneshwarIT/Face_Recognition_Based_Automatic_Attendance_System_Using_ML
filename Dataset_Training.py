from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import numpy as np
#import pyglet

class Dataset_Training:  #_______Creating a main window
    def __init__(self,root):
        self.root=root
        self.root.geometry("1024x720+0+0")
        self.root.title("😛😵🥴🙂😎  Dataset Training for Faces 😀 😊 😉 🙄 😮")
        ##---Project Title
        title_lbl=Label(self.root,text="👨‍👨‍👦‍👦👨‍👨‍👧‍👦  Dataset Training for Faces 👨‍🦱👩‍🦳👨‍🚒",font=("times new roman",27,"bold"),bg="black",fg="red")
        title_lbl.place(x=0,y=0,width=1430,height=53)
    

    #########################################################################
        #img_top=Image.open(r"pts\MLfinalReco.jpg")
        #img_top=img_top.resize((1365,689),Image.ANTIALIAS)
        #self.photoimg_top=ImageTk.PhotoImage(img_top)

        #f_lbl=Label(self.root,image=self.photoimg_top)
        #f_lbl.place(x=0,y=53,width=1365,height=689)
        imgbg=Image.open(r"pts\MLfinalReco.jpg")
        imgbg=imgbg.resize((1365,689),Image.ANTIALIAS)
        self.photoimgbg=ImageTk.PhotoImage(imgbg)

        bg_img=Label(self.root,image=self.photoimgbg)
        bg_img.place(x=0,y=53,width=1365,height=689)
    

    ## Button for training dataset                         # 220 100
        img4=Image.open(r"pts\Face-scan.jpg")
        img4=img4.resize((350,170),Image.ANTIALIAS)
        self.photoimg4=ImageTk.PhotoImage(img4)

        b1=Button(bg_img,image=self.photoimg4,command=self.train_data,cursor="hand2")
        b1.place(x=272,y=350,width=347,height=170)
        b11=Button(bg_img,text="👨‍👨‍👦‍👦👨‍👨‍👧‍👦 Training Dataset 👨‍🦱👩‍🦳👨‍🚒",command=self.train_data,font=("times new roman",18,"bold"),bg="cyan",fg="blue",cursor="hand2")
        b11.place(x=272,y=510,width=347,height=35)
    

    ### Training Dataset
    def train_data(self):
        data_dir=("data")
        path=[os.path.join(data_dir,file) for file in os.listdir(data_dir)]

        faces=[]
        ids=[]

        for image in path:
            img=Image.open(image).convert('L')   # this line converting to the GRAY Scale Images
            imageNp=np.array(img,'uint8')
            id=int(os.path.split(image)[1].split('.')[1])

            faces.append(imageNp)
            ids.append(id)
            cv2.imshow("Faces Training",imageNp)
            cv2.waitKey(1)==13
        ids=np.array(ids)

        ###### Training Algorithm LBPH Classifire

        recognizer=cv2.face.LBPHFaceRecognizer_create()
        recognizer.train(faces,ids)
        recognizer.write("classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Result","Your Dataset Training is Susscessfully Completed !",parent=self.root)

        


    
    


if __name__ == "__main__":
    
    root=Tk()
    obj=Dataset_Training(root)
    root.mainloop()


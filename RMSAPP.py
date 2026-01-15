
from tkinter import*
from PIL import Image,ImageTk,ImageDraw
from course import Classcourse
from student import Classstudent
from result import resultclass
from report import reportclass
from tkinter import messagebox,ttk
import os
from datetime import*
import time
from math import*
import sqlite3

class RMS:
    def __init__(self,window):
        self.window=window
        self.window.title("Result Managment System")
        self.window.geometry("1350x700+0+0")
        self.window.config(bg='white')

        self.logo_dash=ImageTk.PhotoImage(file=r'C:\Users\Rupam\OneDrive\Attachments\Documents\Python first project.py\logo_pppp.png')


        title=Label(self.window,text="Result management System",padx=10,compound=LEFT,image=self.logo_dash,font=("goudy old style",20,'bold'),bg="#033054",fg="white").place(x=0,y=0,relwidth=1,height=50)
        M_frame=LabelFrame(self.window,text="Menu",font=("times new roman",15),bg='white',fg="#031753")
        M_frame.place(x=10,y=70,width=1345,height=80)
        btn_course=Button(M_frame,text='Course',font=('goudy old style',15,'bold'),bg='#0b5377',fg='white',cursor='hand2',command=self.add_course).place(x=20,y=5,width=200,height=40)
        btn_student=Button(M_frame,text='Student',font=('goudy old style',15,'bold'),bg='#0b5377',fg='white',cursor='hand2',command=self.add_student).place(x=240,y=5,width=200,height=40)
        btn_result=Button(M_frame,text='Result',font=('goudy old style',15,'bold'),bg='#0b5377',fg='white',cursor='hand2',command=self.add_result).place(x=460,y=5,width=200,height=40)
        btn_view=Button(M_frame,text='View Student result',font=('goudy old style',15,'bold'),bg='#0b5377',fg='white',cursor='hand2',command=self.add_report).place(x=680,y=5,width=200,height=40)
        btn_logout=Button(M_frame,text='logout',font=('goudy old style',15,'bold'),bg='#0b5377',fg='white',cursor='hand2',command=self.logout).place(x=900,y=5,width=200,height=40)
        btn_exit=Button(M_frame,text='Exit',font=('goudy old style',15,'bold'),bg='#0b5377',fg='white',cursor='hand2',command=self.exit_).place(x=1120,y=5,width=200,height=40)
        
        self.bg_img=Image.open(r'C:\Users\Rupam\OneDrive\Attachments\Documents\Python first project.py\bg.png')
        self.bg_img=self.bg_img.resize((920,350),Image.LANCZOS) #resizeing the image
        self.bg_img=ImageTk.PhotoImage(self.bg_img) # converts the Pillow images into tkinter understandable format

        self.lbl_bg=Label(self.window,image=self.bg_img).place(x=400,y=180,width=920,height=350) 

        self.lbl_course=Label(self.window,text='Total Courses\n [0]',font=('goudy old style',20),bd=10,relief=RIDGE,bg='#e43b06',fg='white')
        self.lbl_course.place(x=400,y=530,width=300,height=100)
        self.lbl_student=Label(self.window,text='Total Students\n [0]',font=('goudy old style',20),bd=10,relief=RIDGE,bg='#0676ad',fg='white')
        self.lbl_student.place(x=710,y=530,width=300,height=100)
        self.lbl_result=Label(self.window,text='Total Results\n [0]',font=('goudy old style',20),bd=10,relief=RIDGE,bg='#038074',fg='white')
        self.lbl_result.place(x=1020,y=530,width=300,height=100)
       
        self.lbl=Label(self.window,text="\nAnalog Clock",font=("Book Antiqua",25,"bold"),fg="white",compound=BOTTOM,bg="#28323C",bd=10)
        self.lbl.place(x=10,y=180,height=450,width=350)
        self.working()
#=====================================================
        footer=Label(self.window,text="SRMS-Result Management System\n Contact us for any technical issue on 826xxxxx76.",font=('goudy old style',12),bg='#262626',fg='white').pack(side=BOTTOM,fill=X)
        self.update_details()
#============================================================
    def update_details(self):
        con=sqlite3.connect(database='rms.db')
        cur=con.cursor()
        try:
           cur.execute("select * from course ")
           cr=cur.fetchall()
           self.lbl_course.config(text=f"Total Courses\n[{str(len(cr))}]")

           cur.execute("select * from student ")
           cr=cur.fetchall()
           self.lbl_student.config(text=f"Total Students\n[{str(len(cr))}]")
 
           cur.execute("select * from result ")
           cr=cur.fetchall()
           self.lbl_result.config(text=f"Total Results\n[{str(len(cr))}]")

           self.lbl_course.after(200,self.update_details)
          
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")

   
   
    def working(self): #(fetching live hour min and sec)
        h=datetime.now().time().hour
        m=datetime.now().time().minute
        s=datetime.now().time().second
        
        hr = (h % 12) * 30 + (m * 0.5)
        min_ = m * 6
        sec_ = s * 6
        self.clock_image(hr,min_,sec_)
        self.img=ImageTk.PhotoImage(file="clock_new.png")
        self.lbl.config(image=self.img)
        self.lbl.after(1000,self.working)



    def clock_image(self,hr,min_,sec_):#clock image 
        clock=Image.new("RGB",(400,400),(40,50,60)) #(image width=400,height=400) & background colour (255,255,255)white
        draw=ImageDraw.Draw(clock) # draw image 
        #===for clock image===
        bg=Image.open('ct.png') #open 
        bg=bg.resize((300,300),Image.LANCZOS)#& resize clock imagec
        clock.paste(bg,(50,50)) # paste image from top 50 and side 50 

        #Formula to rotate the clock anticlockwise
        #angle_in_radian=angle in degrees*math.pi/100
        #line_lenght=100
        #center_x=250
        #center_y=250
        # end_x=center_x+line_length * math.cos(angle_in_radians)
        # end_y=center_y-line_length * math.sin(angle_in_radians)


        #====for hour line======
        origin=200,200
        draw.line((origin,200+50*sin(radians(hr)),200-50*cos(radians(hr))),fill="red",width=4)
        #====for min line======
        draw.line((origin,200+70*sin(radians(min_)),200-70*cos(radians(min_))),fill="white",width=3)
        #====for sec line======
        draw.line((origin,200+80*sin(radians(sec_)),200-80*cos(radians(sec_))),fill="yellow",width=2)
        draw.ellipse((190,190,205,205),fill="#1AD5D5")
        clock.save("clock_new.png")


    def working(self): #(fetching live hour min and sec)
        h=datetime.now().time().hour
        m=datetime.now().time().minute
        s=datetime.now().time().second
        
        hr = (h % 12) * 30 + (m * 0.5)
        min_ = m * 6
        sec_ = s * 6
        self.clock_image(hr,min_,sec_)
        self.img=ImageTk.PhotoImage(file="clock_new.png")
        self.lbl.config(image=self.img)
        self.lbl.after(1000,self.working)


    def add_course(self):
        self.new_win=Toplevel(self.window)
        self.new_obj=Classcourse(self.new_win)    

    def add_student(self):
        self.new_win=Toplevel(self.window)
        self.new_obj=Classstudent(self.new_win)

    def add_result(self):
        self.new_win=Toplevel(self.window)
        self.new_obj=resultclass(self.new_win)

        
    def add_report(self):
        self.new_win=Toplevel(self.window)
        self.new_obj=reportclass(self.new_win)   

    def logout(self):
        op=messagebox.askyesno("Confirm","Do you really want to logou?",parent=self.window)
        if op== True:
            self.window.destroy()
            os.system("python login.py")

    def exit_(self):
        op=messagebox.askyesno("Confirm","Do you really want to Exit?",parent=self.window)
        if op== True:
            self.window.destroy()
            




if __name__=="__main__":
    window=Tk()
    Obj=RMS(window)
    window.mainloop()



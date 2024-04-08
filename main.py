from tkinter import *  # importing tkinter module
# from PIL import Image, ImageTK
from PIL import Image, ImageTk

from customer import Customer_restrn_win
from room import Room_book



class HotelManagementSystem():
    def __init__(self,root):
        self.root = root
        self.root.title("HotelManagementSystem")
        self.root.geometry("1550x800+0+0")

#  ###############################BannerImage################################################
        Img1 = Image.open("C:/Users/user/OneDrive/Desktop/HMS Python Project/Images/bannerImage.jpg")
        Img1= Img1.resize((1555,140))

        self.photoImag1=ImageTk.PhotoImage(Img1)
        lblImg=Label(self.root,image=self.photoImag1,bd=4,relief=RIDGE)
        lblImg.place(x=228, y=0,width= 1135,height=140)

#  ###############################LogoImage################################################
        Img2 = Image.open("C:/Users/user/OneDrive/Desktop/HMS Python Project/Images/Hotellogo.jpeg")
        Img2= Img2.resize((230,140))

        self.photoImag2=ImageTk.PhotoImage(Img2)
        lblImg2=Label(self.root,image=self.photoImag2,bd=4,relief=RIDGE)
        lblImg2.place(x=0, y=0,width= 230,height=140)

#  ############################### Title ################################################
        lbl_title = Label(self.root,text=" Hotel Management System ".upper(),font=("Rockwell",25,"bold"),bg="#100E0F",fg="#DBCCA1",bd=4,relief=RIDGE)
        lbl_title.place(x=0,y=140,width=1365,height=50)


#  ############################### Main Frame ################################################
        main_frame=Frame(self.root,bd=5,relief=RIDGE)
        main_frame.place(x=0,y=190,width=1367,height=620)


#  ############################### Menu ################################################
        lbl_menu = Label(main_frame,text=" MENU".upper(),font=("Rockwell",25,"bold"),bg="#100E0F",fg="#DBCCA1",bd=4,relief=RIDGE)
        lbl_menu.place(x=0,y=0,width=230,height=50)


#  ############################### Menu Frame ################################################
        menu_frame=Frame(main_frame,bd=5,relief=RIDGE)
        menu_frame.place(x=0,y=50,width=230,height=210)

#  ############################### Buttons ################################################
# ---------------------------- customer button ------------------------------------
        cust_btn = Button(menu_frame,text="Customer Registrn",font=("Rockwell",16,"bold"),bg="#100E0F",fg="#DBCCA1",bd=4,relief=RIDGE,cursor="hand2" ,command = self.cust_details)
        cust_btn .place(x=0,y=0,width=221,height=40)

# ---------------------------- Booking button ------------------------------------
        Book_btn = Button(menu_frame,text="Booking",font=("Rockwell",16,"bold"),bg="#100E0F",fg="#DBCCA1",bd=4,relief=RIDGE ,cursor="hand2" ,command = self.BookRoom_details )
        Book_btn .place(x=0,y=40,width=221,height=40)

# ---------------------------- Detail button ------------------------------------
        detail_btn = Button(menu_frame,text="Details",font=("Rockwell",16,"bold"),bg="#100E0F",fg="#DBCCA1",bd=4,relief=RIDGE,cursor="hand2")
        detail_btn .place(x=0,y=80,width=221,height=40)

  
        report_btn = Button(menu_frame,text="Report",font=("Rockwell",16,"bold"),bg="#100E0F",fg="#DBCCA1",bd=4,relief=RIDGE,cursor="hand2")
        report_btn .place(x=0,y=120,width=221,height=40)

# ---------------------------- Logout button ------------------------------------
        logout_btn = Button(menu_frame,text="Logout",font=("Rockwell",16,"bold"),bg="#100E0F",fg="#DBCCA1",bd=4,relief=RIDGE,cursor="hand2")
        logout_btn .place(x=0,y=160,width=221,height=40)


#  ###############################left Bottom corner Image  ################################################
        Img3 = Image.open("C:/Users/user/OneDrive/Desktop/HMS Python Project/Images/leftcorner1.jpeg")
        Img3= Img3.resize((230,340))

        self.photoImag3=ImageTk.PhotoImage(Img3)
        lblImg3=Label(self.root,image=self.photoImag3,bd=4,relief=RIDGE)
        lblImg3.place(x=0, y=455,width= 235,height=300)

#  ############################### Center Image  ################################################
        Img4 = Image.open("C:/Users/user/OneDrive/Desktop/HMS Python Project/Images/MainImage.jpg")
        Img4= Img4.resize((1135,540))

        self.photoImag4=ImageTk.PhotoImage(Img4)
        lblImg4=Label(self.root,image=self.photoImag4,bd=4,relief=RIDGE)
        lblImg4.place(x=233, y=190,width= 1130,height=540)


#  ############################### Customer WIndow  ################################################
    
    def cust_details(self):
        self.new_window=Toplevel(self.root)
        self.cust=Customer_restrn_win(self.new_window)  

#  ############################### Room Booking WIndow  ################################################
    
    def BookRoom_details(self):
        self.new_window=Toplevel(self.root)
        self.cust=Room_book(self.new_window)  

if __name__ == "__main__" :
    root = Tk()
    objec=HotelManagementSystem(root)
    root.mainloop()


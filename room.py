import mysql.connector
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from PIL import Image , ImageTk
import random
from tkcalendar import DateEntry
import datetime

class Room_book:
    def __init__(self,root):
        self.root=root
        self.root.title("Book Room for Customer")
        self.root.geometry("1130x550+237+224")

#  ==================================Variables====================================
        self.Var_cust_mobile1=StringVar()
        self.Var_cust_chec_kin=StringVar()
        self.Var_cust_chec_kout=StringVar()
        self.Var_cust_room_type=StringVar()
        self.Var_cust_meal=StringVar()
        self.Var_cust_room_Available=StringVar()
        self.Var_cust_number_of_days=StringVar()
        self.Var_cust_pai_dtax=StringVar()
        self.Var_cust_sub_total=StringVar()
        self.Var_cust_total_cost=StringVar()


        self.Retrive_Value_cust_ref_cost=StringVar()
        self.Retrive_Value_cust_name_cost=StringVar()
        self.Retrive_Value_cust_gender_cost=StringVar()
        self.Retrive_Value_cust_nationality_cost=StringVar()
        self.Retrive_Value_cust_email_cost=StringVar()
        self.Retrive_Value_cust_address_cost=StringVar()
        self.Retrive_Value_cust_contact_cost=StringVar()




#  ==================================Title====================================
        lbl_title=Label(self.root,text="Room Booking",font=("Rockwell",20,"bold"),bg="#100E0F",fg="#DBCCA1",bd=3,relief=RIDGE)
        lbl_title.place(x=0,y=0,width=1130,height=40)

#  ==================================Title====================================
        img1=Image.open("C:/Users/user/OneDrive/Desktop/HMS Python Project/Images/Hotellogo.jpeg")
        img1=img1.resize((60,40))
        self.photoImag1=ImageTk.PhotoImage(img1)
        lbl_logo=Label(self.root,image=self.photoImag1,bd=2,relief=RIDGE)
        lbl_logo.place(x=0,y=0,width=60,height=40)

#  ==================================LabelFrame====================================
        lbl_Frame= LabelFrame(self.root,text="Book Room",bd=4,relief=RIDGE,padx=2,pady=2,font= ("Rockwell",12,"bold"))
        lbl_Frame.place(x=0,y=40,width=400,height=490) 


#  ==================================Label And Entrys ====================================
# Customer Mobile
#  ----------------------------------Label----------------------------
        lbl_cust_Mobile= Label(lbl_Frame,text="Customer Mobile : ",pady=3,font= ("Rockwell",11,"bold"))
        lbl_cust_Mobile.grid(row=0,column=0,sticky=W)
#  ----------------------------------entry----------------------------
        entry_cust_Mobile=ttk.Entry(lbl_Frame,font=("Rockwell",11,"bold"),width=17,textvariable=self.Var_cust_mobile1 )
        entry_cust_Mobile.grid(row=0,column=1,sticky=W)

# check_in_date
#  ----------------------------------Label----------------------------
        lbl_cust_check_in_date = Label(lbl_Frame,text="Check In Date : ",pady=3,font= ("Rockwell",11,"bold"))
        lbl_cust_check_in_date.grid(row=1,column=0,sticky=W)
#  ----------------------------------entry----------------------------
        def update_number_of_days(event=None):
            self.Var_cust_chec_kout = entry_cust_check_out_date.get_date()
            self.Var_cust_chec_kin = entry_cust_check_in_date.get_date()
            numberofdays = (self.Var_cust_chec_kout - self.Var_cust_chec_kin).days
            self.Var_cust_number_of_days.set(numberofdays)


        min_d = datetime.date.today()
        today_date = datetime.date.today()
        max_d = today_date + datetime.timedelta(days=365 * 2)
        entry_cust_check_in_date = DateEntry(lbl_Frame, font=("Rockwell", 11, "bold"), width=25, selectmode='day', mindate=min_d, maxdate=max_d)
        entry_cust_check_in_date.grid(row=1, column=1)
        entry_cust_check_in_date.bind("<<DateEntrySelected>>", update_number_of_days)


# check_out_date
#  ----------------------------------Label----------------------------
        lbl_Cust_check_out_date = Label(lbl_Frame,text="Check Out Date : ",pady=3,font= ("Rockwell",11,"bold"))
        lbl_Cust_check_out_date.grid(row=2,column=0,sticky=W)
#  ----------------------------------entry----------------------------
        min_d = datetime.date.today()
        today_date = datetime.date.today()
        max_d = today_date + datetime.timedelta(days=365 * 2)
        entry_cust_check_out_date = DateEntry(lbl_Frame, font=("Rockwell", 11, "bold"), width=25, selectmode='day', mindate=min_d, maxdate=max_d)
        entry_cust_check_out_date.grid(row=2, column=1)
        entry_cust_check_out_date.bind("<<DateEntrySelected>>", update_number_of_days)


# room_type
#  ----------------------------------Label----------------------------
        lbl_Cust_room_type = Label(lbl_Frame,text="Room Type : ",pady=3,font= ("Rockwell",11,"bold"))
        lbl_Cust_room_type.grid(row=3,column=0,sticky=W)
#  ----------------------------------Combobox----------------------------
        combo_Cust_room_type=ttk.Combobox(lbl_Frame,font=("Rockwell",11,"bold"),width=25,state="readonly",textvariable=self.Var_cust_room_type)
        combo_Cust_room_type["value"]=("Single","Double","Luxary")
        combo_Cust_room_type.current(0)
        combo_Cust_room_type.grid(row=3,column=1)


# Avaiable Room
#  ----------------------------------Label----------------------------
        lbl_Cust_available_room = Label(lbl_Frame,text="Avaiable Room : ",pady=3,font= ("Rockwell",11,"bold"))
        lbl_Cust_available_room.grid(row=4,column=0,sticky=W)
#  ----------------------------------Combobox----------------------------
        entry_cust_available_room = ttk.Entry(lbl_Frame,font=("Rockwell",11,"bold"),width=25,textvariable=self.Var_cust_room_Available)
        entry_cust_available_room.grid(row=4,column=1)

# Meal
#  ----------------------------------Label----------------------------
        lbl_Cust_meal = Label(lbl_Frame,text="Meal : ",pady=3,font= ("Rockwell",11,"bold"))
        lbl_Cust_meal.grid(row=5,column=0,sticky=W)
#  ----------------------------------Combobox----------------------------
        entry_cust_meal = ttk.Combobox(lbl_Frame,font=("Rockwell",11,"bold"),width=25,textvariable=self.Var_cust_meal)
        entry_cust_meal["values"]=("No meals","1 Meal","2 Meals","3 Meals")
        entry_cust_meal.current(0)
        entry_cust_meal.grid(row=5,column=1)
        

# Number of days
#  ----------------------------------Label----------------------------
        lbl_Cust_number_of_days = Label(lbl_Frame, text="Number of days: ", pady=3, font=("Rockwell", 11, "bold"))
        lbl_Cust_number_of_days.grid(row=6, column=0, sticky="w")
#  ----------------------------------entry----------------------------
        entry_cust_number_of_days = ttk.Entry(lbl_Frame, font=("Rockwell", 11, "bold"), textvariable=self.Var_cust_number_of_days,width=27)
        entry_cust_number_of_days.grid(row=6, column=1)

# Paid tax
#  ----------------------------------Label----------------------------
        lbl_cust_paid_tax = Label(lbl_Frame,text="Paid Tax : ",pady=3,font= ("Rockwell",11,"bold"))
        lbl_cust_paid_tax.grid(row=8,column=0,sticky=W)
#  ----------------------------------entry----------------------------
        entry_cust_paid_tax = ttk.Entry(lbl_Frame,font=("Rockwell",11,"bold"),width=27,textvariable=self.Var_cust_pai_dtax)
        entry_cust_paid_tax.grid(row=8,column=1)



# Sub Total
#  ----------------------------------Label----------------------------
        lbl_Cust_Sub_total = Label(lbl_Frame,text="Sub total : ",pady=3,font= ("Rockwell",11,"bold"))
        lbl_Cust_Sub_total.grid(row=9,column=0,sticky=W)
#  ----------------------------------entry----------------------------
        entry_cust_Sub_total= ttk.Entry(lbl_Frame,font=("Rockwell",11,"bold"),width=27,textvariable=self.Var_cust_sub_total)
        entry_cust_Sub_total.grid(row=9,column=1)

# Total Cost
#  ----------------------------------Label----------------------------
        lbl_Cust_total_cost = Label(lbl_Frame,text="Total Cost : ",pady=3,font= ("Rockwell",11,"bold"))
        lbl_Cust_total_cost.grid(row=10,column=0,sticky=W)
#  ----------------------------------entry----------------------------
        entry_cust_total_cost = ttk.Entry(lbl_Frame,font=("Rockwell",11,"bold"),width=27,textvariable=self.Var_cust_total_cost)
        entry_cust_total_cost.grid(row=10,column=1)

# Click here for button Calculate bill
#  ----------------------------------Label----------------------------
        lbl_Cust_total_cost = Label(lbl_Frame,text="Click here : ",pady=3,font= ("Rockwell",11,"bold"))
        lbl_Cust_total_cost.grid(row=7,column=0,sticky=W)


#  ================================== Button ====================================

#  ----------------------------------BTn fetch----------------------------
        btn_fetch_data=Button(lbl_Frame,text="Fetch Data",font=("Rockwell",9,"bold"),width=8 ,bg="#100E0F",fg="#DBCCA1",bd=3,relief=RIDGE,command=self.Fetch_details)
        btn_fetch_data.place(x=296,y=3,height=22)

#  ----------------------------------Bill fetch----------------------------
        btn_fetch_bill=Button(lbl_Frame,text="Calculate Bill",font=("Rockwell",11,"bold"),width=21 ,bg="#100E0F",fg="#DBCCA1",bd=3,relief=RIDGE)
        btn_fetch_bill.grid(row=7,column=1)
  
#  ----------------------------------BTn Frame----------------------------

        btn_frame=Frame(lbl_Frame,bd=4,relief=RIDGE)
        btn_frame.place(x=0,y=316,width=390,height=90)

#  ----------------------------------BTn Save----------------------------
        btn_save=Button(btn_frame,text="Save",font=("Rockwell",12,"bold"),width=10 ,bg="#100E0F",fg="#DBCCA1",bd=3,relief=RIDGE)
        btn_save.grid(row=0,column=0,padx= 5 , pady=5)
  

#  ----------------------------------BTn Update----------------------------
        btn_Update=Button(btn_frame,text="Update",font=("Rockwell",12,"bold"),width=10 ,bg="#100E0F",fg="#DBCCA1",bd=3,relief=RIDGE)
        btn_Update.grid(row=0,column=1,padx= 5 , pady=5)
  

#  ----------------------------------BTn Delete----------------------------
        btn_Delete=Button(btn_frame,text="Delete",font=("Rockwell",12,"bold"),width=10 ,bg="#100E0F",fg="#DBCCA1",bd=3,relief=RIDGE)
        btn_Delete.grid(row=0,column=2,padx= 5 , pady=5)

#  ----------------------------------BTn Clear----------------------------
        btn_Clear=Button(btn_frame,text="Clear All The Feilds",font=("Rockwell",12,"bold"),width=30 ,bg="#100E0F",fg="#DBCCA1",bd=3,relief=RIDGE)
        # btn_Clear.place(x=30,y=46)
        btn_Clear.grid(row=1,column=0,columnspan = 3)
  
#  ================================== Table Frame for the Data view ====================================

        table_frame= LabelFrame(self.root,text="All Customers Data",bd=4,relief=RIDGE,padx=2,pady=2,font= ("Rockwell",12,"bold"))
        table_frame.place(x=400,y=240,width=720,height=240)

# Search By
#  ----------------------------------Label----------------------------
        lbl_SearchBy = Label(table_frame,text="Search By : ",font= ("Rockwell",11,"bold") ,bg="#100E0F",fg="#DBCCA1")
        lbl_SearchBy.grid(row=0,column=0,sticky=W,pady=5,padx=10)

#  ---------------------------------Combo box----------------------------
        self.var_Search_Type=StringVar()
        combo_Search_Type = ttk.Combobox(table_frame,font= ("Rockwell",11,"bold") ,width=12,state="readonly",textvariable=self.var_Search_Type)
        combo_Search_Type["value"]=("Ref","Name","Mobile")
        combo_Search_Type.current(0)
        combo_Search_Type.grid(row=0,column=1,pady=5,padx=5)

#  ----------------------------------entry----------------------------
        self.var_Search_value = StringVar()
        entry_search_value = ttk.Entry(table_frame,font=("Rockwell",11,"bold"),width=25,textvariable=self.var_Search_value)
        entry_search_value.grid(row=0,column=2,pady=5,padx=5)

#  ----------------------------------BTn Search----------------------------
        btn_search=Button(table_frame,text="Search",font=("Rockwell",11,"bold"),width=10 ,bg="#100E0F",fg="#DBCCA1",bd=3,relief=RIDGE)
        btn_search.grid(row=0,column=3,padx= 5 , pady=5)

#  ----------------------------------BTn Show All----------------------------
        btn_showall=Button(table_frame,text="Show All",font=("Rockwell",11,"bold"),width=10 ,bg="#100E0F",fg="#DBCCA1",bd=3,relief=RIDGE )
        btn_showall.grid(row=0,column=4,pady=5,padx=5)
  
#  ================================== Table Data view ====================================
        Details_tbl_frame=Frame(table_frame,bd=3,relief=RIDGE)
        Details_tbl_frame.place(x=0,y=50,width=700,height=160)

#  ----------------------------------Scrool bar----------------------------
        scroll_x=ttk.Scrollbar(Details_tbl_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(Details_tbl_frame,orient=VERTICAL)

#  ---------------------------------- Dummy head Column in Grid view ----------------------------
        self.customer_Details_table=ttk.Treeview(Details_tbl_frame,columns=("Mobile","Check_in","Check_out","Room_type","Available_room","Meal","Number_of_days","Paid_tax","Sub_total","Total_cost"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

#  ---------------------------------- Set scrool bars to its positions ----------------------------
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

#  ---------------------------------- Set scrool bars to its positions ----------------------------
        scroll_x.config(command=self.customer_Details_table.xview)
        scroll_y.config(command=self.customer_Details_table.yview)

#  ---------------------------------- Dummy column name set  ----------------------------

        self.customer_Details_table.heading("Mobile",text="Mobile Number")
        self.customer_Details_table.heading("Check_in",text="Check In")
        self.customer_Details_table.heading("Check_out",text="Check Out")
        self.customer_Details_table.heading("Room_type",text="Room Type")
        self.customer_Details_table.heading("Available_room",text="Available Room")
        self.customer_Details_table.heading("Meal",text="Meal")
        self.customer_Details_table.heading("Number_of_days",text="Number Of Days")
        self.customer_Details_table.heading("Paid_tax",text="Paid Tax")
        self.customer_Details_table.heading("Sub_total",text="Sub Total")
        self.customer_Details_table.heading("Total_cost",text="Total Cost")

        self.customer_Details_table["show"] = "headings"

#  ---------------------------------- Dummy Width set  ----------------------------

        self.customer_Details_table.column("Mobile",width=100)
        self.customer_Details_table.column("Check_in",width=100)
        self.customer_Details_table.column("Check_out",width=100)
        self.customer_Details_table.column("Room_type",width=100)
        self.customer_Details_table.column("Available_room",width=100)
        self.customer_Details_table.column("Meal",width=100)
        self.customer_Details_table.column("Number_of_days",width=100)
        self.customer_Details_table.column("Paid_tax",width=100)
        self.customer_Details_table.column("Sub_total",width=100)
        self.customer_Details_table.column("Total_cost",width=100)

        self.customer_Details_table.pack(fill=BOTH, expand=1)

        # self.customer_Details_table.bind("<ButtonRelease-1>", self.get_cursor)

        # self.fetch_Data()



#  ==================================Fetched Data LabelFrame====================================
        fetch_lbl_Frame= LabelFrame(self.root,text="Fetched Data",bd=4,relief=RIDGE,padx=2,pady=2,font= ("Rockwell",12,"bold"))
        fetch_lbl_Frame.place(x=400,y=40,width=360,height=200) 


#  ==================================Label Values ====================================
# reference
#  ----------------------------------Label 1----------------------------
        lbl_cust_ref= Label(fetch_lbl_Frame,text="Customer Ref : ",pady=1,font= ("Rockwell",11,"bold"))
        lbl_cust_ref.grid(row=0,column=0,sticky=W)


# Name
#  ----------------------------------Label 1----------------------------
        lbl_cust_Name = Label(fetch_lbl_Frame,text="Name : ",pady=1,font= ("Rockwell",11,"bold"))
        lbl_cust_Name.grid(row=1,column=0,sticky=W)


# Gender
#  ----------------------------------Label 1----------------------------
        lbl_Cust_Gender = Label(fetch_lbl_Frame,text="Gender : ",pady=1,font= ("Rockwell",11,"bold"))
        lbl_Cust_Gender.grid(row=2,column=0,sticky=W)

# Email
#  ----------------------------------Label 1----------------------------
        lbl_Cust_Email = Label(fetch_lbl_Frame,text="Email : ",pady=1,font= ("Rockwell",11,"bold"))
        lbl_Cust_Email.grid(row=3,column=0,sticky=W)


# Nationality
#  ----------------------------------Label 1----------------------------
        lbl_Cust_Nationality = Label(fetch_lbl_Frame,text="Nationality : ",pady=2,font= ("Rockwell",11,"bold"))
        lbl_Cust_Nationality.grid(row=4,column=0,sticky=W)


# Address
#  ----------------------------------Label 1----------------------------
        lbl_Cust_Address = Label(fetch_lbl_Frame,text="Address : ",pady=1,font= ("Rockwell",11,"bold"))
        lbl_Cust_Address.grid(row=5,column=0,sticky=W)


# Contact
#  ----------------------------------Label 1----------------------------
        lbl_Cust_Contact = Label(fetch_lbl_Frame,text="Contact : ",pady=1,font= ("Rockwell",11,"bold"))
        lbl_Cust_Contact.grid(row=6,column=0,sticky=W)



#  ==================================right top corner Image====================================
        img2 = Image.open("C:/Users/user/OneDrive/Desktop/HMS Python Project/Images/roomImg.jpeg")
        img2=img2.resize((350,192))

        self.photoImag2=ImageTk.PhotoImage(img2)
        lblLogo=Label(self.root,image=self.photoImag2,bd=2,relief=RIDGE)
        lblLogo.place(x=762,y=48,width=350,height=192)


    def Fetch_details(self):
        if self.Var_cust_mobile1.get() == "":
            messagebox.showerror("Error", "Please enter Customer mobile number.", parent=self.root)
        else:
            conn = mysql.connector.connect(host="localhost", username="root", password="2002", database="databasetable")
            my_cursor = conn.cursor()
            my_cursor.execute("SELECT * FROM custome_data WHERE Mobile = %s", (self.Var_cust_mobile1.get(),))
            row = my_cursor.fetchone()
            conn.commit()
            conn.close()
            if row is not None:
                self.Retrive_Value_cust_ref_cost = row[0]
                self.Retrive_Value_cust_name_cost = row[1]
                self.Retrive_Value_cust_gender_cost = row[3]
                self.Retrive_Value_cust_contact_cost = row[5]
                self.Retrive_Value_cust_email_cost = row[6]
                self.Retrive_Value_cust_nationality_cost = row[7]
                self.Retrive_Value_cust_address_cost = row[10]
                #  ==================================Fetched Data LabelFrame====================================
                fetch_lbl_Frame= LabelFrame(self.root,text="Fetched Data",bd=4,relief=RIDGE,padx=2,pady=2,font= ("Rockwell",12,"bold"))
                fetch_lbl_Frame.place(x=400,y=40,width=360,height=200) 


#  ==================================Label Values ====================================
# reference
#  ----------------------------------Label ----------------------------
                lbl_cust_ref= Label(fetch_lbl_Frame,text="Customer Ref : ",pady=1,font= ("Rockwell",11,"bold"))
                lbl_cust_ref.grid(row=0,column=0,sticky=W)
#  ----------------------------------Value ----------------------------

                lbl_cust_ref_value = Label(fetch_lbl_Frame, font=("Rockwell", 11, "bold"), width=20,text=self.Retrive_Value_cust_ref_cost)
                lbl_cust_ref_value.grid(row=0, column=1,sticky=W)

# Name  
#  ----------------------------------Label ----------------------------
                lbl_cust_Name = Label(fetch_lbl_Frame,text="Name : ",pady=1,font= ("Rockwell",11,"bold"))
                lbl_cust_Name.grid(row=1,column=0,sticky=W)
#  ----------------------------------Value ----------------------------
                lbl_cust_Name_value = Label(fetch_lbl_Frame, font=("Rockwell", 11, "bold"), width=20,text=self.Retrive_Value_cust_name_cost)
                lbl_cust_Name_value.grid(row=1, column=1,sticky=W)

# Gender        
#  ----------------------------------Label ----------------------------
                lbl_Cust_Gender = Label(fetch_lbl_Frame,text="Gender : ",pady=1,font= ("Rockwell",11,"bold"))
                lbl_Cust_Gender.grid(row=2,column=0,sticky=W)
#  ----------------------------------Value ----------------------------
                lbl_cust_Gender_value = Label(fetch_lbl_Frame, font=("Rockwell", 11, "bold"), width=20,text=self.Retrive_Value_cust_gender_cost)
                lbl_cust_Gender_value.grid(row=2, column=1,sticky=W)
# Email 
#  ----------------------------------Label ----------------------------
                lbl_Cust_Email = Label(fetch_lbl_Frame,text="Email : ",pady=1,font= ("Rockwell",11,"bold"))
                lbl_Cust_Email.grid(row=3,column=0,sticky=W)
#  ----------------------------------Value ----------------------------
                lbl_cust_Email_value = Label(fetch_lbl_Frame, font=("Rockwell", 11, "bold"), width=20,text=self.Retrive_Value_cust_email_cost)
                lbl_cust_Email_value.grid(row=3, column=1,sticky=W)

# Nationality
#  ----------------------------------Label ----------------------------
                lbl_Cust_Nationality = Label(fetch_lbl_Frame,text="Nationality : ",pady=2,font= ("Rockwell",11,"bold"))
                lbl_Cust_Nationality.grid(row=4,column=0,sticky=W)
#  ----------------------------------Value ----------------------------
                lbl_cust_Nationality_value = Label(fetch_lbl_Frame, font=("Rockwell", 11, "bold"), width=20,text=self.Retrive_Value_cust_nationality_cost)
                lbl_cust_Nationality_value.grid(row=4, column=1,sticky=W)

# Address
#  ----------------------------------Label ----------------------------
                lbl_Cust_Address = Label(fetch_lbl_Frame,text="Address : ",pady=1,font= ("Rockwell",11,"bold"))
                lbl_Cust_Address.grid(row=5,column=0,sticky=W)
#  ----------------------------------Value ----------------------------
                lbl_cust_Address_value = Label(fetch_lbl_Frame, font=("Rockwell", 11, "bold"), width=20,text=self.Retrive_Value_cust_address_cost)
                lbl_cust_Address_value.grid(row=5, column=1,sticky=W)

# Contact
#  ----------------------------------Label ----------------------------
                lbl_Cust_Contact = Label(fetch_lbl_Frame,text="Contact : ",pady=1,font= ("Rockwell",11,"bold"))
                lbl_Cust_Contact.grid(row=6,column=0,sticky=W)
#  ----------------------------------Value ----------------------------
                lbl_cust_Contact_value = Label(fetch_lbl_Frame, font=("Rockwell", 11, "bold"), width=20,text=self.Retrive_Value_cust_contact_cost)
                lbl_cust_Contact_value.grid(row=6, column=1,sticky=W)

            else:
                messagebox.showerror("Error", "Data related to mobile number is not found", parent=self.root)

            my_cursor.close()  # Close cursor
















if __name__=="__main__":
    root=Tk()
    obj=Room_book(root)
    root.mainloop()
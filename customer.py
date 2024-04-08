import mysql.connector
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from PIL import Image , ImageTk
import random

class Customer_restrn_win:
    def __init__(self,root):
        self.root=root
        self.root.title("Customer Window")
        self.root.geometry("1130x550+237+224")
        
#  ==================================Variables====================================
        self.var_ref=StringVar()
        x=random.randint(1000,9999)
        self.var_ref.set(str(x))

        self.var_Cust_name = StringVar()
        self.var_Cust_fname = StringVar()
        self.var_Cust_Gender = StringVar()
        self.var_Cust_postcode = StringVar()
        self.var_Cust_mobile = StringVar()
        self.var_Cust_email = StringVar()
        self.var_Cust_nationality = StringVar()
        self.var_Cust_address = StringVar()
        self.var_Cust_idType = StringVar()
        self.var_Cust_idNumber= StringVar()
        self.var_Cust_Address= StringVar()











#  ==================================Title====================================
        lbl_title=Label(self.root,text="Customer Registration Pannel",font= ("Rockwell",20,"bold"),bg="#100E0F",fg="#DBCCA1",bd=3,relief=RIDGE)
        lbl_title.place(x=0,y=0,width=1130,height=40)

#  ==================================Title====================================
        img1 = Image.open("C:/Users/user/OneDrive/Desktop/HMS Python Project/Images/Hotellogo.jpeg")
        img1=img1.resize((60,40))

        self.photoImag1=ImageTk.PhotoImage(img1)
        lblLogo=Label(self.root,image=self.photoImag1,bd=2,relief=RIDGE)
        lblLogo.place(x=0,y=0,width=60,height=40)

#  ==================================LabelFrame====================================
        lbl_Frame= LabelFrame (self.root,text="Customer Details",bd = 2 , relief= RIDGE,padx=2,pady=2,font= ("Rockwell",12,"bold"))
        lbl_Frame.place(x=0,y=40,width=400,height=490)


#  ==================================Label And Entrys ====================================
# Customer Reffernce
#  ----------------------------------Label----------------------------
        lbl_cust_refference= Label(lbl_Frame,text="Customer Refn : ",pady=2,font= ("Rockwell",11,"bold"))
        lbl_cust_refference.grid(row=0,column=0,sticky=W)
#  ----------------------------------entry----------------------------
        entry_cust_refference=ttk.Entry(lbl_Frame,textvariable= self.var_ref,font=("Rockwell",11,"bold"),width=30 ,state="readonly")
        entry_cust_refference.grid(row=0,column=1)

# Customer Name
#  ----------------------------------Label----------------------------
        lbl_cust_Name = Label(lbl_Frame,text="Customer Name : ",pady=2,font= ("Rockwell",11,"bold"))
        lbl_cust_Name.grid(row=1,column=0,sticky=W)
#  ----------------------------------entry----------------------------
        entry_cust_Name=ttk.Entry(lbl_Frame,textvariable= self.var_Cust_name,font=("Rockwell",11,"bold"),width=30)
        entry_cust_Name.grid(row=1,column=1)

# Father Name
#  ----------------------------------Label----------------------------
        lbl_Cust_Fname = Label(lbl_Frame,text="Father Name : ",pady=2,font= ("Rockwell",11,"bold"))
        lbl_Cust_Fname.grid(row=2,column=0,sticky=W)
#  ----------------------------------entry----------------------------
        entry_cust_Fname = ttk.Entry(lbl_Frame,textvariable= self.var_Cust_fname,font=("Rockwell",11,"bold"),width=30)
        entry_cust_Fname.grid(row=2,column=1)


# Gender
#  ----------------------------------Label----------------------------
        lbl_Cust_gender = Label(lbl_Frame,text="Gender : ",pady=2,font= ("Rockwell",11,"bold"))
        lbl_Cust_gender.grid(row=3,column=0,sticky=W)
#  ----------------------------------Combobox----------------------------
        combo_Cust_gender=ttk.Combobox(lbl_Frame,textvariable= self.var_Cust_Gender,font=("Rockwell",11,"bold"),width=28,state="readonly")
        combo_Cust_gender["value"]=("Male","Female","Other")
        combo_Cust_gender.current(0)
        combo_Cust_gender.grid(row=3,column=1)


# Post Code
#  ----------------------------------Label----------------------------
        lbl_Cust_postcode = Label(lbl_Frame,text="Post Code : ",pady=2,font= ("Rockwell",11,"bold"))
        lbl_Cust_postcode.grid(row=4,column=0,sticky=W)
#  ----------------------------------entry----------------------------
        entry_cust_postcode = ttk.Entry(lbl_Frame,textvariable= self.var_Cust_postcode,font=("Rockwell",11,"bold"),width=30)
        entry_cust_postcode.grid(row=4,column=1)

# Mobile Number
#  ----------------------------------Label----------------------------
        lbl_Cust_MobileNo = Label(lbl_Frame,text="Mobile Number : ",pady=2,font= ("Rockwell",11,"bold"))
        lbl_Cust_MobileNo.grid(row=5,column=0,sticky=W)
#  ----------------------------------entry----------------------------
        entry_cust_MobileNo = ttk.Entry(lbl_Frame,textvariable= self.var_Cust_mobile,font=("Rockwell",11,"bold"),width=30)
        entry_cust_MobileNo.grid(row=5,column=1)

# Email Address
#  ----------------------------------Label----------------------------
        lbl_Cust_Email_address = Label(lbl_Frame,text="Email Address : ",pady=2,font= ("Rockwell",11,"bold"))
        lbl_Cust_Email_address.grid(row=6,column=0,sticky=W)
#  ----------------------------------entry----------------------------
        entry_cust_Email_address = ttk.Entry(lbl_Frame,textvariable= self.var_Cust_email,font=("Rockwell",11,"bold"),width=30)
        entry_cust_Email_address.grid(row=6,column=1)

# Nationality
#  ----------------------------------Label----------------------------
        lbl_Cust_Nationality = Label(lbl_Frame,text="Nationality : ",pady=2,font= ("Rockwell",11,"bold"))
        lbl_Cust_Nationality.grid(row=7,column=0,sticky=W)
#  ----------------------------------Combobox----------------------------
        combo_cust_Nationality=ttk.Combobox(lbl_Frame,textvariable= self.var_Cust_nationality,font=("Rockwell",11,"bold"),width=28,state="readonly")
        combo_cust_Nationality["value"] = nationalities = (
    "American",
    "British",
    "Chinese",
    "Indian",
    "Japanese",
    "Russian",
    "German",
    "French",
    "Italian",
    "Brazilian",
    "Canadian",
    "Australian",
    "Mexican",
    "Spanish",
    "South Korean",
    "Nigerian",
    "Egyptian",
    "Indonesian",
    "Turkish",
    "Argentinean",
    "Other"
)
        combo_cust_Nationality.current(0)
        combo_cust_Nationality.grid(row=7,column=1)



# Id Proof Type
#  ----------------------------------Label----------------------------
        lbl_Cust_id_type = Label(lbl_Frame,text="Id Proof Type : ",pady=2,font= ("Rockwell",11,"bold"))
        lbl_Cust_id_type.grid(row=8,column=0,sticky=W)
#  ----------------------------------Combobox----------------------------
        combo_cust_id_type=ttk.Combobox(lbl_Frame,textvariable= self.var_Cust_idType,font=("Rockwell",11,"bold"),width=28,state="readonly")
        combo_cust_id_type["value"] = ("License","Addhar_Card","Pan_Card","PassPort")
        combo_cust_id_type.current(0)
        combo_cust_id_type.grid(row=8,column=1)

# ID Number
#  ----------------------------------Label----------------------------
        lbl_Cust_ID_Number = Label(lbl_Frame,text="ID Number : ",pady=2,font= ("Rockwell",11,"bold"))
        lbl_Cust_ID_Number.grid(row=9,column=0,sticky=W)
#  ----------------------------------entry----------------------------
        entry_cust_ID_Number = ttk.Entry(lbl_Frame,textvariable= self.var_Cust_idNumber,font=("Rockwell",11,"bold"),width=30)
        entry_cust_ID_Number.grid(row=9,column=1)

# Address
#  ----------------------------------Label----------------------------
        lbl_Cust_Address = Label(lbl_Frame,text="Address : ",pady=2,font= ("Rockwell",11,"bold"))
        lbl_Cust_Address.grid(row=10,column=0,sticky=W)
#  ----------------------------------entry----------------------------
        entry_cust_Address = ttk.Entry(lbl_Frame,textvariable= self.var_Cust_Address,font=("Rockwell",11,"bold"),width=30)
        entry_cust_Address.grid(row=10,column=1)


#  ================================== Button ====================================

#  ----------------------------------BTn Frame----------------------------

        btn_frame=Frame(lbl_Frame,bd=4,relief=RIDGE)
        btn_frame.place(x=0,y=295,width=390,height=100)

#  ----------------------------------BTn Add----------------------------
        btn_add=Button(btn_frame,text="Add",font=("Rockwell",12,"bold"),width=10 ,bg="#100E0F",fg="#DBCCA1",bd=3,relief=RIDGE, command= self.add_data)
        btn_add.grid(row=0,column=0,padx= 5 , pady=5)
  

#  ----------------------------------BTn Update----------------------------
        btn_Update=Button(btn_frame,text="Update",font=("Rockwell",12,"bold"),width=10 ,bg="#100E0F",fg="#DBCCA1",bd=3,relief=RIDGE,command=self.Update_data)
        btn_Update.grid(row=0,column=1,padx= 5 , pady=5)
  

#  ----------------------------------BTn Delete----------------------------
        btn_Delete=Button(btn_frame,text="Delete",font=("Rockwell",12,"bold"),width=10 ,bg="#100E0F",fg="#DBCCA1",bd=3,relief=RIDGE,command=self.Delete_Function)
        btn_Delete.grid(row=0,column=2,padx= 5 , pady=5)

#  ----------------------------------BTn Clear----------------------------
        btn_Clear=Button(btn_frame,text="Clear All The Feilds",font=("Rockwell",12,"bold"),width=30 ,bg="#100E0F",fg="#DBCCA1",bd=3,relief=RIDGE,command=self.clear_all_feilds)
        # btn_Clear.place(x=30,y=46)
        btn_Clear.grid(row=1,column=0,columnspan = 3)
  

#  ================================== Table Frame for the Data view ====================================

        table_frame= LabelFrame(self.root,text="All Customers Data",bd=4,relief=RIDGE,padx=2,pady=2,font= ("Rockwell",12,"bold"))
        table_frame.place(x=400,y=40,width=720,height=490)

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
        btn_search=Button(table_frame,text="Search",font=("Rockwell",11,"bold"),width=10,command=self.Search_Data ,bg="#100E0F",fg="#DBCCA1",bd=3,relief=RIDGE)
        btn_search.grid(row=0,column=3,padx= 5 , pady=5)

#  ----------------------------------BTn Show All----------------------------
        btn_showall=Button(table_frame,text="Show All",font=("Rockwell",11,"bold"),width=10 ,bg="#100E0F",fg="#DBCCA1",bd=3,relief=RIDGE , command= self.fetch_Data)
        btn_showall.grid(row=0,column=4,pady=5,padx=5)
  
#  ================================== Table Data view ====================================
        Details_tbl_frame=Frame(table_frame,bd=3,relief=RIDGE)
        Details_tbl_frame.place(x=0,y=40,width=700,height=370)

#  ----------------------------------Scrool bar----------------------------
        scroll_x=ttk.Scrollbar(Details_tbl_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(Details_tbl_frame,orient=VERTICAL)

#  ---------------------------------- Dummy head Column in Grid view ----------------------------
        self.customer_Details_table=ttk.Treeview(Details_tbl_frame,columns=("ref_no","Name","fname","Gender","Postcode","Mobile_no","Email_address","Nationality","Id_type","id_Number","Address"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

#  ---------------------------------- Set scrool bars to its positions ----------------------------
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

#  ---------------------------------- Set scrool bars to its positions ----------------------------
        scroll_x.config(command=self.customer_Details_table.xview)
        scroll_y.config(command=self.customer_Details_table.yview)

#  ---------------------------------- Dummy column name set  ----------------------------

        self.customer_Details_table.heading("ref_no",text="Reffer No")
        self.customer_Details_table.heading("Name",text="Customer Name")
        self.customer_Details_table.heading("fname",text="Father Name")
        self.customer_Details_table.heading("Gender",text="Gender")
        self.customer_Details_table.heading("Postcode",text="Postcode")
        self.customer_Details_table.heading("Mobile_no",text="Mobile No")
        self.customer_Details_table.heading("Email_address",text="Email Address")
        self.customer_Details_table.heading("Nationality",text="Nationality")
        self.customer_Details_table.heading("Id_type",text="Identity Type")
        self.customer_Details_table.heading("id_Number",text="Identity Number")
        self.customer_Details_table.heading("Address",text="Address")

        self.customer_Details_table["show"] = "headings"

#  ---------------------------------- Dummy Width set  ----------------------------

        self.customer_Details_table.column("ref_no",width=100)
        self.customer_Details_table.column("Name",width=100)
        self.customer_Details_table.column("fname",width=100)
        self.customer_Details_table.column("Gender",width=100)
        self.customer_Details_table.column("Postcode",width=100)
        self.customer_Details_table.column("Mobile_no",width=100)
        self.customer_Details_table.column("Email_address",width=100)
        self.customer_Details_table.column("Nationality",width=100)
        self.customer_Details_table.column("Id_type",width=100)
        self.customer_Details_table.column("id_Number",width=100)
        self.customer_Details_table.column("Address",width=100)

        self.customer_Details_table.pack(fill=BOTH, expand=1)

        self.customer_Details_table.bind("<ButtonRelease-1>", self.get_cursor)

        self.fetch_Data()
#  ================================== Function to add data to database and  check if data feilds are empty before adding data  ====================================

    def add_data(self):
        if (self.var_Cust_mobile.get() == "" or 
                self.var_Cust_Address.get() == "" or 
                self.var_Cust_email.get() == "" or 
                self.var_Cust_fname.get() == "" or 
                self.var_Cust_name.get() == "" or 
                self.var_Cust_Gender.get() == "" or 
                self.var_ref.get() == "" or 
                self.var_Cust_idNumber.get() == "" or 
                self.var_Cust_idType.get() == "" or 
                self.var_Cust_postcode.get() == "" or 
                self.var_Cust_nationality.get() == ""):
                messagebox.showerror("Error","Please fill All The Feilds",parent=self.root)
        else:
                try:
                        conn = mysql.connector.connect(host="localhost", username="root", password="2002", database="databasetable")
                        my_cursor = conn.cursor()
                        my_cursor.execute("INSERT INTO custome_data VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", (
                self.var_ref.get(), self.var_Cust_name.get(), self.var_Cust_fname.get(), self.var_Cust_Gender.get(), self.var_Cust_postcode.get(),
                self.var_Cust_mobile.get(), self.var_Cust_email.get(), self.var_Cust_nationality.get(), self.var_Cust_idType.get(), self.var_Cust_idNumber.get(),
                self.var_Cust_Address.get()))
                        conn.commit()
                        messagebox.showinfo("Success", "Customer data has been successfully added", parent=self.root)
                        self.fetch_Data()
                        self.clear_all_feilds()
                except mysql.connector.Error as e:
                        messagebox.showerror("Error", f"Error: {e.msg}", parent=self.root)
                finally:
                        if 'conn' in locals() and conn.is_connected():
                            my_cursor.close()
                            conn.close()


#  ================================== Retrive the data from data base and show in tree view(data grid type)  ====================================

    def fetch_Data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="2002",database="databasetable")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from custome_data")
        row=my_cursor.fetchall()
        if len(row)!=0 :
                self.customer_Details_table.delete(*self.customer_Details_table.get_children())
                for i in row:
                        self.customer_Details_table.insert("",END,values=i)
                conn.commit()
        conn.close()


    def get_cursor(self,event=""):
        cursor_row=self.customer_Details_table.focus()
        content=self.customer_Details_table.item(cursor_row)
        row=content["values"]

        self.var_ref.set(row[0])    
        self.var_Cust_name.set(row[1])    
        self.var_Cust_fname.set(row[2])    
        self.var_Cust_Gender.set(row[3])    
        self.var_Cust_postcode.set(row[4])    
        self.var_Cust_mobile.set(row[5])    
        self.var_Cust_email.set(row[6])    
        self.var_Cust_nationality.set(row[7])    
        self.var_Cust_idType.set(row[8])    
        self.var_Cust_idNumber.set(row[9])    
        self.var_Cust_Address.set(row[10])    


#  ================================== Update BTN Funtion ====================================

    def Update_data(self):
        if (self.var_Cust_mobile.get()=="" or
            self.var_Cust_name.get()=="" or
            self.var_Cust_fname.get()=="" or
            self.var_Cust_mobile.get()=="" or
            self.var_Cust_email.get()=="" or
            self.var_Cust_nationality.get()=="" or
            self.var_Cust_postcode.get()=="" or
            self.var_Cust_idNumber.get()=="" or
            self.var_Cust_Gender.get()=="" or
            self.var_ref.get()=="" or
            self.var_Cust_idType.get()=="" ):
                messagebox.showerror("Error","Please enter all the required feilds",parent=self.root)
        else :
                try:
                        conn=mysql.connector.connect(host="localhost",username="root",password="2002",database="databasetable")
                        my_cursor=conn.cursor()
                        my_cursor.execute("update custome_data set Name = %s,Father_Name=%s,Gender=%s,Postcode=%s,Mobile=%s,Email=%s,Nationality=%s,IdProofType=%s,IdNumber=%s,Address=%s where Ref=%s",(
                            
                 self.var_Cust_name.get(), self.var_Cust_fname.get(), self.var_Cust_Gender.get(), self.var_Cust_postcode.get(),
                self.var_Cust_mobile.get(), self.var_Cust_email.get(), self.var_Cust_nationality.get(), self.var_Cust_idType.get(), self.var_Cust_idNumber.get(),
                self.var_Cust_Address.get(),self.var_ref.get()
                        ))
                        conn.commit()
                        self.fetch_Data()
                        self.clear_all_feilds()
                        conn.close()
                        messagebox.showinfo("Success",f"Customer {self.var_Cust_name.get()} data Has Been Successfully Updated",parent=self.root)


                except Exception as es :
                        messagebox.showerror("Error",f"Customer's data Has Not  Been Updated {es.msg}",parent=self.root)
                finally :
                        if 'conn' in locals() and conn.is_connected():
                                my_cursor.close()
                                conn.close()


#  ================================== Delete BTN Funtion ====================================

    def Delete_Function(self):
    # Ask for confirmation
        if not messagebox.askyesno("Hotel Management System", "Do You Really want to delete this customer's data?", parent=self.root):
            return

        try:
            # Connect to the database
            conn = mysql.connector.connect(host="localhost", username="root", password="2002", database="databasetable")
            my_cursor = conn.cursor()

            # Execute the delete query
            query = "DELETE FROM custome_data WHERE Ref = %s"
            value = (self.var_ref.get(),)  # Ensure value is a tuple
            my_cursor.execute(query, value)

            # Commit the transaction and close the connection
            conn.commit()
            self.fetch_Data()  # Refresh the data after deletion
            self.clear_all_feilds()
        except Exception as e:
            # Handle any errors that occur during the database operation
            messagebox.showerror("Error", f"Error deleting customer data: {e}",parent=self.root)
        finally:
            # Close the connection in a finally block to ensure it always happens
            if conn.is_connected():
                my_cursor.close()
                conn.close()


#  ================================== clear feilds BTN Funtion ====================================

    def clear_all_feilds(self):
        x=random.randint(1000,9999)
        self.var_ref.set(str(x))
        self.var_Cust_name.set("")    
        self.var_Cust_fname.set("")    
        # combo_Cust_gender.current(0)       
        self.var_Cust_postcode.set("")    
        self.var_Cust_mobile.set("")    
        self.var_Cust_email.set("")    
        # combo_cust_Nationality.current(0)    
        # combo_cust_id_type.current(0)       
        self.var_Cust_idNumber.set("")    
        self.var_Cust_Address.set("")  


#  ================================== Search BTN Funtion ====================================
    def Search_Data(self):
        conn = mysql.connector.connect(host="localhost", username="root", password="2002", database="databasetable")
        my_cursor = conn.cursor()
    
        # Prepare the SQL query with placeholders and execute it with parameterized values
        query = "SELECT * FROM custome_data WHERE {} LIKE %s".format(self.var_Search_Type.get())
        search_value = '%' + str(self.var_Search_value.get()) + '%'  # Prepare the search value with wildcards
        my_cursor.execute(query, (search_value,))
    
        rows = my_cursor.fetchall()
        if len(rows) != 0:
            self.customer_Details_table.delete(*self.customer_Details_table.get_children())
            for i in rows:
                self.customer_Details_table.insert("", END, values=i)
            conn.commit()
        conn.close()









#  ================================== Main Funtion ====================================

if __name__=="__main__" :
    root=Tk()
    obj=Customer_restrn_win(root)
    root.mainloop()
# from cgitb import text
# from logging import root
from tkinter import *
from tkinter import ttk
# import random
# import datetime
from tkinter import messagebox
# from tkinter import font
# from webbrowser import get
import mysql.connector
# from mysqlx import Row
# from pip import main

class Hospital:
    def iPrescriptionData(self):
        print(self.NameOfTablets.get())
    def __init__(self,root):
        self.root=root
        self.root.title("hospital management")
        self.root.geometry("1540x800+0+0")

        self.NameOfTablets=StringVar()
        self.Ref=StringVar()
        self.Dose=StringVar() 
        self.Nooftablets=StringVar()
        self.Lot=StringVar()
        self.IssueDate=StringVar()
        self.ExpDate=StringVar()
        self.DailyDose=StringVar()
        self.Storage=StringVar()
        self.NBSNumber=StringVar()
        self.Pname=StringVar()
        self.Dob=StringVar()
        self.Address=StringVar()
        self.SideEffect=StringVar()
        self.FurtherInfo=StringVar()
        self.BloodPressure=StringVar()
        self.Medication=StringVar()
        self.PatientID=StringVar()
        colour_bg="green"
        colour_fg="black"

        lbltitle=Label(self.root,bd=20,relief=RIDGE,text="HOSPITAL MANAGEMENT SYSTEM",fg="red",bg="white",font=("times new roman",50,"bold"))
        lbltitle.pack(side=TOP,fill=X) 

        #===========dataframe=======
        Dataframe=Frame(self.root,bd=20,relief=RIDGE)
        Dataframe.place(x=0,y=130,width=1530,height=400)

        DataframeLeft=LabelFrame(Dataframe,bd=10,relief=RIDGE,padx=10,font=("times new roman ",12,"bold"),text="Patient Infomation")
        DataframeLeft.place(x=0,y=5,width=980,height=350)

        DataframeRight=LabelFrame(Dataframe,bd=10,relief=RIDGE,padx=10,font=("times new roman ",12,"bold"),text="Prescription")
        DataframeRight.place(x=990,y=5,width=460,height=350)

        #======buttonframe======
        ButtonFrame=Frame(self.root,bd=20,relief=RIDGE)
        ButtonFrame.place(x=0,y=530,width=1530,height=70)
        
        #======detailsframe======
        DetailsFrame=Frame(self.root,bd=20,relief=RIDGE)
        DetailsFrame.place(x=0,y=600,width=1530,height=190)

        #=====Dataframeleft===========
        lblNameTablet=Label(DataframeLeft,text="Name Of Tablet",font=("times new roman",14,"bold"),padx=2,pady=6)
        lblNameTablet.grid(row=0,column=0)

        comNameTablet=ttk.Combobox(DataframeLeft,textvariable=self.NameOfTablets,font=("times new roman",12,"bold"),width=32)
        comNameTablet["values"]=("NICE","CORONA VACCINE","ACETAMINOPHEN","ADDERALL","AMLODIPINE","ATIVAN")
        comNameTablet.grid(row=0,column=1)

        lblref=Label(DataframeLeft,text="Refrence No.",font=("arial",13,"bold"),padx=2,pady=4)
        lblref.grid(row=1,column=0,sticky=W)
        txtref=Entry(DataframeLeft,textvariable=self.Ref,font=("arial",13,"bold"),width=30)
        txtref.grid(row=1,column=1)
          

        lbldos=Label(DataframeLeft,text="Dose",font=("arial",13,"bold"),padx=2,pady=6)
        lbldos.grid(row=2,column=0,sticky=W)
        txtdos=Entry(DataframeLeft,textvariable=self.Dose,font=("arial",13,"bold"),width=30)
        txtdos.grid(row=2,column=1)
        
        lblNoOfTablets=Label(DataframeLeft,text="No Of Tablets",font=("arial",13,"bold"),padx=2,pady=6)
        lblNoOfTablets.grid(row=3,column=0,sticky=W)
        txtNoOfTablets=Entry(DataframeLeft,textvariable=self.Nooftablets,font=("arial",13,"bold"),width=30)
        txtNoOfTablets.grid(row=3,column=1)
        
        lblLot=Label(DataframeLeft,text="Lot",font=("arial",13,"bold"),padx=2,pady=6)
        lblLot.grid(row=4,column=0,sticky=W)
        txtLot=Entry(DataframeLeft,textvariable=self.Lot,font=("arial",13,"bold"),width=30)
        txtLot.grid(row=4,column=1)
        
        lblIssueDate=Label(DataframeLeft,text="Issue Date",font=("arial",13,"bold"),padx=2,pady=6)
        lblIssueDate.grid(row=5,column=0,sticky=W)
        txtIssueDate=Entry(DataframeLeft,textvariable=self.IssueDate,font=("arial",13,"bold"),width=30)
        txtIssueDate.grid(row=5,column=1)
        
        lblExpDate=Label(DataframeLeft,text="Exp Date",font=("arial",13,"bold"),padx=2,pady=6)
        lblExpDate.grid(row=6,column=0,sticky=W)
        txtExpDate=Entry(DataframeLeft,textvariable=self.ExpDate,font=("arial",13,"bold"),width=30)
        txtExpDate.grid(row=6,column=1)
        
        lblDailyDose=Label(DataframeLeft,text="Daily Dose",font=("arial",13,"bold"),padx=2,pady=6)
        lblDailyDose.grid(row=7,column=0,sticky=W)
        txtDailyDose=Entry(DataframeLeft,textvariable=self.DailyDose,font=("arial",13,"bold"),width=30)
        txtDailyDose.grid(row=7,column=1)

        lblSideEffect=Label(DataframeLeft,text="Side Effect",font=("arial",13,"bold"),padx=2,pady=6)
        lblSideEffect.grid(row=8,column=0,sticky=W)
        txtSideEffect=Entry(DataframeLeft,textvariable=self.SideEffect,font=("arial",13,"bold"),width=30)
        txtSideEffect.grid(row=8,column=1)
          

        lblFurtherInformation=Label(DataframeLeft,text="Further Information",font=("arial",13,"bold"),padx=2,pady=4)
        lblFurtherInformation.grid(row=0,column=2,sticky=W)
        txtFurtherInformation=Entry(DataframeLeft,textvariable=self.FurtherInfo,font=("arial",13,"bold"),width=30)
        txtFurtherInformation.grid(row=0,column=3)
        
        lblStorageAdvice=Label(DataframeLeft,text="Storage Advice",font=("arial",13,"bold"),padx=2,pady=6)
        lblStorageAdvice.grid(row=2,column=2,sticky=W)
        txtStorageAdvice=Entry(DataframeLeft,textvariable=self.Storage,font=("arial",13,"bold"),width=30)
        txtStorageAdvice.grid(row=2,column=3)
        
        lblMedication=Label(DataframeLeft,text="Medication",font=("arial",13,"bold"),padx=2,pady=6)
        lblMedication.grid(row=3,column=2,sticky=W)
        txtMedication=Entry(DataframeLeft,textvariable=self.Medication,font=("arial",13,"bold"),width=30)
        txtMedication.grid(row=3,column=3)
        
        lblPatientId=Label(DataframeLeft,text="Patient Id",font=("arial",13,"bold"),padx=2,pady=6)
        lblPatientId.grid(row=4,column=2,sticky=W)
        txtPatientId=Entry(DataframeLeft,textvariable=self.PatientID,font=("arial",13,"bold"),width=30)
        txtPatientId.grid(row=4,column=3)
        
        lblNHSNumber=Label(DataframeLeft,text="NHS Number",font=("arial",13,"bold"),padx=2,pady=4)
        lblNHSNumber.grid(row=5,column=2,sticky=W)
        txtNHSNumber=Entry(DataframeLeft,textvariable=self.NBSNumber,font=("arial",13,"bold"),width=30)
        txtNHSNumber.grid(row=5,column=3)
        
        lblPatientName=Label(DataframeLeft,text="Patient Name",font=("arial",13,"bold"),padx=2,pady=6)
        lblPatientName.grid(row=6,column=2,sticky=W)
        txtPatientName=Entry(DataframeLeft,textvariable=self.Pname,font=("arial",13,"bold"),width=30)
        txtPatientName.grid(row=6,column=3)
        
        lblBloodPressure=Label(DataframeLeft,text="Blood Pressure",font=("arial",13,"bold"),padx=2)
        lblBloodPressure.grid(row=1,column=2,sticky=W)
        txtBloodPressure=Entry(DataframeLeft,textvariable=self.BloodPressure,font=("arial",13,"bold"),width=30)
        txtBloodPressure.grid(row=1,column=3)
        
        lblDateOfBirth=Label(DataframeLeft,text="DateOfBirth",font=("arial",13,"bold"),padx=2,pady=6)
        lblDateOfBirth.grid(row=7,column=2,sticky=W)
        txtDateOfBirth=Entry(DataframeLeft,textvariable=self.Dob,font=("arial",13,"bold"),width=30)
        txtDateOfBirth.grid(row=7,column=3)
        
        lblPatientAddress=Label(DataframeLeft,text="Patient Address",font=("arial",13,"bold"),padx=2,pady=6)
        lblPatientAddress.grid(row=8,column=2,sticky=W)
        txtPatientAddress=Entry(DataframeLeft,textvariable=self.Address,font=("arial",13,"bold"),width=30)
        txtPatientAddress.grid(row=8,column=3)
#==============================text data=======================
        self.txtprescription=Text(DataframeRight,font=("arial",12,"bold"),width=45,height=16,padx=2,pady=6)
        self.txtprescription.grid(row=0,column=0)

        # =======button=========
        btnPrescription=Button(ButtonFrame,text="Prescription",command=self.iPrescription,bg=colour_bg ,fg=colour_fg,font=("arial",12,"bold"),width=23,padx=2,pady=6)
        btnPrescription.grid(row=0,column=0)

        btnPrescriptiondata=Button(ButtonFrame,text="Prescription Data",command=self.iPrescriptiondata,bg=colour_bg ,fg=colour_fg,font=("arial",12,"bold"),width=23,padx=2,pady=6)
        btnPrescriptiondata.grid(row=0,column=1)

        btnUpdate=Button(ButtonFrame,text="Update",command=self.update_data,bg=colour_bg ,fg=colour_fg,font=("arial",12,"bold"),width=23,padx=2,pady=6)
        btnUpdate.grid(row=0,column=2)

        btnDelete=Button(ButtonFrame,command=self.idelete,text="Delete",bg=colour_bg ,fg=colour_fg,font=("arial",12,"bold"),width=23,padx=2,pady=6)
        btnDelete.grid(row=0,column=3)

        btnClear=Button(ButtonFrame,command=self.iclear,text="Clear",bg=colour_bg ,fg=colour_fg,font=("arial",12,"bold"),width=23,padx=2,pady=6)
        btnClear.grid(row=0,column=4)

        btnExit=Button(ButtonFrame,command=self.iexit,text="Exit",bg=colour_bg ,fg=colour_fg,font=("arial",12,"bold"),width=23,padx=2,pady=6)
        btnExit.grid(row=0,column=5)

        # ======scrollbar======
        scroll_x=ttk.Scrollbar(DetailsFrame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(DetailsFrame,orient=VERTICAL)
        self.Hospital_table=ttk.Treeview(DetailsFrame,column=("nameofTablets","ref","dose","nooftablets","lot",
                                             "issuedate","expdate","dailydose","storage","nbsnumber","pname","dob","address"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x=ttk.Scrollbar(command=self.Hospital_table.xview)
        scroll_y=ttk.Scrollbar(command=self.Hospital_table.yview)

        self.Hospital_table.heading("nameofTablets",text="Name Of Tablets")
        self.Hospital_table.heading("ref",text="Refrence No.")
        self.Hospital_table.heading("dose",text="Dose")
        self.Hospital_table.heading("nooftablets",text="No. Of Tablets")
        self.Hospital_table.heading("lot",text="Lot")
        self.Hospital_table.heading("issuedate",text="Issue Date")
        self.Hospital_table.heading("expdate",text="Expiry Date")
        self.Hospital_table.heading("dailydose",text="Daily Dose")
        self.Hospital_table.heading("storage",text="Storage")
        self.Hospital_table.heading("nbsnumber",text="NBS Number")
        self.Hospital_table.heading("pname",text="Patient Name")
        self.Hospital_table.heading("dob",text="Date Of Birth")
        self.Hospital_table.heading("address",text="Address")

        self.Hospital_table["show"]="headings"
        # self.Hospital_table.pack(fill=BOTH,expand=1)

        
        self.Hospital_table.column("nameofTablets",width=100)
        self.Hospital_table.column("ref",width=100)
        self.Hospital_table.column("dose",width=100)
        self.Hospital_table.column("nooftablets",width=100)
        self.Hospital_table.column("lot",width=100)
        self.Hospital_table.column("issuedate",width=100)
        self.Hospital_table.column("expdate",width=100)
        self.Hospital_table.column("dailydose",width=100)
        self.Hospital_table.column("storage",width=100)
        self.Hospital_table.column("nbsnumber",width=100)
        self.Hospital_table.column("pname",width=100)
        self.Hospital_table.column("dob",width=100)
        self.Hospital_table.column("address",width=100)
        
        self.Hospital_table.pack(fill=BOTH,expand=1)
        self.Hospital_table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fatch_data()
        #============Functionality declaration=======
        
    def iPrescriptiondata(self):
        if self.NameOfTablets.get()=="" or self.Ref.get()=="":
            messagebox.showerror("error","ERROR!!!!")
        else:
            conn=mysql.connector.connect(host="localhost",user="root",password="123123papa123123",database="gauravdbms")
            cur=conn.cursor()
            cur.execute("insert into hospital values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(self.NameOfTablets.get(),self.Ref.get(),
                                                                        self.Lot.get(),self.IssueDate.get(),
                                                                        self.ExpDate.get(),self.DailyDose.get(),self.Storage.get(),
                                                                        self.NBSNumber.get(),self.Pname.get(),self.Dob.get(),self.Address.get(),
                                                                        self.Dob.get(),self.Nooftablets.get()))
            conn.commit()
            self.fatch_data()
            conn.close()
            messagebox.showinfo("done","successful")
    def update_data(self):
        conn=mysql.connector.connect(host="localhost",user="root",password="123123papa123123",database="gauravdbms")
        cur=conn.cursor()
        cur.execute("update hospital set NameOfTablets=%s,Dose=%s,Nooftablets=%s,Lot=%s,IssueDate=%s,ExpDate=%s,DailyDose=%s,Storage=%s,NBSNumber=%s,Pname=%s,Dob=%s,Address=%s where Ref=%s",(self.NameOfTablets.get(),
        
        self.Dose.get(), 
        self.Nooftablets.get(),
        self.Lot.get(),
        self.IssueDate.get(),
        self.ExpDate.get(),
        self.DailyDose.get(),
        self.Storage.get(),
        self.NBSNumber.get(),
        self.Pname.get(),
        self.Dob.get(),
        self.Address.get(),
        self.Ref.get()
        ))
        
        conn.commit()
        self.fatch_data()
        conn.close()
        messagebox.showinfo("update","BRAVOOO..")
    
    def fatch_data(self):
        conn=mysql.connector.connect(host="localhost",user="root",password="123123papa123123",database="gauravdbms")
        cur=conn.cursor()
        cur.execute("select * from hospital")
        rows=cur.fetchall()
        if len(rows)!=0:
            self.Hospital_table.delete(*self.Hospital_table.get_children())
        for i in rows:
            self.Hospital_table.insert("",END,values=i)
            conn.commit()
        conn.close()
    
    def get_cursor(self,event=""):
        cursor_row=self.Hospital_table.focus()
        content=self.Hospital_table.item(cursor_row)
        row=content["values"]
        
        self.NameOfTablets.set(row[0])
        self.Ref.set(row[1])
        self.Dose.set(row[2]) 
        self.Nooftablets.set(row[3])
        self.Lot.set(row[4])
        self.IssueDate.set(row[5])
        self.ExpDate.set(row[6])
        self.DailyDose.set(row[7])
        self.Storage.set(row[8])
        self.NBSNumber.set(row[9])
        self.Pname.set(row[10])
        self.Dob.set(row[11])
        self.Address.set(row[12])
   
    def iPrescription(self):
        self.txtprescription.insert(END,"Name Of Tablets:\t\t\t"+self.NameOfTablets.get()+"\n")  
        self.txtprescription.insert(END,"Ref Num.:\t\t\t"+self.Ref.get()+"\n")  
        self.txtprescription.insert(END,"Dose:\t\t\t"+self.Dose.get()+"\n")  
        self.txtprescription.insert(END,"Number of Tablets:\t\t\t"+self.Nooftablets.get()+"\n")  
        self.txtprescription.insert(END,"Patient Name:\t\t\t"+self.Pname.get()+"\n")  
        self.txtprescription.insert(END,"Issue date:\t\t\t"+self.IssueDate.get()+"\n")  
        self.txtprescription.insert(END,"Patient ID:\t\t\t"+self.PatientID.get()+"\n")    
        self.txtprescription.insert(END,"Date Of Birth:\t\t\t"+self.Dob.get()+"\n")  
        self.txtprescription.insert(END,"Lot:\t\t\t"+self.Lot.get()+"\n")  
        self.txtprescription.insert(END,"Medication:\t\t\t"+self.Medication.get()+"\n")  
        self.txtprescription.insert(END,"Daily Dose:\t\t\t"+self.DailyDose.get()+"\n")
        self.txtprescription.insert(END,"Storage:\t\t\t"+self.Storage.get()+"\n")
        self.txtprescription.insert(END,"Side Effect:\t\t\t"+self.SideEffect.get()+"\n")  
        self.txtprescription.insert(END,"Expiry Date:\t\t\t"+self.ExpDate.get()+"\n")  
        self.txtprescription.insert(END,"NHS Number:\t\t\t"+self.NBSNumber.get()+"\n")
        self.txtprescription.insert(END,"Patient Address:\t\t\t"+self.Address.get()+"\n")  

    def idelete(self):
        conn=mysql.connector.connect(host="localhost",user="root",password="123123papa123123",database="gauravdbms")
        cur=conn.cursor()
        query="delete from hospital where Ref=%s "
        value=(self.Ref.get(),)
        cur.execute(query,value)
        conn.commit()
        self.fatch_data()
        messagebox.showinfo("Delete","Oops Deleted")

    def iclear(self):
        self.NameOfTablets.set("")
        self.Ref.set("")
        self.Dose.set("") 
        self.Nooftablets.set("")
        self.Lot.set("")
        self.IssueDate.set("")
        self.ExpDate.set("")
        self.DailyDose.set("")
        self.Storage.set("")
        self.NBSNumber.set("")
        self.Pname.set("")
        self.Dob.set("")
        self.Address.set("")
        self.BloodPressure.set("")
        self.Medication.set("")
        self.FurtherInfo.set("")
        self.PatientID.set("")
        self.SideEffect.set("")
        self.txtprescription.delete("1.0",END)

    def iexit(self):
        iexit=messagebox.askyesno("Hospital Management System","BYEEEE")
        if iexit>0:
            root.destroy()
            return




root=Tk()
ob=Hospital(root)
root.mainloop()
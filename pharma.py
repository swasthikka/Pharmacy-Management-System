from tkinter import*
from PIL import Image,ImageTk
from tkinter import ttk
import mysql.connector
from tkinter import messagebox

# ==============addMed variable ===========
        self.addmed_var=StringVar()
        self.refMed_var=StringVar()


class PharmacyManagementSystem:
    def __init__(self,root):
        self.root=root
        self.root.title("Pharmacy Management System")
        self.root.geometry("1550x800+0+0")

        lbltitle=Label(self.root,text="PHARMACY MANAGEMENT SYSTEM",bd=7, relief=RIDGE
                      ,bg="white",fg="darkblue",font=("times new roman",40,"bold"),padx=3)
        
        lbltitle.pack(side=TOP,fill=X)
        file_path = r"C:\Pharmacy-Management-System\Pharmacy-Management-System-master\tabletlogo.png"
        file_path2=r"C:\Pharmacy-Management-System\Pharmacy-Management-System-master\img2.jpg"
        file_path3=r"C:\Pharmacy-Management-System\Pharmacy-Management-System-master\img3.jpg"
        file_path4=r"C:\Pharmacy-Management-System\Pharmacy-Management-System-master\img4.jpg"

        

        img1 = Image.open(file_path)
        img1 = img1.resize((60,60),Image.Resampling.LANCZOS)
        self.photoimg1=ImageTk.PhotoImage(img1)
        b1=Button(self.root,image=self.photoimg1,borderwidth=0)
        b1.place(x=30,y=7)
        #================Data Frame========================
        DataFrame=Frame(self.root,bd=7,relief=RIDGE,padx=10)
        DataFrame.place(x=0,y=120,width=1530,height=350)

        DataFrameLeft=LabelFrame(DataFrame,bd=7,relief=RIDGE,padx=10,text="Medicine Information",
                                 fg="darkblue",font=("times new roman",20,"bold"))
        DataFrameLeft.place(x=0,y=5,width=800,height=350)
        DataFrameRight=LabelFrame(DataFrame,bd=7,relief=RIDGE,padx=20,text="Medicine Add Department",
                                 fg="darkblue",font=("times new roman",20,"bold"))
        DataFrameRight.place(x=800,y=5,width=400,height=350)
        #===================buttonsFrame========================
        ButtonFrame=Frame(self.root,bd=7,relief=RIDGE,padx=10)
        ButtonFrame.place(x=0,y=430,width=1530,height=50)
        #====================MainButton========================
        btnAddData=Button(ButtonFrame,text="Medicine Add",font=("times new roman",20,"bold"),bg="darkblue",fg="white")
        btnAddData.grid(row=0,column=0)

        btnAddData=Button(ButtonFrame,text="Update",font=("times new roman",20,"bold"),bg="darkblue",fg="white")
        btnAddData.grid(row=0,column=1)

        btnAddData=Button(ButtonFrame,text="Delete",font=("times new roman",20,"bold"),bg="darkblue",fg="white")
        btnAddData.grid(row=0,column=2)

        btnAddData=Button(ButtonFrame,text="Reset",font=("times new roman",20,"bold"),bg="darkblue",fg="white")
        btnAddData.grid(row=0,column=3)

        btnAddData=Button(ButtonFrame,text="Exit",font=("times new roman",20,"bold"),bg="darkblue",fg="white")
        btnAddData.grid(row=0,column=4)
        #=======================Search BY=======================
        lblSearch=Label(ButtonFrame,text="Search by",font=("times new roman",20,"bold"),bg="darkblue",fg="white")
        lblSearch.grid(row=0,column=5,sticky=W)

        serch_combo=ttk.Combobox(ButtonFrame,width=12,font=("times new roman",13,"bold"),state="readonly")
        serch_combo.grid(row=0,column=6)
        serch_combo["values"]=("Ref","Medname","Lot")
        serch_combo.grid(row=0,column=6)
        serch_combo.current(0)

        txtSerch=Entry(ButtonFrame,bd=3,relief=RIDGE,width=12,font=("times new roman",20,"bold"))
        txtSerch.grid(row=0,column=7)

        searchBtn=Button(ButtonFrame,text="Search",width=7,font=("times new roman",20,"bold"),bg="darkblue",fg="white")
        searchBtn.grid(row=0,column=8)
        searchBtn.place(x=1259)

        showAll=Button(ButtonFrame,text="Show",width=7,font=("times new roman",20,"bold"),fg="white",bg="darkblue")
        showAll.grid(row=0,column=9)
        showAll.place(x=1380)


        #====================label and entry====================
        lblrefno=Label(DataFrameLeft,text="Reference No",font=("times new roman",13,"bold"))
        lblrefno.grid(row=0,column=0,sticky=W)

        ref_combo=ttk.Combobox(DataFrameLeft,width=23,font=("times new roman",13,"bold"),state="readonly")
        ref_combo["values"]=("Ref","Medname","Lot")
        ref_combo.grid(row=0,column=1)
        ref_combo.current(0)

        lblCmpName=Label(DataFrameLeft,font=("times new roman",12,"bold"),text="Company:",padx=2,pady=6)
        lblCmpName.grid(row=1,column=0,sticky=W)
        txtCmpName=Entry(DataFrameLeft,font=("times new roman",12,"bold"),bg="white",bd=2,relief=RIDGE,width=27)
        txtCmpName.grid(row=1,column=1)

        
        lblTypeofMedicine=Label(DataFrameLeft,text="Type",font=("times new roman",13,"bold"))
        lblTypeofMedicine.grid(row=2,column=0,sticky=W)

        comTypeofMedicine=ttk.Combobox(DataFrameLeft,width=23,font=("times new roman",13,"bold"),state="readonly")
        comTypeofMedicine["values"]=("Tablet","Liquid","Capsules","Topical Medicines","Drops","Inhalse","Injection")
        comTypeofMedicine.grid(row=2,column=1)
        comTypeofMedicine.current(0)


    #=======================Add medicine========================
        lblMedicineName=Label(DataFrameLeft,font=("times new roman",12,"bold"),text="Medicine Name",padx=2,pady=6)
        lblMedicineName.grid(row=3,column=0,sticky=W)

        comMedicineName=ttk.Combobox(DataFrameLeft,state="readonly",width=23,font=("times new roman",13,"bold"))
        comMedicineName["value"]=("nice","novel")
        comMedicineName.current(0)
        comMedicineName.grid(row=3,column=1)

        lblLotNo=Label(DataFrameLeft,font=("times new roman",12,"bold"),text="Lot No:",padx=2,pady=6)
        lblLotNo.grid(row=4,column=0,sticky=W)
        txtLotNo=Entry(DataFrameLeft,font=("times new roman",12,"bold"),bg="white",bd=2,relief=RIDGE,width=29)
        txtLotNo.grid(row=4,column=1)

        lblIssueDate=Label(DataFrameLeft,font=("times new roman",12,"bold"),text="Issue Date:",padx=2,pady=6)
        lblIssueDate.grid(row=5,column=0,sticky=W)
        txtIssueDate=Entry(DataFrameLeft,font=("times new roman",12,"bold"),bg="white",bd=2,relief=RIDGE,width=29)
        txtIssueDate.grid(row=5,column=1)

        lblExDate=Label(DataFrameLeft,font=("times new roman",12,"bold"),text="Exp Date:",padx=2,pady=6)
        lblExDate.grid(row=6,column=0,sticky=W)
        txtExDate=Entry(DataFrameLeft,font=("times new roman",12,"bold"),bg="white",bd=2,relief=RIDGE,width=29)
        txtExDate.grid(row=6,column=1)

        
        lblPrecWarning=Label(DataFrameLeft,font=("times new roman",12,"bold"),text="Prec & Warning:",padx=2,pady=6)
        lblPrecWarning.grid(row=0,column=2,sticky=W)
        txtPrecWarning=Entry(DataFrameLeft,font=("times new roman",12,"bold"),bg="white",bd=2,relief=RIDGE,width=29)
        txtPrecWarning.grid(row=0,column=3)

        lblDosage=Label(DataFrameLeft,font=("times new roman",12,"bold"),text="Dosage:",padx=2,pady=6)
        lblDosage.grid(row=1,column=2,sticky=W)
        txtDosage=Entry(DataFrameLeft,font=("times new roman",12,"bold"),bg="white",bd=2,relief=RIDGE,width=29)
        txtDosage.grid(row=1,column=3)

        lblPrice=Label(DataFrameLeft,font=("times new roman",12,"bold"),text="Price:",padx=2,pady=6)
        lblPrice.grid(row=2,column=2,sticky=W)
        txtPrice=Entry(DataFrameLeft,font=("times new roman",12,"bold"),bg="white",bd=2,relief=RIDGE,width=29)
        txtPrice.grid(row=2,column=3)

        lblProductQt=Label(DataFrameLeft,font=("times new roman",12,"bold"),text="Product QT:",padx=2,pady=6)
        lblProductQt.grid(row=3,column=2,sticky=W)
        txtProductQt=Entry(DataFrameLeft,font=("times new roman",12,"bold"),bg="white",bd=2,relief=RIDGE,width=29)
        txtProductQt.grid(row=3,column=3,sticky=W)

        lblUses=Label(DataFrameLeft,font=("times new roman",12,"bold"),text="Uses:",padx=2,pady=6)
        lblUses.grid(row=4,column=2,sticky=W)
        txtUses=Entry(DataFrameLeft,font=("times new roman",12,"bold"),bg="white",bd=2,relief=RIDGE,width=29)
        txtUses.grid(row=4,column=3)

        lblSideEffect=Label(DataFrameLeft,font=("times new roman",12,"bold"),text="Side Effect:",padx=2,pady=6)
        lblSideEffect.grid(row=5,column=2,sticky=W)
        txtSideEffect=Entry(DataFrameLeft,font=("times new roman",12,"bold"),bg="white",bd=2,relief=RIDGE,width=29)
        txtSideEffect.grid(row=5,column=3)

        #_______VKC_______#
        #==========Images=============#
        lblhome=Label(DataFrameLeft,font=("arial",15,"bold"),text="Stay SANK Stay safe:",padx=2,pady=6,bg="white",fg="red",width=30)
        lblhome.place(x=365,y=210)
        
  

      # ==================== dataframeRight======================

        DataFrameRight=LabelFrame(DataFrame,bd=7,relief=RIDGE,padx=20,text="Medicine Add Department",fg="darkblue",font=("times new roman",20,"bold"))
        DataFrameRight.place(x=800,y=5,width=700,height=350)
    
        img2 = Image.open(file_path2)
        img2 = img2.resize((150,120),Image.Resampling.LANCZOS)
        self.photoimg2=ImageTk.PhotoImage(img2)
        b1=Button(self.root,image=self.photoimg2,borderwidth=0)
        b1.place(x=1330,y=170)
    
        img4 = Image.open(file_path4)
        img4 = img4.resize((150,120),Image.Resampling.LANCZOS)
        self.photoimg4=ImageTk.PhotoImage(img4)
        b1=Button(self.root,image=self.photoimg4,borderwidth=0)
        b1.place(x=1330,y=300) 
    
        lblrefno=Label(DataFrameRight,font=("times new roman",12,"bold"),text="Reference No:")
        lblrefno.place(x=0,y=10)
        txtrefno=Entry(DataFrameRight,textvariable=self.refMed_var,font=("times new roman",12,"bold"),bg="white",bd=2,relief=RIDGE,width=20)
        txtrefno.place(x=135,y=10)
    
        lblmedName=Label(DataFrameRight,font=("times new roman",12,"bold"),text="Medicine Name:")
        lblmedName.place(x=0,y=45)
        txtmedName=Entry(DataFrameRight,textvariable=self.addmed_var,font=("times new roman",12,"bold"),bg="white",bd=2,relief=RIDGE,width=20)
        txtmedName.place(x=135,y=45)
    
    #==================side frame==================

        side_frame=Frame(DataFrameRight,bd=4,relief=RIDGE,bg="white")
        side_frame.place(x=0,y=90,width=300,height=170)
    
        sc_x=ttk.Scrollbar(side_frame,orient=HORIZONTAL)
        sc_x.pack(side=BOTTOM,fill=X)
        sc_y=ttk.Scrollbar(side_frame,orient=VERTICAL)
        sc_y.pack(side=RIGHT,fill=Y)

        self.medicine_table=ttk.Treeview(side_frame,column=("ref","medname"),xscrollcommand=sc_x.set,yscrollcommand=sc_y.set)

        sc_x.config(command=self.medicine_table.xview)  
        sc_y.config(command=self.medicine_table.yview)

        self.medicine_table.heading("ref",text="Ref")
        self.medicine_table.heading("medname",text="Medicine Name")

        self.medicine_table["show"]="headings"
        self.medicine_table.pack(fill=BOTH,expand=1)

        self.medicine_table.column("ref",width=100)
        self.medicine_table.column("medname",width=100)
        self.medicine_table.bind("<ButtonRelease-1>",self.Medget_cursor)

        # ============ Medicine Add Buttons===================
        down_frame=Frame(DataFrameRight,bd=4,relief=RIDGE,bg="darkblue")
        down_frame.place(x=330,y=10,width=138,height=230)

        btnAddmed=Button(down_frame,command=self.AddMed,text="ADD",font=("times new roman",20,"bold"),width=8,bg="#00008B",fg="white",pady=2)
        btnAddmed.grid(row=0,column=0)

        btnUpdatemed=Button(down_frame,command=self.UpdateMed,text="UPDATE",font=("times new roman",20,"bold"),width=8,bg="#0000CD",fg="white",pady=2)
        btnUpdatemed.grid(row=1,column=0)

        btnDeletemed=Button(down_frame,text="DELETE",font=("times new roman",20,"bold"),width=8,bg="#00008B",fg="white",pady=2)
        btnDeletemed.grid(row=2,column=0)

        btnClearmed=Button(down_frame,text="CLEAR",font=("times new roman",20,"bold"),width=8,bg="#0000CD",fg="white",pady=2)
        btnClearmed.grid(row=3,column=0)

       #==========Frame details=================
        Framedetails=Frame(self.root,bd=15,relief=RIDGE)
        Framedetails.place(x=0,y=510,width=1530,height=250)

    #===========Main Table & scrollbar============
        Table_frame=Frame(self.root,bd=15,relief=RIDGE)
        Table_frame.place(x=10,y=510,width=1530,height=250)

        scroll_x=ttk.Scrollbar(Table_frame,orient=HORIZONTAL)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y=ttk.Scrollbar(Table_frame,orient=VERTICAL)
        scroll_y.pack(side=RIGHT,fill=Y)

        self.pharmacy_table=ttk.Treeview(Table_frame,column=("ref","companyname","type","tabletname","lotno","issuedate",
                                                             "expdate","uses","sideeffect","warning","dosage","price","productqt")
                                                             ,xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.pharmacy_table.xview)
        scroll_y.config(command=self.pharmacy_table.yview) 

        self.pharmacy_table["show"]="headings"

        self.pharmacy_table.heading("ref",text="Reference No")
        self.pharmacy_table.heading("companyname",text="Company Name")
        self.pharmacy_table.heading("type",text="Type of Medicine")
        self.pharmacy_table.heading("tabletname",text="Tablet Name")
        self.pharmacy_table.heading("lotno",text="Lot No")
        self.pharmacy_table.heading("issuedate",text="Issue Date")
        self.pharmacy_table.heading("expdate",text="Exp Date")
        self.pharmacy_table.heading("uses",text="Uses")
        self.pharmacy_table.heading("sideeffect",text="Side Effect")
        self.pharmacy_table.heading("warning",text="Prec&Warning")
        self.pharmacy_table.heading("dosage",text="Dosage")
        self.pharmacy_table.heading("price",text="Price")
        self.pharmacy_table.heading("productqt",text="Product Qts")
        self.pharmacy_table.pack(fill=BOTH,expand=1)

        self.pharmacy_table.column("ref",width=100)
        self.pharmacy_table.column("companyname",width=100)
        self.pharmacy_table.column("type",width=100)
        self.pharmacy_table.column("tabletname",width=100)
        self.pharmacy_table.column("lotno",width=100)
        self.pharmacy_table.column("issuedate",width=100)
        self.pharmacy_table.column("expdate",width=100)
        self.pharmacy_table.column("uses",width=100)
        self.pharmacy_table.column("sideeffect",width=100)
        self.pharmacy_table.column("warning",width=100)
        self.pharmacy_table.column("dosage",width=100)
        self.pharmacy_table.column("price",width=100)
        self.pharmacy_table.column("productqt",width=100)
        #_________VKC_end__________#

        self.fetch_dataMed()
#shruthi
#befor medicine add button

#------

# add medicine functionality==========
def AddMed(self):
    conn=mysql.connector.connect(host="localhost",username="root",password="anvitha",database="anvitha")
    my_cursor=conn.cursor()
    my_cursor.execute("insert into pharma(Ref,MedName) values(%s,%s)",(
                                                                    self.refMed_var.get(),
                                                                    self.Addmed_var.get()



                                                                        ))
    conn.commit()
    self.fetch_dataMed()
    self.Medget_cursor()
    conn.close()
    messagebox.showinfo("Success","Medicine Added") 

def fetch_dataMed(self):
    conn=mysql.connector.connect(host="localhost",username="root",password="anvitha",database="anvitha")
    my_cursor=conn.cursor()
    my_cursor.execute("select * from pharma")
    rows=my_cursor.fetchall()
    if len(rows)!=0:
        self.medicine_table.delete(*self.medicine_table.get_children())
        for i in rows:
            self.medicine_table.insert("",END,values=i)
        conn.commit()
    conn.close()

    #+===medgetcursor====
def Medget_cursor(self,event=""):
    cursor_row=self.medicine_table.focus()
    content=self.medicine_table.item(cursor_row)
    row=content["values"]
    self.refMed_var.set(row[0])
    self-addmed_var.set(row[1])


def UpdateMed(self):
    if self.refMed_var.get()=="" or self.addmed_var.get()=="":
        messagebox.showerror("Error","All fields are Required")
    else:
        conn=mysql.connector.connect(host="localhost",username="root",password="anvitha",database="anvitha")
        my_cursor=conn.cursor()
        my_cursor.execute("update pharma set MedName=%s where Ref=%s",(
                                                                    self.addmed_var.get(),
                                                                    self.refMed_var.get(),
                                                                    ))
    conn.commit()
    self.fetch_dataMed()
    conn.close()

    messagebox.showinfo("Success","Medicine has been Updated")



#________anvitha last part ___________
def DeleteMed (self):
    conn=mysql.connector.connect(host="localhost", username="root", password="anvitha", database="anvitha")
    my_cursor=conn.cursor()

    sql="delete from pharma where Ref=%s"
    val=(self.refMed_var.get(),)
    my_cursor.execute(sql, val)

    conn.commit()
    self.fetch_dataMed()
    conn.close()

def ClearMEd(self):
    self.refMed_var.set("")
    self.addmed_var.set("")

# ======================= Main Table =================

def add_data(self) :
    if self.ref_var.get()=="" or self.lot.get()=="":
        messagebox.showerror ("Error","All fields are required")
    else:    
        conn=mysql.connector.connect (host ="localhost", username= "root", password= "anvitha", database="anvitha")
        my_cursor=conn.cursor()
        my_cursor.execute("insert into pharmacy values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                            self.ref_var.get(),
                                                                                            self.cmpName_var.get(),
                                                                                            self.typeMed_var.get(),
                                                                                            self.medName_var.get(),
                                                                                            self.lot_var.get(),
                                                                                            self.issuedate_var.get(),
                                                                                            self.expdate_var.get(),
                                                                                            self.uses_var.get(),
                                                                                            self.sideEffect_var.get(),
                                                                                            self.warning_var.get(),
                                                                                            self.dosage_var.get(),
                                                                                        self.price_var.get(),
                                                                                        self.product_var.get()
                                                                                        ))
        conn.commit()
        self.fatch_data()
        conn.close()
        messagebox.showinfo("Success","data has been inserted")

def fetch_data(self):
    conn=mysql.connector.connect (host ="localhost", username= "root", password= "anvitha", database="anvitha")
    my_cursor=conn.cursor()
    my_cursor.execute ("select * from pharmacy")
    row=my_cursor.fetchall()
    if len(row)!=0:
        self.pharmacy_table.delete(*self.pharmacy_table.get_children())
        for i in row:
            self.pharmacy_table.insert("", END, values=i)
        conn.commit()
    conn.close()

def get_cursor (self,ev="") :
    cursor_row=self.medicine_table.focus() content=self.medicine_table.item(cursor_row)
    row=content["values"]
    
    self.ref_var.set(row[0]),
    self.cmpName_var.set(row[1]),
    self.typeMed_var.set(row[2]),
    self.medName_var.set(row[3]),
    self.lot_var.set(row[4]),
    self.issuedate_var.set(row[5]),
    self.expdate_var.set(row[6]),
    self.uses_var.set(row[7]),
    self.sideEffect_var.set(row[8]),
    self.warning_var.set(row[9]),
    self.dosage_var.set(row[10]),
    self.price_var.set(row[11]),
    self.product_var.set(row[12])

def Update(self):
    if self.ref_var.get()=="" or self.lot_var.get()=="":
        messagebox.showerror("Error", "All fields are Required")
    else:
        conn=mysql.connector.connect(host="localhost", username="root", password="anvitha", database="anvitha") my_cursor=conn.cursor()
        my_cursor.execute("update pharmacy set cmpName=%s, Type=%s, medname=%s, lot=%s, isuuedate=%d,expdate=%s, uses=%s, sideeffects= %s, warning=%s, dosage= %s, price=%s, product=%s  where refno=%s", (
        self.addmed_var.get(),
        self.refMed_var.get(),
        conn.commit()
        self.fetch_dataMed()
        conn.close()
        messagebox.showinfo("Success", "Medicine has been Updated")




if __name__ == "__main__":
    root=Tk()
    obj=PharmacyManagementSystem(root)
    root.mainloop()




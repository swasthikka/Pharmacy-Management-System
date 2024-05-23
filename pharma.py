from tkinter import*
from PIL import Image,ImageTk
from tkinter import ttk

class PharmacyManagementSystem:
    def __init__(self,root):
        self.root=root
        self.root.title("Pharmacy Management System")
        self.root.geometry("1550x800+0+0")

        lbltitle=Label(self.root,text="PHARMACY MANAGEMENT SYSTEM",bd=7, relief=RIDGE
                      ,bg="white",fg="darkblue",font=("times new roman",40,"bold"),padx=3)
        
        lbltitle.pack(side=TOP,fill=X)
        file_path = r"D:\College\Sem 4\CS6106\Project\tabletlogo.png"

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
        ButtonFrame.place(x=0,y=420,width=1530,height=50)
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

        showAll=Button(ButtonFrame,text="Show",width=7,font=("times new roman",20,"bold"),fg="white",bg="darkblue")
        showAll.grid(row=0,column=9)


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


if __name__ == "__main__":
    root=Tk()
    obj=PharmacyManagementSystem(root)
    root.mainloop()




#________anvitha last part ___________
def DeleteMed (self):
    conn=mysql.connector.connect(host="localhost", username="root", password="", database="mydata")
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

import tkinter as tk
from tkinter import messagebox
import pymysql
import mysql.connector

try:
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Anshul@1234",
        database="bank"  # Ensure this is the correct database name
    )
    cursor = conn.cursor()
    print("Database Connected Successfully!")
except mysql.connector.Error as err:
    print(f"Error: {err}")
    exit()
    
class bank():
    def __init__(self,root):
        self.root = root
        self.root.title("Bank Management")
        
        
        scrn_width = self.root.winfo_screenwidth()
        scrn_height = self.root.winfo_screenheight()
        
        self.root.geometry(f"{scrn_width}x{scrn_height}+0+0")
        
        mainLabel = tk.Label(self.root,text="Bank Account Management System", font=("Arial",40,"bold"),bg="light green",bd=5, relief="groove")
        mainLabel.pack(side="top",fill="x")
        
        mainFrame = tk.Frame(self.root,bg="light gray",bd=5, relief="ridge")
        mainFrame.place(x=500, y=90 , width=450, height=550)
        
        openAcBtn = tk.Button(mainFrame,command=self.openAc ,width=20,text="Open Account", bg="light blue", bd=3, relief="raised",font=("Arial",20,"bold"))
        openAcBtn.grid(row=0, column=0, padx=40,pady=65)
        
        depBtn = tk.Button(mainFrame,width=20,text="Deposit",command=self.deposit, bg="light blue", bd=3, relief="raised",font=("Arial",20,"bold"))
        depBtn.grid(row=1, column=0, padx=40,pady=65)
        
        wdBtn = tk.Button(mainFrame,width=20,text="Withdraw",command=self.wd ,bg="light blue", bd=3, relief="raised",font=("Arial",20,"bold"))
        wdBtn.grid(row=2, column=0, padx=40,pady=65)
    
    
        
    def openAc(self):
        self.openAcFrame = tk.Frame(self.root,bg="light gray",bd=5, relief="ridge")
        self.openAcFrame.place(x=500, y=90 , width=450, height=550)
            
            
        uNameLabel = tk.Label(self.openAcFrame,text="User Name",bg="light gray",font=("Arial",15,"bold"))
        uNameLabel.grid(row=0, column=0, padx=20, pady=30)
        self.uNameIn = tk.Entry(self.openAcFrame, width=15,font=("Arial",15))
        self.uNameIn.grid(row=0, column=1, padx=5, pady=30)
            
             
        uPWLabel = tk.Label(self.openAcFrame,text="Enter Password:",bg="light gray",font=("Arial",15,"bold"))
        uPWLabel.grid(row=1, column=0, padx=20, pady=30)
        self.uPWIn = tk.Entry(self.openAcFrame, width=15,font=("Arial",15))
        self.uPWIn.grid(row=1, column=1, padx=5, pady=30)
            
             
        confirmLabel = tk.Label(self.openAcFrame,text="Confirm Password",bg="light gray",font=("Arial",15,"bold"))
        confirmLabel.grid(row=2, column=0, padx=20, pady=30)
        self.confirmIn = tk.Entry(self.openAcFrame, width=15,font=("Arial",15))
        self.confirmIn.grid(row=2, column=1, padx=5, pady=30)
            
        okBtn= tk.Button(self.openAcFrame,command=self.insert,text="OK",width=10,bg="light blue", bd=3, relief="raised",font=("Arial",15,"bold"))
        okBtn.grid(row=3, column=0, padx=40,pady=200)
            
        
        closeBtn= tk.Button(self.openAcFrame,command=self.close_openAc,text="Close",width=10,bg="light blue", bd=3, relief="raised",font=("Arial",15,"bold"))
        closeBtn.grid(row=3, column=1, padx=40,pady=200)
            
    def close_openAc(self):
        self.openAcFrame.destroy()
        
    
    def insert(self):
        uName = self.uNameIn.get() 
        uPW = self.uPWIn.get()
        confirm= self.confirmIn.get()
        
        if uPW == confirm:
            con = pymysql.connect(host="localhost",user="root",passwd="Anshul@1234",database="bank")
            cur = con.cursor()
            cur.execute("Insert into account (userName,password) values(%s,%s)",(uName,uPW))
            con.commit()
            con.close()
            tk.messagebox.showinfo("Success","Account Opened Successfully")
            self.clear()
        else:
            tk.messagebox.showerror("Error","Access Denied!")    
            self.clear()

    def clear(self):
        self.uNameIn.delete(0, tk.END)
        self.uPWIn.delete(0, tk.END)
        self.confirmIn.delete(0, tk.END)
        
    def deposit(self):
        self.depFrame = tk.Frame(self.root,bg="light gray",bd=5, relief="ridge")
        self.depFrame.place(x=500, y=90 , width=450, height=550)
            
            
        NameLabel = tk.Label(self.depFrame,text="User Name",bg="light gray",font=("Arial",15,"bold"))
        NameLabel.grid(row=0, column=0, padx=20, pady=30)
        self.NameIn = tk.Entry(self.depFrame, width=15,font=("Arial",15))
        self.NameIn.grid(row=0, column=1, padx=5, pady=30)
            
        amountLabel = tk.Label(self.depFrame,text="Enter Amount:",bg="light gray",font=("Arial",15,"bold"))
        amountLabel.grid(row=1, column=0, padx=20, pady=30)
        self.amountIn = tk.Entry(self.depFrame, width=15,font=("Arial",15))
        self.amountIn.grid(row=1, column=1, padx=5, pady=30)
        
        okBtn= tk.Button(self.depFrame,command=self.deposite_fun,text="Deposit",width=10,bg="light blue", bd=3, relief="raised",font=("Arial",15,"bold"))
        okBtn.grid(row=2, column=0, padx=40,pady=230)
            
        
        closeBtn= tk.Button(self.depFrame,command=self.close_deposite,text="Close",width=10,bg="light blue", bd=3, relief="raised",font=("Arial",15,"bold"))
        closeBtn.grid(row=2, column=1, padx=40,pady=230)
    
    def deposite_fun(self):
        Name = self.NameIn.get() 
        amount = int(self.amountIn.get())
        
        con = pymysql.connect(host="localhost",user="root",password="Anshul@1234",database="bank")
        cur = con.cursor()
        cur.execute("select balance from account where userName = %s",(Name))
        data= cur.fetchone()
        if data:
            balance = data[0]
            if data[0] is None:
                balance = 0
            update = balance +amount
            cur.execute("update account set balance = %s where userName = %s",(update,Name))
            con.commit()
            con.close()
            tk.messagebox.showinfo("Success","Amount Deposited Successfully")
            
            
            
           
        else:
            tk.messagebox.showerror("Error","Invalid Customer Name")    
            
            
    def close_deposite(self):
        self.depFrame.destroy()  
    def wd(self):
        self.wdFrame = tk.Frame(self.root,bg="light gray",bd=5, relief="ridge")
        self.wdFrame.place(x=500, y=90 , width=450, height=550)
            
            
        cNameLabel = tk.Label(self.wdFrame,text="User Name",bg="light gray",font=("Arial",15,"bold"))
        cNameLabel.grid(row=0, column=0, padx=20, pady=30)
        self.cNameIn = tk.Entry(self.wdFrame, width=15,font=("Arial",15))
        self.cNameIn.grid(row=0, column=1, padx=5, pady=30)
            
             
        cPWLabel = tk.Label(self.wdFrame,text="Enter Password:",bg="light gray",font=("Arial",15,"bold"))
        cPWLabel.grid(row=1, column=0, padx=20, pady=30)
        self.cPWIn = tk.Entry(self.wdFrame, width=15,font=("Arial",15))
        self.cPWIn.grid(row=1, column=1, padx=5, pady=30)
            
             
        wdLabel = tk.Label(self.wdFrame,text="Enter Amount:",bg="light gray",font=("Arial",15,"bold"))
        wdLabel.grid(row=2, column=0, padx=20, pady=30)
        self.wdIn = tk.Entry(self.wdFrame, width=15,font=("Arial",15))
        self.wdIn.grid(row=2, column=1, padx=5, pady=30)
            
        okBtn= tk.Button(self.wdFrame,command=self.wd_fun,text="Withdraw",width=10,bg="light blue", bd=3, relief="raised",font=("Arial",15,"bold"))
        okBtn.grid(row=3, column=0, padx=40,pady=200)
            
        
        closeBtn= tk.Button(self.wdFrame,command=self.close_wd,text="Close",width=10,bg="light blue", bd=3, relief="raised",font=("Arial",15,"bold"))
        closeBtn.grid(row=3, column=1, padx=40,pady=200)
   
   
    def wd_fun(self):
        name = self.cNameIn.get()
        pw = self.cPWIn.get()
        amount = int(self.wdIn.get())
        
        con = pymysql.connect(host="localhost",user="root",password="Anshul@1234",database="bank")
        cur = con.cursor()
        cur.execute("select userPW,balance from account where userName= %s",name)
        data = cur.fetchone()
        if data:
           if data[0]==pw:
               if data[1] >= amount:
                   update = data[1] - amount
                   cur.execute("update account set balance=%s where userName=%s",(update,name))
                   con.commit()
                   con.close()
                   tk.messagebox.showinfo("Success","OPeration was success")      
          
                   
               else:
                  tk.messagebox.showerror("Error","Insufficient Balance!")      
           
           else:
               tk.messagebox.showerror("Error","Invalid Customer Password")
        else:
            tk.messagebox.showerror("Error","Invalid Customer Name!")      
          
    def  close_wd(self):
        self.wdFrame.destroy()   
        
           
root = tk.Tk()
obj = bank(root)
root.mainloop()
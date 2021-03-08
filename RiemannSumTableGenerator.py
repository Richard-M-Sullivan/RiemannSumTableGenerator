import tkinter as tk
import tkinter.messagebox
from tkinter import ttk
from math import *

#setup application

class Application():
    
    MAX_N_VALUE = 100000
    MIN_N_VALUE = 1
    WINDOW_MIN_X = 350
    WINDOW_MIN_Y = 230

    def __init__(self,master,title):
        #initialize class memeber varables
        self.errorLog = "" 
        self.table = [] 
        self.function = ""
        self.n = ""
        self.upper_bound = ""
        self.lower_bound = ""
        self.converted_function = ""
        
        #initialize gui and widgets
        self.root =  master
        self.root.title(title)
        #set window options
        root.title(str(title))
        root.minsize(Application.WINDOW_MIN_X,Application.WINDOW_MIN_Y)


        #create frames and widgets

        self.windowFrame = tk.Frame(padx=30,pady=30)

        self.functionFrame = tk.Frame(master=self.windowFrame)

        self.functionLabel = tk.Label(master=self.functionFrame,text="Function:")
        self.functionEntry = tk.Entry(master=self.functionFrame)

        self.nFrame = tk.Frame(master=self.windowFrame)

        self.nLabel = tk.Label(master=self.nFrame, text="n:")
        self.nEntry = tk.Entry(master=self.nFrame)

        self.upperBoundFrame = tk.Frame(master=self.windowFrame)

        self.upperBoundLabel = tk.Label(master=self.upperBoundFrame, text="Upper Bound:")
        self.upperBoundEntry = tk.Entry(master=self.upperBoundFrame) 

        self.lowerBoundFrame = tk.Frame(master=self.windowFrame)

        self.lowerBoundLabel = tk.Label(master=self.lowerBoundFrame, text="Lower Bound:")
        self.lowerBoundEntry = tk.Entry(master=self.lowerBoundFrame)

        self.submitButton = tk.Button(master=self.root,bg="white",text="submit",command=self.calculateValues)

        self.tableTree = ttk.Treeview(master=self.root)
        
        #setup the table
        self.tableTree["columns"] = ["i","f(xi)","C","Cf(xi)","xm","f(xm)"]
        self.tableTree.column("#0"    ,anchor="w",width=0)
        self.tableTree.column("i"     ,anchor="w",minwidth=25,width=120)
        self.tableTree.column("f(xi)" ,anchor="w",minwidth=25,width=120)
        self.tableTree.column("C"     ,anchor="w",minwidth=25,width=120)
        self.tableTree.column("Cf(xi)",anchor="w",minwidth=25,width=120)
        self.tableTree.column("xm"    ,anchor="w",minwidth=25,width=120)
        self.tableTree.column("f(xm)" ,anchor="w",minwidth=25,width=120)

        self.tableTree.heading("#0"    ,text=""       ,anchor="w")
        self.tableTree.heading("i"     ,text="i"      ,anchor="w")
        self.tableTree.heading("f(xi)" ,text="f(xi)"  ,anchor="w")
        self.tableTree.heading("C"     ,text="C"      ,anchor="w")
        self.tableTree.heading("Cf(xi)",text="C*f(xi)",anchor="w")
        self.tableTree.heading("xm"    ,text="xm"     ,anchor="w")
        self.tableTree.heading("f(xm)" ,text="f(xm)"  ,anchor="w")

        self.tableTree["show"] = "headings"
        # add frames to window
        self.windowFrame.pack(anchor="w")
        self.functionFrame.pack(anchor="e")
        self.nFrame.pack(anchor="e")
        self.upperBoundFrame.pack(anchor="e")
        self.lowerBoundFrame.pack(anchor="e")


        # add widgets to frames
        self.functionEntry.pack(side="right")
        self.functionLabel.pack(side="right")

        self.nEntry.pack(side="right")
        self.nLabel.pack(side="right")

        self.upperBoundEntry.pack(side="right")
        self.upperBoundLabel.pack(side="right")

        self.lowerBoundEntry.pack(side="right")
        self.lowerBoundLabel.pack(side="right")

        self.submitButton.pack(padx=30,pady=(0,30),anchor="w")
        self.tableTree.pack(pady=(0,30))
        #setup complete
        
        #enter the applicaiton main loop to start application
        tk.mainloop()

    def calculateValues(self):#called by the submit button
        #getting values from the fields

        #check if the values are new
        function = self.functionEntry.get()
        n = self.nEntry.get()
        upper_bound = self.upperBoundEntry.get()
        lower_bound = self.lowerBoundEntry.get()
        
        #if the values are the same do nothing
        if (self.function == function and self.n == n 
            and self.upper_bound == upper_bound
            and self.lower_bound == lower_bound):
            pass
        #if the values are new then redo calculations
        else:
            self.function = function
            self.n = n
            self.upper_bound = upper_bound
            self.lower_bound = lower_bound
            #error checking
            if self.checkValues():
                #if no errors generate a new table to display
                self.convert_function()
                self.generate_table()
                self.new_tableTree()
            #if there is an error show the error log
            else:
                tk.messagebox.showinfo("Response",self.get_error_log())


    def checkValues(self):
        #calls the check functions for the corresponding entry fields
        self.clear_error_log()
        good = 0 
        good += self.check_function()
        good += self.check_n()
        good += self.check_upper_bound()
        good += self.check_lower_bound()
        return good == 0

    def check_function(self):
        return 0

    def check_n(self):
        try:
            n = int(self.n)
        except ValueError:
            self.append_error_log("you need to make n an interger")
            return 1
        except Exception:
            self.append_error_log("you did somthing wrong")
            return 1
        else:
            if n > Application.MAX_N_VALUE:
                self.append_error_log("your n value is too high. try: "+str(Application.MAX_N_VALUE))
                return 1
            elif n < Application.MIN_N_VALUE:
                self.append_error_log("your n value is too low. try: "+str(Application.MIN_N_VALUE))
                return 1
            else:
                return 0;

    def check_upper_bound(self):
        try:
            upper = float(self.upper_bound)
        except ValueError:
            self.append_error_log("you upper bound needs to be a number (floating point or int)")
            return 1
        except Exception:
            self.append_error_log("you did somthing wrong")
            return 1
        else:
            return 0

    def check_lower_bound(self):
        try:
            lower = float(self.lower_bound)
        except ValueError:
            self.append_error_log("lower bounds needs to be a number (floating point or int)")
            return 1
        except Exception:
            self.append_error_log("you did somthing wrong")
            return 1
        else:
            try: 
                upper = float(self.upper_bound)
            except Exception:
                self.append_error_log("unable to compare upper and lower bound")
                return 1
            else:
                if lower < upper:
                    return 0
                else:
                    self.append_error_log("lower bound needs to be less than upper bound")
                    return 1
        return 0

    def convert_function(self):
        displacement = 0
        function = self.function
        for i in range(len(function)-1):
            val1 = function[i+displacement]
            val2 = function[i+displacement+1]
            print(function,i,displacement,val1,val2)
            op = self.generate_operator(val1,val2)

            if not(op == ""):
                function = function[0:i+displacement+1]+op+function[i+displacement+1:]
                displacement += 1

        converted_function = function
                
    def generate_operator(self,val1,val2):
            #if the value is a number
            if val1.isnumeric():
                #return nothing if both numbers
                if val2.isnumeric():
                    return ""
                #else you need to multiply
                elif (val2 == "(" or val2 == "x"):
                    return "*"
                else:
                    return""
            #if the first value is a ) or x
            elif val1 == ")" or val1 == "x":
                #if the second value is not an operator then multiply
                if val2.isnumeric() or val2=="(" or val2 =="x":
                    return "*"
                else:
                    return ""
            else:
                return ""
                
            
            

    def generate_table(self):
        #the needed fields that the table has to generate are as follows:
        # i, xi, f(xi), c, c(fxi), xm, f(xm)
        self.table=[]
        self.table.append([self.n,"xi","f(xi)","c","cf(xi)","xm","f(xm)"])
         
    def new_tableTree(self):
        #clear the previous tree
        for record in self.tableTree.get_children():
            self.tableTree.delete(record)
        #insert all the needed data into the new tree
        for row in self.table:    
            self.tableTree.insert(parent="",index="end",iid="0",values=row)

    def clear_error_log(self):
        self.error_log = ""

    def append_error_log(self,error_string):
        if self.error_log == "":
            self.error_log += error_string
        else:
            self.error_log += "\n"+error_string

    def get_error_log(self):
        return self.error_log

#create window
root = tk.Tk()
app = Application(root,"Riemann Sum Calculator")




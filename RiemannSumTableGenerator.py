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
        self.L_var = tk.StringVar()
        self.R_var = tk.StringVar()
        self.T_var = tk.StringVar()
        self.M_var = tk.StringVar()
        self.S_var = tk.StringVar()

        self.L_var.set("nan")
        self.R_var.set("nan")
        self.T_var.set("nan")
        self.M_var.set("nan")
        self.S_var.set("nan")

        
        #initialize gui and widgets
        self.root =  master
        self.root.title(title)
        #set window options
        root.title(str(title))
        root.minsize(Application.WINDOW_MIN_X,Application.WINDOW_MIN_Y)


        #create frames and widgets
        #outermost frame to hold entry and display frame
        self.windowFrame = tk.Frame(master=self.root,padx=30,pady=30)
        #holds all of the frames for the entry widgets
        self.entryFrame = tk.Frame(master=self.windowFrame)
        #all below are entry frames and widgets
        self.functionFrame = tk.Frame(master=self.entryFrame)

        self.functionLabel = tk.Label(master=self.functionFrame,text="Function:")
        self.functionEntry = tk.Entry(master=self.functionFrame)

        self.nFrame = tk.Frame(master=self.entryFrame)

        self.nLabel = tk.Label(master=self.nFrame, text="n:")
        self.nEntry = tk.Entry(master=self.nFrame)

        self.upperBoundFrame = tk.Frame(master=self.entryFrame)

        self.upperBoundLabel = tk.Label(master=self.upperBoundFrame, text="Upper Bound:")
        self.upperBoundEntry = tk.Entry(master=self.upperBoundFrame) 

        self.lowerBoundFrame = tk.Frame(master=self.entryFrame)

        self.lowerBoundLabel = tk.Label(master=self.lowerBoundFrame, text="Lower Bound:")
        self.lowerBoundEntry = tk.Entry(master=self.lowerBoundFrame)
        #end entry widgets
        
        #holds all of the display frames
        self.displayFrame = tk.Frame(master=self.windowFrame,padx=30)
        #display frames and widgets
        self.lFrame = tk.Frame(master=self.displayFrame)

        self.lLabel = tk.Label(master=self.lFrame,text="L=")
        self.lAnswerLabel = tk.Label(master=self.lFrame,textvariable=self.L_var)

        self.rFrame = tk.Frame(master=self.displayFrame)

        self.rLabel = tk.Label(master=self.rFrame,text="R=")
        self.rAnswerLabel = tk.Label(master=self.rFrame,textvariable=self.R_var)

        self.tFrame = tk.Frame(master=self.displayFrame)

        self.tLabel = tk.Label(master=self.tFrame,text="T=")
        self.tAnswerLabel = tk.Label(master=self.tFrame,textvariable=self.T_var)

        self.mFrame = tk.Frame(master=self.displayFrame)

        self.mLabel = tk.Label(master=self.mFrame,text="M=")
        self.mAnswerLabel = tk.Label(master=self.mFrame,textvariable=self.M_var)

        self.sFrame = tk.Frame(master=self.displayFrame)

        self.sLabel= tk.Label(master=self.sFrame,text="S=")
        self.sAnswerLabel= tk.Label(master=self.sFrame,textvariable=self.S_var)


        self.submitButton = tk.Button(master=self.root,bg="white",text="submit",command=self.calculateValues)

        self.tableTree = ttk.Treeview(master=self.root)
        
        #setup the table
        self.tableTree["columns"] = ["i","xi","f(xi)","C","Cf(xi)","xm","f(xm)"]
        self.tableTree.column("#0"    ,anchor="w",width=0)
        self.tableTree.column("i"     ,anchor="w",minwidth=25,width=35)
        self.tableTree.column("xi"     ,anchor="w",minwidth=25,width=120)
        self.tableTree.column("f(xi)" ,anchor="w",minwidth=25,width=220)
        self.tableTree.column("C"     ,anchor="w",minwidth=25,width=25)
        self.tableTree.column("Cf(xi)",anchor="w",minwidth=25,width=220)
        self.tableTree.column("xm"    ,anchor="w",minwidth=25,width=120)
        self.tableTree.column("f(xm)" ,anchor="w",minwidth=25,width=220)

        self.tableTree.heading("#0"    ,text=""       ,anchor="w")
        self.tableTree.heading("i"     ,text="i"      ,anchor="w")
        self.tableTree.heading("xi"    ,text="xi"     ,anchor="w")
        self.tableTree.heading("f(xi)" ,text="f(xi)"  ,anchor="w")
        self.tableTree.heading("C"     ,text="C"      ,anchor="w")
        self.tableTree.heading("Cf(xi)",text="C*f(xi)",anchor="w")
        self.tableTree.heading("xm"    ,text="xm"     ,anchor="w")
        self.tableTree.heading("f(xm)" ,text="f(xm)"  ,anchor="w")

        self.tableTree["show"] = "headings"

        # add frames to window
        self.windowFrame.pack(anchor="w")

        self.entryFrame.pack(side="left",anchor="e")
        self.functionFrame.pack(anchor="e")
        self.nFrame.pack(anchor="e")
        self.upperBoundFrame.pack(anchor="e")
        self.lowerBoundFrame.pack(anchor="e")

        self.displayFrame.pack(side="left",anchor="e")
        self.lFrame.pack(anchor="w")
        self.rFrame.pack(anchor="w")
        self.tFrame.pack(anchor="w")
        self.mFrame.pack(anchor="w")
        self.sFrame.pack(anchor="w")


        # add widgets to frames
        self.functionEntry.pack(side="right")
        self.functionLabel.pack(side="right")

        self.nEntry.pack(side="right")
        self.nLabel.pack(side="right")

        self.upperBoundEntry.pack(side="right")
        self.upperBoundLabel.pack(side="right")

        self.lowerBoundEntry.pack(side="right")
        self.lowerBoundLabel.pack(side="right")



        self.lLabel.pack(side="left")
        self.lAnswerLabel.pack(side="left")

        self.rLabel.pack(side="left")
        self.rAnswerLabel.pack(side="left")

        self.tLabel.pack(side="left")
        self.tAnswerLabel.pack(side="left")

        self.mLabel.pack(side="left")
        self.mAnswerLabel.pack(side="left")

        self.sLabel.pack(side="left")
        self.sAnswerLabel.pack(side="left")



        self.submitButton.pack(padx=30,pady=(0,30),anchor="w")
        self.tableTree.pack(padx=30,pady=(0,30))
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
                self.updateLRTMS()
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
        if len(self.function) == 0:
            self.append_error_log("you need to specify a function")
            return 1
        else:
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
            op = self.generate_operator(val1,val2)

            if not(op == ""):
                if op == "**":
                    function = function[0:i+displacement]+op+function[i+displacement+1:] 
                else:
                    function = function[0:i+displacement+1]+op+function[i+displacement+1:]
                displacement += 1

        self.converted_function = function


    def generate_operator(self,val1,val2):
            #if the value is a number
            if val1.isdigit():
                #return nothing if both numbers
                if val2.isdigit():
                    return ""
                #else you need to multiply
                elif (val2 == "(" or val2 == "x"):
                    return "*"
                elif (val2.isalpha()):
                    return "*"
                else:
                    return""
            #if the first value is a ) or x
            elif val1 == ")" or val1 == "x":
                #if the second value is not an operator then multiply
                if (val2.isdigit() or val2=="(" or val2.isalpha()):
                    return "*"
                else:
                    return ""
            elif val1 == "^":
                return "**"
            else:
                return ""
                

    def generate_table(self):
        #the needed fields that the table has to generate are as follows:
        # i, xi, f(xi), c, c(fxi), xm, f(xm)
        self.table=[]
        dx = (int(self.upper_bound) - int(self.lower_bound))/int(self.n)
        c = 0
        xm = 0

        for i in range(int(self.n)+1):
            xi = i*dx+int(self.lower_bound) 
            fxi = eval(self.converted_function,globals().update({"x":xi}),locals())
            if(int(self.n) % 2 == 0):
                if i == 0 or i == int(self.n):
                    c = 1
                elif i % 2 == 0:
                    c = 2
                else:
                    c = 4
            if i > 0:
                xm = xi - dx/2

            fxm = eval(self.converted_function,globals().update({"x":xm}),locals())

            self.table.append([str(i),str(round(xi,6)),str(round(fxi,6)),str(c),
            str(round(c*fxi,6)),round(xm,6),str(round(fxm,6))])
            self.table[0][6] = "0"


    def new_tableTree(self):
        #clear the previous tree
        for record in self.tableTree.get_children():
            self.tableTree.delete(record)
        #insert all the needed data into the new tree
        for row in self.table:    
            self.tableTree.insert(parent="",index="end",iid=row[0],values=row)


    def updateLRTMS(self):
        dx = (float(self.upper_bound) - float(self.lower_bound)) / int(self.n)
        fxi_sum = 0
        cfxi_sum = 0
        fxm_sum = 0
        
        for i in range(len(self.table)):
            fxi_sum += float(self.table[i][2])
            fxm_sum += float(self.table[i][6])
            cfxi_sum += float(self.table[i][4])

        self.L_var.set(str(round((fxi_sum - float(self.table[len(self.table)-1][2]))*dx ,6)))
        self.R_var.set(str(round((fxi_sum - float(self.table[0][2]))*dx ,6)))
        self.T_var.set(str(round((float(self.L_var.get())+float(self.R_var.get()))/2 ,6)))
        self.M_var.set(str(round((fxm_sum - float(self.table[0][6]))*dx ,6)))
        self.S_var.set(str(round((cfxi_sum)*dx/3.0 ,6)))

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




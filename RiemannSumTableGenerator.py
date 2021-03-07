import tkinter as tk

#setup application

#create window
root = tk.Tk()

#set window options
root.title("Riemann Sum Table Generator")
root.minsize(350,230)


#create frames and widgets

windowFrame = tk.Frame(padx=30,pady=30)

functionFrame = tk.Frame(master=windowFrame)

functionLabel = tk.Label(master=functionFrame,text="Function:")
functionEntry = tk.Entry(master=functionFrame)

nFrame = tk.Frame(master=windowFrame)

nLabel = tk.Label(master=nFrame, text="n:")
nEntry = tk.Entry(master=nFrame)

upperBoundFrame = tk.Frame(master=windowFrame)

upperBoundLabel = tk.Label(master=upperBoundFrame, text="Upper Bound:")
upperBoundEntry = tk.Entry(master=upperBoundFrame) 

lowerBoundFrame = tk.Frame(master=windowFrame)

lowerBoundLabel = tk.Label(master=lowerBoundFrame, text="Lower Bound:")
lowerBoundEntry = tk.Entry(master=lowerBoundFrame)

submitButton = tk.Button(text="submit")


# add frames to window
windowFrame.pack()
functionFrame.pack(anchor="e")
nFrame.pack(anchor="e")
upperBoundFrame.pack(anchor="e")
lowerBoundFrame.pack(anchor="e")


# add widgets to frames
functionEntry.pack(side="right")
functionLabel.pack(side="right")

nEntry.pack(side="right")
nLabel.pack(side="right")

upperBoundEntry.pack(side="right")
upperBoundLabel.pack(side="right")

lowerBoundEntry.pack(side="right")
lowerBoundLabel.pack(side="right")

submitButton.pack(pady=(0,30))
#setup complete


#enter the applicaiton main loop to start application
root.mainloop()


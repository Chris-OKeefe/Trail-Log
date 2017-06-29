from Tkinter import *
import csv

##Notes:
#This acts as input to a CSV trail log file.
#Write up a README and put on Github
#Write follow-up scripts that calculate total distance based on length and trail type
#and that calculate distance hiked in a month, year, and total since I've started hiking.
#it could be cool if I could get data from map my hike in here for a dashboard-y report.

master = Tk()
master.wm_title("Trail Log")
trailType = IntVar()
dayOrNight = IntVar()

def enter_button():
    with open('/home/chris/Documents/Programs/Python-general/Trail-Log/trail-log.csv', 'a') as f:
        w = csv.writer(f,dialect='excel')
        w.writerow([trailName.get(), location.get(), date.get(), length.get(), trailType.get(), friend.get(), dayOrNight.get()])
        
#Total distance is an ex=post calcuation made by using the value of length if trailType is loop,
# and doubling the value of an out and back trail

Label(master, text = "Trail Name") .grid(row = 0)
Label(master, text = "Location") .grid(row = 1)
Label(master, text = "State") .grid(row = 2)
Label(master, text = "Date") .grid(row = 3)
Label(master, text = "Length") .grid(row = 4)
Label(master, 
      text="Type of trail:",
      justify = LEFT,
      padx = 20). grid(row = 5, column = 0)
Radiobutton(master, 
            text="Out and Back",
            padx = 20, 
            variable=trailType, 
            value=2). grid(row = 6, column = 0) # this way I can use the value to code total length later.
Radiobutton(master, 
            text="Loop",
            padx = 20, 
            variable=trailType, 
            value=1). grid(row = 7, column = 0)
Label(master, 
      text="Day or Night Hike?",
      justify = LEFT,
      padx = 20). grid(row = 5, column = 1)
Radiobutton(master, 
            text="Day",
            padx = 20, 
            variable=dayOrNight, 
            value=0). grid(row = 6, column = 1)
Radiobutton(master, 
            text="Night",
            padx = 20, 
            variable=dayOrNight, 
            value=1). grid(row = 7, column = 1)
Label(master, text = "with..."). grid(row = 8)

Label(master, text = "Notes"). grid(row = 9)
            
trailName = Entry(master) 
location = Entry(master)
state = Entry(master) #Validate as two-letter symbol? Or validate compared to list of states?
state.insert(10, "CA")
date = Entry(master) #validate as date
length = Entry(master) #validate as float
friend = Entry(master)
notes = Entry(master)

myButton=Button(master,text='Enter',command=enter_button)

trailName.grid(row = 0, column = 1)
location.grid(row = 1, column = 1)
state.grid(row = 2, column = 1)
date.grid(row = 3, column = 1)
length.grid(row = 4, column = 1)
friend.grid(row = 8, column = 1)
notes.grid(row = 9, column = 1)
myButton.grid(row = 10, column = 0)

Button(master, text='Quit', command=master.quit).grid(row=10, column=1, sticky=W, pady=4)

mainloop()


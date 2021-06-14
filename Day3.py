#importing library
from tkinter import * #this imports everything in tkinter
from tkinter import ttk

window = Tk()
#Declaring Window Title
window.title("Registration Form Screen")

#Declaring Window size
window.geometry('1200x1200')

#Declaring Window Color
window.configure(background = "wheat")

label= Label(window,text="Registration Form",width=25,font = ("bold italic",30))
label.grid(row =0,column = 4)
#below four fields are declared
Firstname = Label(window ,text = "First Name:").grid(row = 2,column = 0)

LastName = Label(window ,text = "Last Name:").grid(row = 3,column = 0)

Email = Label(window ,text = "Email Id:").grid(row = 4,column = 0)

Age = Label(window ,text = "Age:").grid(row = 5,column = 0)

Gender=Label(window,text="Gender:").grid(row = 6,column = 0)

ContactNumber = Label(window ,text = "Contact Number:").grid(row = 8,column = 0)

AlternatePhn = Label(window ,text = "Alternate Contact Number:").grid(row = 9,column = 0)

AdhaarNumber = Label(window ,text = "Adhaar Number:").grid(row = 10,column = 0)

PanCard = Label(window ,text = "Pan Card:").grid(row = 11,column = 0)

DrivingLicenseNumber = Label(window ,text = "Driving License Number:").grid(row = 12,column = 0)

University = Label(window ,text = "University:").grid(row = 13,column = 0)

Linkedin = Label(window ,text = "Linkedin URL:").grid(row = 14,column = 0)

Github = Label(window ,text = " Github URL:").grid(row = 15,column = 0)

Instagram = Label(window ,text = "Instagram URL:").grid(row = 16,column = 0)


Firstname1 = Entry(window).grid(row = 2,column = 1)
Lastname1 = Entry(window).grid(row = 3,column = 1)
Email1 = Entry(window).grid(row = 4,column = 1)
Age1 = Entry(window).grid(row = 5,column = 1)
var2=IntVar()
Gender= Radiobutton(window,text="Male",variable=var2,value=1 ).grid(row = 6,column = 1)
Gender1=Radiobutton(window,text="Female",variable=var2,value=2 ).grid(row = 7,column = 1)
Contactnumber1 = Entry(window).grid(row = 8,column = 1)
Alternatephn1 = Entry(window).grid(row = 9,column = 1)
Adhaarnumber1 = Entry(window).grid(row = 10,column = 1)
Pancard1 = Entry(window).grid(row = 11,column = 1)
DrivingLicenseNumber1 = Entry(window).grid(row = 12,column = 1)
University1 = Entry(window).grid(row = 13,column = 1)
Linkedin1 = Entry(window).grid(row = 14,column = 1)
Github1 = Entry(window).grid(row = 15,column = 1)
Instagram1 = Entry(window).grid(row = 16,column = 1)
var1=IntVar()
Checkbutton(window,text= "accept terms and condition", variable=var1).place(x=50,y=380)
#function declaration
def clicked():
        res = "Welcome to " + txt.get()
        lbl.configure(text= res)
btn = ttk.Button(window ,text="Submit").place(x = 70,y=420)
window.mainloop()
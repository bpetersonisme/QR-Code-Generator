from tkinter import *
from tkinter import messagebox
import os
import pyqrcode


#Creating the base window for the GUI
window = Tk()
window.title("QR Code Generator")
choice = 0


#function generate the qr code
def generate():
    if len(Subject.get())!=0 :
        global qr,photo
        qr = pyqrcode.create(Subject.get())
        photo = BitmapImage(data = qr.xbm(scale=8))
    else:
        messagebox.showinfo("Please Enter some Subject")
    try:
        showcode()
    except:
        pass


#function to show the qr code
def showcode():
    imageLabel.config(image = photo)
    subLabel.config(text="QR of " + Subject.get())


#function to save the generated code locally in png format
def save():
    dir = os.getcwd() + "\\QR Codes"
    if not os.path.exists(dir):
        os.makedirs(dir)
    try:
        if len(name.get())!=0:
            print("Choice is", choice)
            if choice == 0:
                qr.png(os.path.join(dir,name.get()+".png"),scale=8)
            elif choice == 1:
                qr.png(os.path.join(dir,name.get()+".png"),scale=16)
            else: 
                qr.png(os.path.join(dir,name.get()+".png"),scale=32) 
        else:
            messagebox.showinfo("Please enter a File Name")
    except:
        messagebox.showinfo("Generate the QR code first!")

def saveSmall(): 
    global choice 
    choice = 0
    save() 
    
def saveMedium():
    global choice 
    choice = 1
    save()
    
def saveLarge():
    global choice 
    choice = 2
    save()

#designing the GUI
Sub = Label(window,text="Enter subject", font=("Helvetica", 12))
Sub.grid(row =0,column =0,sticky=N+S+W+E)

FName = Label(window,text="Enter FileName", font=("Helvetica", 12))
FName.grid(row =1,column =0,sticky=N+S+W+E)

Subject = StringVar()
SubEntry = Entry(window,textvariable = Subject, font=("Helvetica", 12))
SubEntry.grid(row =0,column =1,sticky=N+S+W+E)

name = StringVar()
nameEntry = Entry(window,textvariable = name, font=("Helvetica", 12))
nameEntry.grid(row =1,column =1,sticky=N+S+W+E)

button = Button(window,text = "Generate",width=10,command = generate, font=("Helvetica", 12))
button.grid(row =0,column =4,sticky=N+S+W+E)

imageLabel = Label(window)
imageLabel.grid(row =2,column =1,sticky=N+S+W+E)

subLabel = Label(window,text="")
subLabel.grid(row =3,column =1,sticky=N+S+W+E)

'''
saveB = Button(window,text="Save as PNG",width=15,command = save, font=("Helvetica", 12))
saveB.grid(row =1,column =3,sticky=N+S+W+E)
'''

saveBSmall = Button(window, text="Small", width=10,command = saveSmall, font=("Helvetica", 12))
saveBSmall.grid(row=1, column=3,sticky=N+S+W+E)

saveBSmall = Button(window, text="Medium", width=10,command = saveMedium, font=("Helvetica", 12))
saveBSmall.grid(row=1, column=4,sticky=N+S+W+E)

saveBSmall = Button(window, text="Large", width=10,command = saveLarge, font=("Helvetica", 12))
saveBSmall.grid(row=1, column=5,sticky=N+S+W+E)

#making the GUI resposnsive
Rows = 3
Columns = 6

for row in range(Rows+1):
    window.grid_rowconfigure(row,weight=1)

for col in range(Columns+1):
    window.grid_columnconfigure(col,weight=1)


#looping the GUI
window.mainloop()

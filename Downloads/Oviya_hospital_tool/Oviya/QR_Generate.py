#Importing necessary packages.
import pyqrcode
import png
from pyqrcode import QRCode
import os
import tkinter as tk
from tkinter import *
from tkinter import simpledialog
import sys

def resource_path(relative):
    return os.path.join(os.environ.get("_MEIPASS2",os.path.abspath(".")),relative)
    
#Writing logic of task.
i=0
def New_patient():
    Patient_name = simpledialog.askstring("Patient_Name", "Please enter the Patient's name",parent=Window)
    global i
    i = i+1
    os.system("notepad"+" "+resource_path("Prescriptions")+"\\"+str(i)+"_"+str(Patient_name)+".txt")
    #Reading text file.
    with open(resource_path("Prescriptions")+"\\"+str(i)+"_"+str(Patient_name)+".txt") as f:
        lines = f.readlines()
    Prescription = Patient_name
    for j in range(0,len(lines)):
        Prescription = Prescription+"#"+lines[j][0:len(lines[j])-1]
    #Generating QR code.
    print(Prescription)
    QR = pyqrcode.create(Prescription)
    QR.png(resource_path("QR_code_Images")+"\\"+str(i)+"QR.png", scale = 6)



Window=tk.Tk()
Window.geometry('800x600')
Window.title('Hospital prescription tool.')
Window.configure(background='#CDCDCD')
B=Button(Window, text ="New Patient", command = New_patient)
B.configure(background='#364156', foreground='white',font=('arial',10,'bold'))
B.pack(side=BOTTOM,pady=50)
Window.mainloop()


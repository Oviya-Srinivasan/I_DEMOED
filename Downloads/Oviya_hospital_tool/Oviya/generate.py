import pyqrcode
import os
import tkinter as tk
from tkinter import Button, simpledialog, Label, Entry, messagebox

def resource_path(relative):
    return os.path.join(os.environ.get("_MEIPASS2", os.path.abspath(".")), relative)

def create_prescription_qr(patient_name, prescription_lines):
    prescription = patient_name + "#" + "#".join(prescription_lines)
    qr = pyqrcode.create(prescription)
    qr.png(resource_path("QR_code_Images") + f"/{i}QR.png", scale=6)

def new_patient():
    patient_name = simpledialog.askstring("Patient Name", "Please enter the Patient's name", parent=window)
    if patient_name:
        global i
        i += 1
        prescription_file_path = resource_path("Prescriptions") + f"/{i}_{patient_name}.txt"
        os.system("notepad " + prescription_file_path)
        
        # Check if the prescription file exists and read its contents
        if os.path.exists(prescription_file_path):
            with open(prescription_file_path, "r") as f:
                prescription_lines = f.read().splitlines()
            create_prescription_qr(patient_name, prescription_lines)
            messagebox.showinfo("Success", "QR code generated successfully.")
        else:
            messagebox.showerror("Error", "Prescription file not found.")

window = tk.Tk()
window.geometry('800x600')
window.title('Hospital Prescription Tool')
window.configure(background='#CDCDCD')

i = 0  # Global counter for patient records

# Create labels and entry fields for patient name and prescription
patient_name_label = Label(window, text="Patient Name:", font=('arial', 12))
patient_name_label.pack(pady=20)

patient_name_entry = Entry(window, font=('arial', 12))
patient_name_entry.pack()

new_patient_button = Button(window, text="New Patient", command=new_patient, font=('arial', 10, 'bold'))
new_patient_button.pack(pady=20)

window.mainloop()

import qrcode
import tkinter as tk
from PIL import Image, ImageTk

# Database of medicine names and their fixed costs (replace with your actual data)
medicine_costs = {
    "Abacavir": 120.00,
    "Acetaminophen": 80.50,
    "Aclidinium": 150.25,
    # Add more medicines and their costs here
    "Medicine4": 99.99,
    "Medicine5": 55.75,
}

# Create a dictionary to store medicine names and their associated costs in INR
medicine_prices_INR = {}

# List of medicine names (replace with your actual data)
medicine_names = ["Abacavir", "Acetaminophen", "Aclidinium", "Medicine4", "Medicine5"]  # Add more medicine names here

# Assign fixed costs from the database to medicines
for medicine in medicine_names:
    if medicine in medicine_costs:
        medicine_prices_INR[medicine] = medicine_costs[medicine]
    else:
        print(f"Cost not found for {medicine}.")

# Calculate the total cost for all medicines
total_cost = sum(medicine_prices_INR.values())

# Print the total cost with the INR symbol
print(f"Total Cost for All Medicines: ₹{total_cost:.2f}")

# Define the UPI payment link with the total cost and other necessary details
upi_payment_link = f"upi://pay?pa=preethabalaji2905@oksbi&pn=Preetha Balaji&tn=Total%20Cost&am={total_cost}&cu=INR"

# Create a function to display the QR code in a Tkinter window
def display_qr_code():
    # Generate a QR code
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(upi_payment_link)
    qr.make(fit=True)
   
    # Create a QR code image
    img = qr.make_image(fill_color="black", back_color="white")
   
    # Create a Tkinter window
    window = tk.Tk()
    window.title("Google Pay QR Code")
   
    # Convert the QR code image to a PhotoImage
    qr_image = ImageTk.PhotoImage(image=Image.fromarray(img))

    # Create a label to display the QR code image
    qr_label = tk.Label(window, image=qr_image)
    qr_label.photo = qr_image  # Keep a reference to prevent image from being garbage collected
    qr_label.pack()
   
    # Start the Tkinter main loop
    window.mainloop()

# Call the function to display the QR code in the Tkinter window
display_qr_code()
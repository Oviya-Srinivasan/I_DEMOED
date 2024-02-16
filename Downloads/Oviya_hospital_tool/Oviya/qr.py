import qrcode

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

# Generate a QR code for the total cost
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data(f"Total Cost: ₹{total_cost:.2f}")
qr.make(fit=True)

# Create a QR code image
img = qr.make_image(fill_color="black", back_color="white")

# Save the QR code image to a file
img.save("total_cost_qr.png")

print("QR code for total cost saved as 'total_cost_qr.png'")
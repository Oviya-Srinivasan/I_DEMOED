from flask import Flask, render_template, request, send_file,redirect,url_for
import qrcode

app = Flask(__name__, template_folder="templates")

@app.route('/')
def index():
    return render_template('hospital.html')

@app.route('/generate', methods=['POST'])
def generate_qr_code():
    data_fields = request.form.to_dict()  
    combined_data = "\n".join(data_fields.values())  
    # Generate QR code
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(combined_data)
    qr.make(fit=True)
    qr_img = qr.make_image(fill_color="black", back_color="white")
    # Save the QR code as an image (optional)
    qr_img.save('static/qrcode.png')
    return send_file("static/qrcode.png", mimetype='image/png')

if __name__ == '__main__':
    app.run(debug=True)

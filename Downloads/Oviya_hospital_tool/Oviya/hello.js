// Import the Nodemailer library
const nodemailer = require('nodemailer');

// Create a transporter to send emails
const transporter = nodemailer.createTransport({
    service: 'Gmail', // Use your email service provider
    auth: {
        user: 'your_email@gmail.com', // Your email address
        pass: 'your_email_password' // Your email password
    }
});

// Assuming you have customer, prescription, and remaining medicine data
const customerName = 'John Doe';
const prescribedMedicines = ['Medicine A', 'Medicine B'];
const remainingMedicines = ['Medicine C', 'Medicine D']; // Add remaining medicines here

// Define email content with placeholders for personalization
const mailOptions = {
    from: 'your_email@gmail.com', // Sender's email address
    to: 'customer_email@example.com', // Recipient's email address
    subject: 'Medication Purchase Reminder',
    text: `Dear ${customerName}, please complete your medication purchase for ${prescribedMedicines.join(', ')} and consider adding ${remainingMedicines.join(', ')} to your order. Visit our website for more details.`,
    html: `<p>Dear ${customerName},</p><p>Please complete your medication purchase for ${prescribedMedicines.join(', ')} and consider adding ${remainingMedicines.join(', ')} to your order. Visit our website for more details.</p>`
};

// Send the personalized email
transporter.sendMail(mailOptions, (error, info) => {
    if (error) {
        console.log('Email not sent:', error);
    } else {
        console.log('Email sent:', info.response);
    }
});
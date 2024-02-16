<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Doctor Medicine Generation</title>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/qrcodejs/1.0.0/qrcode.min.js"></script>
    <style>
        /* Global styles */
        body {
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 0;
        }
        .banner {
            position: relative;
            text-align: center;
            background-image: url('bg1.png'); /* Set the background image */
            background-size: cover; /* Make the background image cover the entire banner area */
            height: 300px; /* Adjust the height as needed */
        }

        .banner img {
            display: none; /* Hide the image element if you want to display only the background image */
        }

       nav {
            position: absolute;
            top: 0;
            left: 0;
            background-color: rgba(0, 0, 0, 0.7); /* Add background color with transparency for better readability */
            width: 100%; /* Make the navigation bar span the full width */
            padding: 10px 20px; 
         }

.cf:after {
    clear: both;
}

.cf {
    *zoom: 1;
}

.menu,
.submenu {
    margin: 0;
    padding: 0;
    list-style: none;
}

.menu {
            list-style: none;
            margin: 0;
            padding: 0;
        }
        .menu > li {
            display: inline;
            margin-right: 20px; /* Adjust the spacing between menu items */
       }

        .menu a {
            color: #fff;
            text-decoration: none;
            font-size: 16px; /* Adjust the font size */
            text-transform: uppercase;
        }

.menu li:hover {
    background: #87CEEB; /* Light blue on hover */
}

.menu > li > a {
    transform: skewX(-25deg);
    padding: 1em 2em;
}

/* Dropdown */
.submenu {
    position: absolute;
    width: 200px;
   left: 50%;
    margin-left: -100px;
    transform: skewX(-25deg);
    transform-origin: left top;
}

.submenu li {
    background-color: #34495e; /* Original submenu background color */
    position: relative;
    overflow: hidden;
}

.submenu > li > a {
    padding: 1em 2em;
}

.submenu > li::after {
    content: '';
    position: absolute;
    top: -125%;
    height: 100%;
    width: 100%;
    box-shadow: 0 0 50px rgba(0, 0, 0, .9);
}

.submenu > li:nth-child(odd) {
    transform: skewX(-25deg) translateX(0);
}

.submenu > li:nth-child(odd) > a {
    transform: skewX(25deg);
}

.submenu > li:nth-child(odd)::after {
    right: -50%;
    transform: skewX(-25deg) rotate(3deg);
}

.submenu > li:nth-child(even) {
    transform: skewX(25deg) translateX(0);
}

.submenu > li:nth-child(even) > a {
    transform: skewX(-25deg);
}

.submenu > li:nth-child(even)::after {
    left: -50%;
    transform: skewX(25deg) rotate(3deg);
}

/* Show dropdown */
.submenu,
.submenu li {
    opacity: 0;
    visibility: hidden;
}

.submenu li {
    transition: .2s ease transform;
}

.menu > li:hover .submenu,
.menu > li:hover .submenu li {
    opacity: 1;
    visibility: visible;
}

.menu > li:hover .submenu li:nth-child(even) {
    transform: skewX(25deg) translateX(15px);
}

.menu > li:hover .submenu li:nth-child(odd) {
    transform: skewX(-25deg) translateX(-15px);
}

        /* Search Bar styles */
        .search-bar {
            text-align: center;
            margin: 10px;
            float: center;
        }

        .search-bar input[type="text"] {
            padding: 10px 50px;
            border: 1px solid #ccc;
            border-radius: 5px;
        }

        .search-button {
            background-color: #333;
            color: #fff;
            border: none;
            border-radius: 5px;
            padding: 10px 20px;
            cursor: pointer;
        }

        /* Medicine Details Modal styles */
        .modal {
            display: none;
            position: fixed;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%);
            width: 360px;
            /*max-width: 400px;*/
            background-color: #fff;
            border-radius: 5px;
            z-index: 1000;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        }

        .modal-content {
            padding: 20px;
        }

        /* Add a close button inside the modal */
        .close-button {
            position: absolute;
            top: 10px;
            right: 10px;
            cursor: pointer;
        }

        .modal h2 {
            font-size: 24px;
            margin-bottom: 10px;
        }

        .modal input[type="text"], .modal input[type="number"] {
            width: 300px;
            padding: 10px;
            margin-bottom: 10px;
            border: 1px solid #ccc;
            border-radius: 5px;
        }

        .modal .add-button {
            background-color: #333;
            color: #fff;
            border: none;
            border-radius: 5px;
            padding: 10px 20px;
            cursor: pointer;
        }

        .prescription {
            margin-top: 5px;
            padding: 10px;
            border: 1px solid #ccc;
            border-radius: 5px;
            background-color: #f9f9f9;
        }

        .prescription h2 {
            background-color: #AEDFF7;
            color: black;
            padding: 20px;
            border-radius: 5px 5px 0 0;
            margin: -10px -10px 10px -10px;
        }

        .prescription ul {
            list-style-type: none;
            padding: 0;
        }

        .prescription li {
            margin-bottom: 10px;
            border: 1px solid #ccc;
            border-radius: 5px;
            background-color: #fff;
            padding: 10px;
            display: flex;
            justify-content: space-between;
            align-items: center;
            position: relative;
        }

        .prescription li:not(:last-child)::after {
            content: '';
            position: absolute;
            bottom: -1px;
            left: 0;
            width: 100%;
            height: 1px;
            background-color: #ccc;
        }

        /* Medicine list styles */
        ul {
            list-style-type: none;
            padding: 0;
        }

        ul li {
            margin-bottom: 10px;
        }

        .patient-details {
            margin-bottom: 20px;
            padding: 10px;
            border: 1px solid #ccc;
            border-radius: 5px;
            background-color: #f0f0f0;
        }

        .edit-button, .delete-button {
            background-color: #333;
            color: #fff;
            border: none;
            border-radius: 5px;
            padding: 5px 10px;
            cursor: pointer;
        }

        .edit-button:hover, .delete-button:hover {
            background-color: #555;
        }

        #print-button {
            background-color: #333;
            color: #fff;
            border: none;
            border-radius: 5px;
            padding: 10px 20px;
            cursor: pointer;
            float: right;
            margin: 20px;
        }

        #generate-qrcode-button {
            background-color: #333;
            color: #fff;
            border: none;
            border-radius: 5px;
            padding: 10px 20px;
            cursor: pointer;
            margin: 20px;
        }

        #print-button:hover {
            background-color: #0056b3;
        }

        #generate-qrcode-button:hover {
            background-color: #0056b3;
        }

        aside.patient-details {
    width: 30%;
    padding: 15px;
    margin-left: 15px;
    float: right;
    font-style: italic;
    background-color: #f0f8ff;
    border-radius: 10px;
    box-shadow: 0px 8px 16px 0px rgba(0,0,0,0.2);
}

aside.patient-details p {
    font-size: 1em;
    color: #333;
}

aside.patient-details h2 {
    color: #015bba;
    font-size: 1.5em;
}

        /* Footer styles */
        *{
    margin: 0; padding: 0;
    border: 0; outline: 0;
    font-family:system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif;
    list-style: none;
    text-decoration: none;
}
:root{
    --theme-col: #87CEEB;
}
.space-y-2 > :not([hidden]) ~ :not([hidden]) {
    --tw-space-y-reverse: 0;
    margin-top: calc(0.5rem * calc(1 - var(--tw-space-y-reverse)));
    margin-bottom: calc(0.5rem * var(--tw-space-y-reverse));
}
footer{
    background-color: #111010;
}
.f-item-con{
    padding: 1.5rem 4rem;
    display: grid;
    grid-template-columns: repeat(3, minmax(0, 1fr));
    grid-gap: 2rem;
}
footer .app-name{
    color: white;
    border-left: 4px solid var(--theme-col);
    padding-left: 1.5rem;
    font-size: 1.875rem;
    line-height: 2.25rem;
    font-weight: 700;
}
.app-name .app-initial{
    color: var(--theme-col);
}
footer .app-info p{
    color: white;
    padding-left: 1.65rem;
}

footer .footer-title{ 
    font-size: 1.25rem;
    line-height: 1.75rem;
    color: white;
    border-left: 4px solid var(--theme-col);
    padding-left: 1.5rem;
    height: fit-content;
}
footer ul{ 
    padding-left: 1.75rem;
    color: white;
    font-size: 0.875rem/* 14px */;
    line-height: 1.25rem;
    margin-top: .5rem;
}
footer ul li{ 
    margin: .25rem 0;
    cursor: pointer;
    color: #d4d4d4;
    width: fit-content;
}
footer ul li:hover{
    color: white;
}
footer .help-sec{
    grid-column-start: 2;
}
footer .cr-con{
    background-color: #232127;
    color: white;
    padding: 1rem 4rem;
    text-align: center;
}
.g-i-t{
    display: grid;
    grid-column-start: 3;
    grid-row-start: 1;
    grid-row-end: 3;
}
.g-i-t form{
    display: flex;
    flex-direction: column;
    margin-top: 1rem;
    --tw-space-y-reverse: 0;
    margin-top: calc(0.5rem * calc(1 - var(--tw-space-y-reverse)));
    margin-bottom: calc(0.5rem * var(--tw-space-y-reverse));
}
form .g-inp{
    padding: .25rem .5rem;
    font-size: 16px;
}
.g-inp textarea{
    height: 150px;
}
.f-btn{
    padding: .25rem 1rem;
    background-color: var(--theme-col);
    border-radius: .25rem;
    font-size: 16px;
    color: white;
    font-weight: 500;
}
main {
    height: 500px;
    margin: 10px; /* Adjust the margin as needed */
    padding: 20px; /* Optionally, add padding as well */
    background-color: #fff; /* Optionally, set a background color */
    border: 1px solid #ccc; /* Optionally, add a border */
    border-radius: 5px; /* Optionally, add border-radius for rounded corners */
}

#medicine-input {
            width: 300px;
            padding: 10px;
            border: 1px solid #ccc;
            border-radius: 5px;
        }
    </style>
</head>
<body>
    <h2 style="background-color: #333; color: #fff; padding: 10px; border-radius: 2px 25px; text-align: center;"> MediGen </h2>
    <div class="banner">
        <!-- Display the image if needed -->
        <img src="bg1.png" alt="Banner Image">
    </div>
    <nav>
       <ul class="menu cf">
           <li> <a href="#">Home</a></li>
           <li> <a href="#">Patient's History</a></li>
           <li> <a href="#">Doctor's Profile</a></li>
       </ul>
    </nav>

    <div class="search-bar">
        <input type="text" id="medicine-input" list="medicine-options" placeholder="Search for Medicine...">
        <datalist id="medicine-options">
            <!-- Medicine options will be added here dynamically -->
        </datalist>
        <a href="#" class="search-button" onclick="searchMedicine()">Search</a>
    </div>
    <main>
        <aside class="patient-details">
        <div>
            <input type="text" id="patient-id" placeholder="Enter Patient's ID">
            <button class="search-button" onclick="displayPatientDetails()">Submit</button>
        </div>
        <div class="patient-details" id="patient-details">
            <h2>Patient Details</h2>
            <p><strong>Name:</strong> <span id="patient-name"></span></p>
            <p><strong>Gender:</strong> <span id="patient-gender"></span></p>
            <p><strong>Address:</strong> <span id="patient-address"></span></p>
            <p><strong>Blood Type:</strong> <span id="patient-blood-type"></span></p>
            <p><strong>Allergies:</strong> <span id="patient-allergies"></span></p>
            <p><strong>Last Visited:</strong> <span id="patient-last-visited"></span></p>
            <p><strong>Email:</strong> <span id="patient-email"></span></p> <!-- Display the email -->
        </div>
    </aside>

    <!-- Medicine Details Modal -->
    <div id="medicineDetailsModal" class="modal">
        <div class="modal-content">
            <h2>Medicine Details</h2>
            <p id="medicine-name"></p>
            <input type="number" id="dosage" placeholder="Dosage (mg)">
            <input type="number" id="duration" placeholder="Duration (days)">
            <button class="add-button" onclick="addMedicineToPrescription()">Add to Prescription</button>
            <button class="cancel-button" onclick="closeModal()">Cancel</button>
        </div>
    </div>
    <!-- Prescription -->
    <div class="prescription">
        <h2>Prescription</h2>
        <ul id="prescription-list">
            <!-- Prescription items will be added here -->
        </ul>
    </div>
    
    <div id="qrcode"></div>
    <button id="print-button" onclick="printPrescriptionWithQR()">Print Prescription</button>
    <button id="generate-qrcode-button" onclick="generateQRCode()">Generate QR Code</button>
    <!-- Add the "Share via Email" button here -->
    <button id="share-email-button" onclick="sharePrescriptionByEmail()">Share via Email</button>
 </main>
    <script>
        let prescriptionString = '';
       // Get the input element and the datalist
       const medicineInput = document.getElementById('medicine-input');
        const medicineOptions = document.getElementById('medicine-options');

        // List of medicine names
        const medicineNames = [
    "Abacavir",
    "Acetaminophen",
    "Aclidinium",
    "Adalimumab",
    "Albuterol",
    "Alendronate",
    "Allopurinol",
    "Alprazolam",
    "Amlodipine",
    "Amoxicillin",
    "Atenolol",
    "Atorvastatin",
    "Azithromycin",
    "Benazepril",
    "Bisoprolol",
    "Budesonide",
    "Candesartan",
    "Captopril",
    "Carvedilol",
    "Celecoxib",
    "Cephalexin",
    "Cetirizine",
    "Ciprofloxacin",
    "Clonazepam",
    "Clopidogrel",
    "Dapagliflozin",
    "Dexlansoprazole",
    "Diazepam",
    "Diclofenac",
    "Digoxin",
    "Diltiazem",
    "Duloxetine",
    "Enalapril",
    "Escitalopram",
    "Esomeprazole",
    "Ezetimibe",
    "Famotidine",
    "Felodipine",
    "Fenofibrate",
    "Fexofenadine",
    "Fluconazole",
    "Fluticasone",
    "Gabapentin",
    "Gemfibrozil",
    "Glimepiride",
    "Glipizide",
    "Hydrochlorothiazide",
    "Hydrocodone",
    "Hydroxyzine",
    "Ibuprofen",
    "Imipramine",
    "Irbesartan",
    "Isosorbide",
    "Januvia",
    "Lansoprazole",
    "Levofloxacin",
    "Lisinopril",
    "Loratadine",
    "Losartan",
    "Lovastatin",
    "Meloxicam",
    "Metformin",
    "Methotrexate",
    "Metoprolol",
    "Montelukast",
    "Naproxen",
    "Nebivolol",
    "Nifedipine",
    "Nitroglycerin",
    "Olanzapine",
    "Omeprazole",
    "Ondansetron",
    "Pantoprazole",
    "Paroxetine",
    "Perindopril",
    "Phenytoin",
    "Piroxicam",
    "Pregabalin",
    "Propranolol",
    "Quetiapine",
    "Rabeprazole",
    "Ramipril",
    "Ranitidine",
    "Rosuvastatin",
    "Sertraline",
    "Simvastatin",
    "Tadalafil",
    "Telmisartan",
    "Trazodone",
    "Valsartan",
    "Venlafaxine",
    "Warfarin",
    "Xanax",
    "Zolpidem"
];

        // Function to update the datalist options based on input
        function updateMedicineOptions() {
            const searchInput = medicineInput.value.trim().toLowerCase();
            const matchingMedicines = medicineNames.filter(name => name.toLowerCase().startsWith(searchInput));

            // Clear existing options
            medicineOptions.innerHTML = '';

            // Add matching options to the datalist
            matchingMedicines.forEach(medicine => {
                const option = document.createElement('option');
                option.value = medicine;
                medicineOptions.appendChild(option);
            });
        }

        // Attach an input event listener to trigger the update
        medicineInput.addEventListener('input', updateMedicineOptions);


        const patients = [
    {
        id: "1",
        name: "John Doe",
        gender: "Male",
        address: "123 Main St, City",
        bloodType: "A+",
        allergies: "None",
        lastVisited: "2023-09-01",
        email: "2021it0532@svce.ac.in" // Add email for John Doe
    },
    {
        id: "2",
        name: "Jane Smith",
        gender: "Female",
        address: "456 Elm St, Town",
        bloodType: "B-",
        allergies: "Pollen",
        lastVisited: "2023-08-15",
        email: "2021it0532@svce.ac.in" // Add email for Jane Smith
    },
    {
        id: "3",
        name: "Bob Johnson",
        gender: "Male",
        address: "789 Oak St, Village",
        bloodType: "O+",
        allergies: "Peanuts",
        lastVisited: "2023-09-03",
        email: "2021it0532@svce.ac.in" // Add email for Bob Johnson
    },
    {
        id: "4",
        name: "Alice Brown",
        gender: "Female",
        address: "101 Pine St, Village",
        bloodType: "AB+",
        allergies: "None",
        lastVisited: "2023-08-25",
        email: "2021it0532@svce.ac.in" // Add email for Alice Brown
    },
    {
        id: "5",
        name: "Chris Davis",
        gender: "Male",
        address: "202 Cedar St, Town",
        bloodType: "A-",
        allergies: "Cat Hair",
        lastVisited: "2023-09-02",
        email: "2021it0532@svce.ac.in" // Add email for Chris Davis
    },
];

        let currentEditingMedicine = null;

        function searchMedicine() {
            const searchInput = document.getElementById('medicine-input').value.trim().toLowerCase();
            const matchingMedicines = medicineNames.filter(name => name.toLowerCase().includes(searchInput));

            if (matchingMedicines.length > 0) {
                const medicineName = matchingMedicines[0]; // Display the first matching medicine
                displayMedicineModal(medicineName);
            } else {
                alert('Medicine not found.');
            }
        }

        function displayMedicineModal(medicineName) {
            const modal = document.getElementById('medicineDetailsModal');
            const modalContent = document.querySelector('.modal-content');
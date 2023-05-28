from flask import Flask, render_template
from PIL import Image

app = Flask(__name__)

# Home Page
@app.route('/')
def home():
    return render_template('home.html')

# Patients Page
@app.route('/patients')
def patients():
    # Retrieve patient data from your database or any other source
    patients = [...]  # Replace with actual patient data
    
    return render_template('patients.html', patients=patients)

# Appointments Page
@app.route('/appointments')
def appointments():
    # Retrieve appointment data from your database or any other source
    appointments = [...]  # Replace with actual appointment data
    
    return render_template('appointments.html', appointments=appointments)

# Reports Page
@app.route('/reports')
def reports():
    # Retrieve report data from your database or any other source
    reports = [...]  # Replace with actual report data
    
    return render_template('reports.html', reports=reports)

# Doctors page
@app.route('/doctors')
def doctors():
    # Retrieve doctor data from your database or any other source
    doctors = [...]  # Replace with actual doctor data
    
    return render_template('doctors.html', doctors=doctors)

# Image Resizing
def resize_images():
    resize_image('static/Doctors.jpg', 'static/resized_Doctors.jpg', (250, 125))
    resize_image('static/appointments.jpg', 'static/resized_appointments.jpg', (250, 125))
    resize_image('static/female doctor.png', 'static/resized_female doctor.png', (250, 125))
    resize_image('static/female icon.png', 'static/resized_female icon.png', (250, 125))
    resize_image('static/male doctor.png', 'static/resized_male doctor.png', (250, 125))
    resize_image('static/Male icon.png', 'static/resized_male icon.png', (250, 125))
    resize_image('static/patient icon.png', 'static/resized_patient icon.png', (250, 125))
    resize_image('static/Report.png', 'static/resized_report.png', (250, 125))
    resize_image('static/hospital.jpg', 'static/resized_hospital.jpg', (1520,250))
    # Add more image resizing operations for other images as needed

def resize_image(image_path, output_path, size):
    image = Image.open(image_path)
    resized_image = image.resize(size)
    resized_image.save(output_path)

# Resize the images when the Flask application starts running
resize_images()

if __name__ == '__main__':
    app.run()

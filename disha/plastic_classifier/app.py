import os
import random
import sqlite3
from flask import Flask, render_template, request, redirect, url_for
from werkzeug.utils import secure_filename
from database import init_db

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = os.path.join('static', 'uploads')
app.config['ALLOWED_EXTENSIONS'] = {'png', 'jpg', 'jpeg'}

os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
init_db()

PLASTIC_TYPES = ['PET (Polyethylene Terephthalate)', 'HDPE (High-Density Polyethylene)', 
                 'PVC (Polyvinyl Chloride)', 'LDPE (Low-Density Polyethylene)', 
                 'PP (Polypropylene)', 'PS (Polystyrene)']

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

@app.route('/', methods=['GET', 'POST'])
def index():
    prediction = None
    if request.method == 'POST':
        if 'file' not in request.files:
            return redirect(request.url)
        file = request.files['file']
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(filepath)

            # Simulated CV/AI prediction logic
            detected_type = random.choice(PLASTIC_TYPES)
            confidence = round(random.uniform(82.0, 98.5), 2)

            # Save to Database History
            conn = sqlite3.connect("database.db")
            cursor = conn.cursor()
            cursor.execute("INSERT INTO predictions (filename, plastic_type, confidence) VALUES (?, ?, ?)",
                           (filename, detected_type, confidence))
            conn.commit()
            conn.close()

            prediction = {
                'filename': filename,
                'plastic_type': detected_type,
                'confidence': confidence
            }

    return render_template('index.html', prediction=prediction)

@app.route('/history')
def history():
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    cursor.execute("SELECT filename, plastic_type, confidence, created_at FROM predictions ORDER BY id DESC")
    records = cursor.fetchall()
    conn.close()
    return render_template('history.html', records=records)

if __name__ == '__main__':
    app.run(debug=True)


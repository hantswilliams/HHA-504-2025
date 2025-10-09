from flask import Flask, render_template, request, redirect, url_for
import sqlite3
from datetime import datetime
import requests

app = Flask(__name__)

# Database initialization
def init_db():
    conn = sqlite3.connect('ehr.db')
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS patients (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            first_name TEXT NOT NULL,
            last_name TEXT NOT NULL,
            wbc REAL,
            wbc_interpretation TEXT,
            plt REAL,
            hg REAL,
            hct REAL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    conn.commit()
    conn.close()

# Initialize database on startup
init_db()

@app.route('/')
def index():
    # Get all patients from database
    conn = sqlite3.connect('ehr.db')
    c = conn.cursor()
    c.execute('SELECT * FROM patients ORDER BY created_at DESC')
    patients = c.fetchall()
    conn.close()
    return render_template('index.html', patients=patients)

@app.route('/add_patient', methods=['POST'])
def add_patient():
    first_name = request.form.get('first_name')
    last_name = request.form.get('last_name')
    wbc = request.form.get('wbc')
    plt = request.form.get('plt')
    hg = request.form.get('hg')
    hct = request.form.get('hct')


    ## send wbc value to https://hants-pythontest-507-714433739872.europe-west1.run.app/?wbc={wbc} expecting normal/abnormal response
    wbc_interpretation = 'N/A'

    if wbc:
        try:
            response = requests.get(f'https://hants-pythontest-507-714433739872.europe-west1.run.app/?wbc={wbc}')
            if response.status_code == 200:
                wbc_interpretation = response.text
            else:
                wbc_interpretation = 'Error'
        except Exception as e:
            wbc_interpretation = 'Error'

    conn = sqlite3.connect('ehr.db')
    c = conn.cursor()
    c.execute('''
        INSERT INTO patients (first_name, last_name, wbc, wbc_interpretation, plt, hg, hct)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    ''', (first_name, last_name, wbc, wbc_interpretation, plt, hg, hct))
    conn.commit()
    conn.close()

    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5020)

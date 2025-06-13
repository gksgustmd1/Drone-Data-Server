from flask import Flask, request, jsonify, redirect
from config import Config
from schema import db, License
from datetime import datetime
import os

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)

#check firmware
FIRMWARE_FOLDER = 'firmwares'
FIRMWARE_FILENAME = 'test.txt'  
FIRMWARE_URL = f'http://52.78.137.212:5000/download/{FIRMWARE_FILENAME}'  

#log path
LOG_ROOT = '/root/Drone-log-data'

@app.route('/check_license', methods=['POST'])
def check_license():
    data = request.get_json()
    if not data or 'serial' not in data:
        return jsonify({'error': 'Missing serial'}), 400

    serial = data['serial']
    license_entry = License.query.filter_by(serial=serial).first()

    if license_entry:
        return redirect(FIRMWARE_URL, code=302)
#        return jsonify({
#            'status': 'valid',
#            'firmware_url': FIRMWARE_URL
#        }), 200
    else:
        return jsonify({'status': 'invalid'}), 403


#endpoint
@app.route('/download/<filename>')
def download_firmware(filename):
    file_path = os.path.join(FIRMWARE_FOLDER, filename)
    if os.path.exists(file_path):
        from flask import send_file
        return send_file(file_path, as_attachment=True)
    else:
        return "File not found", 404

#log data write
@app.route('/upload_log', methods=['POST'])
def upload_log():
    serial = request.form.get('serial')
    file = request.files.get('log_file')

    if not serial or not file:
        return "Missing serial or log_file", 400

    #create license dir 
    save_dir = os.path.join(LOG_ROOT, serial)
    os.makedirs(save_dir, exist_ok=True)

    #create log file:format.txt
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    filename = f"log_{timestamp}.txt"
    save_path = os.path.join(save_dir, filename)

    file.save(save_path)

    return f"Log saved to {save_path}", 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

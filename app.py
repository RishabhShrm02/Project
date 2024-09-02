from flask import Flask, request, jsonify, render_template
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'image' not in request.files:
        return jsonify({'message': 'No file part'}), 400

    file = request.files['image']
    if file.filename == '':
        return jsonify({'message': 'No selected file'}), 400

    if file:
        try:
          
            filename = secure_filename(file.filename)
            file_path = os.path.join('uploads', filename) 
            file.save(file_path)
            
            
            return jsonify({'message': f'File uploaded successfully: {filename}'}), 200
        except Exception as e:
            return jsonify({'message': 'Error processing file', 'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask, request, jsonify
import os
from datetime import datetime

app = Flask(__name__)

# Endpoint to receive the image and return a sample response
@app.route('/upload', methods=['POST'])
def upload_image():
    if 'file' not in request.files:
        return jsonify({'error': 'No file provided'}), 400

    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No file selected'}), 400

    # Saving the image temporarily
    filename = f"{datetime.now().strftime('%Y%m%d%H%M%S')}_{file.filename}"
    filepath = os.path.join('uploads', filename)
    os.makedirs('uploads', exist_ok=True)
    file.save(filepath)

    # Simulated response data
    response_data = {
        'message': 'Image processed successfully',
        'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        'filename': filename
    }

    return jsonify(response_data), 200

if __name__ == '__main__':
    app.run(debug=True)

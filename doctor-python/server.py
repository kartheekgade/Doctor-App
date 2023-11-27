from flask import Flask, request, jsonify
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)

@app.route('/upload-audio', methods=['POST'])
def upload_audio():
    try:
        audio_file = request.files['audio']
        # Process the audio file here (you can replace this with your actual processing logic)
        # For demonstration purposes, let's just print the file details
        print(f"Received audio file: {audio_file.filename}")
        return jsonify({"message": "Converted the audio"})
    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == '__main__':
    app.run(debug=True)

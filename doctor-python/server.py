from flask import Flask, request, jsonify, send_file
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)

# UPLOAD_FOLDER = 'uploads'
# app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
@app.route('/upload-audio', methods=['POST'])
def upload_audio():
    try:
        audio_file = request.files['audio']
        # Process the audio file here (you can replace this with your actual processing logic)
        # For demonstration purposes, let's just print the file details
        print(f"Received audio file: {audio_file.filename}")
        # For demonstration purposes, generate placeholder URLs for video and PDF previews
        # video_url = f"http://localhost:5000/previews/{audio_filename}_video.mp4"
        # pdf_url = f"http://localhost:5000/previews/{audio_filename}_preview.pdf"
        # return jsonify({"videoUrl": video_url, "pdfUrl": pdf_url})
        return jsonify({"message": "Audio file received."})
    except Exception as e:
        return jsonify({"error": str(e)})
@app.route('/get-video', methods=['GET'])
def get_video():
    video_path = r'C:\Users\krthk\OneDrive\Documents\DigitalHealth\sample-mp4-file-small.mp4'
    return send_file(video_path, as_attachment=True)

@app.route('/get-pdf', methods=['GET'])
def get_pdf():
    pdf_path = r'C:\Users\krthk\OneDrive\Documents\DigitalHealth\HW1.pdf'
    return send_file(pdf_path, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)

# from flask import Flask, request, jsonify, send_file
# from flask_cors import CORS
# import os
# import uuid

# app = Flask(__name__)
# CORS(app)

# UPLOAD_FOLDER = 'uploads'
# PREVIEW_FOLDER = 'previews'
# app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
# app.config['PREVIEW_FOLDER'] = PREVIEW_FOLDER

# def process_audio(audio_path):
#     # Replace this with your actual audio processing logic
#     # For demonstration purposes, assume audio processing creates video and PDF files
#     video_path = os.path.join(app.config['PREVIEW_FOLDER'], f"{uuid.uuid4()}_video.mp4")
#     pdf_path = os.path.join(app.config['PREVIEW_FOLDER'], f"{uuid.uuid4()}_preview.pdf")

#     # Your processing logic here...

#     return video_path, pdf_path

# @app.route('/upload-audio', methods=['POST'])
# def upload_audio():
#     try:
#         audio_file = request.files['audio']

#         if audio_file:
#             # Save the audio file to the server
#             audio_filename = f"{str(uuid.uuid4())}.wav"
#             audio_path = os.path.join(app.config['UPLOAD_FOLDER'], audio_filename)
#             audio_file.save(audio_path)

#             # Process the audio file
#             video_path, pdf_path = process_audio(audio_path)

#             return jsonify({"videoPath": video_path, "pdfPath": pdf_path})
#         else:
#             return jsonify({"error": "No audio file received."})

#     except Exception as e:
#         return jsonify({"error": str(e)})

# @app.route('/previews/<filename>')
# def preview_file(filename):
#     return send_file(os.path.join(app.config['PREVIEW_FOLDER'], filename), as_attachment=True)

# if __name__ == '__main__':
#     app.run(debug=True)

from flask import Flask, request, render_template, send_file
import os
from nlp_parser import parse_prompt
from video_processor import process_video

app = Flask(__name__)
UPLOAD_FOLDER = 'static/uploads'
OUTPUT_FOLDER = 'static/outputs'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if 'video' not in request.files or not request.form.get('prompt'):
            return render_template('index.html', error='Missing video or prompt')

        video = request.files['video']
        prompt = request.form['prompt']
        video_path = os.path.join(UPLOAD_FOLDER, video.filename)
        output_filename = f"edited_{video.filename}"
        output_path = os.path.join(OUTPUT_FOLDER, output_filename)

        video.save(video_path)
        action = parse_prompt(prompt)

        if action.get('error'):
            return render_template('index.html', error=action['error'])

        success = process_video(video_path, output_path, action)
        if success:
            return send_file(output_path, as_attachment=True)
        else:
            return render_template('index.html', error='Video processing failed')

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
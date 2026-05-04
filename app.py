import os
from flask import Flask, render_template, request, jsonify
from werkzeug.utils import secure_filename
from database import init_db, get_all_history
from pipeline import run_pipeline

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024 # 16MB max limit

# Ensure uploads folder exists
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

# Initialize database
init_db()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/history')
def history():
    return render_template('history.html')

@app.route('/api/analyze', methods=['POST'])
def analyze():
    if 'resume' not in request.files:
        return jsonify({"error": "No resume file provided"}), 400
    
    file = request.files['resume']
    job_description = request.form.get('job_description', '')
    
    if file.filename == '':
        return jsonify({"error": "No selected file"}), 400
        
    if not job_description:
        return jsonify({"error": "Job description is required"}), 400

    if file:
        filename = secure_filename(file.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)
        
        try:
            # Run the AI pipeline
            result = run_pipeline(filepath, job_description)
            return jsonify(result)
        except Exception as e:
            print("ERROR IN PIPELINE:", e)
            return jsonify({"error": str(e)}), 500
        finally:
            # cleanup
            if os.path.exists(filepath):
                os.remove(filepath)

@app.route('/api/history', methods=['GET'])
def fetch_history():
    data = get_all_history()
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
